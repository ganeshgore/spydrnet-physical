#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

import spydrnet as sdn


class SVGComposer:
    """
    Class create SVG composer based on yosys and netlist SVG.
    """

    def __init__(self):
        # nothing to do during initialization
        pass

    # TODO
    # Add option to suppress stdout printing of the yosys compilation
    # Finish documentation and add in sphinx index
    def run(self, netlist, yosys_cmmds="", svgout_file="out.svg"):
        """
        Main method to run composer

        args:
            netlist
            yosys_cmmds
            svgout_file

        """
        verilog_file = "_"+svgout_file.replace(".svg", ".v")
        sdn.compose(netlist, verilog_file, skip_constraints=True)
        top = netlist.top_instance.reference.name

        json_file = "_"+svgout_file.replace(".svg", ".json")
        os.system(f"yosys -p 'prep -top {top}; " +
                  yosys_cmmds +
                  f" write_json {json_file};' " +
                  f"{verilog_file}")
        os.system(f"netlistsvg {json_file} -o {svgout_file};")
