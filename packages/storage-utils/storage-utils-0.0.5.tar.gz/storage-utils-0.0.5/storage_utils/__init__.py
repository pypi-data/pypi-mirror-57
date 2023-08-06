#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
if platform.system() != "Windows":
    from .local import *
from .s3 import *
from .hdfs import *

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
