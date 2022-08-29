"""
======================
Optimizing module pins
======================
This example demonstrate how to optimize the module pins based on the
connectivity of the current instances.


**Before Optimization**
.. image:: ../../../examples/OpenFPGA_basic/_simple_design.svg
   :width: 60%
   :align: center

**After Optimization**
.. image:: ../../../examples/OpenFPGA_basic/_simple_design_post_opt_pins.svg
   :width: 60%
   :align: center

"""

import logging

import spydrnet as sdn
from spydrnet_physical.composers.svg.composer import SVGComposer


logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')

with open("_simple_design.v", "w", encoding="UTF-8") as fp:
    fp.write('''
    module top(in0, out);
        input in0;
        output [1:0]out;

        block1 instance1 (.in0(in0), .in1(in0), .out(out[0]));
        block1 instance2 (.in0(in0), .in1(in0), .out(out[1]));

    endmodule

    `celldefine
    module block1(in0, in1, out);
        input in0;
        input in1;
        output out;

    endmodule
    `endcelldefine
    ''')

netlist = sdn.parse("_simple_design.v")

composer = SVGComposer()
composer.run(netlist, file_out="_simple_design.svg")

next(netlist.get_definitions("block1")).OptPins()

composer = SVGComposer()
composer.run(netlist, file_out="_simple_design_post_opt_pins.svg")
