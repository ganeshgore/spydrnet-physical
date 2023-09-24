"""
This class is created for OpenFPGA related netlist transformations
"""
import logging

from spydrnet_physical.util import Tile01
from spydrnet_physical.util.shell import launch_shell

logger = logging.getLogger('spydrnet_logs')


class Tile04(Tile01):
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
                    instance_grid[x][y] = next(self._top_module.get_instances(f"grid_*_{x}__{y}_"))
                except StopIteration:
                    logger.warning(f"grid not found at {x} {y}")

        instance_list = {}
        for x in range(0, self.fpga_size[0]+1):
            for y in range(0, self.fpga_size[1]+1):
                if instance_grid[x][y] is None:
                    continue
                try:
                    inst = []
                    inst.append(instance_grid[x][y])
                    try:
                        inst.append(next(tm.get_instances(f"cbx_{x}__{y}_")))
                    except StopIteration:
                        pass
                    try:
                        inst.append(next(tm.get_instances(f"cby_{x}__{y}_")))
                    except StopIteration:
                        pass
                    inst.append(next(tm.get_instances(f"sb_{x}__{y}_")))

                    if x == 1:
                        inst.append(next(tm.get_instances(f"cby_{x-1}__{y}_")))
                        inst.append(next(tm.get_instances(f"sb_{x-1}__{y}_")))
                    if y == 1:
                        inst.append(next(tm.get_instances(f"cbx_{x}__{y-1}_")))
                        inst.append(next(tm.get_instances(f"sb_{x}__{y-1}_")))
                    if y == 1 and x == 1:
                        inst.append(next(tm.get_instances(f"sb_{x-1}__{y-1}_")))


                    # Vertical search (max 16 height)
                    for y_off in range(1, 16):
                        if y+y_off > self.fpga_size[1]:
                            break
                        if not instance_grid[x][y+y_off] is None:
                            break
                        try:
                            inst.append(next(tm.get_instances(f"cbx_{x}__{y+y_off}_")))
                        except StopIteration:
                            pass
                        try:
                            inst.append(next(tm.get_instances(f"cby_{x}__{y+y_off}_")))
                        except StopIteration:
                            pass
                        inst.append(next(tm.get_instances(f"sb_{x}__{y+y_off}_")))


                    tile_name = inst[0].reference.name.replace('grid_', '')
                    uname = tile_name + ":" + "_".join([i.reference.name for i in inst])

                    instance_list[uname] = instance_list.get(uname, [])
                    instance_list[uname].append((tuple(inst),f"tile_{x}__{y}_"))

                except StopIteration:
                    logger.warning(f"Missing instance at {x} {y}")

        keys = sorted(instance_list.keys(), reverse=True,
                      key=lambda x: len(instance_list[x]))

        module_names = []
        for indx, key in enumerate(keys):
            module_name = f"{key.split(':')[0]}_tile"
            indx = 0
            while module_name in module_names:
                indx = indx+1
                module_name = f"{key.split(':')[0]}_tile_{indx}"

            logger.info(f"Creating {module_name} with {len(instance_list[key])} instances")
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
