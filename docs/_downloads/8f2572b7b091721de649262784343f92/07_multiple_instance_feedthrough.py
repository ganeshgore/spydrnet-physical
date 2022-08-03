#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================
Generating feedthrough from multiple instances
==============================================

This example demonstrates how to generate feedthrough from multiple instances.
If multiple instances belong to the same reference module it should reuser 
the feedthrough instead of creating independent feedthrough to pass through each instance.

"""

import logging

import spydrnet as sdn
import spydrnet_physical as sdnphy

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')

# TODO
logger.warning("NotImplemented")
