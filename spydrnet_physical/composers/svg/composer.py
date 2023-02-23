#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import json
import logging
import spydrnet as sdn

logger = logging.getLogger('spydrnet_logs')


class SVGComposer:
    """
    Class create SVG composer based on yosys and netlist SVG.
    """

    def __init__(self):
        """
        Initialise configuration for hierarchical viewer
        """
        self.config = {
            "hierarchy": {
                "enable": "modules",
                "expandLevel": 1,
                "expandModules": {
                    "types": [],
                    "ids": []
                },
                "colour": ["#e9e9e9"]
            },
            "top": {
                "enable": False,
                "module": ""
            }
        }

    def expand_all(self):
        """
        This will add add the modules without black
        box tags to the exapand list
        """
        raise NotImplementedError

    def expand(self, modules=(), instances=()):
        """
        Adds modules or instances to the expand list
        """
        self.config["hierarchy"]["expandModules"]["types"].extend(modules)
        self.config["hierarchy"]["expandModules"]["ids"].extend(instances)

    # TODO
    # Add option to suppress stdout printing of the yosys compilation
    # Finish documentation and add in sphinx index
    def run(self, netlist, yosys_cmmds="", file_out="out.svg", netlistsvg="netlistsvg", top_module=None):
        """
        Main method to run composer

        args:
            netlist
            yosys_cmmds
            file_out

        """
        # Create Verilog file for yosys synthesis
        verilog_file = "_" + file_out.replace(".svg", ".v")
        sdn.compose(netlist, verilog_file, skip_constraints=True)
        top = top_module or netlist.top_instance.reference.name

        json_file = "_" + file_out.replace(".svg", ".json")
        os.system(
            f"yosys -l _{top}_synth.log -p 'prep -top {top}; "
            + yosys_cmmds
            + f" write_json {json_file};' "
            + f"{verilog_file} > /dev/null"
        )
        logger.info("Yosys synthesis finished")

        # Create configuration for netlist svg
        with open(f"_{top}_config.json", "w", encoding="utf-8") as fp:
            json.dump(self.config, fp, indent=4)
        svg_command = f"{netlistsvg} {json_file} -o {file_out} "
        svg_command += f"--config _{top}_config.json;"
        os.system(svg_command)
        logger.info("Netlist rendered '%s'", file_out)
