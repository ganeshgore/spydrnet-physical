"""
This is OpenFPGA generated Verilog Netlist Parser Class
"""

import logging
import os
import pickle
import re
from collections import OrderedDict
from fnmatch import fnmatch
from pathlib import Path
from typing import Callable

import spydrnet as sdn
from spydrnet_physical.util import FPGAGridGen, initial_placement

logger = logging.getLogger('spydrnet_logs')


class OpenFPGA:
    '''
    This is top-level clas of OpenFPGa which provides methods for 
    different generic netlist restructuring

    '''

    def __init__(self, grid, netlist, library="work", top_module="fpga_top",
                 arch_xml=None):
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
        self.write_modules_paths = []  # Stores written definitions names
        self.tile_creator = None
        self.config_creator = None
        if arch_xml:
            self.load_grid(arch_xml)
        else:
            self.fpga_grid = None
        self.register_placement_creator(initial_placement)

    @property
    def netlist(self):
        """
        Returns library
        """
        return self._netlist

    @property
    def library(self):
        """
        Returns library
        """
        return self._library

    @property
    def top_module(self) -> sdn.Definition:
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
        self.placement_creator = cls(self.fpga_size,
                                     self._netlist,
                                     self.fpga_grid,
                                     * args, **kwargs)

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

    def create_placement(self, *args, **kwargs):
        """
        Proxy fucntion to add placement and shaping information to each instance
        """
        if not self.placement_creator:
            logger.error("placement_creator not registered")
        return self.placement_creator.create_placement(*args, **kwargs)

    def place_pins(self):
        """
        This adds pin placment nforamtion to tile instances
        """
        NotImplementedError

    def render_floorplan(self):
        """ This method runs the fpga render class to assign
        shape and location to each module instance"""
        pass

    @staticmethod
    def get_custom_boundary(points):
        path = points.split()
        direction = path[0].lower()
        origin = path[1:3]
        boundary = [int(float(origin[0])), int(float(origin[1]))]
        for pt in map(int, map(float, path[3:])):
            if direction == 'v':
                boundary.extend([boundary[-2], boundary[-1]+pt])
                direction = 'h'
            else:
                boundary.extend([boundary[-2]+pt, boundary[-1]])
                direction = 'v'
        return boundary

    @staticmethod
    def get_cross_shape_boundary(points):
        a, b, c, d, e, f = points
        sequence = ([(b, 0), (b, f),
                     (0, f), (0, (f+a)),
                     (b, (f+a)), (b, (a+c+f)),
                     ((b+d), (a+c+f)), ((b+d), (a+f)),
                     ((b+d+e), (a+f)), ((b+d+e), f),
                     ((b+d), f), ((b+d), 0)])
        seen = set()
        u = [x for x in sequence if not (x in seen or seen.add(x))]
        return [val for sublist in u for val in sublist]

    def save_shaping_data(self, pattern="*", scale=1, filename=None):
        output = []
        output.append("{:^20} {:^20} {:^10} {:^10} {:^5} {:^8} {:<20}".format(
            "INSTANCE", "MODULE", "LOC_X", "LOC_Y", "SHAPE", "BBOX_PT", "POINTS"))
        output.append(" = ="*30)
        for instance in self.top_module.get_instances(pattern):
            if "ASSIG" in instance.reference.name:
                continue
            S = instance.reference.properties.get("SHAPE", "rect")
            W = instance.reference.properties.get("WIDTH", 0)
            H = instance.reference.properties.get("HEIGHT", 0)
            P = instance.reference.properties.get("POINTS", 0)
            points = self.get_cross_shape_boundary(P) if S == "cross" else \
                (0, 0, 0, H, W, H, W, 0) if S == "rect" else \
                self.get_custom_boundary(P) if S == "custom" else \
                logger.exception("Unknown shape {} on module {}".format(S,
                                                                        instance.reference.name))
            output.append("{:^20} {:^20} {: 10.2f} {: 10.2f} {:^8} {:^5} {:20}".format(
                instance.name,
                instance.reference.name,
                scale*instance.properties.get("LOC_X", 0),
                scale*instance.properties.get("LOC_Y", 0),
                S,
                4 if S == "rect" else int(len(points)/2),
                " ".join(map(lambda x: f"{x*scale: 6.3f}", points))))
        if filename:
            with open(filename, "w") as fp:
                fp.write("\n".join(output))

    def show_placement_data(self, pattern="*", filename=None):
        output = []
        output.append(" = ="*30)
        output.append("%20s %20s %5s %5s %5s %5s %8s %20s" % ("INSTANCE", "MODULE", "LOC_X", "LOC_Y",
                                                              "WIDTH", "HEIGHT", "SHAPE", "POINTS"))
        output.append(" = ="*30)
        for instance in self.top_module.get_instances(pattern):
            output.append("%20s %20s %5d %5d %5d %5d %8s " % (
                instance.name,
                instance.reference.name,
                instance.properties.get("LOC_X", 0),
                instance.properties.get("LOC_Y", 0),
                instance.reference.properties.get("WIDTH", 0),
                instance.reference.properties.get("HEIGHT", 0),
                instance.reference.properties.get("SHAPE", "--"),
            ))
        print("\n".join(output))
        if filename:
            with open(filename, "w") as fp:
                fp.write("\n".join(output))

    def show_utilization_data(self, pattern="*", filename=None):
        output = []
        output.append(" = ="*30)
        output.append("{:<20s} {:8s} {:6} {:>16} {:>16} {:>8} {:>8}      {}".format(
            "INSTANCE", "SHAPE", "UTIL %", "AREA", "SC_AREA", "WIDTH", "HEIGHT", "POINTS"))
        output.append(" = ="*30)
        seen = []
        for instance in self.top_module.get_instances(pattern):
            if instance.reference.name in seen:
                continue
            if "ASSIG" in instance.reference.name:
                continue
            output.append("{:<20s} {:8s} {:.2%} {:16.2f} {:16.2f} {:8} {:8}      {}".format(
                instance.reference.name,
                instance.reference.properties.get("SHAPE", "--"),
                instance.reference.properties.get(
                    "AREA_UM", "--")/instance.reference.area,
                instance.reference.area,
                instance.reference.properties.get("AREA_UM", "--"),
                instance.reference.properties.get("WIDTH", 0),
                instance.reference.properties.get("HEIGHT", 0),
                instance.reference.properties.get("POINTS", "--"),
            ))
            seen.append(instance.reference.name)
        print("\n".join(output))
        if filename:
            with open(filename, "w") as fp:
                fp.write("\n".join(output))

    def design_instance_map(self, pattern="*", quiet=False):
        design = self._top_module
        inst_cnt = {}
        for inst in design.children:
            if "ASSIG" in inst.reference.library.name:
                continue
            if not inst.reference.name in inst_cnt.keys():
                inst_cnt[inst.reference.name] = []
            inst_cnt[inst.reference.name].append(inst.name)
        return OrderedDict(sorted(inst_cnt.items(),
                                  reverse=True,
                                  key=lambda t: t[1]))

    def design_top_stat(self, pattern="*", quiet=False, filename=None, function=[]):
        '''
        Get statistics of the top module

        Reference       Count
        ========================
        '''
        output_str = []
        design = self._top_module
        inst_cnt = {}
        for inst in design.children:
            if "ASSIG" in inst.reference.library.name:
                continue
            inst_cnt[inst.reference.name] = 1 + \
                inst_cnt.get(inst.reference.name, 0)
        inst_cnt = OrderedDict(sorted(inst_cnt.items(),
                                      reverse=True,
                                      key=lambda t: t[1]))
        output_str.append("= = "*10)
        output_str.append("= = "*3 + " DESIGN STATS " + "= "*7)
        output_str.append("= = "*10)
        output_str.append(f"    top_module : {design.name}")
        output_str.append(f"    definitions: {len(inst_cnt)}")
        output_str.append(f"    instances  : {len(design.children)}")
        output_str.append("= = "*10)
        output_str.append("{: >20} {: >8}".format('References', 'count'))
        output_str.append("- - "*10)
        for def_ in sorted(inst_cnt.keys()):
            if fnmatch(def_, pattern):
                output_str.append("{: >20} {: >8}".format(
                    def_ if len(def_) < 20 else f"...{def_[-17:]}", inst_cnt[def_]))
            for each in function:
                output_str[-1] += each(next(design.get_definitions(def_)))
        if not quiet:
            print("\n".join(output_str))
        if filename:
            with open(filename, 'w') as fp:
                fp.write("\n".join(output_str))
        return inst_cnt

    def remove_direct_interc(self):
        direct_interc = next(
            self._top_module.get_definitions("direct_*"), None)
        if not direct_interc:
            return
        ports = {p.name: p for p in direct_interc.get_ports()}
        for each in list(self._top_module.get_instances("direct_interc_*")):
            wire_from = each.pins[ports["in"].pins[0]].wire
            wire_to = each.pins[ports["out"].pins[0]].wire
            for eachpin in wire_to.pins:
                wire_to.disconnect_pin(eachpin)
                wire_from.connect_pin(eachpin)
            self._top_module.remove_child(each)

    def merge_all_grid_ios(self):
        '''
        This method creates the group of ``grid_io`` and neighbouring ``connection_box``
        whichcna be merge. 

        Variable ``cb_list``, ``grid_io_list`` first creates the list of instances on 
        the periphery of the FPGA, starting from the left bottom corner and going clockwise

        ``merge_list`` is a dictionary which creates the group of instances for
        different unique pairs of the IO and CB blocks 
        '''
        WIDTH = self.fpga_size[0]
        HEIGHT = self.fpga_size[1]
        label = ["cby*"]*HEIGHT + ["cbx*"]*WIDTH + \
            ["cby*"]*HEIGHT + ["cbx*"]*WIDTH
        x_pts = [0]*HEIGHT + list(range(1, WIDTH+1)) + \
                [WIDTH]*HEIGHT + list(range(WIDTH, 0, -1))
        y_pts = list(range(1, HEIGHT)) + [HEIGHT]*(WIDTH+1) + \
            list(range(HEIGHT, 0, -1)) + [0]*WIDTH
        cb_list = ["%s_%d__%d_" % (each) for each in zip(label, x_pts, y_pts)]

        label = ["grid*left*"]*HEIGHT + ["grid*top*"]*WIDTH + \
            ["grid*right*"]*HEIGHT + ["grid*bottom*"]*WIDTH
        x_pts = [0]*HEIGHT + list(range(1, WIDTH+1)) + \
                [WIDTH+1]*HEIGHT + list(range(WIDTH, 0, -1))
        y_pts = list(range(1, HEIGHT+1)) + [HEIGHT+1]*(WIDTH) + \
            list(range(HEIGHT, 0, -1)) + [0]*WIDTH
        grid_io_list = ["%s_%d__%d_" % (each)
                        for each in zip(label, x_pts, y_pts)]

        merge_list = {}
        for cb, io in zip(cb_list, grid_io_list):
            try:
                io = next(self._netlist.get_instances(io))
                cb = next(self._netlist.get_instances(cb))
            except StopIteration:
                logger.exception("Missing instance %s %s" % (cb, io))
            lbl = f"{io.reference.name}_{cb.reference.name}"
            merge_list[lbl] = merge_list.get(lbl, [])
            merge_list[lbl] += [((io, cb), cb.name+"_new")]

        new_defs = []
        for _, instance_list in merge_list.items():
            new_module_name = instance_list[0][0][1].reference.name+"_new"
            mainDef, instance_list = self.top_module.merge_multiple_instance(
                instance_list,
                new_definition_name=new_module_name)
            new_defs.append(
                next(self.library.get_definitions(new_module_name)))
            new_defs[-1].OptPins()
            next(self.library.get_definitions(
                mainDef.name[:-4])).name += "_old"
            mainDef.name = mainDef.name[:-4]
            for inst in instance_list:
                inst.name = inst.name[:-4]
        return new_defs

    def remove_config_chain(self, name="ccff_"):
        """ Remove configuration chain from design """
        cable_list = []
        for cable in list(self.top_module.get_cables(f"*{name}*")):
            cable_list.append(cable.name)
            for pin in list(cable.wires[0].pins):
                if isinstance(pin, sdn.OuterPin):
                    pin.wire.disconnect_pin(pin)
            if not cable.is_port_cable:
                self.top_module.remove_cable(cable)
        return cable_list

    def remove_undriven_nets(self, pattern="*"):
        '''
        Removes undriven/floating nets from the top level

        the net name with undriven keyword in the name is considered as floating nets
        '''
        removed_cables = []
        for cable in self._top_module.get_cables(f"*undriven{pattern}"):
            removed_cables.append(cable.name)
            for wire in cable.wires:
                for pin in wire.pins:
                    wire.disconnect_pin(pin)
            self._top_module.remove_cable(cable)
        return removed_cables

    # def _convert_to_bus(self, module: sdn.Definition, in_patt: str,
    #                     out_patt: str, sort_pins: (Callable) = None):
    #     """
    #     Convertes matching `in_patt` pins to bus with `out_patt` name
    #     """
    #     def get_pins(x): return fnmatch(x.name, in_patt)
    #     ports = list(module.get_ports(filter=get_pins))
    #     port_names = [port.name for port in ports]
    #     suffix = os.path.commonprefix(port_names)
    #     pre_fix = os.path.commonprefix([each[::-1] for each in port_names])
    #     port_names = [each.replace(suffix,"") for each in port_names]
    #     port_names = [each.replace(pre_fix, "") for each in port_names]
    #     def sort_pins(x): return int(port_names[ports.index(x)])
    #     if ports:
    #         ports = sorted(ports, key=sort_pins)
    #         return module.combine_ports(out_patt, ports)

    def _convert_to_bus(self, module: sdn.Definition, in_patt: str,
                        out_patt: str, sort_pins: (Callable) = None):
        """
        Convertes matching `in_patt` pins to bus with `out_patt` name
        """
        def get_pins(x): return fnmatch(x.name, in_patt)
        ports = list(module.get_ports(filter=get_pins))
        if ports:
            # ports = sorted(ports, key=sort_pins or (lambda x: x.name))
            module.combine_ports(out_patt, ports)

    def create_grid_io_bus(self, inpad="inpad", outpad="outpad", sort_pins=None):
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
                self._convert_to_bus(grid_io, f"{side}*_pin_{inpad}_*",
                                     f"io_{side}_in", sort_pins=sort_pins)
                self._convert_to_bus(grid_io, f"{side}*_pin_{outpad}_*",
                                     f"io_{side}_out", sort_pins=sort_pins)

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

        # for port in grid_clb.get_ports("*pin_clk*"):
        #     grid_clb.remove_port(port)

        #  =========  grid_clb renaming =========
        for side in sides:
            #  Input pins
            self._convert_to_bus(grid_clb, f"{side}*_pin_I_*",
                                 f"grid_{side}_in")
            # self._convert_to_bus(grid_clb, f"{side}*_pin_O_*",
            #                      f"grid_{side}_out")

    def create_sb_bus(self, pins=[]):
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
        pins = pins + [("O", "in"), ("inpad", "inpad")]
        sides = ("top", "right", "bottom", "left")
        for sb in self._library.get_definitions("sb_*"):
            for s1 in sides:
                for s2 in sides:
                    # input pins from each corner
                    for pin in pins:
                        self._convert_to_bus(sb, f"{s1}_{s2}_grid_*_pin_{pin[0]}_*",
                                             f"grid_{s1}_{s2[0]}_{pin[1]}")

    def create_cb_bus(self, pins=[]):
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
        pins = pins + [("I", "out"), ("outpad", "outpad")]
        sides = ("top", "right", "bottom", "left")
        for cbx in self._library.get_definitions("cb?_*"):
            for indx, s1 in enumerate(sides):
                # Input pins
                for pin in pins:
                    self._convert_to_bus(cbx, f"*{s1}_grid_*__pin_{pin[0]}_*",
                                         f"grid_{s1}_{pin[1]}")

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

        .. rst-class:: ascii

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
        while self.write_modules_paths:
            self.write_modules_paths.pop()

    def write_include_file(self, filename, relative_from=None):
        relative_from = relative_from or os.environ.get('VERILOG_PROJ_DIR', "")
        with open(filename, "w") as fp:
            for filepath in self.write_modules_paths:
                filepath = str(filepath).replace(relative_from, ".")
                fp.write(f'`include "{filepath}"' + '\n')

    def save_netlist(self, patten="*",  location=".", sort_print=False,
                     skip_constraints=True, sort_cables=False,
                     sort_instances=False, sort_ports=False):
        '''
        Save verilog files
        '''
        for definition in self._library.get_definitions(patten):
            if definition.name in self.written_modules:
                continue
            if sort_ports:
                definition._ports.sort(
                    key=lambda x: str(x._direction) + x.name)
            if sort_cables:
                definition._cables.sort(key=lambda x: x.name)
            if sort_instances:
                definition._children.sort(key=lambda x: x.name)
            logger.debug("Writing %s", definition.name)
            Path(location).mkdir(parents=True, exist_ok=True)
            filepath = os.path.join(location, f"{definition.name}.v")
            sdn.compose(self._netlist,
                        filename=filepath,
                        sort_all=sort_print,
                        skip_constraints=skip_constraints,
                        definition_list=[definition.name],
                        write_blackbox=True)
            self.write_modules_paths.append(filepath)
            self.written_modules.append(definition.name)
        return self.written_modules

    def load_grid(self, pickle_path) -> FPGAGridGen:
        if isinstance(pickle_path, FPGAGridGen):
            self.fpga_grid = pickle_path
        else:
            with open(pickle_path, 'rb') as fp:
                self.fpga_grid: FPGAGridGen = pickle.load(fp)

    def get_top_instance(self, x, y):
        """
        This method generates the grid instance information given the 
        cordinate points 
        """
        if 0 in (x, y):
            return "top"
        if (x % 2 == 0) and (y % 2 == 0):
            grid_lbl = self.fpga_grid.get_block(int(x/2), int(y/2))
            return "%s_%d__%d_" % grid_lbl
        module = {
            True: "sb",
            (x % 2 == 1) and (y % 2 == 0): "cby",
            (x % 2 == 0) and (y % 2 == 1): "cbx"}[True]
        xi, yi = int(x/2), int(y/2)
        if module == "sb":
            if self.fpga_grid.grid[yi+1][xi+1] == self.fpga_grid.UP_ARROW:
                grid_lbl = self.fpga_grid.get_block(xi, yi)
                return "%s_%d__%d_" % grid_lbl
        elif module == "cby":
            if self.fpga_grid.grid[yi][xi+1] in [self.fpga_grid.UP_ARROW, self.fpga_grid.RIGHT_ARROW]:
                grid_lbl = self.fpga_grid.get_block(xi, yi)
                return "%s_%d__%d_" % grid_lbl
        elif module == "cbx":
            if self.fpga_grid.grid[yi+1][xi] in [self.fpga_grid.UP_ARROW]:
                grid_lbl = self.fpga_grid.get_block(xi, yi)
                return "%s_%d__%d_" % grid_lbl
        return f"{module}_{int(x/2)}__{int(y/2)}_"

    def fix_grid_pin_names(self, regex=r".*__pin_(.*)_0_",
                           module="grid_*", name_map=None):
        '''
        This method is used to fix the pin names on the grid modules

        Args:
            regex(str): Regex string used to extract the name of the port
        '''
        name_map = name_map or (lambda x: x)
        eachmodule: sdn.module
        for eachmodule in self.top_module.get_definitions(module):
            logger.debug(f"Fixing pins on {eachmodule.name} module")
            top_port: sdn.Port
            for top_port in eachmodule.get_ports("*"):
                pin_name = re.match(regex, top_port.name)
                if pin_name:
                    pin_name = name_map(pin_name.groups()[0])
                    top_port.change_name(pin_name)
                    logger.debug(f"{top_port.name} =>> {pin_name}")
