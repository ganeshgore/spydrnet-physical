"""
"""
import typing
from spydrnet_physical.util import GridFloorplanGen

if typing.TYPE_CHECKING:
    import spydrnet as sdn


class OpenFPGA_Tile_Generator:

    def __init__(self, grid, netlist, library, top_module):
        self.fpga_size = grid
        self._netlist = netlist
        self._library = library
        self._top_module = top_module

    def create_tiles(self):
        '''
        This will be extendned in the class
        '''
        raise NotImplementedError


class OpenFPGA_Placement_Generator:
    """
    Template class to create OpenFPGA Placement generator
    """
    fpga_size = (0, 0)
    """ (int, int): Size of the FPGA """

    netlist = (0, 0)
    """ (sdn.netlist): Design netlist """

    fpga_grid = (0, 0)
    """ (list(list)): Two dimentional list of mapping instances to grid """

    design_grid = None
    """ (GridFloorplanGen): Design grid markers """

    def __init__(self, grid_size, netlist, fpga_grid):
        self.fpga_size = grid_size
        self._netlist = netlist
        self._top_module = netlist.top_instance.reference
        self.fpga_grid = fpga_grid
        self.design_grid = GridFloorplanGen(grid_size[0]*2 + 1, grid_size[1]*2 + 1,
                                            grid_x=200, grid_y=200)

    def create_placement(self):
        '''
        This will be extendned in the class
        '''
        raise NotImplementedError

    def update_placement(self):
        '''
        This will be extendned in the class
        '''
        raise NotImplementedError


class OpenFPGA_Config_Generator:

    def __init__(self, grid, netlist, library, top_module):
        self.fpga_size = grid
        self._netlist = netlist
        self._library = library
        self._top_module = top_module
        self._head = "ccff_head"
        self._tail = "ccff_tail"
        self.cable_name = "ccff_wire"

    def add_configuration_scheme(self):
        '''
        This will be extendned in the class
        '''
        raise NotImplementedError

    def write_fabric_key(self):
        '''
        This will be extendned in the class
        '''
        raise NotImplementedError

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @head.setter
    def head(self, value):
        self._head = value

    @tail.setter
    def tail(self, value):
        self._tail = value

    def _connect_instances(self, module, inst_list):
        for from_inst, to_inst in zip(inst_list[:-1], inst_list[1:]):
            cable = self._top_module.create_cable(
                f"{from_inst.name}__{to_inst.name}_ccff_tail")
            wire = cable.create_wire()
            wire.connect_pin(next(from_inst.get_port_pins(self.tail)))
            wire.connect_pin(next(to_inst.get_port_pins(self.head)))
        return cable
