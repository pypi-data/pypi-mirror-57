# -*- coding: utf-8 -*-
"""Setup helper library.
"""
from __future__ import absolute_import
from __future__ import print_function


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "1ba7bffb-c00b-4691-a3e9-e392f968e437"

__version__ = "01.01.001"

import os,sys

import fnmatch
import re
import tempfile
import shutil


class SetupJavaXError(Exception):
    pass

