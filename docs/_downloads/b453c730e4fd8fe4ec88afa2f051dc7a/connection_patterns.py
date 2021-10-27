"""
==============================
Connection Pattern Generation
==============================

This example demonstrate how to genrate different connection pattern
for routing global signals


**Output2** Fishbone routing pattern gerneation

.. image:: ../../../examples/OpenFPGA/_fishbone_pattern.svg
    :width: 300px

.. image:: ../../../examples/OpenFPGA/_fishbone_pattern_90.svg
    :width: 300px

"""

from os import path
import spydrnet as sdn
from spydrnet_physical.util.connection_pattern import ConnectionPattern

p_manager = ConnectionPattern(5, 5)
fishbone_pattern = p_manager.get_fishbone()
p_manager.render_pattern().saveas("_fishbone_pattern.svg",pretty=True, indent=4)
fishbone_pattern.rotate(90)
p_manager.render_pattern().saveas("_fishbone_pattern_90.svg",pretty=True, indent=4)

