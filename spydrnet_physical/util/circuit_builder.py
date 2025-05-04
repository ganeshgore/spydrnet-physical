"""
circuit_builder.py

This module provides utility functions for building and manipulating circuit components,
like multiplexers (MUX), decoders, shift registers etc.
"""

import logging
import math
import spydrnet as sdn

logger = logging.getLogger("spydrnet_logs")


class circuit_builder:

    @staticmethod
    def create_mux_instance(
        top: sdn.Definition,
        name: str,
        reference: sdn.Definition,
        inputs_w,
        output_w: sdn.Wire,
        select_w,
    ):
        """
        Creates a multiplexer (MUX) instance in the given top module with given multiplexer module.
        Args:
            top (Module): The top module where the MUX instance will be created.
            name (str): The name of the MUX instance.
            reference (Module): The reference module for the MUX instance.
            inputs_w (list[Wire]): A list of input wires to be connected to the MUX instance.
            output_w (Wire): The output wire to be connected to the MUX instance.
        Returns:
            Instance: The created MUX instance.
        Raises:
            AssertionError: If the number of input pins in the reference module does not match the number of input wires.

        Note: The input pins in the reference module should be named as `IN0`, `IN1`, `IN2`, etc.
        and output pin named as `OUT`
        """
        # Create Mux Instance
        inst = top.create_child(name, reference=reference)

        input_ports = sorted(reference.get_ports("IN*"), key=lambda x: int(x.name[2:]))
        # TODO: Replace this with wire mismatch assertion error
        assert len(input_ports) == len(
            inputs_w
        ), f"Number of input pins should match the number of input wires {len(input_ports)} != {len(inputs_w)}"

        # Connect input pins
        for indx, each_port in enumerate(input_ports):
            inputs_w[indx].connect_pin(inst.pins[each_port.pins[0]])

        select_pins = next(reference.get_ports("SEL")).pins
        # Connect select pins
        for indx, each_pin in enumerate(select_pins):
            select_w[indx].connect_pin(inst.pins[each_pin])

        # Connect output pins
        output_w.connect_pin(inst.pins[next(reference.get_ports("OUT")).pins[0]])
        return inst

    @staticmethod
    def build_tree_like_mux(
        definition: sdn.Definition,
        inputs,
        mux_dictionary: dict,
        select_cable=None,
        suffix="",
    ):
        """
        Builds a tree-like multiplexer (MUX) structure within a given definition.
        This function constructs a hierarchical MUX structure using the provided
        inputs and a dictionary that defines the available MUX sizes. The MUXes
        are created in a tree-like fashion, where smaller MUXes are combined to
        form larger ones (prioritising the use of larger MUXes) until a single
        output is produced.
        Args:
            definition (Definition): The definition object where the MUX structure
                will be created.
            inputs (list): A list of input wires to be connected to the MUX tree.
            mux_dictionary (dict): A dictionary where keys are MUX sizes and values
                are the corresponding MUX definitions.
            suffix (str, optional): A suffix to append to the MUX instance names.
                Defaults to an empty string.
        Returns:
            output_net(sdn.wire): The output wire of the MUX tree.
        """

        def _group_inputs(inputs, size):
            group_index = len(inputs) - (len(inputs) % size)
            return [inputs[i : i + size] for i in range(0, group_index, size)], inputs[
                group_index:
            ]

        def _mux_tree(inputs, level=0, stage=0, select_cable=None):
            logger.debug(f"Stage1 inputs: {len(inputs)}")
            # If single net return it as it is
            if len(inputs) == 1:
                return inputs[0]

            # If the input can be mapped to any of the available MUX sizes
            # instantiate the corresponding MUX and return the output wire
            if len(inputs) in mux_dictionary.keys():
                mux_size = len(inputs)
                mux_name = f"mux{mux_size}_{level}_{stage}{suffix}"
                out_cable = definition.create_cable(mux_name, wires=1)
                req_sel_lines = math.ceil(math.log2(len(inputs)))
                if len(select_cable.wires) < level - 1 + req_sel_lines:
                    select_cable.create_wires(
                        level - 1 + req_sel_lines - len(select_cable.wires)
                    )
                circuit_builder.create_mux_instance(
                    definition,
                    mux_name + "_inst",
                    mux_dictionary[mux_size],
                    inputs,
                    out_cable.wires[0],
                    select_cable._wires[level - 1 :],
                )
                return out_cable.wires[0]

            # If mux size is not available, group the inputs into the largest
            # possible MUX size and recursively call the function
            grouped_inputs = []
            for size in sorted(mux_dictionary.keys(), reverse=True):
                grouped, remaining = _group_inputs(inputs, size)
                grouped_inputs.extend(grouped)
                if len(remaining) == 1:
                    grouped_inputs.append(remaining)
                    inputs = []
                else:
                    inputs = remaining

            max_select_line = max(len(group) for group in grouped_inputs)
            max_select_line = math.ceil(math.log2(max_select_line))

            # If group can be mapped to mux size, create mux and return output wire
            next_level_inputs = []
            for stage, group in enumerate(grouped_inputs):
                if len(group) == 1:
                    next_level_inputs.extend(group)
                else:
                    next_wire = _mux_tree(group, level, stage, select_cable)
                    next_level_inputs.append(next_wire)

            return _mux_tree(
                next_level_inputs, level + max_select_line, 0, select_cable
            )

        if select_cable is None:
            select_cable = next(definition.get_cables(f"select_{suffix}"), None)
        if select_cable is None:
            select_cable = definition.create_cable(f"select_{suffix}", wires=1)
        output_net = _mux_tree(inputs, 1, 1, select_cable)
        return output_net, select_cable

    @staticmethod
    def add_and_gate(
        definition: sdn.Definition,
        and_gate: sdn.Definition,
        input_wires,
        output_wire: sdn.Wire,
        suffix="",
    ):
        inst = definition.create_child(f"and_gate{suffix}", reference=and_gate)

        input_ports = sorted(and_gate.get_ports("IN*"), key=lambda x: int(x.name[2:]))

        # Connect input pins
        for indx, each_port in enumerate(input_ports):
            input_wires[indx].connect_pin(inst.pins[each_port.pins[0]])

        # Connect output pins
        output_wire.connect_pin(inst.pins[next(and_gate.get_ports("OUT")).pins[0]])
        return inst

    @staticmethod
    def build_sipo_register(
        library: sdn.Library,
        flop_module: sdn.Definition,
        width: int,
        depth: int,
        suffix="",
    ):
        sipo_def = library.create_definition(
            "sipo_reg" + suffix,
        )
        sipo_def.create_port("shift_in", direction=sdn.IN, pins=width)
        sipo_def.create_port("reset", direction=sdn.IN, pins=1)
        sipo_def.create_port("clock", direction=sdn.IN, pins=1)
        sipo_def.create_port("enable", direction=sdn.IN, pins=1)
        sipo_def.create_port("shift_out", direction=sdn.OUT, pins=width)
        sipo_def.create_port("out", direction=sdn.OUT, pins=width * depth)

        sipo_reset_w = sipo_def.create_cable("reset", wires=1).wires[0]
        sipo_enable_w = sipo_def.create_cable("enable", wires=1).wires[0]
        sipo_clk_w = sipo_def.create_cable("clock", wires=1).wires[0]
        sipo_out_cable = sipo_def.create_cable("out", wires=width * depth)

        for d in range(depth):
            if d == 0:
                in_cable = sipo_def.create_cable(f"shift_in", wires=depth)
            else:
                in_cable = out_cable
            out_cable = sipo_def.create_cable(
                f"shift_out" if d == depth - 1 else f"shift_out_{d}", wires=depth
            )
            for w in range(width):
                flop_inst = sipo_def.create_child(
                    f"flop_{w}_{d}{suffix}", reference=flop_module
                )
                sipo_reset_w.connect_pin(
                    flop_inst.pins[next(flop_module.get_ports("RESET")).pins[0]]
                )
                sipo_enable_w.connect_pin(
                    flop_inst.pins[next(flop_module.get_ports("ENABLE")).pins[0]]
                )
                sipo_clk_w.connect_pin(
                    flop_inst.pins[next(flop_module.get_ports("CLK")).pins[0]]
                )
                in_cable.wires[w].connect_pin(
                    flop_inst.pins[next(flop_module.get_ports("D")).pins[0]]
                )
                out_cable.wires[w].connect_pin(
                    flop_inst.pins[next(flop_module.get_ports("Q")).pins[0]]
                )
            out_cable.assign_cable(
                sipo_out_cable, upper=(width * (d + 1)) - 1, lower=width * d
            )
        return sipo_def

    @staticmethod
    def build_interconnect(module, input_len, output_len, mux_dict):
        """
        Builds an interconnect module with input, output, and selection ports.

        This method creates an interconnect module that connects multiple input
        wires to multiple output wires using a tree-like multiplexer structure.
        The selection lines determine which input is routed to each output.

        Args:
            module (Definition): The definition object where the interconnect
            module will be created.
            input_len (int): Number of input wires.
            output_len (int): Number of output wires.
            mux_dict (dict): A dictionary where keys are MUX sizes and values
            are the corresponding MUX definitions.

        Returns:
            Definition: The created interconnect module definition.

        example:
            netlist = sdnphy.load_netlist_by_name("std_genlib")
            library = netlist.create_library("top")
            module = sdn.create_definition("interconnect")
            input_len = 8
            output_len = 2
            mux_dict = {
                2: sdn.create_definition("MUX2"),
                4: sdn.create_definition("MUX4"),
            }
            interconnect = build_interconnect(module, input_len, output_len, mux_dict)
        """
        sram_len = math.ceil(math.log2(input_len)) * output_len
        module.create_port("in", direction=sdn.IN, pins=input_len)
        module.create_port("out", direction=sdn.OUT, pins=output_len)
        module.create_port("sel", direction=sdn.IN, pins=sram_len)

        in_c = module.create_cable("in", wires=input_len)
        out_c = module.create_cable("out", wires=output_len)
        sel_c = module.create_cable("sel", wires=sram_len)

        for out_w in out_c.wires:
            out_w_ret, _ = circuit_builder.build_tree_like_mux(
                definition=module,
                inputs=in_c.wires,
                mux_dictionary=mux_dict,
                select_cable=sel_c,
                suffix=f"_{out_w.index()}",
            )
            out_w_ret.assign_wire(out_w)
        return module
