"""
This class is created for OpenFPGA related netlist transformations
"""
import logging

from spydrnet_physical.util import Tile01
from spydrnet_physical.util.shell import launch_shell

logger = logging.getLogger('spydrnet_logs')


class HeteroSuperTile(Tile01):
    """
    Creates Tile04 style tiling structure
    """

    def create_tiles(self):
        '''
        Creates tiles
        '''
        tm = self._top_module
        instance_grid = [[None for _ in range(self.fpga_size[1]+1)] for _ in range(self.fpga_size[0]+1)]
        for x in range(1, self.fpga_size[0]+1):
            for y in range(1, self.fpga_size[1]+1):
                try:
                    instance_grid[x][y] = next(self._top_module.get_instances(f"*_{x}__{y}_"))
                except StopIteration:
                    logger.warning(f"grid not found at {x} {y}")

        instance_list = {}
        curr_y = 1
        for indx_row, each_row in enumerate(self.TILE_ROW_HEIGHT):
            curr_x = 1
            for indx_col, each_col in enumerate(self.TILE_COL_WIDTH):
                # print(f"({each_row:2d}, {each_col:2d})", end=" ")
                # print(f"({curr_y:3d}, {curr_x:3d})", end=" :")
                inst = []
                for c in range(curr_x, curr_x+each_col):
                    for r in range(curr_y, curr_y + each_row):
                        # print(f"{c}-{r}", end=" ")
                        if instance_grid[c][r] is None:
                            continue
                        else:
                            inst.append(instance_grid[c][r])
                if len(inst):
                    uname = inst[-1].reference.name.replace("tile","stile")
                    # print(uname, end=" ")
                    uname = uname + ":" + "_".join([i.reference.name for i in inst])

                    instance_list[uname] = instance_list.get(uname, [])
                    instance_list[uname].append(
                        (tuple(inst), f"stile_{indx_row}__{indx_col}_")
                    )
                    # print(uname, end=" ")

                # print()
                curr_x+=each_col
            curr_y+=each_row

        # instance_list = {}
        # for x in range(0, self.fpga_size[0]+1):
        #     for y in range(0, self.fpga_size[1]+1):
        #         inst = []
        #         if instance_grid[x][y] is None:
        #             continue
        #         elif instance_grid[x][y].reference.name == "bram_tile":
        #             inst.append(instance_grid[x][y])
        #             logger.info(f"= = = = = = BRAM_TILE {x} {y} = = = = = = ")
        #             for height in range(6):
        #                 for width in range(1,6):
        #                     inst.append(instance_grid[x - width][y + height])
        #                     print(instance_grid[x - width][y + height])
        #             uname = "bram_stile"

        #         elif instance_grid[x][y].reference.name == "dsp_tile":
        #             inst.append(instance_grid[x][y])
        #             logger.info(f"= = = = = = DSP_TILE {x} {y} = = = = = = ")
        #             for height in range(3):
        #                 for width in range(1,6):
        #                     inst.append(instance_grid[x - width][y + height])
        #                     print(instance_grid[x - width][y + height])
        #             uname = "dsp_stile"
        #         else:
        #             continue

        #         uname = uname + ":" + "_".join([i.reference.name for i in inst])

        #         instance_list[uname] = instance_list.get(uname, [])
        #         instance_list[uname].append((tuple(inst),f"stile_{x}__{y}_"))

        keys = sorted(
            instance_list.keys(), reverse=True, key=lambda x: len(instance_list[x])
        )

        module_names = []
        for indx, key in enumerate(keys):
            module_name = f"{key.split(':')[0]}"
            indx = 0
            while module_name in module_names:
                indx = indx + 1
                module_name = f"{key.split(':')[0]}_{indx}"

            logger.info(
                f"Creating {module_name} with {len(instance_list[key])} instances"
            )
            self.merge_and_update(instance_list[key], module_name)
            module_names.append(module_name)

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
