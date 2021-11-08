"""
This class is created for OpenFPGA related netlist transformations
"""
import logging
from spydrnet_physical.util import OpenFPGA_Tile_Generator

logger = logging.getLogger('spydrnet_logs')


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
