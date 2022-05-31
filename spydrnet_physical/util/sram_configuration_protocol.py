"""
Details the SRAM configuration protocol

.. rst-class:: ascii

::

         +--------+--------+--------+--------+
         |        |        |        |        |
    W[3] |        |        |        |        |
         |        |        |        |        |
         +-----------------------------------+
         |        |        |        |        |
    W[2] |        |        |        |        |
         |        |        |        |        |
         +-----------------------------------+
         |        |        |        |        |
    W[1] |        |        |        |        |
         |        |        |        |        |
         +-----------------------------------+
         |        |        |        |        |
    W[0] |        |        |        |        |
         |        |        |        |        |
         +--------+--------+--------+--------+
            b[0]     b[1]     b[2]     b[3]

"""

import logging
import math
from copy import deepcopy

import spydrnet as sdn
from spydrnet_physical.util.shell import launch_shell
from spydrnet_physical.util import OpenFPGA_Config_Generator

logger = logging.getLogger('spydrnet_logs')


class sram_configuration(OpenFPGA_Config_Generator):
    """
    This example demonstrate how configuration chain can be restructured after
    the tile tranformation. This method is better suited while creating
    a configuration after the physical tranformation. However mapping the
    sequence back to the original sequence could require complex scripting.
    """
    word_line_rows = []
    """Stores number of word lines in each row """

    bit_line_cols = []
    """Stores number of bit lines in each column """

    _config_bits_matrix = []

    def __init__(self, grid, netlist, library, top_module):
        super().__init__(grid, netlist, library, top_module)
        w_lines = next(self._top_module.get_ports("wl*"))
        b_lines = next(self._top_module.get_ports("bl*"))
        logger.debug("Found total %d bits", w_lines.size)
        assert w_lines.size == b_lines.size, "Mismatch WL and BL size"
        # self._config_bits_matrix = [[0]*self.fpga_size[0]]*self.fpga_size[0]
        self._config_bits_matrix = [[0 for _ in range(self.fpga_size[0])]
                                    for _ in range(self.fpga_size[1])]

        self.word_line_rows = [0] * self.fpga_size[1]
        self.bit_line_cols = [0] * self.fpga_size[0]
        self.annotate_configuration_bits()

    def print_configuration_bit_matrix(self, matrix=None):
        """
        Print the configuration bits matrix extracted from the fabric 
        """
        matrix = matrix or self._config_bits_matrix
        for y_pt in range(self.fpga_size[1]-1, -1, -1):
            for x_pt in range(self.fpga_size[0]):
                bits = matrix[y_pt][x_pt]
                print(f"{bits:4}", end="  ")
            print()

    def get_tile(self, x_pt, y_pt):
        """Returns the instance associated with the specific x and y cordinate"""
        return next(self._top_module.get_instances(f"*_{x_pt}__{y_pt}_*"))

    def annotate_configuration_bits(self):
        '''
        Adds number of configuration bit information to the each modules
        property
        '''
        for each_def in self._top_module.get_definitions("*"):
            w_lines = next(each_def.get_ports("wl*"))
            b_lines = next(each_def.get_ports("bl*"))
            assert w_lines.size == b_lines.size, "Mismatch WL and BL size"
            logger.debug("%20s %d", each_def.name, w_lines.size)
            each_def.properties["CONFIG_BITS"] = w_lines.size

        for x_pt in range(self.fpga_size[0]):
            for y_pt in range(self.fpga_size[1]):
                inst = self.get_tile(x_pt+1, y_pt+1)
                self._config_bits_matrix[y_pt][x_pt] = \
                    inst.reference.properties.get(
                        "CONFIG_BITS", 0)

    def add_configuration_scheme(self):
        ''' Creates configuration chain '''
        logger.debug("Adding memory configuration protocol")
        self._top_module.remove_port(next(self._top_module.get_ports("wl*")))
        self._top_module.remove_port(next(self._top_module.get_ports("bl*")))
        # TODO This part should be copied to the remove_cables method
        wl_cable = next(self._top_module.get_cables("wl*"))
        for each_wire in wl_cable.wires:
            for pins in each_wire.pins[::-1]:
                each_wire.disconnect_pin(pins)
        bl_cable = next(self._top_module.get_cables("bl*"))
        for each_wire in bl_cable.wires:
            for pins in each_wire.pins[::-1]:
                each_wire.disconnect_pin(pins)
        self._top_module.remove_cable(next(self._top_module.get_cables("wl")))
        self._top_module.remove_cable(next(self._top_module.get_cables("bl")))

        self._create_wl_ports()
        self._create_bl_ports()
        self._create_wl_connection()
        self._create_bl_connection()

        logger.debug(self.fpga_size)

    def remove_bl_wl_lines(self):
        for module in self._top_module.get_definitions("*"):
            wl_port = next(module.get_ports("wl"), None)
            if wl_port:
                module.remove_port(wl_port)
            bl_port = next(module.get_ports("bl"), None)
            if bl_port:
                module.remove_port(bl_port)

    def _create_wl_connection(self):
        top = self._top_module
        bl_lines = top.create_cable(f"wl_in", wires=sum(self.word_line_rows))
        for y_pt in range(self.fpga_size[1]):
            width = self.word_line_rows[y_pt]
            pre_instance = None
            for x_pt in range(self.fpga_size[1]):
                instance = self.get_tile(x_pt+1, y_pt+1)
                iname = instance.name
                cable = top.create_cable(f"{iname}_wl_in", wires=width)
                port = next(instance.get_ports("wl_in"))
                cable.connect_instance_port(instance, port)
                if pre_instance:
                    port = next(pre_instance.get_ports("wl_out"))
                    cable.connect_instance_port(pre_instance, port)
                else:
                    cable.assign_cable(bl_lines,
                                       sum(self.word_line_rows[:y_pt+1]),
                                       sum(self.word_line_rows[:y_pt]),
                                       reverse=True)
                pre_instance = instance

    def _create_bl_connection(self):
        top = self._top_module
        wl_lines = top.create_cable(f"bl_in", wires=sum(self.bit_line_cols))
        for x_pt in range(self.fpga_size[1]):
            width = self.bit_line_cols[x_pt]
            pre_instance = None
            for y_pt in range(self.fpga_size[1]):
                instance = self.get_tile(x_pt+1, y_pt+1)
                iname = instance.name
                cable = top.create_cable(f"{iname}_bl_in", wires=width)
                port = next(instance.get_ports("bl_in"))
                cable.connect_instance_port(instance, port)
                if pre_instance:
                    port = next(pre_instance.get_ports("bl_out"))
                    cable.connect_instance_port(pre_instance, port)
                else:
                    cable.assign_cable(wl_lines,
                                       sum(self.bit_line_cols[:x_pt+1]),
                                       sum(self.bit_line_cols[:x_pt]),
                                       reverse=True)
                pre_instance = instance

    def _create_bl_ports(self):
        """
        Create BL lines in each row

        TODO: Change method to identify the port size on eachmodule and then create
        """
        for x_pt in range(self.fpga_size[1]):
            width = self.bit_line_cols[x_pt]
            for y_pt in range(self.fpga_size[1]):
                module = self.get_tile(x_pt+1, y_pt+1).reference
                # Make sure bl_in port exist
                bl_in = next(module.get_ports("bl_in"), None)
                if not bl_in:
                    module.create_port("bl_in", direction=sdn.IN, pins=width)
                else:
                    while bl_in.size < width:
                        bl_in.create_pin()
                # Make sure bl_out port exist
                bl_out = next(module.get_ports("bl_out"), None)
                if not bl_out:
                    module.create_port("bl_out", direction=sdn.OUT, pins=width)
                else:
                    while bl_out.size < width:
                        bl_out.create_pin()
                # Make sure crosponding cable exists
                bl_in_cables = next(module.get_cables("bl_in"), None)
                if not bl_in_cables:
                    bl_in_cables = module.create_cable("bl_in", wires=width)
                else:
                    while bl_in_cables.size < width:
                        bl_in_cables.create_wire()
                # Make sure crosponding cable exists
                bl_out_cables = next(module.get_cables("bl_out"), None)
                if not bl_out_cables:
                    bl_out_cables = module.create_cable("bl_out", wires=width)
                else:
                    while bl_out_cables.size < width:
                        bl_out_cables.create_wire()

                assignement = next(module.get_instances(
                    "bl_in_bl_out_assign"), None)
                if assignement:
                    module.remove_child(assignement)
                bl_in_cables.assign_cable(bl_out_cables)

    def _create_wl_ports(self):
        """
        Create WL lines in each row

        TODO: Change method to identify the port size on eachmodule and then create
        """
        for y_pt in range(self.fpga_size[1]):
            width = self.word_line_rows[y_pt]
            for x_pt in range(self.fpga_size[1]):
                module = self.get_tile(x_pt+1, y_pt+1).reference
                # Make sure wl_in port exist
                wl_in = next(module.get_ports("wl_in"), None)
                if not wl_in:
                    module.create_port("wl_in", direction=sdn.IN, pins=width)
                else:
                    while wl_in.size < width:
                        wl_in.create_pin()
                # Make sure wl_out port exist
                wl_out = next(module.get_ports("wl_out"), None)
                if not wl_out:
                    module.create_port("wl_out", direction=sdn.OUT, pins=width)
                else:
                    while wl_out.size < width:
                        wl_out.create_pin()
                # Make sure crosponding cable exists
                wl_in_cables = next(module.get_cables("wl_in"), None)
                if not wl_in_cables:
                    wl_in_cables = module.create_cable("wl_in", wires=width)
                else:
                    while wl_in_cables.size < width:
                        wl_in_cables.create_wire()
                # Make sure crosponding cable exists
                wl_out_cables = next(module.get_cables("wl_out"), None)
                if not wl_out_cables:
                    wl_out_cables = module.create_cable("wl_out", wires=width)
                else:
                    while wl_out_cables.size < width:
                        wl_out_cables.create_wire()

                assignement = next(module.get_instances(
                    "wl_in_wl_out_assign"), None)
                if assignement:
                    module.remove_child(assignement)
                wl_in_cables.assign_cable(wl_out_cables)

    def set_wl_distribution(self, lines):
        """
        Sets fixed number of word lines for each row of the FPGA grid.

        Args:
            lines (list): List of integer indicating lines in each row 
        """
        self.word_line_rows = lines
        for x_pt in range(self.fpga_size[0]):
            bits = [self._config_bits_matrix[i][x_pt]
                    for i in range(self.fpga_size[1])]
            self.bit_line_cols[x_pt] = math.ceil(max(bits)/lines[x_pt])
        logger.debug(self.bit_line_cols)

    def set_bl_distribution(self, lines):
        pass

    def write_fabric_key(self):
        '''
        This will be extendned in the class
        '''
        return

    def _create_inter_tiles(self):
        inst_list = []
        for y in range(self.fpga_size[1], 0, -1):
            for x in sorted(range(self.fpga_size[0], 0, -1), reverse=(y+1) % 2):
                print(f"*{x}_{y}*")
                inst = next(self._top_module.get_instances(f"*{x}__{y}*"))
                inst_list.append(inst)
        self._connect_instances(self._top_module, inst_list)
        head_cable = next(self._top_module.get_cables(self.head))
        first_head = next(inst_list[0].get_port_pins(self.head))
        head_cable.wires[0].connect_pin(first_head)
        tail_cable = next(self._top_module.get_cables(self.tail))
        last_tail = next(inst_list[-1].get_port_pins(self.tail))
        tail_cable.wires[0].connect_pin(last_tail)

    def _create_intra_tiles(self):
        for each in ["top_right_tile", "top_tile", "top_left_tile",
                     "left_tile", "tile", "right_tile",
                     "bottom_right_tile", "bottom_left_tile"]:
            tile = next(self._library.get_definitions(each))

            # Remove ccff related cables and port from tile
            for cable in list(tile.get_cables("ccff*")):
                for pin in list(cable.wires[0].pins):
                    pin.wire.disconnect_pin(pin)
                tile.remove_cable(cable)
            for port in list(tile.get_ports("ccff*")):
                tile.remove_port(port)

            # Create chain
            inst_list = sorted([inst for inst in tile.get_instances()],
                               key=(lambda x: self.order.index(x.reference.name)))
            self._connect_instances(tile, inst_list)

            # Create ccff_head port
            tile.create_port(self._head, direction=sdn.IN, pins=1)
            ccff_head_wire = tile.create_cable(self._head, wires=1).wires[0]
            ccff_head_wire.connect_pin(
                next(inst_list[0].get_port_pins(self.head)))

            # Create ccff_tail port
            tile.create_port(self._tail, direction=sdn.OUT, pins=1)
            ccff_tail_wire = tile.create_cable(self._tail, wires=1).wires[0]
            ccff_tail_wire.connect_pin(
                next(inst_list[-1].get_port_pins(self.tail)))
