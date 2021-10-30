"""
=========================================
Demonstrate how to render basic floorplan
=========================================

Properties on different objects

**On Definitions**
WIDTH and HEIGHT = The rectangular dimension of the module

**On Instances**:
LOC_X and LOC_Y = Location of the component with respect to its parrent

**On Ports**:
_SIDE      : On whihc side the port is placed [left/right/bottom/top]
_OFFSET    : Offset from the origin of that side, Considering clockwise direction
first point on respective side is considered as origin


Download final annotated verilog netlist:
:download:`_annotate_netlist.v <../../../examples/OpenFPGA/_annotate_netlist.v>`

.. image:: ../../../examples/OpenFPGA/_basic_hierarchy_floorplan.svg
    :width: 500px

"""


from os import path
import spydrnet as sdn
from pprint import pprint
import spydrnet_physical as sdnphy
from spydrnet_physical.util.get_floorplan import FloorPlanViz

PROPERTY = "VERILOG.InlineConstraints"

netlist = sdnphy.load_netlist_by_name('basic_hierarchy')
top = netlist.top_instance.reference

module1 = next(netlist.get_definitions("module1"))
module2 = next(netlist.get_definitions("module2"))

inst_1_0 = next(top.get_instances("inst_1_0"))
inst_1_1 = next(top.get_instances("inst_1_1"))

inst_2_0 = next(top.get_instances("inst_2_0"))
inst_2_1 = next(top.get_instances("inst_2_1"))

top.properties["WIDTH"] = "250"
top.properties["HEIGHT"] = "250"

inst_1_0.properties["LOC_X"] = "50"
inst_1_0.properties["LOC_Y"] = "50"

inst_1_1.properties["LOC_X"] = "50"
inst_1_1.properties["LOC_Y"] = "150"

inst_2_0.properties["LOC_X"] = "150"
inst_2_0.properties["LOC_Y"] = "50"

inst_2_1.properties["LOC_X"] = "150"
inst_2_1.properties["LOC_Y"] = "150"


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

next(module1.get_ports("in0")).properties["SIDE"] = "left"
next(module1.get_ports("in0")).properties["OFFSET"] = "10"

next(module1.get_ports("in1")).properties["SIDE"] = "left"
next(module1.get_ports("in1")).properties["OFFSET"] = "30"

next(module1.get_ports("out")).properties["SIDE"] = "right"
next(module1.get_ports("out")).properties["OFFSET"] = "20"

next(module2.get_ports("in0")).properties["SIDE"] = "left"
next(module2.get_ports("in0")).properties["OFFSET"] = "10"

next(module2.get_ports("in1")).properties["SIDE"] = "left"
next(module2.get_ports("in1")).properties["OFFSET"] = "30"

next(module2.get_ports("out")).properties["SIDE"] = "right"
next(module2.get_ports("out")).properties["OFFSET"] = "20"

top.get_ports()

fp = FloorPlanViz(top)
fp.compose()
dwg = fp.get_svg()
dwg.saveas("_basic_hierarchy_floorplan.svg", pretty=True, indent=4)

sdn.compose(netlist, '_annotate_netlist.v', write_constrains=True)
