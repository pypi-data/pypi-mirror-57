# -*- coding: utf-8 -*-

# python 3 compatibility
from __future__ import absolute_import, division, print_function, unicode_literals

import abc
import io
import logging
import os
import sys
import types
from collections import Sequence

import requests
import six
import stevedore
from frutils.frutils import *  # noqa: F403
from six import string_types

from .defaults import *  # noqa: F403
from .exceptions import FrklConfigException

yaml = StringYAML(typ="safe")
yaml.default_flow_style = False

try:
    set
except NameError:
    # noinspection PyDeprecation,PyCompatibility
    from sets import Set as set

__metaclass__ = type

log = logging.getLogger("frkl")


# ------------------------------------------------------------
# utility methods


# extensions
# ------------------------------------------------------------------------
def load_extension(name, **init_params):
    """Loading a processor extension.

    Args:
      name (str): the registered name of the extension
      init_params (dict): the parameters to initialize the extension object

    Returns:
      FrklConfig: the extension object
    """

    log2 = logging.getLogger("stevedore")
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(logging.Formatter("PLUGIN ERROR -> %(message)s"))
    out_hdlr.setLevel(logging.DEBUG)
    log2.addHandler(out_hdlr)
    log2.setLevel(logging.INFO)

    log.debug("Loading extension...")

    print(name)
    print(init_params)

    mgr = stevedore.driver.DriverManager(
        namespace="frkl.frk", name=name, invoke_on_load=True, invoke_kwds=init_params
    )

    log.debug(
        "Registered plugins: {}".format(", ".join(ext.name for ext in mgr.extensions))
    )

    return mgr


@six.add_metaclass(abc.ABCMeta)
class ConfigProcessor(object):
    """Abstract base class for config url/content manipulators.

    In order to enable configuration urls and content to be written as quickly and minimal as possible, frkl supports pluggable processors that can manipulate the configuration urls and contents. For example, urls can be abbreviated 'gh' -> 'https://raw.githubusercontent.com/blahblah'.
    """

    def __init__(self, **init_params):
        """
        Args:
          init_params (dict): arguments to initialize the processor
        """

        self.init_params = init_params

        self.current_input_config = None
        self.current_context = None
        self.last_call = False

    def get_input_format(self):
        """Returns the format of the accepted input.

        Defaults to 'STRING'
        """

        return STRING_FORMAT

    def get_output_format(self):
        """Returns the format of the output.

        Defaults to the same as the 'get_input_format' method.
        """

        return self.get_input_format()

    def set_current_config(self, input_config, context):
        """Sets the current configuration.

        Calls the 'new_config' method after assigning the new input configuration to the 'self.current_input_config' variable.

        Args:
          input_config (object): current configuration to be processed
          context (dict): dict that describes the current context / processing state
        """

        if isinstance(input_config, types.GeneratorType):
            raise Exception("Can't deal with Type 'Generator' as a value.")

        self.current_input_config = input_config
        self.current_context = context

        self.last_call = self.current_context["last_call"]
        self.new_config()

    def new_config(self):
        """Can be overwritten to initially compute a new config after it is first set.

        The newly (last) added input configuration is stored in the 'self.current_input_config' variable.
        """

        pass

    def get_additional_configs(self):
        """Returns additional configs if applicable.

        This is called before the 'process' method.

        Returns:
          list: other configs to be processed next
        """

        return None

    def process(self):
        """Processes the config url or content.

        Calls the 'process_current_config' method internally

        Returns:
          object: processed config url or content
        """

        if self.last_call:
            if self.current_input_config or self.handles_last_call():
                return self.process_current_config()
            else:
                return None
        else:
            return self.process_current_config()

    def handles_last_call(self):
        """Returns whether this processor wants to be called at the end of a processing run again.

        If the preceding processor returns a non-None value, this is ignored and the processor is called anyway.

        Returns:
          bool: whether to call this processor for the 'special' last run
        """

        return False

    @abc.abstractmethod
    def process_current_config(self):
        """Processes the config url or content.

        Returns:
          object: processed config url or content
        """

        pass


class EnsureUrlProcessor(ConfigProcessor):
    """Makes sure the provided string is a url, then downloads the target and reads the content."""

    def get_config(self, config_file_url):
        """Retrieves the config (if necessary), and returns its content.

        Config can be either a path to a local yaml file, an url to a remote yaml file, or a json string.

        Args:
          config_file_url (str): the url/path/json content
        """

        # check if file first
        if os.path.exists(config_file_url):
            log.debug("Opening as file: {}".format(config_file_url))
            with io.open(config_file_url, encoding="utf-8") as f:
                content = f.read()

        # check if url
        elif config_file_url.startswith("http"):

            log.debug("Opening as url: {}".format(config_file_url))
            verify_ssl = True
            try:
                r = requests.get(config_file_url, verify=verify_ssl)
                r.raise_for_status()
                content = r.text
            except (Exception) as e:
                raise FrklConfigException(
                    "Could not retrieve url: {}".format(config_file_url), e
                )
        else:
            raise FrklConfigException(
                "Not a supported config file url or no local file found: {}".format(
                    config_file_url
                )
            )

        return content

    def process_current_config(self):

        result = self.get_config(self.current_input_config)
        return result


class ParentPathProcessor(ConfigProcessor):
    def get_output_format(self):
        return STRING_FORMAT

    def get_input_format(self):
        return STRING_FORMAT

    def process_current_config(self):

        url = self.current_input_config

        if not is_url_or_abbrev(url) and not os.path.isabs((url)):
            url = os.path.abspath(url)

        parent = os.path.dirname(url)

        return parent


class RemoveKeysProcessor(ConfigProcessor):
    def __init__(self, keys_to_remove=None, **kwargs):

        super(RemoveKeysProcessor, self).__init__(**kwargs)
        if keys_to_remove is None:
            keys_to_remove = []
        self.keys_to_remove = keys_to_remove

    def get_output_format(self):
        return DICT_FORMAT

    def get_input_format(self):
        return DICT_FORMAT

    def process_current_config(self):

        new_config = self.current_input_config

        if isinstance(new_config, (list, tuple, CommentedSeq)):
            for c in new_config:
                if isinstance(c, (dict, CommentedMap, OrderedDict)):
                    for key in self.keys_to_remove:
                        c.pop(key, None)

        elif isinstance(new_config, (dict, CommentedMap, OrderedDict)):
            for key in self.keys_to_remove:
                new_config.pop(key, None)

        return new_config


class EnsurePythonObjectProcessor(ConfigProcessor):
    """Makes sure the provided string is either valid yaml (or json -- not implemented yet), and converts it into a python object.

    Args:
        safe (bool): whether to use the 'safe' type for the yaml parser. This will destroy the order of any source dicts.
    """

    def __init__(self, safe_load=True, **kwargs):

        super(EnsurePythonObjectProcessor, self).__init__(**kwargs)
        self.safe_load = safe_load

    def get_output_format(self):
        return "PYTHON"

    def process_current_config(self):

        if not self.safe_load:
            temp = StringYAML()
            config_obj = temp.load(self.current_input_config)
        else:
            config_obj = yaml.load(self.current_input_config)
        return config_obj


class ToYamlProcessor(ConfigProcessor):
    """Takes a python object and returns the string representation.
    """

    def get_input_format(self):
        return PYTHON_FORMAT

    def get_output_format(self):
        return STRING_FORMAT

    def process_current_config(self):
        result = yaml.dump(self.current_input_config)
        return result


class IdProcessor(ConfigProcessor):
    """Adds an id to every config item."""

    def __init__(self, **init_params):

        super(IdProcessor, self).__init__(**init_params)
        self.id_type = init_params.get("id_type", "enumerate")
        self.id_name = init_params.get("id_name", "id")
        self.id_key = init_params.get("id_key", False)

        if not self.id_key:
            raise FrklConfigException("No 'id_key' value provided for IdProcessor")

        self.current_id = 0

    def get_input_format(self):
        return PYTHON_FORMAT

    def validate_init(self):

        return True

    def process_current_config(self):
        self.current_input_config[self.id_key][self.id_name] = self.current_id
        self.current_id = self.current_id + 1

        return self.current_input_config


class MergeProcessor(ConfigProcessor):
    """Gathers all configs and returns a list of all results as single element."""

    def __init__(self, **init_params):

        super(MergeProcessor, self).__init__(**init_params)

    def get_input_format(self):

        return ALL_FORMAT

    def new_config(self):
        if not self.last_call:
            self.configs.append(self.current_input_config)

    def process_current_config(self):

        if self.last_call:
            return self.configs
        else:
            return None

    def handles_last_call(self):
        return True


class DictInjectionProcessor(ConfigProcessor):
    """A processor to 'inject' dictionaries and dictionary values into other dictionaries, according to predefined rules.
    """

    def __init__(self, **init_params):

        super(DictInjectionProcessor, self).__init__(**init_params)
        self.injection_dicts = init_params["injection_dicts"]
        if isinstance(self.injection_dicts, dict):
            self.injection_dicts = [self.injection_dicts]

        self.on_top = init_params.get("merge_on_top", False)
        self.separator = init_params.get("key_separator", "/")

    def get_input_format(self):

        return PYTHON_FORMAT

    def process_current_config(self):

        config = self.current_input_config

        result = None
        for inj_dict in self.injection_dicts:

            for key, value in inj_dict.items():

                key_hierarchy = key.split(self.separator)
                current_config = config
                for part_key in key_hierarchy:

                    if part_key in current_config.keys():
                        current_config = current_config[part_key]
                    else:
                        current_config = None
                        break

                if not current_config or current_config not in value.keys():
                    continue

                merge_dict = inj_dict[key][current_config]

                if self.on_top:
                    result = dict_merge(config, merge_dict)
                else:
                    result = dict_merge(merge_dict, config)

                config = result

        return result


class FrklProcessor(ConfigProcessor):
    """A processor to 'expand' python dictionaries using a pre-defined schema.

    This is a bit more complicated to explain than I'd like it to be. For that reason, there is an extra
    page in the docs: link (XXX)
    """

    def __init__(self, **init_params):

        # self.stem_key = None
        # self.default_leaf_key = None
        # self.default_leaf_default_key = None
        # self.other_valid_keys = None
        # self.default_leaf_key_map = None
        # self.all_keys = None
        # self.use_context = None
        # self.values_so_far = None

        super(FrklProcessor, self).__init__(**init_params)

        self.stem_key = init_params[STEM_KEY_NAME]
        self.default_leaf_key = init_params[DEFAULT_LEAF_KEY_NAME]
        self.default_leaf_default_key = init_params.get(
            DEFAULT_LEAF_DEFAULT_KEY_NAME, None
        )
        if self.default_leaf_default_key is None:
            raise FrklConfigException("No default leaf default key specified.")
        self.other_valid_keys = init_params.get(OTHER_VALID_KEYS_NAME, [])
        self.default_leaf_key_map = init_params.get(DEFAULT_LEAF_KEY_MAP_NAME, None)
        if self.default_leaf_key_map is None:
            self.default_leaf_key_map = self.default_leaf_key

        if isinstance(self.default_leaf_key_map, string_types):
            if "/" in self.default_leaf_key_map:
                tokens = self.default_leaf_key_map.split("/")
                if not len(tokens) == 2:
                    raise FrklConfigException(
                        "Default value for move_key_map can't be parsed as it has more than 2 parts (separated by '/': {})".format(
                            self.default_leaf_key_map
                        )
                    )
                self.default_leaf_key_map = {"*": (tokens[0], tokens[1])}
            else:
                self.default_leaf_key_map = {
                    "*": (self.default_leaf_key_map, DEFAULT_LEAF_DEFAULT_KEY)
                }
        elif isinstance(self.default_leaf_key_map, dict):
            # make sure the move_key_map has the right format
            for key in self.default_leaf_key_map.keys():
                value = self.default_leaf_key_map[key]
                if isinstance(value, (list, tuple)):
                    if not len(value) == 2:
                        raise FrklConfigException(
                            "Value for move_key_map can't be parsed as it has more than 2 parts (separated by '/': {})".format(
                                value
                            )
                        )
                    self.default_leaf_key_map[key] = value
                else:
                    if not isinstance(value, string_types) and not len(value) == 2:
                        raise FrklConfigException(
                            "move_key_map needs a list or tuple as value type with length '2': {}".format(
                                self.default_leaf_key_map
                            )
                        )

                    if "/" in value:
                        tokens = value.split("/")

                        if not len(tokens) == 2:
                            raise FrklConfigException(
                                "Value for move_key_map can't be parsed as it has more than 2 parts (separated by '/': {})".format(
                                    value
                                )
                            )
                        self.default_leaf_key_map[key] = (tokens[0], tokens[1])
                    else:
                        self.default_leaf_key_map[key] = (
                            value,
                            DEFAULT_LEAF_DEFAULT_KEY,
                        )

        else:
            raise FrklConfigException(
                "Type '{}' not supported for move_key_map.".format(
                    type(self.default_leaf_key_map)
                )
            )

        self.all_keys = set([self.stem_key, self.default_leaf_key])
        self.all_keys.update(self.other_valid_keys)

        for item in self.default_leaf_key_map.values():
            self.all_keys.add(item[0])

        self.use_context = init_params.get("use_context", False)
        if self.use_context and isinstance(self.use_context, bool):
            self.use_context = FRKL_CONTEXT_DEFAULT_KEY
        elif self.use_context and not isinstance(self.use_context, string_types):
            raise FrklConfigException(
                "'use_context' keyword needs to be of type bool or string: {}".format(
                    init_params
                )
            )

        if START_VALUES_NAME in init_params.keys():
            self.values_so_far = init_params[START_VALUES_NAME]
        else:
            self.values_so_far = {}

        self.configs = []

    def get_input_format(self):

        return PYTHON_FORMAT

    def new_config(self):

        # make sure the new value is a dict, with only allowed keys
        if isinstance(self.current_input_config, (list, tuple)):
            self.configs.extend(self.current_input_config)
        else:
            self.configs.append(self.current_input_config)

        if self.use_context:
            self.current_context[self.use_context] = self.values_so_far

    def process_current_config(self):

        result = self.frklize(self.current_input_config, self.values_so_far)
        return result

    def frklize(self, config, current_vars):
        """Recursively called function which generates (expands) and yields dictionaries matching
        certain criteria (containing leaf_node keys, for example).

        Args:
          config (object): the input config
          current_vars (dict): current state of the (overlayed) var cache
        """

        # making sure the new value is a dict, with only allowed keys
        if isinstance(config, string_types):
            config = {self.default_leaf_key: {self.default_leaf_default_key: config}}

        if isinstance(config, (list, tuple, Sequence)):
            for item in config:
                for result in self.frklize(item, copy.deepcopy(current_vars)):
                    yield result
        else:

            if not isinstance(config, (dict, CommentedMap, OrderedDict)):

                raise FrklConfigException(
                    "Not a supported type for value '{}': {}".format(
                        config, type(config)
                    )
                )

            new_value = {}

            # check whether any of the known keys is available here, if not,
            # we check whether there is a default key registered for the name of the keys
            if not any(x in config.keys() for x in self.all_keys):

                if not len(config) == 1:
                    raise FrklConfigException(
                        "This form of configuration is not implemented yet (can't have more than one key if key is not among the known keys): {} -- current vars: {}".format(
                            config, current_vars
                        )
                    )
                else:
                    key = next(iter(config))
                    value = config[key]

                    insert_leaf_key = self.default_leaf_key
                    insert_leaf_key_key = self.default_leaf_default_key
                    new_value.setdefault(insert_leaf_key, {})[insert_leaf_key_key] = key

                    if not isinstance(value, dict):
                        if key in self.default_leaf_key_map.keys():
                            val_key = self.default_leaf_key_map[key][0]
                            val_key_key = self.default_leaf_key_map[key][1]
                        elif "*" in self.default_leaf_key_map.keys():
                            val_key = self.default_leaf_key_map["*"][0]
                            val_key_key = self.default_leaf_key_map["*"][1]
                        else:
                            raise FrklConfigException(
                                "Can't find entry in move_key_map for key '{}' in order to move value: {}"
                            ).format(key, value)
                        new_value.setdefault(val_key, {})[val_key_key] = value

                    else:
                        if all(x in self.all_keys for x in value.keys()):
                            dict_merge(new_value, value, copy_dct=False)
                        elif all(x not in self.all_keys for x in value.keys()):
                            if key in self.default_leaf_key_map.keys():
                                migrate_key = self.default_leaf_key_map[key][0]
                            elif "*" in self.default_leaf_key_map.keys():
                                migrate_key = self.default_leaf_key_map["*"][0]
                            else:
                                raise FrklConfigException(
                                    "Can't find default_leaf_key to move values of key '{}".format(
                                        key
                                    )
                                )

                            new_value.setdefault(migrate_key, {}).update(value)
                            new_value[migrate_key].update(value)
                        else:
                            for key, value in value.items():

                                if key in self.all_keys:
                                    if isinstance(value, dict):
                                        dict_merge(
                                            new_value.setdefault(key, {}),
                                            value,
                                            copy_dct=False,
                                        )
                                    else:
                                        new_value[key] = value

                                else:
                                    if key in self.default_leaf_key_map.keys():
                                        migrate_key = self.default_leaf_key_map[key][0]
                                    elif "*" in self.default_leaf_key_map.keys():
                                        migrate_key = self.default_leaf_key_map["*"][0]
                                    else:
                                        raise FrklConfigException(
                                            "Can't find default_leaf_key to move values of key '{}".format(
                                                key
                                            )
                                        )

                                    if isinstance(value, dict):
                                        new_value.setdefault(migrate_key, {}).update(
                                            value
                                        )
                                        new_value[migrate_key].update(value)
                                    else:
                                        new_value.setdefault(migrate_key, {})[
                                            key
                                        ] = value

                            # raise FrklConfigException("Mixed keys.")

            else:
                # check whether all keys are allowed

                for key in config.keys():
                    if key not in self.all_keys:
                        raise FrklConfigException(
                            "Key '{}' not allowed, since it is an unknown keys amongst known keys in config: {}".format(
                                key, config
                            )
                        )

                new_value = config

                # if self.stem_key in new_value.keys() and self.default_leaf_key in new_value.keys():
                # raise FrklConfigException(
                # "Configuration can't have both stem key ({}) and default leaf key ({}) on the same level: {}".
                # format(self.stem_key, self.default_leaf_key, new_value))

            # at this point we have an 'expanded' dict

            stem_branch = new_value.pop(self.stem_key, NO_STEM_INDICATOR)
            # merge new values with current_vars
            dict_merge(current_vars, new_value, copy_dct=False)
            # TODO: check if this needs deepcopy
            new_value = copy.copy(current_vars)

            if stem_branch == NO_STEM_INDICATOR:
                # TODO: double check logic here
                # if self.default_leaf_key in new_value.keys() and self.default_leaf_default_key in new_value[self.default_leaf_key].keys():
                if self.default_leaf_key in new_value.keys():
                    yield new_value

            else:
                # TODO: check if this needs deepcopy
                for item in self.frklize(stem_branch, copy.copy(current_vars)):
                    yield item


class Jinja2TemplateProcessor(ConfigProcessor):
    """Processor to replace all occurrences of Jinja template strings with values (predefined,
    or potentially dynamically processed in an earlier step).

    Args:
        template_values (dict): a dictionary containing the values to replace template strings with
        use_environment_vars (bool): whether to also use current environment variables  in the replacement dict. If True, it'll stored under the key 'LOCAL_ENV', if string, that will be used as key
        use_context (bool): whether to also use the frkl context in the replacement dict.  If True, it'll stored under the key 'frkl_vars', if string, that will be used as key
        delimiter_profile (dict): the jinja2 delimters
        **init_params (dict): additional config for the parent class
    """

    def __init__(
        self,
        template_values=None,
        use_environment_vars=False,
        use_context=False,
        delimiter_profile=JINJA_DELIMITER_PROFILES["default"],
        **init_params
    ):

        super(Jinja2TemplateProcessor, self).__init__(**init_params)
        if not template_values:
            template_values = {}
        self.template_values = template_values
        self.use_environment_vars = use_environment_vars
        if self.use_environment_vars and isinstance(self.use_environment_vars, bool):
            self.use_environment_vars = DEFAULT_LOCAL_ENV_VARS_KEY
        elif self.use_environment_vars and not isinstance(
            self.use_environment_vars, string_types
        ):
            raise FrklConfigException(
                "'use_environment_vars' keyword needs to be of type bool or string: {}".format(
                    use_environment_vars
                )
            )

        self.use_context = use_context
        if self.use_context and isinstance(self.use_context, bool):
            self.use_context = FRKL_CONTEXT_DEFAULT_KEY
        elif self.use_context and not isinstance(self.use_context, string_types):
            raise FrklConfigException(
                "'use_context' keyword needs to be of type bool or string: {}".format(
                    use_context
                )
            )
        self.jinja_env = Environment(**delimiter_profile)

    def get_input_format(self):

        return STRING_FORMAT

    def process_current_config(self):

        old_string = self.current_input_config

        env = {}

        if self.use_context:
            frkl_vars = self.current_context.get(self.use_context, {})
            dict_merge(env, frkl_vars, copy_dct=False)

        dict_merge(env, self.template_values, copy_dct=False)

        new_string = replace_string(
            old_string,
            replacement_dict=env,
            jinja_env=self.jinja_env,
            local_env_vars_key=self.use_environment_vars,
        )
        return new_string


class YamlTextSplitProcessor(ConfigProcessor):
    """Splits a string if it can find certain keywords at the beginning of a line.

    Args:
        keywords (list): a list of keywords
    """

    def __init__(self, **init_params):

        super(YamlTextSplitProcessor, self).__init__(**init_params)
        self.keywords = init_params["keywords"]
        self.current_lines = []

    def get_input_format(self):
        return STRING_FORMAT

    def process_current_config(self):

        if self.last_call:
            if self.current_lines:
                yield "\n".join(self.current_lines)
        else:
            new_config = self.current_input_config

            for line in new_config.splitlines():
                if self.current_lines and any(
                    line.startswith(keyword) for keyword in self.keywords
                ):
                    yield "\n".join(self.current_lines)
                    self.current_lines = [line]
                else:
                    self.current_lines.append(line)

    def handles_last_call(self):
        return True


class RegexProcessor(ConfigProcessor):
    """Replaces all occurences of regex matches.

    Args:
        regexes (dict): a map of regexes and their replacements
    """

    def __init__(self, **init_params):

        super(RegexProcessor, self).__init__(**init_params)
        self.regexes = init_params["regexes"]

    def get_input_format(self):
        return STRING_FORMAT

    def process_current_config(self):
        new_config = self.current_input_config

        for regex, replacement in self.regexes.items():
            new_config = re.sub(regex, replacement, new_config)

        return new_config


class LoadMoreConfigsProcessor(ConfigProcessor):
    """Processort to load additional configs from configs.

    If an incoming configuration is a list of strings, it'll interprete it as list of
    urls and adds it in front of the list of 'yet-to-process' configs of this processing run.

    Use this with caution, since if this gets a list of string that is not a list of urls, it
    will still treat it like one and your run will fail.
    """

    def get_input_format(self):

        return PYTHON_FORMAT

    def get_output_format(self):

        return NONE_FORMAT

    def process_current_config(self):

        if is_list_of_strings(self.current_input_config):
            return None
        else:
            return self.current_input_config

    def get_additional_configs(self):

        if is_list_of_strings(self.current_input_config):
            return self.current_input_config
        else:
            return None


class UrlAbbrevProcessor(ConfigProcessor):
    """Replaces strings in an input configuration url with its expanded version.

    The default constructor without any arguments will create a processor only using the default, inbuilt abbreviations

    """

    def __init__(self, **init_params):

        super(UrlAbbrevProcessor, self).__init__(**init_params)

        abbrevs = init_params.get("abbrevs", False)
        add_default_abbrevs = init_params.get("add_default_abbrevs", True)

        if not abbrevs:
            if add_default_abbrevs:
                self.abbrevs = DEFAULT_URL_ABBREVIATIONS_FILE
            else:
                self.abbrevs = {}
        else:
            if add_default_abbrevs:
                self.abbrevs = copy.deepcopy(DEFAULT_URL_ABBREVIATIONS_FILE)
                dict_merge(self.abbrevs, abbrevs, copy_dct=False)
            else:
                self.abbrevs = copy.deepcopy(abbrevs)

        self.verbose = init_params.get("verbose", False)
        self.opt_split_string = "::"

    def get_input_format(self):

        return STRING_FORMAT

    def process_current_config(self):

        result = self.expand_config(self.current_input_config)
        return result

    def expand_config(self, config):
        """Expands abbreviated configuration urls that start with `<token>:`.

        This is a convenience for the user, as they don't have to type out long urls if they don't want to.

        To make it easier to remember (and shorter to type) config urls, *frkl*
        supports abbreviations which will be replaced before attempting to load a
        configuration. In addition to inbuild abbreviations, a custom ones can be
        piped into the Frkl constructor. This needs to be a dictionary of string to
        string (abbreviation -> full url-part, eg. ``freckles_configs -->
        https://raw.githubusercontent.com/makkus/freckles/master/examples``, which
        would enable the user to provide this config url:
        ``freckles_config:quickstart.yml``) or string to list (abbreviation -> list
        of tokens to assemble the finished string, which for example for getting
        raw files from the master branch of a github repo would look like:
        ["https://raw.githubusercontent.com", frutils.defaults.URL_PLACEHOLDER, frutils.defaults.URL_PLACEHOLDER,
        "master] -- the input config ``gh:makkus/freckles/examples/quickstart.yml``
        would result in the same string as in the first example above -- this
        method is a bit more fragile, because the input string can't have less
        tokens seperated by '/' than the value list).

        Args:
          config (str): the configuration url/json/etc...

        Returns:
          str: the configuration with all occurances of registered abbreviations replaced

        """

        # check if string contains branch information
        branch = None
        opt_split_string = "::"
        if opt_split_string in config:
            tokens = config.split(opt_split_string)
            opt = tokens[1:-1]
            if not opt:
                raise Exception(
                    "Not a valid url, needs at least 2 split strings ('{}')".format(
                        opt_split_string
                    )
                )
            if len(opt) != 1:
                raise Exception(
                    "Not a valid url, can only have 1 branch: {}".format(opt)
                )
            branch = opt[0]

        prefix, sep, rest = config.partition(":")

        if self.opt_split_string in rest:
            tokens = rest.split(self.opt_split_string)
            rest = "{}{}".format(tokens[0], tokens[-1])
            opt = tokens[1:-1]
            if not opt:
                raise Exception(
                    "Invalid url, need at least two option splitters ('{}'): {}".format(
                        self.opt_split_string, config
                    )
                )
        else:
            opt = None

        if prefix in self.abbrevs.keys():

            if isinstance(self.abbrevs[prefix], string_types):
                return "{}{}".format(self.abbrevs[prefix], rest)
            else:
                tokens = rest.split("/")
                tokens_copy = copy.copy(tokens)

                min_tokens = self.abbrevs[prefix].count(URL_PLACEHOLDER)

                result_string = ""
                for t in self.abbrevs[prefix]:

                    if t == URL_PLACEHOLDER:
                        if not tokens:
                            raise FrklConfigException(
                                "Can't expand url '{}': not enough parts, need at least {} parts seperated by '/' after ':'".format(
                                    config, min_tokens
                                )
                            )
                        to_append = tokens.pop(0)
                        if not to_append:
                            raise FrklConfigException(
                                "Last token empty, can't expand: {}".format(tokens_copy)
                            )
                    else:
                        to_append = t

                    result_string += to_append

                if tokens:
                    postfix = "/".join(tokens)
                    result_string += postfix

                # if opt:
                #    opt_appendix = "::".join(opt)

                if string_is_templated(result_string, DEFAULT_FRKL_JINJA_ENVIRONMENT):

                    if branch:
                        repl_dict = {"branch": branch}
                    else:
                        repl_dict = {"branch": "master"}

                    result_string = replace_string(
                        result_string,
                        repl_dict,
                        jinja_env=DEFAULT_FRKL_JINJA_ENVIRONMENT,
                        local_env_vars_key=False,
                    )

                if self.verbose:
                    print("Expanding '{}' -> '{}'".format(config, result_string))

                return result_string
        else:
            return config
