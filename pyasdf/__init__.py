# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals, print_function

"""
pyasdf: Python library for reading and writing Advanced Scientific
Data Format (ASDF) files
"""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

__all__ = ['AsdfFile', 'AsdfType', 'AsdfExtension',
           'Stream', 'open', 'test', 'commands',
           'ValidationError']


from .asdf import AsdfFile
from .asdftypes import AsdfType
from .extension import AsdfExtension
from .stream import Stream
from . import commands

from jsonschema import ValidationError


open = AsdfFile.read
