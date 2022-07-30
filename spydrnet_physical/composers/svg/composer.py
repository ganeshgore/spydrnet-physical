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
    def run(self, netlist, yosys_cmmds="", file_out="out.svg"):
        """
        Main method to run composer

        args:
            netlist
            yosys_cmmds
            file_out

        """
        verilog_file = "_"+file_out.replace(".svg", ".v")
        sdn.compose(netlist, verilog_file, skip_constraints=True)
        top = netlist.top_instance.reference.name

        json_file = "_"+file_out.replace(".svg", ".json")
        os.system(f"yosys -p 'prep -top {top}; " +
                  yosys_cmmds +
                  f" write_json {json_file};' " +
                  f"{verilog_file}")
        os.system(f"netlistsvg {json_file} -o {file_out};")
