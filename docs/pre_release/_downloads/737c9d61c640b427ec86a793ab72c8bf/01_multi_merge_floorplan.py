'''
=========================================
Demonstrate how to render basic floorplan
=========================================

Output
======

.. image:: ../../../examples/OpenFPGA_rendering/_merge_multiple_floorplan_before.svg
    :width: 400px

.. image:: ../../../examples/OpenFPGA_rendering/_merge_multiple_floorplan.svg
    :width: 400px

'''


import logging

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.util import get_names
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

top.properties["WIDTH"] = 250
top.properties["HEIGHT"] = 300

module1.properties["SHAPE"] = "cross"  # cross Shape
module1.properties["POINTS"] = [40, 0, 40, 40, 40, 0]  # A, B, C, D , E, F

module2.properties["SHAPE"] = "rect"
module2.properties["WIDTH"] = 60
module2.properties["HEIGHT"] = 40

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#         Set the LOC_X, LOC_Y on all the instances
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

inst_1_0.properties["LOC_X"] = 50
inst_1_0.properties["LOC_Y"] = 20

inst_2_0.properties["LOC_X"] = 130
inst_2_0.properties["LOC_Y"] = 20

inst_1_1.properties["LOC_X"] = 50
inst_1_1.properties["LOC_Y"] = 170

inst_2_1.properties["LOC_X"] = 130
inst_2_1.properties["LOC_Y"] = 170


fp = FloorPlanViz(top)
fp.compose(skip_connections=True)
dwg = fp.get_svg()
dwg.saveas("_merge_multiple_floorplan_before.svg", pretty=True, indent=4)


main_def, instance_list = top.merge_multiple_instance([((inst_1_0, inst_2_0), 'merged_inst_2_0'),
                                                       ((inst_1_1, inst_2_1), 'merged_inst_2_1')],
                                                      new_definition_name="NewModule")

fp = FloorPlanViz(top)
fp.compose(skip_connections=True)
dwg = fp.get_svg()
dwg.saveas("_merge_multiple_floorplan.svg", pretty=True, indent=4)
