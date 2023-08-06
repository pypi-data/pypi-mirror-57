#!/usr/bin/env python3
# coding: utf-8
"""
Allows accessing the module
"""
from .etna import EtnaWrapper
import etna.watcher as watcher


__all__ = ["EtnaWrapper", "watcher"]
