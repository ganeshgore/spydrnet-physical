#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import json
import logging
import spydrnet as sdn
from pathlib import Path

logger = logging.getLogger("spydrnet_logs")


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
                "expandModules": {"types": [], "ids": []},
                "colour": ["#e9e9e9"],
            },
            "top": {"enable": False, "module": ""},
        }

    def expand_all(self, netlist):
        """
        This will add add the modules without black
        box tags to the exapand list
        """
        instance_names = [d.name for d in netlist.top_instance.get_instances()]
        self.config["hierarchy"]["expandModules"]["ids"].extend(instance_names)
        logger.debug(f"Expanding all [{len(instance_names)}] module. {instance_names}")

    def expand(self, modules=None, instances=None):
        """
        Adds modules or instances to the expand list
        """
        if not modules is None:
            self.config["hierarchy"]["expandModules"]["types"].extend(modules)
        if not instances is None:
            self.config["hierarchy"]["expandModules"]["ids"].extend(instances)

    # TODO
    # Add option to suppress stdout printing of the yosys compilation
    # Finish documentation and add in sphinx index
    def run(
        self,
        netlist,
        yosys_cmmds="",
        file_out="out.svg",
        netlistsvg="netlistsvg",
        top_module=None,
        expand_modules=None,
        expand_instances=None,
        expand_all=True,
    ):
        """
        Main method to run composer

        args:
            netlist
            yosys_cmmds
            file_out

        """
        # Create Verilog file for yosys synthesis
        verilog_file = str(file_out).replace(".svg", "_.v")
        sdn.compose(netlist, verilog_file, skip_constraints=False)
        top = top_module or netlist.top_instance.reference.name

        json_file = str(file_out).replace(".svg", "_.json")
        os.system(
            f"yosys -l _{top}_synth.log -p 'prep -top {top}; "
            + yosys_cmmds
            + f" write_json {json_file};' "
            + f"{verilog_file} > /dev/null"
        )
        logger.info("Yosys synthesis finished")

        # Create configuration for netlist svg
        if expand_all:
            self.expand_all(netlist)
        self.expand(modules=expand_modules, instances=expand_instances)
        config_file = str(file_out).replace(".svg", "_config.json")
        skin_file = (
            Path(__file__).parent.parent.parent
            / "support_files"
            / "skin-files"
            / "sdnphy-skin.svg"
        )
        with open(config_file, "w", encoding="utf-8") as fp:
            json.dump(self.config, fp, indent=4)
        svg_command = f"{netlistsvg} {json_file} -o {file_out} "
        svg_command += f" --config {config_file}"
        svg_command += f" --skin {skin_file};"
        logger.debug(f"Executing command {svg_command}")
        os.system(svg_command)
        logger.info("Netlist rendered '%s'", file_out)
