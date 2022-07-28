#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

import spydrnet as sdn


class SVGComposer:

    def __init__(self):
        pass

    def run(self, netlist, file_out="out.svg"):
        """ Main method to run composer """
        verilog_file = "_"+file_out.replace(".svg", ".v")
        sdn.compose(netlist, verilog_file, skip_constraints=True)
        top = netlist.top_instance.reference.name

        json_file = "_"+file_out.replace(".svg", ".json")
        os.system(f"yosys -p 'prep -top {top}; " +
                  f" write_json {json_file};' " +
                  f"{verilog_file}")
        os.system(f"netlistsvg {json_file} -o {file_out};")
