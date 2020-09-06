#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
.. __init__

Initialisation module of `pygridmap` package.

**Contents**
"""

# *credits*:      `gjacopo <jacopo.grazzini@ec.europa.eu>`_ 
# *since*:        June 2020

from os import path as osp

__THISFILE          = __file__ # useles...
__THISDIR           = osp.dirname(__THISFILE)

__all__             = ['base', 'gridding', 'overlay']#analysis:ignore
