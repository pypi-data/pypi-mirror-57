# -*- coding: utf-8 -*-
import io
import os

from pkg_resources import DistributionNotFound, get_distribution

# flake8: noqa

from .defaults import DEFAULT_FRKL_JINJA_ENVIRONMENT
from .frkl import (
    Frkl,
    load_object_from_url_or_path,
    load_string_from_url_or_path,
    load_templated_string_from_url_chain,
)
from .frklist import Frklist, FrklistContext
from .helpers import content_from_url, dict_from_url, download_cached_file, get_full_url
from .processors import (
    EnsurePythonObjectProcessor,
    EnsureUrlProcessor,
    FrklProcessor,
    LoadMoreConfigsProcessor,
    UrlAbbrevProcessor,
)
from .utils import VarsType

__author__ = """Markus Binsteiner"""
__email__ = "makkus@posteo.de"

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    try:
        version_file = os.path.join(os.path.dirname(__file__), "version.txt")

        if os.path.exists(version_file):
            with io.open(version_file, encoding="utf-8") as vf:
                __version__ = vf.read()
        else:
            __version__ = "unknown"

    except (Exception):
        pass

    if __version__ is None:
        __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound
