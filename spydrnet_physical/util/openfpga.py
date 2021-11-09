
import logging
import os
import re
from collections import OrderedDict
from fnmatch import fnmatch
from pathlib import Path
from typing import Callable
from spydrnet.ir.definition import Definition
from spydrnet_physical.util import initial_placement

import spydrnet as sdn

logger = logging.getLogger('spydrnet_logs')


class OpenFPGA:

    def __init__(self, grid, netlist, library="work", top_module="fpga_top"):
        '''
        Init class with OpenFPGA netlist

        args:
            grid (int, int): Size of the FPGA grid
            netlist (sdn.netlist): Pass OpenFPGA core netlist
            library (str): library name
            top_module (str): top_module name
        '''
        self.fpga_size = grid
        self._netlist = netlist
        self._library = next(netlist.get_libraries(library))
        self._top_module = next(self._library.get_definitions(top_module))
        netlist.top_instance = self._top_module
        self.written_modules = []  # Stores written definitions names
        self.tile_creator = None
        self.config_creator = None
        self.register_placement_creator(initial_placement)

    @property
    def library(self):
        """
        Returns library
        """
        return self._library

    @property
    def top_module(self) -> Definition:
        """
        Returns top_module
        """
        return self._top_module

    def register_tile_generator(self, cls, *args, **kwargs):
        """
        This registers the tile generator class to OpenFPGA base class
        """
        self.tile_creator = cls(
            self.fpga_size, self._netlist, self.library, self._top_module, *args, **kwargs)

    def register_config_generator(self, cls, *args, **kwargs):
        """
        This registers the tile generator class to OpenFPGA base class
        """
        self.config_creator = cls(
            self.fpga_size, self._netlist, self.library, self._top_module, *args, **kwargs)

    def register_placement_creator(self, cls, *args, **kwargs):
        """
        This registers the tile generator class to OpenFPGA base class
        """
        self.placement_creator = cls(
            self.fpga_size, self._netlist, self.library, self._top_module, *args, **kwargs)

    def create_tiles(self):
        """
        proxy function to create_tiles method of  tile_creator class
        """
        if not self.tile_creator:
            logger.error("tile_creator not registered")
        return self.tile_creator.create_tiles()

    def add_configuration_scheme(self):
        """
        proxy function to create_tiles method of tile_creator class
        """
        if not self.config_creator:
            logger.error("config_creator not registered")
        return self.config_creator.add_configuration_scheme()

    def create_placement(self):
        """
        Proxy fucntion to add placement and shaping information to each instance
        """
        if not self.placement_creator:
            logger.error("placement_creator not registered")
        return self.placement_creator.create_placement()

    def place_pins(self):
        """
        This adds pin placment nforamtion to tile instances
        """
        NotImplementedError

    def render_floorplan(self):
        """ This method runs the fpga render class to assign
        shape and location to each module instance"""
        pass

    def show_placement_data(self, pattern="*"):
        print("%20s %20s %5s %5s %5s %5s" % ("MODULE", "INSTANCE", "LOC_X", "LOC_Y",
                                             "WIDTH", "HEIGHT"))
        print(" = ="*20)
        for instance in self.top_module.get_instances(pattern):
            print("%20s %20s %5d %5d %5d %5d" % (
                instance.name,
                instance.reference.name,
                instance.properties.get("LOC_X", 0),
                instance.properties.get("LOC_Y", 0),
                instance.reference.properties.get("WIDTH", 0),
                instance.reference.properties.get("HEIGHT", 0),
            ))

    def design_top_stat(self):
        '''
        Get statistics of the top module

        Reference       Count
        ========================
        '''
        design = self._top_module
        print("= = "*10)
        print("= = "*3 + " DESIGN STATS " + "= "*7)
        print("= = "*10)
        print(f"    top_module : {design.name}")
        print(f"    instances  : {len(design.children)}")
        print("= = "*10)
        inst_cnt = {}
        for inst in design.children:
            inst_cnt[inst.reference.name] = 1 + \
                inst_cnt.get(inst.reference.name, 0)
        inst_cnt = OrderedDict(sorted(inst_cnt.items(),
                                      reverse=True,
                                      key=lambda t: t[1]))
        print("{: >20} {: >8}".format('References', 'count'))
        print("- - "*10)
        for def_, count in inst_cnt.items():
            print("{: >20} {: >8}".format(
                def_ if len(def_) < 20 else f"...{def_[-17:]}", count))
        return inst_cnt

    def remove_config_chain(self):
        """ Remove configuration chain from design """
        cable_list = []
        for cable in list(self.top_module.get_cables("*ccff_*")):
            cable_list.append(cable.name)
            for pin in list(cable.wires[0].pins):
                if isinstance(pin, sdn.OuterPin):
                    pin.wire.disconnect_pin(pin)
            if not cable.is_port_cable:
                self.top_module.remove_cable(cable)
        return cable_list

    def remove_undriven_nets(self):
        '''
        Removes undriven/floating nets from the top level

        the net name with undriven keyword in the name is considered as floating nets
        '''
        removed_cables = []
        for cable in self._top_module.get_cables("*undriven*"):
            removed_cables.append(cable.name)
            self._top_module.remove_cable(cable)
        return removed_cables

    def _convert_to_bus(self, module: sdn.Definition, in_patt: str,
                        out_patt: str, sort_pins: (Callable) = None):
        """
        Convertes matching `in_patt` pins to bus with `out_patt` name
        """
        def get_pins(x): return fnmatch(x.name, in_patt)
        ports = list(module.get_ports(filter=get_pins))
        if ports:
            ports = sorted(ports, key=sort_pins or (lambda x: x.name))
            module.combine_ports(out_patt, ports)

    def create_grid_io_bus(self):
        """
        Convert `grid_io` Input/Output pins to bus structure
        ::
          # Input Pins
          right_width_0_height_0_subtile_*__pin_inpad_0_    -> io_right_in
          left_width_0_height_0_subtile_*__pin_inpad_0_     -> io_left_in
          top_width_0_height_0_subtile_*__pin_inpad_0_      -> io_top_in
          bottom_width_0_height_0_subtile_*__pin_inpad_0_   -> io_bottom_in

          # Output Pins
          right_width_0_height_0_subtile_*__pin_outpad_0_   -> io_right_out
          left_width_0_height_0_subtile_*__pin_outpad_0_    -> io_left_out
          top_width_0_height_0_subtile_*__pin_outpad_0_     -> io_top_out
          bottom_width_0_height_0_subtile_*__pin_outpad_0_  -> io_bottom_out
        """
        sides = ("left", "top", "right", "bottom")

        #  =========  grid_io renaming =========
        for grid_io in self._library.get_definitions("grid_io*"):
            for side in sides:
                #  Input pins
                self._convert_to_bus(grid_io, f"{side}*_pin_outpad_*",
                                     f"io_{side}_in")
                self._convert_to_bus(grid_io, f"{side}*_pin_outpad_*",
                                     f"io_{side}_out")

    def create_grid_clb_bus(self):
        '''
        Convert `grid_clb` Input/Output pins to bus structure
        ::
          # Input Pins
          right_width_0_height_0_subtile_*__pin_I_0_    -> grid_right_in
          left_width_0_height_0_subtile_*__pin_I_0_     -> grid_left_in
          top_width_0_height_0_subtile_*__pin_I_0_      -> grid_top_in
          bottom_width_0_height_0_subtile_*__pin_I_0_   -> grid_bottom_in

          # Output Pins
          right_width_0_height_0_subtile_*__pin_O_0_    -> grid_right_out
          left_width_0_height_0_subtile_*__pin_O_0_     -> grid_left_out
          top_width_0_height_0_subtile_*__pin_O_0_      -> grid_top_out
          bottom_width_0_height_0_subtile_*__pin_O_0_   -> grid_bottom_out
        '''

        sides = ("left", "top", "right", "bottom")
        grid_clb = next(self._library.get_definitions("grid_clb*"))

        for port in grid_clb.get_ports("*pin_clk*"):
            grid_clb.remove_port(port)

        #  =========  grid_clb renaming =========
        for side in sides:
            #  Input pins
            self._convert_to_bus(grid_clb, f"{side}*_pin_I_*",
                                 f"grid_{side}_in")
            self._convert_to_bus(grid_clb, f"{side}*_pin_O_*",
                                 f"grid_{side}_out")

    def create_sb_bus(self):
        """
        Convert `sb` Input pins to bus structure
        ::
          # Input Pins
          top_left_grid_right_width_0_height_0_subtile_*__pin_O_*_      -> sb_top_l_in
          top_right_grid_left_width_0_height_0_subtile_*__pin_O_*_      -> sb_top_r_in
          bottom_left_grid_right_width_0_height_0_subtile_*__pin_O_*_   -> sb_bottom_l_in
          bottom_right_grid_left_width_0_height_0_subtile_*__pin_O_*_   -> sb_bottom_r_in

          left_top_grid_bottom_width_0_height_0_subtile_*__pin_O_*_     -> sb_left_t_in
          left_bottom_grid_top_width_0_height_0_subtile_*__pin_O_*_     -> sb_left_b_in
          right_top_grid_bottom_width_0_height_0_subtile_*__pin_O_*_    -> sb_right_t_in
          right_bottom_grid_top_width_0_height_0_subtile_*__pin_O_*_    -> sb_right_b_in
        """

        sides = ("top", "right", "bottom", "left")
        for sb in self._library.get_definitions("sb_*"):
            for s1 in sides:
                for s2 in sides:
                    # input pins from each corner
                    self._convert_to_bus(sb, f"{s1}_{s2}_grid_*_pin_O_*",
                                         f"grid_{s1}_{s2[0]}_in")
                    self._convert_to_bus(sb, f"*{s1}_{s2}_grid_*__pin_inpad_*",
                                         f"grid_{s1}_{s2[0]}_inpad")

    def create_cb_bus(self):
        """
        Convert `cb` Input pins to bus structure
        ::

          right_grid_left_width_0_height_0_subtile_*__pin_I_*_      -> grid_right_in
          left_grid_right_width_0_height_0_subtile_*__pin_I_*_      -> grid_left_in
          top_grid_bottom_width_0_height_0_subtile_*__pin_I_*_      -> grid_top_in
          bottom_grid_top_width_0_height_0_subtile_*__pin_I_*_      -> grid_bottom_in

          right_grid_left_width_0_height_0_subtile_*__pin_outpad_*_ -> grid_right_in
          left_grid_right_width_0_height_0_subtile_*__pin_outpad_*_ -> grid_left_in
          top_grid_bottom_width_0_height_0_subtile_*__pin_outpad_*_ -> grid_top_in
          bottom_grid_top_width_0_height_0_subtile_*__pin_outpad_*_ -> grid_bottom_in
        """
        sides = ("top", "right", "bottom", "left")
        for cbx in self._library.get_definitions("cb?_*"):
            for indx, s1 in enumerate(sides):
                # Input pins
                self._convert_to_bus(cbx, f"*{s1}_grid_*__pin_I_*",
                                     f"grid_{s1}_out")
                self._convert_to_bus(cbx, f"*{s1}_grid_*__pin_outpad_*",
                                     f"grid_{s1}_outpad")

    def _get_cordinates(self, name):
        x, y = map(int, re.match(r".*_(\w+)__(\w+)_", name).groups())
        return x, y

    def _create_grid_out_feedthrough(self, clb, side):
        ft_map = {}
        for grid in clb.references:
            cable = grid.get_port_cables(f"grid_{side}_out")[0]
            x, y = self._get_cordinates(grid.name)
            through_inst_name = {
                "left": f"cby_{x-1}__{y+0}_",
                "right": f"cby_{x-0}__{y+0}_",
                "top": f"cbx_{x+0}__{y+0}_",
                "bottom": f"cbx_{x+0}__{y-1}_",
            }[side]
            through_inst = next(
                self._top_module.get_instances(through_inst_name))
            ref_name = through_inst.reference.name
            ft_map[ref_name] = ft_map.get(ref_name, [])
            ft_map[ref_name].append((cable, (through_inst,)))

        for ref_name, inst_map in ft_map.items():
            cables, new_ports = self._top_module.create_ft_multiple(inst_map)
            side1, side2, oppo_side = {
                "left": ('top', 'bottom', 'right'),
                "right": ('top', 'bottom', 'left'),
                "top": ('left', 'right', 'bottom'),
                "bottom": ('left', 'right', 'top'),
            }[side]
            new_ports[0][0].change_name(f"grid_{oppo_side}_in")
            new_ports[0][1].change_name(f"grid_{side1}_{side[0]}_out")
            for cable in cables:
                cable.name = cable.name.replace("_out_", f"_{side1}_out_")

            cables, new_ports = self._top_module.create_ft_multiple(inst_map)
            new_ports[0][0].change_name(f"grid_{oppo_side}_in2")
            new_ports[0][1].change_name(f"grid_{side2}_{side[0]}_out")
            for cable in cables:
                cable.name = cable.name.replace("_out_", f"_{side2}_out_")
            next(self._library.get_definitions(ref_name)).OptPins()

    def create_grid_clb_feedthroughs(self):
        '''
        Creates feedthrough for ``grid_clb`` outputs, to convert digonal
        connections to horizontal and vertical

        `grid_clb` output on each side is feedthrough from connection box as
        shown in the following example (onle left side feedthroughs are shown)
        ::
          +-----+                       +-----+
          |     |                       |     |
          |     +--+                    |     +--+
          | SB     |                    | SB     |
          |     +-++                    |     +--+
          |     | |                     |     |
          +-----+ |                     +--+--+
                  |  +------               |       +------
          +-----+ |  |                  +-----+    |
          |     | |  |                  |  |  |    |
          |     | +--+ CLB              |  +-------+ CLB
          | CBX | |  |                  |  |  |    |
          +-----+ |  |                  +-----+    |
                  |  |                     |       |
          +-----+ |  +------            +--+--+    +------
          |     | |                     |     |
          |     +-++                    |     +--+
          | SB     |                    | SB     |
          |     +--+                    |     +--+
          |     |                       |     |
          +-----+                       +-----+
          Before                After feedthrough creations
        '''
        clb = next(self._library.get_definitions("grid_clb"))

        self._create_grid_out_feedthrough(clb, 'left')
        self._create_grid_out_feedthrough(clb, 'right')
        self._create_grid_out_feedthrough(clb, 'top')
        self._create_grid_out_feedthrough(clb, 'bottom')

    def clear_written_modules(self):
        while self.written_modules:
            self.written_modules.pop()

    def save_netlist(self, patten="*",  location=".", skip_constraints=True):
        '''
        Save verilog files
        '''
        for definition in self._library.get_definitions(patten):
            if definition.name in self.written_modules:
                continue
            logger.debug("Writing %s", definition.name)
            Path(location).mkdir(parents=True, exist_ok=True)
            sdn.compose(self._netlist,
                        filename=os.path.join(
                            location, f"{definition.name}.v"),
                        skip_constraints=skip_constraints,
                        definition_list=[definition.name],
                        write_blackbox=True)
            self.written_modules.append(definition.name)
        return self.written_modules
