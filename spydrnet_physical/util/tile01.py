"""
This class is created for OpenFPGA related netlist transformations
"""
import logging
from pprint import pprint

import spydrnet as sdn
from spydrnet_physical.util import (OpenFPGA_Config_Generator,
                                    OpenFPGA_Tile_Generator, get_names)
from spydrnet_physical.util.shell import launch_shell

logger = logging.getLogger('spydrnet_logs')


class config_chain_simple(OpenFPGA_Config_Generator):
    """
    This shows how the configuration chain can be built
    """

    def __init__(self, grid, netlist, library, top_module):
        super().__init__(grid, netlist, library, top_module)
        self.chain1 = []
        self.chain2 = []
        self.chain = [self.chain1, self.chain2]
        self.order = ['grid_io_right', 'grid_io_top', 'grid_io_left',
                      'grid_io_bottom', 'cbx_1__4_', 'cbx_1__1_', 'cbx_1__0_',
                      'cby_0__1_', 'cby_1__1_', 'cby_4__1_', 'sb_0__0_',
                      'sb_0__1_', 'sb_0__4_', 'sb_1__0_', 'sb_1__1_',
                      'sb_1__4_', 'sb_4__0_', 'sb_4__1_', 'sb_4__4_',
                      'grid_clb']

    def write_fabric_key():
        pass

    def add_configuration_scheme(self):
        ''' Creates configuration chain '''
        logger.info("Running configuration")
        self.add_top_row()
        self.add_middle_rows()
        self.add_last_row()
        chain1 = []
        for inst in self.chain1:
            chain1.append(next(self._top_module.get_instances(inst)))
        self.chain1 = chain1

        self._connect_instances(self._top_module, chain1)
        self._connect_top_module()

    def _connect_top_module(self):
        head_cable = next(self._top_module.get_cables(self.head), None)
        first_head = next(self.chain1[0].get_port_pins(self.head))
        head_cable.wires[0].connect_pin(first_head)

        tail_cable = next(self._top_module.get_cables(self.tail), None)
        last_tail = next(self.chain1[-1].get_port_pins(self.tail))
        tail_cable.wires[0].connect_pin(last_tail)

    def add_top_row(self):
        x = self.fpga_size[0]
        y = self.fpga_size[1]
        self.chain1.append(f"grid_io*{x+1}__{y}*")
        for x in range(self.fpga_size[0], 0, -1):
            self.chain1.append(f"sb*{x}__{y}*")
            self.chain1.append(f"cby*{x}__{y}*")
            self.chain1.append(f"grid_clb*{x}__{y}*")
            self.chain1.append(f"cbx*{x}__{y}*")
            self.chain1.append(f"grid_io*{x}__{y+1}*")
        self.chain1.append(f"sb*0__{y}*")
        self.chain1.append(f"cby*0__{y}*")
        self.chain1.append(f"grid_io*_0__{y}*")

    def add_middle_rows(self):
        for y in range(self.fpga_size[1]-1, 1, -1):
            if (y+1) % 2:
                for x in range(self.fpga_size[0], 0, -1):
                    if x == self.fpga_size[0]:
                        self.chain1.append(f"sb*_{x}__{y}*")
                        self.chain1.append(f"grid_io*_{x+1}__{y}*")
                        self.chain1.append(f"cby*_{x}__{y}*")
                    self.chain1.append(f"grid_clb*{x}__{y}*")
                    self.chain1.append(f"cbx*{x}__{y}*")
                    self.chain1.append(f"sb*{x-1}__{y}*")
                    self.chain1.append(f"cby*{x-1}__{y}*")
                self.chain1.append(f"grid_io*_0__{y}*")
            else:
                for x in range(1, self.fpga_size[0]+1):
                    if x == 1:
                        self.chain1.append(f"sb*_0__{y}*")
                        self.chain1.append(f"grid_io*_0__{y}*")
                        self.chain1.append(f"cby*_0__{y}*")
                    self.chain1.append(f"grid_clb*{x}__{y}*")
                    self.chain1.append(f"cbx*{x}__{y}*")
                    self.chain1.append(f"sb*{x}__{y}*")
                    self.chain1.append(f"cby*{x}__{y}*")
                self.chain1.append(f"grid_io*_{x+1}__{y}*")

    def add_last_row(self):
        y = 1
        self.chain1.append(f"sb*_0__1*")
        self.chain1.append(f"cby*_0__1*")
        self.chain1.append(f"grid_io*_0__1*")
        self.chain1.append(f"sb*_0__0*")
        for x in range(1, self.fpga_size[0]+1):
            self.chain1.append(f"grid_io_*{x}__{y-1}*")
            self.chain1.append(f"cbx*{x}__{y-1}*")
            self.chain1.append(f"grid_clb*{x}__{y}*")
            self.chain1.append(f"cbx*{x}__{y}*")
            self.chain1.append(f"sb*{x}__{y}*")
            self.chain1.append(f"cby*{x}__{y}*")
            self.chain1.append(f"sb*{x}__{y-1}*")
        self.chain1.append(f"grid_io_*{x+1}__{y}*")


class config_chain_01(OpenFPGA_Config_Generator):
    """
    This example demonstrate how configuration chain can be restructured after
    the tile tranformation. This method is better suited while creating
    a configuration after the physical tranformation. However mapping the
    sequence back to the original sequence could require complex scripting.
    # TODO : Need better explanation
    """

    def __init__(self, grid, netlist, library, top_module):
        super().__init__(grid, netlist, library, top_module)
        self.order = ['grid_io_right', 'grid_io_top',
                      'grid_io_left', 'grid_io_bottom',
                      'cbx_1__4_', 'cbx_1__1_', 'cbx_1__0_',
                      'cby_0__1_', 'cby_1__1_', 'cby_4__1_',
                      'sb_0__0_', 'sb_0__1_', 'sb_0__4_',
                      'sb_1__0_', 'sb_1__1_', 'sb_1__4_',
                      'sb_4__0_', 'sb_4__1_', 'sb_4__4_',
                      'grid_clb']

    def write_fabric_key():
        pass

    def add_configuration_scheme(self):
        ''' Creates configuration chain '''
        logger.info("Running configuration")
        self._create_intra_tiles()
        self._create_inter_tiles()

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


class Tile01(OpenFPGA_Tile_Generator):

    def create_tiles(self):
        '''
        Creates tiles
        '''
        # ##############  Main Tiles  ##############
        self._main_tile()

        # ##############  Side Tiles  ##############
        self._left_tile()
        self._right_tile()
        self._top_tile()
        self._bottom_tile()

        # ############## Corner Tiles ##############
        self._top_left_tile()
        self._top_right_tile()
        self._bottom_left_tile()
        self._bottom_right_tile()

    def _main_tile(self):
        '''Create main Tiles
        ::

                              +-----+
                              |     |
                +-------+ +----     ---+
                |  CBY  | |     SB     |
                +-------+ +----     ---+
            +---------------+ |     |
            |               | +-----+
            |               | +-----+
            |               | |     |
            |      CLB      | | CBX |
            |               | +-----+
            |               |
            +---------------+

      '''
        merge_module_list = []
        for x in range(2, self.fpga_size[0]):
            for y in range(2, self.fpga_size[1]):
                clb = next(self._library.get_instances(f"grid_clb_{x}__{y}_"))
                cbx = next(self._library.get_instances(f"cbx_{x}__{y}_"))
                cby = next(self._library.get_instances(f"cby_{x}__{y}_"))
                sb = next(self._library.get_instances(f"sb_{x}__{y}_"))
                merge_module_list.append(((clb, cbx, cby, sb),
                                          f"tile_{x}__{y}_"))

        self._top_module.merge_multiple_instance(merge_module_list,
                                                 new_definition_name="tile")
        next(self._library.get_definitions("tile")).OptPins()

    def _left_tile(self):
        '''        Create Left Tiles
        ::
            +-----+                  +-----+
            |     |                  |     |
            |     +--+ +-------+ +---+     +--+
            | SB     | |  CBY  | |     SB     |
            |     +--+ +-------+ +---+     +--+
            |     | +--------------+ |     |
            +-----+ |              | +-----+
            +-----+ |              | +-----+
            |     | |              | |     |
            | CBX | |     CLB      | | CBX |
            +-----+ |              | +-----+
                    |              |
                    +--------------+
        '''
        instance_list = []
        for i in range(2, self.fpga_size[0]):
            clb = next(self._library.get_instances(f"grid_clb_1__{i}_"))
            cby0 = next(self._library.get_instances(f"cby_0__{i}_"))
            cby1 = next(self._library.get_instances(f"cby_1__{i}_"))
            cbx1 = next(self._library.get_instances(f"cbx_1__{i}_"))
            sb0 = next(self._library.get_instances(f"sb_0__{i}_"))
            sb1 = next(self._library.get_instances(f"sb_1__{i}_"))
            grid_io = next(self._library.get_instances(
                f"grid_io_left_0__{i}_"))
            instance_list.append(((clb, cby0, cby1, cbx1, sb0, sb1, grid_io),
                                  f"tile_1__{i}_"))

        self._top_module.merge_multiple_instance(instance_list,
                                                 new_definition_name="left_tile")
        next(self._library.get_definitions("left_tile")).OptPins()

    def _right_tile(self):
        '''    Create Right Tiles
        ::
                             +-----+
                             |     |
                +-------+ +--+     |
                |  CBY  | |    SB  |
                +-------+ +--+     |
            +--------------+ |     |
            |              | +-----+
            |              | +-----+
            |              | |     |
            |     CLB      | | CBX |
            |              | +-----+
            |              |
            +--------------+
        '''
        instance_list = []
        for i in range(2, self.fpga_size[0]):
            clb = next(self._library.get_instances(
                f"grid_clb_{self.fpga_size[0]}__{i}_"))
            cbx1 = next(self._library.get_instances(
                f"cbx_{self.fpga_size[0]}__{i}_"))
            cby0 = next(self._library.get_instances(
                f"cby_{self.fpga_size[0]}__{i}_"))
            sb0 = next(self._library.get_instances(
                f"sb_{self.fpga_size[0]}__{i}_"))
            grid_io = next(self._library.get_instances(
                f"grid_io_right_{self.fpga_size[0]+1}__{i}_"))
            instance_list.append(((clb, cbx1, cby0, sb0, grid_io),
                                  f"tile_{self.fpga_size[0]}__{i}_"))

        self._top_module.merge_multiple_instance(instance_list,
                                                 new_definition_name=f"right_tile")
        next(self._library.get_definitions("right_tile")).OptPins()

    def _top_tile(self):
        '''     Create Top Tiles
        ::
               +-------+ +------------+
               |  CBY  | |     SB     |
               +-------+ +---+     +--+
            +--------------+ |     |
            |              | +-----+
            |              | +-----+
            |              | |     |
            |     CLB      | | CBX |
            |              | +-----+
            |              |
            +--------------+
        '''
        merge_module_list = []
        for i in range(2, self.fpga_size[1]):
            clb = next(self._library.get_instances(
                f"grid_clb_{i}__{self.fpga_size[1]}_"))
            cbx = next(self._library.get_instances(
                f"cbx_{i}__{self.fpga_size[1]}_"))
            cby = next(self._library.get_instances(
                f"cby_{i}__{self.fpga_size[1]}_"))
            sb = next(self._library.get_instances(
                f"sb_{i}__{self.fpga_size[1]}_"))
            grid_io = next(self._library.get_instances(
                f"grid_io_top_{i}__{self.fpga_size[1]+1}_"))
            merge_module_list.append(((clb, cbx, cby, sb, grid_io),
                                      f"tile_{i}__{self.fpga_size[1]}_"))

        self._top_module.merge_multiple_instance(merge_module_list,
                                                 new_definition_name="top_tile")
        next(self._library.get_definitions("top_tile")).OptPins()

    def _bottom_tile(self):
        '''   Create Bottom Tiles
        ::
                             +-----+
                             |     |
               +-------+ +---+     +--+
               |  CBY  | |     SB     |
               +-------+ +---+     +--+
            +--------------+ |     |
            |              | +-----+
            |              | +-----+
            |              | |     |
            |     CLB      | | CBX |
            |              | +-----+
            |              | +-----+
            +--------------+ |     |
               +-------+ +---+     +--+
               |  CBY  | |     SB     |
               +-------+ +------------+
        '''
        instance_list = []
        for i in range(2, self.fpga_size[1]):
            clb = next(self._library.get_instances(f"grid_clb_{i}__1_"))
            cbx0 = next(self._library.get_instances(f"cbx_{i}__0_"))
            cbx1 = next(self._library.get_instances(f"cbx_{i}__1_"))
            cby1 = next(self._library.get_instances(f"cby_{i}__1_"))
            sb0 = next(self._library.get_instances(f"sb_{i}__0_"))
            sb1 = next(self._library.get_instances(f"sb_{i}__1_"))
            grid_io = next(self._library.get_instances(
                f"grid_io_bottom_{i}__0_"))
            instance_list.append(((clb, cbx0, cbx1, cby1, sb0, sb1, grid_io),
                                  f"tile_{i}__1_"))

        self._top_module.merge_multiple_instance(instance_list,
                                                 new_definition_name=f"bottom_tile")
        next(self._library.get_definitions("bottom_tile")).OptPins()

    def _top_left_tile(self):
        '''       Create top left tile
        ::
            +--------+ +-------+ +------------+
            |  SB    | |  CBY  | |     SB     |
            |     +--+ +-------+ +---+     +--+
            |     | +--------------+ |     |
            +-----+ |              | +-----+
            +-----+ |              | +-----+
            |     | |              | |     |
            | CBX | |     CLB      | | CBX |
            +-----+ |              | +-----+
                    |              |
                    +--------------+
        '''
        merge_module_list = []
        clb = next(self._library.get_instances(
            f"grid_clb_1__{self.fpga_size[1]}_"))
        cbx0 = next(self._library.get_instances(
            f"cbx_1__{self.fpga_size[1]}_"))
        cby0 = next(self._library.get_instances(
            f"cby_0__{self.fpga_size[1]}_"))
        cby1 = next(self._library.get_instances(
            f"cby_1__{self.fpga_size[1]}_"))
        sb0 = next(self._library.get_instances(f"sb_0__{self.fpga_size[1]}_"))
        sb1 = next(self._library.get_instances(f"sb_1__{self.fpga_size[1]}_"))
        grid_io_0 = next(self._library.get_instances(
            f"grid_io_top_1__{self.fpga_size[1]+1}_"))
        grid_io_1 = next(self._library.get_instances(
            f"grid_io_left_0__{self.fpga_size[1]}_"))
        merge_module_list.append(((clb, cbx0, cby0, cby1, sb0, sb1, grid_io_0, grid_io_1),
                                  f"tile_1__{self.fpga_size[1]}_"))
        self._top_module.merge_multiple_instance(merge_module_list,
                                                 new_definition_name=f"top_left_tile")
        next(self._library.get_definitions("top_left_tile")).OptPins()

    def _top_right_tile(self):
        '''          Create top right tile
        ::
            +------------+ +-------+ +---------+
            |     SB     | |  CBY  | |     SB  |
            +---+     +--+ +-------+ +---+     |
                |     | +--------------+ |     |
                +-----+ |              | +-----+
                +-----+ |              | +-----+
                |     | |              | |     |
                | CBX | |     CLB      | | CBX |
                +-----+ |              | +-----+
                        |              |
                        +--------------+
        '''
        merge_module_list = []
        clb = next(self._library.get_instances(
            f"grid_clb_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        cbx0 = next(self._library.get_instances(
            f"cbx_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        cby0 = next(self._library.get_instances(
            f"cby_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        sb0 = next(self._library.get_instances(
            f"sb_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        grid_io_0 = next(self._library.get_instances(
            f"grid_io_right_{self.fpga_size[0]+1}__{self.fpga_size[1]}_"))
        grid_io_1 = next(self._library.get_instances(
            f"grid_io_top_{self.fpga_size[0]}__{self.fpga_size[1]+1}_"))
        merge_module_list.append(((clb, cbx0, cby0, sb0, grid_io_0, grid_io_1),
                                  f"tile_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        self._top_module.merge_multiple_instance(merge_module_list,
                                                 new_definition_name=f"top_right_tile")
        next(self._library.get_definitions("top_right_tile")).OptPins()

    def _bottom_left_tile(self):
        '''      Create bottom left tile
        ::
            +-----+                  +-----+
            |     |                  |     |
            |     +--+ +-------+ +---+     +--+
            | SB     | |  CBY  | |     SB  |  |
            |     +--+ +-------+ +---+     +--+
            |     | +--------------+ |     |
            +-----+ |              | +-----+
            +-----+ |              | +-----+
            |     | |              | |     |
            | CBX | |     CLB      | | CBX |
            +-----+ |              | +-----+
            +-----+ |              | +-----+
            |     | +--------------+ |     |
            |     +--+ +-------+ +---+     +--+
            | SB     | |  CBY  | |     SB     |
            +--------+ +-------+ +------------+

        '''
        merge_module_list = []
        clb = next(self._library.get_instances("grid_clb_1__1_"))
        cbx0 = next(self._library.get_instances("cbx_1__0_"))
        cbx1 = next(self._library.get_instances("cbx_1__1_"))
        cby0 = next(self._library.get_instances("cby_0__1_"))
        cby1 = next(self._library.get_instances("cby_1__1_"))
        sb0 = next(self._library.get_instances("sb_0__0_"))
        sb1 = next(self._library.get_instances("sb_0__1_"))
        sb2 = next(self._library.get_instances("sb_1__0_"))
        sb3 = next(self._library.get_instances("sb_1__1_"))
        grid_io_0 = next(self._library.get_instances("grid_io_left_0__1_"))
        grid_io_1 = next(self._library.get_instances("grid_io_bottom_1__0_"))
        merge_module_list.append(((clb, cbx0, cbx1, cby0, cby1, sb0, sb1,
                                   sb2, sb3, grid_io_0, grid_io_1),
                                  "tile_1__1_"))
        self._top_module.merge_multiple_instance(merge_module_list,
                                                 new_definition_name=f"bottom_left_tile")

        next(self._library.get_definitions("bottom_left_tile")).OptPins()

    def _bottom_right_tile(self):
        ''' Create bottom right tile
        ::
                              +-----+
                              |     |
                +-------+ +---+     |
                |  CBY  | |     SB  |
                +-------+ +---+     |
             +--------------+ |     |
             |              | +-----+
             |              | +-----+
             |              | |     |
             |     CLB      | | CBX |
             |              | +-----+
             |              | +-----+
             +--------------+ |     |
                +-------+ +---+     |
                |  CBY  | |     SB  |
                +-------+ +---------+
        '''
        merge_module_list = []
        clb = next(self._library.get_instances(
            f"grid_clb_{self.fpga_size[0]}__1_"))
        cbx0 = next(self._library.get_instances(
            f"cbx_{self.fpga_size[0]}__0_"))
        cbx1 = next(self._library.get_instances(
            f"cbx_{self.fpga_size[0]}__1_"))
        cby0 = next(self._library.get_instances(
            f"cby_{self.fpga_size[0]}__1_"))
        sb0 = next(self._library.get_instances(f"sb_{self.fpga_size[0]}__0_"))
        sb1 = next(self._library.get_instances(f"sb_{self.fpga_size[0]}__1_"))
        grid_io_0 = next(self._library.get_instances(
            f"grid_io_bottom_{self.fpga_size[0]}__0_"))
        grid_io_1 = next(self._library.get_instances(
            f"grid_io_right_{self.fpga_size[0]+1}__1_"))
        merge_module_list.append(((clb, cbx0, cbx1, cby0, sb0, sb1, grid_io_0, grid_io_1),
                                  f"tile_{self.fpga_size[0]}__1_"))
        self._top_module.merge_multiple_instance(merge_module_list,
                                                 new_definition_name="bottom_right_tile")
        next(self._library.get_definitions("bottom_right_tile")).OptPins()
