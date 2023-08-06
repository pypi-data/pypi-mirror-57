# -*- coding: utf-8 -*-

__title__ = "shinkei"
__author__ = "Lorenzo"
__license__ = "MIT"
__copyright__ = "Copyright 2019 Lorenzo"
__docformat__ = "restructedtext en"
__version__ = "0.1.6"

import logging

from . import ext  # noqa: F401
from .client import Client, connect  # noqa: F401
from .exceptions import *  # noqa: F401
from .handlers import Handler, HandlerMeta, listens_to  # noqa: F401
from .objects import MetadataPayload, Version, VersionMetadata  # noqa: F401
from .querybuilder import Node, QueryBuilder  # noqa: F401

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, _):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
