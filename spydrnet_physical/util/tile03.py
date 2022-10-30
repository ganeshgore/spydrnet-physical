"""
This class is created for OpenFPGA related netlist transformations
"""
import logging

from spydrnet_physical.util import Tile01

logger = logging.getLogger('spydrnet_logs')


class Tile03(Tile01):
    """
    Creates Tile02 style tiling structure
    """

    def create_tiles(self):
        '''
        Creates tiles
        '''
        # ##############  Main Tiles  ##############
        self._main_tile()

        # ##############  Side Tiles  ##############
        self._right_tile()
        self._top_tile()

        # # ############## Corner Tiles ##############
        self._top_left_tile()
        self._top_right_tile()
        self._bottom_left_tile()
        self._bottom_right_tile()

        self._left_tile()
        self._bottom_tile()

        # self.fpga_size[0] += 1
        # self.fpga_size[1] += 1

    def merge_and_update_wrapper(self, instance_list, tile_name):
        '''
        This method takes the group of list of instances and create a multiple
        instances list
        '''
        if not instance_list:
            return
        # Create first tile
        keys = sorted(instance_list.keys(), reverse=True,
                      key=lambda x: len(instance_list[x]))
        self.merge_and_update(instance_list[keys[0]], tile_name)
        # Create extra tile
        for indx, key in enumerate(keys[1:]):
            self.merge_and_update(instance_list[key], f"{tile_name}_{indx+1}")

    def merge_and_update(self, instance_list, tile_name):
        """
        Merges given list of instances and updates width and height parameter
        """
        self._top_module.merge_multiple_instance(instance_list,
                                                 new_definition_name=tile_name)
        tile = next(self._library.get_definitions(tile_name))
        tile.OptPins()
        self._update_placement(instance_list)

    def _get_width_height(self, instance_list):
        x_min, y_min = float("inf"), float("inf")
        x_max, y_max = 0, 0
        for instance in instance_list[0][0]:
            properties = instance.properties
            ref_properties = instance.reference.properties
            LOC_X = properties.get("LOC_X", 0)
            LOC_Y = properties.get("LOC_Y", 0)
            x_min = min(x_min, LOC_X)
            y_min = min(y_min, LOC_Y)
            x_max = max(x_max, LOC_X+ref_properties["WIDTH"])
            y_max = max(y_max, LOC_Y+ref_properties["HEIGHT"])
        return ((x_max-x_min), (y_max-y_min))

    def _update_placement(self, instance_list):
        x_loc, y_loc = float("inf"), float("inf")
        # get instance with llx and lly value
        for indx, instance in enumerate(instance_list[0][0]):
            x = instance.properties.get("LOC_X", 0)
            y = instance.properties.get("LOC_Y", 0)
            if (x < x_loc):
                index_x, x_loc = indx, x
            if (y < y_loc):
                index_y, y_loc = indx, y

        for instances, new_name in instance_list:
            new_inst = next(self._top_module.get_instances(new_name))
            new_inst.properties["LOC_X"] = instances[index_x].properties.get(
                "LOC_X", 0)
            new_inst.properties["LOC_Y"] = instances[index_y].properties.get(
                "LOC_Y", 0)
            logger.debug("%s assigned %d %d", new_name,
                         new_inst.properties["LOC_X"],
                         new_inst.properties["LOC_Y"])

    def _main_tile(self):
        '''Create main Tiles

        .. rst-class:: ascii

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
        instance_list = {}
        for x in range(1, self.fpga_size[0]):
            for y in range(1, self.fpga_size[1]):
                try:
                    clb, cbx, cby, sb = None, None, None, None
                    clb = next(self._top_module.get_instances(
                        f"grid_clb_{x}__{y}_"))
                    cbx = next(self._top_module.get_instances(
                        f"cbx_{x}__{y}_"))
                    cby = next(self._top_module.get_instances(
                        f"cby_{x}__{y}_"))
                    sb = next(self._top_module.get_instances(f"sb_{x}__{y}_"))
                    category = f"{clb.reference.name}_{cbx.reference.name}"
                    category += f"_{cby.reference.name}_{sb.reference.name}"
                    instance_list[category] = instance_list.get(category, [])
                    instance_list[category].append(((clb, cbx, cby, sb),
                                                    f"tile_{x}__{y}_"))
                except StopIteration:
                    logger.debug("Missing instance at [%s %s] %s %s %s %s",
                                 x, y, clb, cbx, cby, sb)

        self.merge_and_update_wrapper(instance_list, "tile")

    def _left_tile(self):
        ''' Create Left Tiles

        .. rst-class:: ascii

        ::

             +-----+
             |     |
             |     +--+
             | SB     |
             |     +--+
             |     |
             +-----+
             +-----+
             |     |
             | CBX |
             +-----+

        '''
        instance_list = {}
        get_instances = self._top_module.get_instances
        for i in range(2, self.fpga_size[1]):
            try:
                cby0, sb0 = None, None
                grid_io = next(get_instances(f"grid_io_left_1__{i}_"))
                cby1 = next(get_instances(f"cby_1__{i}_"))
                cbx1 = next(get_instances(f"cbx_1__{i}_"))
                sb1 = next(get_instances(f"sb_1__{i}_"))
                cby0 = next(get_instances(f"cby_0__{i}_"))
                sb0 = next(get_instances(f"sb_0__{i}_"))
                category = f"_{cby0.reference.name}_{sb0.reference.name}"
                instance_list[category] = instance_list.get(category, [])
                instance_list[category].append(((cby0, sb0, grid_io, cby1, cbx1, sb1),
                                                f"tile_1__{i}_"))
            except StopIteration:
                logger.debug("Missing instance at [%s] %s %s", i, cby0, sb0)

        self.merge_and_update_wrapper(instance_list, "left_tile")

    def _right_tile(self):
        '''    Create Right Tiles

        .. rst-class:: ascii

        ::

                             +-----+
                             |     |
                +-------+ +--+     |
                |  CBY  | |    SB  |
                +-------+ +--+     |
            +--------------+ |     |
            |              | +-----+
            |              | +-----+
            |   GRID_IO    | | CBX |
            |              | +-----+
            |              |
            +--------------+

        '''
        instance_list = {}
        for i in range(2, self.fpga_size[0]):
            try:
                clb, cbx1, cby0, sb0 = None, None, None, None
                clb = next(self._top_module.get_instances(
                    f"grid_io_right_{self.fpga_size[0]}__{i}_"))
                cbx1 = next(self._top_module.get_instances(
                    f"cbx_{self.fpga_size[0]}__{i}_"))
                cby0 = next(self._top_module.get_instances(
                    f"cby_{self.fpga_size[0]}__{i}_"))
                sb0 = next(self._top_module.get_instances(
                    f"sb_{self.fpga_size[0]}__{i}_"))
                category = f"{clb.reference.name}_{cbx1.reference.name}"
                category += f"_{cby0.reference.name}_{sb0.reference.name}"
                instance_list[category] = instance_list.get(category, [])
                instance_list[category].append(((clb, cbx1, cby0, sb0),
                                                f"tile_{self.fpga_size[0]}__{i}_"))
            except StopIteration:
                logger.debug("Missing instance at %s [right] %s %s %s %s",
                             i, clb, cbx1, cby0, sb0)
        self.merge_and_update_wrapper(instance_list, "right_tile")

    def _top_tile(self):
        '''     Create Top Tiles

        .. rst-class:: ascii

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
        instance_list = {}
        for i in range(1, self.fpga_size[0]):
            try:
                clb, cbx, cby, sb = None, None, None, None
                clb = next(self._top_module.get_instances(
                    f"grid_io_top*_{i}__{self.fpga_size[1]}_"))
                cbx = next(self._top_module.get_instances(
                    f"cbx*_{i}__{self.fpga_size[1]}_"))
                cby = next(self._top_module.get_instances(
                    f"cby*_{i}__{self.fpga_size[1]}_"))
                sb = next(self._top_module.get_instances(
                    f"sb*_{i}__{self.fpga_size[1]}_"))

                category = f"{clb.reference.name}_{cbx.reference.name}"
                category += f"_{cby.reference.name}_{sb.reference.name}"
                instance_list[category] = instance_list.get(category, [])
                instance_list[category].append(((clb, cbx, cby, sb),
                                                f"tile_{i}__{self.fpga_size[1]}_"))
                logger.info("top_tiles types %s", instance_list.keys())
            except StopIteration:
                logger.debug("Missing instance at %s [right] %s %s %s %s",
                             i, clb, cbx, cby, sb)

        self.merge_and_update_wrapper(instance_list, "top_tile")

    def _bottom_tile(self):
        '''   Create Bottom Tiles

        .. rst-class:: ascii

        ::

                           +-----+
                           |     |
             +-------+ +---+     +--+
             |  CBY  | |     SB     |
             +-------+ +------------+

        '''
        instance_list = {}
        get_instances = self._top_module.get_instances
        try:
            for i in range(2, self.fpga_size[0]):
                cbx0, sb0 = None, None

                grid_io = next(get_instances(f"grid_io_bottom*_{i}__1_"))
                cby1 = next(get_instances(f"cby*_{i}__1_"))
                cbx1 = next(get_instances(f"cbx*_{i}__1_"))
                sb1 = next(get_instances(f"sb*_{i}__1_"))

                cbx0 = next(get_instances(f"cbx*_{i}__0_"))
                sb0 = next(get_instances(f"sb*_{i}__0_"))

                category = f"{cbx0.reference.name}_{sb0.reference.name}"
                category += f"_{sb1.reference.name}_{grid_io.reference.name}"
                category += f"_{cby1.reference.name}_{cbx1.reference.name}"
                instance_list[category] = instance_list.get(category, [])
                instance_list[category].append(((cbx0, sb0, grid_io, cby1, cbx1, sb1),
                                                f"tile_{i}__1_"))
            logger.info("Bottom_tile types %s", instance_list.keys())
        except StopIteration:
            logger.debug("Missing instance at %s [bottom] %s %s", i, cbx0, sb0)

        self.merge_and_update_wrapper(instance_list, "bottom_tile")

    def _top_left_tile(self):
        '''       Create top left tile

        .. rst-class:: ascii

        ::

            +--------+
            |  SB    |
            |     +--+
            |     |
            +-----+
            +-----+
            |     |
            | CBY |
            +-----+

        '''
        instance_list = []
        _, H = self.fpga_size
        get_instances = self._top_module.get_instances
        try:
            grid_io, cby1, cbx1, sb1, cby0, sb0 = None, None, None, None, None, None
            grid_io = next(get_instances(f"grid_io_left_1__{H}_"))
            cby1 = next(get_instances(f"cby_1__{H}_"))
            cbx1 = next(get_instances(f"cbx_1__{H}_"))
            sb1 = next(get_instances(f"sb_1__{H}_"))

            cby0 = next(get_instances(f"cby_0__{self.fpga_size[1]}_"))
            sb0 = next(get_instances(f"sb_0__{self.fpga_size[1]}_"))

            instance_list.append(((sb0, cby0, grid_io, cby1, cbx1, sb1),
                                  f"tile_1__{self.fpga_size[1]}_"))
        except StopIteration:
            logger.debug("Missing instance at top_left %s %s", cby0, sb0)
            return
        self.merge_and_update(instance_list, "left_top_tile")

    def _top_right_tile(self):
        '''          Create top right tile

        .. rst-class:: ascii

        ::

              +-------+ +---------+
              |  CBY  | |     SB  |
              +-------+ +---+     |
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
        try:
            clb, cbx0, cby0, sb0 = None, None, None, None
            clb = next(self._top_module.get_instances(
                f"grid_*_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
            cbx0 = next(self._top_module.get_instances(
                f"cbx_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
            cby0 = next(self._top_module.get_instances(
                f"cby_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
            sb0 = next(self._top_module.get_instances(
                f"sb_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
            instance_list.append(((clb, cbx0, cby0, sb0),
                                  f"tile_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        except StopIteration:
            logger.debug("Missing instance at top_right %s %s %s %s",
                         clb, cbx0, cby0, sb0)
            return

        self.merge_and_update(instance_list, "right_top_tile")

    def _bottom_left_tile(self):
        '''      Create bottom left tile

        .. rst-class:: ascii

        ::

             +-----+
             |     |
             |     +--+
             | SB     |
             +--------+

        '''
        instance_list = []
        get_instances = self._top_module.get_instances
        try:
            grid_io = next(get_instances("grid_io_*_1__1_"))
            cby1 = next(get_instances("cby_1__1_"))
            cbx1 = next(get_instances("cbx_1__1_"))
            sb1 = next(get_instances("sb_1__1_"))

            sb0 = next(get_instances("sb_0__0_"))
            cby01 = next(get_instances("cby_0__1_"))
            sb01 = next(get_instances("sb_0__1_"))
            cbx10 = next(get_instances("cbx_1__0_"))
            sb010 = next(get_instances("sb_1__0_"))

            instance_list.append(((grid_io, cby1, cbx1, sb1, sb0,
                                 cby01, sb01, cbx10, sb010),
                                "tile_1__1_"))
        except StopIteration:
            logger.debug("Missing instance at left_bottom %s %s %s %s %s %s %s %s %s",
                 grid_io, cby1, cbx1, sb1, sb0, cby01, sb01, cbx10, sb010)
            return

        self.merge_and_update(instance_list, "left_bottom_tile")

    def _bottom_right_tile(self):
        ''' Create bottom right tile

        .. rst-class:: ascii

        ::

                +-----+
                |     |
                | CBX |
                +-----+
                +-----+
                |     |
            +---+     |
            |     SB  |
            +---------+

        '''
        instance_list = []
        W, _ = self.fpga_size

        get_instances = self._top_module.get_instances

        try:
            clb = next(get_instances(f"grid_*_{W}__1_"))

            sb10 = next(get_instances(f"sb_{W}__0_"))
            sb11 = next(get_instances(f"sb_{W}__1_"))

            cbx00 = next(get_instances(f"cbx_{W}__0_"))
            cbx01 = next(get_instances(f"cbx_{W}__1_"))

            cby10 = next(get_instances(f"cby_{W}__1_"))

            instance_list.append(((clb, sb11, sb10, cbx00, cbx01, cby10),
                                    f"tile_{W}__1_"))
        except StopIteration:
            logger.debug("Missing instance")
            return

        self.merge_and_update(instance_list, "right_bottom_tile")
