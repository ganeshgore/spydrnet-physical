"""
This is OpenFPGA generated Verilog Netlist Parser Class
"""

import logging
import math
import os
import pickle
import re
import tempfile
from collections import OrderedDict
from fnmatch import fnmatch
from pathlib import Path
from typing import Callable

import spydrnet as sdn
from spydrnet_physical.util import FPGAGridGen, initial_placement

logger = logging.getLogger("spydrnet_logs")

PROP = "VERILOG.InlineConstraints"


class OpenFPGA:
    """
    This is top-level clas of OpenFPGa which provides methods for
    different generic netlist restructuring

    """

    SC_HEIGHT = 1
    CPP = 0.2
    GLOBAL_SCALE = 100
    SC_GRID = SC_HEIGHT * CPP

    def __init__(
        self,
        grid,
        netlist=None,
        verilog_files=None,
        cell_files=None,
        library="work",
        top_module="fpga_top",
        arch_xml=None,
    ):
        """
        Init class with OpenFPGA netlist

        args:
            grid (int, int): Size of the FPGA grid
            netlist (sdn.netlist): Pass OpenFPGA core netlist
            library (str): library name
            top_module (str): top_module name
        """
        self.fpga_size = list(grid)
        if netlist:
            self._netlist = netlist
        elif verilog_files:
            with tempfile.NamedTemporaryFile(suffix=".v") as fp:
                for each_file in verilog_files:
                    with open(each_file, "r", encoding="UTF-8") as fpv:
                        fp.write(str.encode(" ".join(fpv.readlines())))
                if cell_files:
                    fp.write("`celldefine\n".encode())
                    for each_file in cell_files:
                        with open(each_file, "r", encoding="UTF-8") as fpv:
                            fp.write(str.encode(" ".join(fpv.readlines())))
                    fp.write("`endcelldefine\n".encode())
                fp.seek(0)
                self._netlist = sdn.parse(fp.name)
        else:
            logger.error("Provide verilog either verilog files or netlist object")
        self._library = next(self._netlist.get_libraries(library))
        self._top_module = next(self._library.get_definitions(top_module))
        self._netlist.top_instance = self._top_module
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
            self.fpga_size,
            self._netlist,
            self.library,
            self._top_module,
            *args,
            **kwargs,
        )

    def register_config_generator(self, cls, *args, **kwargs):
        """
        This registers the tile generator class to OpenFPGA base class
        """
        self.config_creator = cls(
            self.fpga_size,
            self._netlist,
            self.library,
            self._top_module,
            *args,
            **kwargs,
        )

    def register_placement_creator(self, cls, *args, **kwargs):
        """
        This registers the tile generator class to OpenFPGA base class
        """
        self.placement_creator = cls(
            self.fpga_size, self._netlist, self.fpga_grid, *args, **kwargs
        )
        self.placement_creator.CPP = self.CPP
        self.placement_creator.SC_HEIGHT = self.SC_HEIGHT
        self.placement_creator.SC_GRID = self.CPP * self.SC_HEIGHT

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
        raise NotImplementedError()

    def render_floorplan(self):
        """This method runs the fpga render class to assign
        shape and location to each module instance"""
        pass

    @staticmethod
    def get_custom_boundary(points):
        path = points.split()
        direction = path[0].lower()
        origin = path[1:3]
        boundary = [int(float(origin[0])), int(float(origin[1]))]
        for pt in map(int, map(float, path[3:])):
            if direction == "v":
                boundary.extend([boundary[-2], boundary[-1] + pt])
                direction = "h"
            else:
                boundary.extend([boundary[-2] + pt, boundary[-1]])
                direction = "v"
        offset_x = -1 * int(min(map(float, boundary[::2])))
        offset_y = -1 * int(min(map(float, boundary[1::2])))
        for indx in range(0, len(boundary), 2):
            boundary[indx] += offset_x
            boundary[indx + 1] += offset_y
        return boundary

    @staticmethod
    def get_cross_shape_boundary(points):
        a, b, c, d, e, f = points
        sequence = [
            (b, 0),
            (b, f),
            (0, f),
            (0, (f + a)),
            (b, (f + a)),
            (b, (a + c + f)),
            ((b + d), (a + c + f)),
            ((b + d), (a + f)),
            ((b + d + e), (a + f)),
            ((b + d + e), f),
            ((b + d), f),
            ((b + d), 0),
        ]
        seen = set()
        u = [x for x in sequence if not (x in seen or seen.add(x))]
        return [val for sublist in u for val in sublist]

    def save_shaping_data(self, pattern="*", scale=None, filename=None, custom_entry=None):
        """
        Save the shaping data
        """
        output = []
        scale = scale or self.GLOBAL_SCALE
        output.append(
            "{:^20} {:^20} {:^10} {:^10} {:^5} {:^8} {:<20}".format(
                "INSTANCE", "MODULE", "LOC_X", "LOC_Y", "SHAPE", "BBOX_PT", "POINTS"
            )
        )
        output.append(" = =" * 30)
        for instance in sorted(
            list(self.top_module.get_instances(pattern)), key=lambda x: x.name
        ):
            if "ASSIG" in instance.reference.name:
                continue
            if instance.reference.name.startswith("const"):
                continue
            S = instance.reference.properties.get("SHAPE", "rect")
            W = instance.reference.properties.get("WIDTH", 0)
            H = instance.reference.properties.get("HEIGHT", 0)
            P = instance.reference.properties.get("POINTS", 0)
            points = (
                self.get_cross_shape_boundary(P)
                if S == "cross"
                else (0, 0, 0, H, W, H, W, 0)
                if S == "rect"
                else self.get_custom_boundary(P)
                if S == "custom"
                else logger.exception(
                    "Unknown shape %s on module %s", S, instance.reference.name
                )
            )

            output.append(
                "{:^20} {:^20} {: 10.{precision}f} {: 10.{precision}f} {:^8} {:^5} {:20}".format(
                    instance.name,
                    instance.reference.name,
                    scale * instance.properties.get("LOC_X", 0),
                    scale * instance.properties.get("LOC_Y", 0),
                    S,
                    4 if S == "rect" else int(len(points) / 2),
                    " ".join(map(lambda x: f"{x*scale: 6.3f}", points)),
                    precision=int(round(math.log(1 / scale, 10))),
                )
            )

        W = float(self.top_module.properties.get("WIDTH", 1000))
        H = float(self.top_module.properties.get("HEIGHT", 1000))

        output.append(
            "{:^20} {:^20} {: 10.{precision}f} {: 10.{precision}f} {:^8} {:^5} {:20}".format(
                self.top_module.name,
                self.top_module.name,
                0,
                0,
                "rect",
                4,
                " ".join(map(lambda x: f"{x*scale: 6.3f}", (0, 0, 0, H, W, H, W, 0))),
                precision=int(round(math.log(1 / scale, 10))),
            )
        )
        if custom_entry:
            for p in custom_entry:
                output.append(
                    "{:^20} {:^20} {: 10.{precision}f} {: 10.{precision}f} {:^8} {:^5} {:20}".format(
                        *p,
                        precision=int(round(math.log(1 / scale, 10))),
                    )
                )
        if filename:
            with open(filename, "w", encoding="UTF-8") as fp:
                fp.write("\n".join(output))
                fp.write("\n")
        return output

    def show_placement_data(self, pattern="*", filename=None):
        """
        This shows  the placement data of each instance on the screen
        """
        output = []
        output.append(" = =" * 30)
        # fmt: off
        output.append("%20s %20s %5s %8s %8s %8s %8s %20s"
                % ("INSTANCE", "MODULE", "LOC_X", "LOC_Y",
                   "WIDTH", "HEIGHT", "SHAPE", "POINTS"))
        # fmt: on
        output.append(" = =" * 30)
        for instance in self.top_module.get_instances(pattern):
            output.append(
                f"{instance.name:20s} "
                + f"{instance.reference.name:20s} "
                + f"{instance.properties.get('LOC_X', 0): 5d} "
                + f"{instance.properties.get('LOC_Y', 0): 5d} "
                + f"{instance.reference.properties.get('WIDTH', 0):5d} "
                + f"{instance.reference.properties.get('HEIGHT', 0):5d} "
                + f"{instance.reference.properties.get('SHAPE', '--'):8s} "
            )
        print("\n".join(output))
        if filename:
            with open(filename, "w", encoding="UTF-8") as fp:
                fp.write("\n".join(output))

    def show_utilization_data(self, pattern="*", filename=None):
        """
        Show the utilization of the modules
        """
        output = []
        output.append(" = =" * 30)
        output.append(
            f"{'MODULE':>20s} {'SHAPE':8s} {'UTIL %':6} {'AREA':>16} {'SC_AREA_GRID':>16} {'SC_AREA_UM':>16}"
            + f"{'WIDTH':>8} {'HEIGHT':>8}      {'POINTS':<10}"
        )

        output.append(" = =" * 30)
        seen = []
        for instance in self.top_module.get_instances(pattern):
            if instance.reference.name in seen:
                continue
            if "ASSIG" in instance.reference.name:
                continue
            if instance.reference.name.startswith("const"):
                continue

            output.append(
                "{:<20s} {:8s} {:.2%} {:16.2f} {:16d} {:16.2f} {:8} {:8}      {}".format(
                    instance.reference.name,
                    instance.reference.properties.get("SHAPE", "--"),
                    instance.reference.utilization,
                    instance.reference.area,
                    instance.reference.properties.get("AREA", 0),
                    instance.reference.properties.get("AREA_UM", 0),
                    instance.reference.properties.get("WIDTH", 0),
                    instance.reference.properties.get("HEIGHT", 0),
                    instance.reference.properties.get("POINTS", "--"),
                )
            )
            seen.append(instance.reference.name)
        print("\n".join(output))
        if filename:
            with open(filename, "w", encoding="UTF-8") as fp:
                fp.write("\n".join(output))

    def design_instance_map(self, pattern="*", quiet=False):
        """
        Returns instance current netlist instance map
        """
        design = self._top_module
        inst_cnt = {}
        for inst in design.children:
            if "ASSIG" in inst.reference.library.name:
                continue
            if inst.reference.name.startswith("const"):
                continue
            if fnmatch(inst.reference.name, pattern):
                if not inst.reference.name in inst_cnt.keys():
                    inst_cnt[inst.reference.name] = []
                inst_cnt[inst.reference.name].append(inst.name)
        return OrderedDict(sorted(inst_cnt.items(), reverse=True))

    def design_top_stat(self, pattern="*", quiet=False, filename=None, function=()):
        """
        Get statistics of the top module

        Reference       Count
        ========================
        """
        output_str = []
        design = self._top_module
        inst_cnt = {}
        for inst in design.children:
            if "ASSIG" in inst.reference.library.name:
                continue
            if inst.reference.name.startswith("const"):
                continue
            if fnmatch(inst.reference.name, pattern):
                inst_cnt[inst.reference.name] = 1 + inst_cnt.get(inst.reference.name, 0)
        inst_cnt = OrderedDict(
            sorted(inst_cnt.items(), reverse=True, key=lambda t: t[1])
        )
        output_str.append("= = " * 10)
        output_str.append("= = " * 3 + " DESIGN STATS " + "= " * 7)
        output_str.append("= = " * 10)
        output_str.append(f"    top_module : {design.name}")
        output_str.append(f"    definitions: {len(inst_cnt)}")
        output_str.append(f"    instances  : {sum([v for _, v in inst_cnt.items()])}")
        output_str.append("= = " * 10)
        output_str.append("{: >20} {: >8}".format("References", "count"))
        output_str.append("- - " * 10)
        for def_ in sorted(inst_cnt.keys()):
            if fnmatch(def_, pattern):
                output_str.append(
                    "{: >20} {: >8}".format(
                        def_ if len(def_) < 20 else f"...{def_[-17:]}", inst_cnt[def_]
                    )
                )
            for each in function:
                output_str[-1] += each(next(design.get_definitions(def_)))
        if not quiet:
            print("\n".join(output_str))
        if filename:
            with open(filename, "w", encoding="UTF-8") as file_ptr:
                file_ptr.write("\n".join(output_str))
        return inst_cnt

    def remove_direct_interc(self):
        """
        Removes direct interconnects from the OpenFPGA netlist
        """
        direct_interc = next(self._top_module.get_definitions("direct_*"), None)
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
        """
        This method creates the group of ``grid_io`` and neighbouring ``connection_box``
        whichcna be merge.

        Variable ``cb_list``, ``grid_io_list`` first creates the list of instances on
        the periphery of the FPGA, starting from the left bottom corner and going clockwise

        ``merge_list`` is a dictionary which creates the group of instances for
        different unique pairs of the IO and CB blocks
        """
        WIDTH = self.fpga_size[0]
        HEIGHT = self.fpga_size[1]
        label = (
            ["cby*"] * HEIGHT + ["cbx*"] * WIDTH + ["cby*"] * HEIGHT + ["cbx*"] * WIDTH
        )
        x_pts = (
            [0] * HEIGHT
            + list(range(1, WIDTH + 1))
            + [WIDTH] * HEIGHT
            + list(range(WIDTH, 0, -1))
        )
        y_pts = (
            list(range(1, HEIGHT))
            + [HEIGHT] * (WIDTH + 1)
            + list(range(HEIGHT, 0, -1))
            + [0] * WIDTH
        )
        cb_list = ["%s_%d__%d_" % (each) for each in zip(label, x_pts, y_pts)]

        label = (
            ["grid*left*"] * HEIGHT
            + ["grid*top*"] * WIDTH
            + ["grid*right*"] * HEIGHT
            + ["grid*bottom*"] * WIDTH
        )
        x_pts = (
            [0] * HEIGHT
            + list(range(1, WIDTH + 1))
            + [WIDTH + 1] * HEIGHT
            + list(range(WIDTH, 0, -1))
        )
        y_pts = (
            list(range(1, HEIGHT + 1))
            + [HEIGHT + 1] * (WIDTH)
            + list(range(HEIGHT, 0, -1))
            + [0] * WIDTH
        )
        grid_io_list = ["%s_%d__%d_" % (each) for each in zip(label, x_pts, y_pts)]

        merge_list = {}
        for cb, io in zip(cb_list, grid_io_list):
            try:
                io = next(self._netlist.get_instances(io))
                cb = next(self._netlist.get_instances(cb))
            except StopIteration:
                logger.warning("Missing instance %s %s", cb, io)
                continue
            lbl = f"{io.reference.name}_{cb.reference.name}"
            merge_list[lbl] = merge_list.get(lbl, [])
            merge_list[lbl] += [((io, cb), cb.name + "_new")]

        new_defs = []
        for _, instance_list in merge_list.items():
            new_module_name = instance_list[0][0][1].reference.name + "_new"
            mainDef, instance_list = self.top_module.merge_multiple_instance(
                instance_list, new_definition_name=new_module_name
            )
            new_defs.append(next(self.library.get_definitions(new_module_name)))
            new_defs[-1].OptPins()
            next(self.library.get_definitions(mainDef.name[:-4])).name += "_old"
            mainDef.name = mainDef.name[:-4]
            for inst in instance_list:
                inst.name = inst.name[:-4]
        return new_defs

    def remove_config_chain(self, name="ccff_"):
        """Remove configuration chain from design"""
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
        """
        Removes undriven/floating nets from the top level

        the net name with undriven keyword in the name is considered as floating nets
        """
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

    def _convert_to_bus(
        self,
        module: sdn.Definition,
        in_patt: str,
        out_patt: str,
        sort_pins: (Callable) = None,
        is_downto=True,
    ):
        """
        Convertes matching `in_patt` pins to bus with `out_patt` name
        """
        new_port, new_cable = None, None

        def get_pins(x):
            return fnmatch(x.name, in_patt)

        ports = list(module.get_ports(filter=get_pins))
        if sort_pins:
            ports = sorted(ports, keys=sort_pins)
        if ports:
            new_port, new_cable = module.combine_ports(out_patt, ports, is_downto)
        return new_port, new_cable

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
                self._convert_to_bus(
                    grid_io,
                    f"{side}*_pin_{inpad}_*",
                    f"io_{side}_in",
                    sort_pins=sort_pins,
                )
                self._convert_to_bus(
                    grid_io,
                    f"{side}*_pin_{outpad}_*",
                    f"io_{side}_out",
                    sort_pins=sort_pins,
                )

    def create_grid_clb_bus(self, pins=None, grid_module="grid_clb"):
        """
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

        """

        sides = ("left", "top", "right", "bottom")

        pins = (pins or []) + [("I", "in"), ("O", "out")]
        #  =========  grid_clb renaming =========
        for grid_clb in self._library.get_definitions(f"{grid_module}*"):
            for side in sides:
                #  Input pins
                for pin in pins:
                    self._convert_to_bus(
                        grid_clb, f"{side}*_pin_{pin[0]}_*", f"grid_{side}_{pin[1]}"
                    )

    def create_sb_bus(self, pins=None):
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
        pins = (pins or []) + [("O", "in"), ("inpad", "inpad")]
        sides = ("top", "right", "bottom", "left")
        for sb in self._library.get_definitions("sb_*"):
            for s1 in sides:
                for s2 in sides:
                    # input pins from each corner
                    for pin in pins:
                        self._convert_to_bus(
                            sb,
                            f"{s1}_{s2}_grid_*_pin_{pin[0]}_*",
                            f"grid_{s1}_{s2[0]}_{pin[1]}",
                        )

    def create_cb_bus(self, pins=None):
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
        pins = (pins or []) + [("I", "out"), ("outpad", "outpad")]
        sides = ("top", "right", "bottom", "left")
        for cbx in self._library.get_definitions("cb?_*"):
            for indx, s1 in enumerate(sides):
                # Input pins
                for pin in pins:
                    self._convert_to_bus(
                        cbx, f"*{s1}_grid_*__pin_{pin[0]}_*", f"grid_{s1}_{pin[1]}"
                    )

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
            through_inst = next(self._top_module.get_instances(through_inst_name))
            ref_name = through_inst.reference.name
            ft_map[ref_name] = ft_map.get(ref_name, [])
            ft_map[ref_name].append((cable, (through_inst,)))

        for ref_name, inst_map in ft_map.items():
            cables, new_ports = self._top_module.create_ft_multiple(inst_map)
            side1, side2, oppo_side = {
                "left": ("top", "bottom", "right"),
                "right": ("top", "bottom", "left"),
                "top": ("left", "right", "bottom"),
                "bottom": ("left", "right", "top"),
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
        """
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
        """
        clb = next(self._library.get_definitions("grid_clb"))

        self._create_grid_out_feedthrough(clb, "left")
        self._create_grid_out_feedthrough(clb, "right")
        self._create_grid_out_feedthrough(clb, "top")
        self._create_grid_out_feedthrough(clb, "bottom")

    def clear_written_modules(self):
        while self.written_modules:
            self.written_modules.pop()
        while self.write_modules_paths:
            self.write_modules_paths.pop()

    def write_include_file(self, filename, relative_from=None):
        relative_from = relative_from or os.environ.get("VERILOG_PROJ_DIR", "")
        with open(filename, "w", encoding="UTF-8") as fp:
            for filepath in self.write_modules_paths:
                filepath = Path(filepath).relative_to(relative_from)
                fp.write(f'`include "{filepath}"' + "\n")

    def save_netlist(
        self,
        pattern="*",
        location=".",
        sort_all=False,
        skip_constraints=True,
        sort_cables=False,
        sort_instances=False,
        sort_ports=False,
        write_blackbox=True,
    ):
        """
        Save verilog files
        """
        for definition in sorted(
            list(self._library.get_definitions(pattern)), key=lambda x: x.name
        ):
            if definition.name in self.written_modules:
                continue
            # if sort_ports:
            #     definition._ports.sort(
            #         key=lambda x: str(x._direction) + x.name)
            # if sort_cables:
            #     definition._cables.sort(key=lambda x: x.name)
            # if sort_instances:
            #     definition._children.sort(key=lambda x: x.name)
            logger.debug("Writing %s", definition.name)
            Path(location).mkdir(parents=True, exist_ok=True)
            filepath = os.path.join(location, f"{definition.name}.v")
            sdn.compose(
                self._netlist,
                filename=filepath,
                sort_all=sort_all,
                skip_constraints=skip_constraints,
                definition_list=[definition.name],
                write_blackbox=write_blackbox,
            )
            self.write_modules_paths.append(filepath)
            self.written_modules.append(definition.name)
        return self.written_modules

    def load_grid(self, pickle_path) -> FPGAGridGen:
        if isinstance(pickle_path, FPGAGridGen):
            self.fpga_grid = pickle_path
        else:
            with open(pickle_path, "rb") as fp:
                self.fpga_grid: FPGAGridGen = pickle.load(fp)

    def get_top_instance(self, x, y):
        """
        This method generates the grid instance information given the
        cordinate points
        """
        return self.fpga_grid.get_top_instance(x, y)

    def fix_grid_pin_names(
        self, regex=r".*__pin_(.*)_0_", module="grid_*", name_map=None
    ):
        """
        This method is used to fix the pin names on the grid modules

        Args:
            regex(str): Regex string used to extract the name of the port
        """
        name_map = name_map or (lambda x: x)
        eachmodule: sdn.module
        for eachmodule in self.top_module.get_definitions(module):
            logger.debug("Fixing pins on %s module", eachmodule.name)
            top_port: sdn.Port
            for top_port in eachmodule.get_ports("*"):
                pin_name = re.match(regex, top_port.name)
                if pin_name:
                    pin_name = name_map(pin_name.groups()[0])
                    logger.debug("%s =>> %s", top_port.name, pin_name)
                    top_port.change_name(pin_name)

    def annotate_area_information(self, filename, skipline=0):
        """
        This method annotated the area infomration on each
        definition of the top level module
        """
        with open(filename, "r", encoding="UTF-8") as fp:
            for line in fp.readlines()[skipline:]:
                if not (line):
                    continue
                line = line.replace(",", " ")
                module = line.split()[0]
                area = line.split()[1] or 0
                area_grid = int(
                    float(area) * (self.GLOBAL_SCALE**2) / (self.SC_HEIGHT * self.CPP)
                )
                try:
                    ref = next(self.top_module.get_definitions(module))
                    logger.debug(
                        "%s [%s] area is set to %d %f",
                        ref.name,
                        module,
                        int(area_grid),
                        float(area),
                    )
                    ref.data[PROP]["AREA"] = int(area_grid)
                    ref.data[PROP]["AREA_UM"] = float(area) * (self.GLOBAL_SCALE**2)
                except StopIteration:
                    logger.warning(
                        "Area annotation: %s not found in the netlist ", module
                    )

    def annotate_shaping_information(self, filename, skipline=2):
        """
        This method annotated the area infomration on each
        definition of the top level module
        """
        with open(filename, "r", encoding="UTF-8") as fp:
            for line in fp.readlines()[skipline:]:
                if not (line):
                    continue
                line = line.replace(",", " ")
                INSTANCE, MODULE, LOC_X, LOC_Y = line.split()[:4]
                points = line.split()[6:]
                try:
                    if self.top_module.name == INSTANCE:
                        inst = self.netlist.top_instance
                    else:
                        inst = next(self.top_module.get_instances(INSTANCE))

                        inst.data[PROP]["LOC_X"] = int(float(LOC_X) * self.GLOBAL_SCALE)
                        inst.data[PROP]["LOC_Y"] = int(float(LOC_Y) * self.GLOBAL_SCALE)

                    inst.reference[PROP]["WIDTH"] = int(float(points[4])*self.GLOBAL_SCALE)
                    inst.reference[PROP]["HEIGHT"] = int(float(points[5])*self.GLOBAL_SCALE)

                except StopIteration:
                    logger.warning(
                        "shaping annotation: %s[%s] not found in the netlist ",
                        INSTANCE,
                        MODULE,
                    )

    # print the hierarchy of a netlist
    def hierarchy(
        self, current_instance, indentation="", level=0, max_depth=10, output=""
    ):
        if level > max_depth:
            return output
        reference = (
            current_instance.reference
            if isinstance(current_instance, sdn.Instance)
            else current_instance
        )
        inst_name = (
            current_instance.name if isinstance(current_instance, sdn.Instance) else ""
        )
        if not ("SDN_VERILOG" in reference.name):
            line = f"{indentation} {level} {inst_name}" + f"[{reference.name}]\n"
            output += line
            print(line, end="")
        for child in reference.children:
            output = self.hierarchy(
                child,
                indentation + "     ",
                level + 1,
                max_depth=max_depth,
                output=output,
            )
        return output

    def update_module_label(self, get_label=None):
        """
        Adde area information to label
        """

        def add_area_detail(ref):
            util = ref.utilization
            ref.data[PROP]["UTIL"] = util
            return f"[{util:.2%}]"

        get_label = get_label or add_area_detail
        for inst in self.top_module.get_instances("*"):
            ref = inst.reference
            ref.data[PROP]["LABEL"] = get_label(ref)
            # if util > 0.9:
            #     ADDITIONAL_STYLES += f".{ref.name}" + \
            #         "{fill:#b22222 !important;}\n"

    def get_overutils_styles(self, target=0.95, color="#D60B00"):
        """
        Analyzes utilisation of each module and returns CSS string to highlight
        in the SVG
        """
        additional_styles = ""
        for eachmdoule in self.top_module.get_definitions():
            if eachmdoule.utilization > target:
                additional_styles += (
                    f"\n.{eachmdoule.name}" + f"{{ fill: {color} !important }} \n"
                )
        return additional_styles
