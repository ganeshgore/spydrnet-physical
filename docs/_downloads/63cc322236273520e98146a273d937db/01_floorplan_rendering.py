'''
=========================================
Demonstrate how to render basic floorplan
=========================================


.. include:: ../../../../spydrnet_physical/util/FloorPlanViz.py
    :start-after: """
    :end-before: """

Output
======

Download final annotated verilog netlist:
:download:`_annotate_netlist.v <../../../../examples/OpenFPGA/rendering/_annotate_netlist.v>`

.. image:: ../../../../examples/OpenFPGA/rendering/_basic_hierarchy_floorplan.svg
    :width: 500px

'''


import logging
from os import path
from pprint import pprint

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.util import FloorPlanViz

PROPERTY = "VERILOG.InlineConstraints"

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='DEBUG', filename="01_floorplan_rendering")

netlist = sdnphy.load_netlist_by_name('basic_hierarchy')
top = netlist.top_instance.reference

module1 = next(netlist.get_definitions("module1"))
module2 = next(netlist.get_definitions("module2"))

inst_1_0 = next(top.get_instances("inst_1_0"))
inst_1_1 = next(top.get_instances("inst_1_1"))

inst_2_0 = next(top.get_instances("inst_2_0"))
inst_2_1 = next(top.get_instances("inst_2_1"))


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#         Set the WIDTH HEIGHT on the defition
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

top.properties["WIDTH"] = "250"
top.properties["HEIGHT"] = "250"

module1.properties["HEIGHT"] = "60"
module1.properties["HEIGHT"] = "60"

module2.properties["HEIGHT"] = "40"
module2.properties["HEIGHT"] = "40"


module1.properties["SHAPE"] = "cross"  # cross Shape
module1.properties["POINTS"] = [25, 25, 25, 25, 25, 25]  # A, B, C, D , E, F

module2.properties["SHAPE"] = "custom"  # cross Shape
module2.properties["POINTS"] = "V 0 0 10 -10 10 30 -20 -20"

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#         Set the Pin locations on the Modules
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

next(top.get_ports("in0")).properties["SIDE"] = "left"
next(top.get_ports("in0")).properties["OFFSET"] = "10"

next(top.get_ports("in1")).properties["SIDE"] = "left"
next(top.get_ports("in1")).properties["OFFSET"] = "30"

next(top.get_ports("bus_in")).properties["SIDE"] = "left"
next(top.get_ports("bus_in")).properties["OFFSET"] = "50"

next(top.get_ports("out0")).properties["SIDE"] = "right"
next(top.get_ports("out0")).properties["OFFSET"] = "20"

next(top.get_ports("bus_out")).properties["SIDE"] = "right"
next(top.get_ports("bus_out")).properties["OFFSET"] = "40"

next(module1.get_ports("in0")).properties["SIDE"] = "top"
next(module1.get_ports("in0")).properties["SIDE2"] = "right"
next(module1.get_ports("in0")).properties["OFFSET"] = "10"

next(module1.get_ports("in1")).properties["SIDE"] = "left"
next(module1.get_ports("in1")).properties["OFFSET"] = "10"

next(module1.get_ports("out")).properties["SIDE"] = "right"
next(module1.get_ports("out")).properties["OFFSET"] = "20"

next(module2.get_ports("in0")).properties["SIDE"] = "left"
next(module2.get_ports("in0")).properties["OFFSET"] = "10"

next(module2.get_ports("in1")).properties["SIDE"] = "left"
next(module2.get_ports("in1")).properties["OFFSET"] = "30"

next(module2.get_ports("out")).properties["SIDE"] = "right"
next(module2.get_ports("out")).properties["OFFSET"] = "20"

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#         Set the LOC_X, LOC_Y on all the instances
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

inst_1_0.properties["LOC_X"] = "50"
inst_1_0.properties["LOC_Y"] = "50"

inst_1_1.properties["LOC_X"] = "50"
inst_1_1.properties["LOC_Y"] = "150"

inst_2_0.properties["LOC_X"] = "150"
inst_2_0.properties["LOC_Y"] = "50"

inst_2_1.properties["LOC_X"] = "150"
inst_2_1.properties["LOC_Y"] = "150"


fp = FloorPlanViz(top)
fp.compose(skip_connections=False)
dwg = fp.get_svg()
dwg.saveas("_basic_hierarchy_floorplan.svg", pretty=True, indent=4)

sdn.compose(netlist, '_annotate_netlist.v')
