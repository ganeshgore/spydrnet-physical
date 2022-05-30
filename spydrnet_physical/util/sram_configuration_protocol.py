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
import spydrnet as sdn
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
        self.w_lines = next(self._top_module.get_ports("wl*"))
        self.b_lines = next(self._top_module.get_ports("bl*"))
        logger.debug("Found total %d bits", self.w_lines.size)
        assert self.w_lines.size == self.b_lines.size, "Mismatch WL and BL size"
        # self._config_bits_matrix = [[0]*self.fpga_size[0]]*self.fpga_size[0]
        self._config_bits_matrix = [[0 for _ in range(self.fpga_size[0])]
                                    for _ in range(self.fpga_size[1])]
        self.annotate_configuration_bits()

    def _print_configuration_bit_matrix(self):
        """
        Print the configuration bits matrix extracted from the fabric 
        """
        for y_pt in range(self.fpga_size[1]-1, -1, -1):
            for x_pt in range(self.fpga_size[0]):
                bits = self._config_bits_matrix[y_pt][x_pt]
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
        logger.debug(self.fpga_size)

    def set_wl_distribution(self, lines):
        pass

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
