# -*- coding: utf-8 -*-

# python 3 compatibility
from __future__ import absolute_import, division, print_function, unicode_literals

import copy
import logging
import os
import sys

from frutils import StringYAML
from frutils.defaults import (
    DEFAULT_URL_ABBREVIATIONS_FILE,
    DEFAULT_URL_ABBREVIATIONS_REPO,
    JINJA_DELIMITER_PROFILES,
)
from ruamel.yaml.comments import CommentedSeq
from six import string_types
from stevedore import driver

from frkl import load_string_from_url_or_path

from .exceptions import FrklistConfigException

GLOBAL_ENV_ID_COUNTER = 1110
GLOBAL_TASKLIST_ID_COUNTER = 1110


def GLOBAL_TASKLIST_ID():
    global GLOBAL_TASKLIST_ID_COUNTER
    GLOBAL_TASKLIST_ID_COUNTER = GLOBAL_TASKLIST_ID_COUNTER + 1
    return GLOBAL_TASKLIST_ID_COUNTER


def GLOBAL_ENV_ID():
    global GLOBAL_ENV_ID_COUNTER
    GLOBAL_ENV_ID_COUNTER = GLOBAL_ENV_ID_COUNTER + 1
    return GLOBAL_ENV_ID_COUNTER


yaml = StringYAML()
yaml.default_flow_style = False

log = logging.getLogger("nsbl")


def create_tasklist(tasklist, context=None, meta=None, vars=None):
    """Loading the tasklist class

    Args:
      name (str): the registered name of the extension
      init_params (dict): the parameters to initialize the extension object

    Returns:
      DictletFinder: the extension object
    """

    log2 = logging.getLogger("stevedore")
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(logging.Formatter("freckles plugin error -> %(message)s"))
    out_hdlr.setLevel(logging.DEBUG)
    log2.addHandler(out_hdlr)
    log2.setLevel(logging.INFO)

    if context is None:
        context = {}

    if meta is None:
        meta = {}

    if vars is None:
        vars = {}

    plugin_name = meta.get("tasklist-type", "default")

    log.debug("Loading freckles tasklist plugin '{}'...")

    mgr = driver.DriverManager(
        namespace="frkl.frkists",
        name=plugin_name,
        invoke_on_load=True,
        invoke_args=(tasklist,),
        invoke_kwds={"context": context, "meta": meta, "vars": vars},
    )

    log.debug(
        "Registered frklist: {}".format(", ".join(ext.name for ext in mgr.extensions))
    )

    return mgr.driver


class Frklist(object):
    def __init__(self, itemlist, context=None, meta=None, vars=None):

        self.itemlist_raw = itemlist
        if context is None:
            context = FrklistContext()
        self.context = context
        # if not isinstance(context, FrklistContext):
        #     self.context = copy.deepcopy(context)
        #     self.context = self.create_context(self.context)
        # else:
        #     self.context = context
        self.itemlist_raw_type = None

        if meta is None:
            meta = {}
        else:
            meta = copy.deepcopy(meta)
        self.meta = self.process_meta_properties(meta, copy.deepcopy(itemlist))

        self.itemlist_id = self.meta["list_id"]
        self.env_id = self.meta["env_id"]

        if vars is None:
            vars = {}
        else:
            vars = copy.deepcopy(vars)
        self.vars = vars

        self.itemlist_pre = self.preprocess_tasklist(
            copy.deepcopy(itemlist),
            self.context,
            copy.deepcopy(self.meta),
            copy.deepcopy(self.vars),
        )

        self.itemlist = self.expand_and_augment_tasklist(self.itemlist_pre)

    def preprocess_tasklist(self, tasklist, context, meta, vars):

        if isinstance(tasklist, string_types):
            self.itemlist_raw_type = "string"
            content = load_string_from_url_or_path(
                tasklist,
                create_python_object=True,
                template_vars=vars,
                use_environment_vars=True,
                delimiter_profile=JINJA_DELIMITER_PROFILES["freckles"],
            )
            return content
        elif isinstance(tasklist, (list, tuple, CommentedSeq)):
            self.itemlist_raw_type = "list"
            return tasklist
        else:
            raise FrklistConfigException(
                "Invalid type for tasklist: {}".format(type(tasklist))
            )

    def process_meta_properties(self, meta_dict, tasklist):

        if "list_id" not in meta_dict.keys():
            meta_dict["list_id"] = GLOBAL_TASKLIST_ID()
        if "env_id" not in meta_dict.keys():
            meta_dict["env_id"] = GLOBAL_ENV_ID()

        if isinstance(tasklist, string_types):
            meta_dict["itemlist_raw_type"] = "string"
            if "itemlist_parent" not in meta_dict.keys():
                meta_dict["itemlist_parent"] = os.path.dirname(tasklist)
        else:
            meta_dict["itemlist_raw_type"] = "list"
            if "itemlist_parent" not in meta_dict.keys():
                meta_dict["itemlist_parent"] = None

        return meta_dict

    def render_tasklist(self, **kwargs):

        return yaml.dump(self.itemlist)

    def expand_and_augment_tasklist(self, tasklist):

        return tasklist

    # def create_context(self, context_params):
    #
    #     return FrklistContext()


class DefaultFrklist(Frklist):
    def __init__(self, itemlist, **kwargs):

        super(DefaultFrklist, self).__init__(itemlist, **kwargs)


class FrklistContext(object):
    def __init__(
        self,
        base_directory=None,
        allow_remote=False,
        allow_untrusted_urls=False,
        trusted_urls=None,
        abbrevs=None,
        urls=None,
    ):
        """The context a tasklist lives in.

        This is shared among all the tasklists of the same type.

        Args:
            base_directory (str): the directory to be used for relative paths, defaults to 'os.getcwd()'
            allow_remote (bool): whether to allow the auto-download of remote artefacts (Ansible roles, tasklists, etc.
            allow_untrusted_urls (bool): if 'allow_remote', allow the download of urls that don't start with strings not contained in 'trusted_urls'
            trusted_urls (list): a list of urls (and/or abbrevs) indicating urls to download from (if 'allow_untrsuted_urls' is False
            abbrevs (dict): a dictionary of abbreviation mappings in the form of {<abbrev_alias>: <abbrev_dict>}
            urls (dict): a dictionary of paths, sorted by the type of artefacts they hold (e.g. task-aliases, Ansible roles, etc.)
        """

        if base_directory is None:
            base_directory = os.getcwd()
        self.base_directory = base_directory

        self.allow_remote = allow_remote
        self.allow_untrusted_urls = allow_untrusted_urls
        if trusted_urls is None:
            trusted_urls = []

        if self.allow_remote and not self.allow_untrusted_urls and not trusted_urls:
            log.warn(
                "'allow_untrusted_urls' is set to false, but no trusted_urls specified, setting 'allow_remote' to false"
            )
            self.allow_remote = False

        if not abbrevs:
            abbrevs = {
                "file": DEFAULT_URL_ABBREVIATIONS_FILE,
                "repo": DEFAULT_URL_ABBREVIATIONS_REPO,
            }
        self.abbrevs = abbrevs

        if urls is None:
            self.urls = {}
        else:
            self.urls = self.cleanup_environment_paths(urls)

    def cleanup_environment_paths(self, environment_paths):

        result = {}
        for path_type, paths in environment_paths.items():

            if not paths:
                paths = []
            if isinstance(paths, string_types):
                paths = [paths]
            elif isinstance(paths, tuple):
                paths = list(paths)

            paths[:] = [os.path.realpath(os.path.expanduser(p)) for p in paths]

            paths[:] = [p for p in paths if os.path.exists(p)]
            result[path_type] = paths

        return result
