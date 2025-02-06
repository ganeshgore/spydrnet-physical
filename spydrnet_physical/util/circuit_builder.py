"""
circuit_builder.py

This module provides utility functions for building and manipulating circuit components,
like multiplexers (MUX), decoders, shift registers etc.
"""

import logging
import spydrnet_physical as sdn

logger = logging.getLogger("spydrnet_logs")


class circuit_builder:

    @staticmethod
    def create_mux_instance(
        top: sdn.Definition,
        name: str,
        reference: sdn.Definition,
        inputs_w: list[sdn.Wire],
        output_w: sdn.Wire,
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
        """
        # Create Mux Instance
        inst = top.create_child(name, reference=reference)

        input_pins = next(reference.get_ports("in")).pins
        # TODO: Replace this with wire mismatch assertion error
        assert len(input_pins) == len(
            inputs_w
        ), f"Number of input pins should match the number of input wires {len(input_pins)} != {len(inputs_w)}"

        # Connect input pins
        for indx, each_pin in enumerate(input_pins):
            inputs_w[indx].connect_pin(inst.pins[each_pin])

        # Connect output pins
        output_w.connect_pin(inst.pins[next(reference.get_ports("out")).pins[0]])
        return inst

    @staticmethod
    def build_tree_like_mux(
        definition: sdn.Definition,
        inputs: list[sdn.Wires],
        mux_dictionary: dict,
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

        def _mux_tree(inputs, level=0, stage=0):
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
                circuit_builder.create_mux_instance(
                    definition,
                    mux_name,
                    mux_dictionary[mux_size],
                    inputs,
                    out_cable.wires[0],
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

            # If group can be mapped to mux size, create mux and return output wire
            next_level_inputs = []
            for stage, group in enumerate(grouped_inputs):
                if len(group) == 1:
                    next_level_inputs.extend(group)
                else:
                    next_wire = _mux_tree(group, level + 1, stage)
                    next_level_inputs.append(next_wire)

            return _mux_tree(next_level_inputs, level + 2)

        output_net = _mux_tree(inputs)
        return output_net
