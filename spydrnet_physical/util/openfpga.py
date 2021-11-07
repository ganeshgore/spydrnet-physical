"""
This class is created for OpenFPGA related netlist transformations
"""
import logging
from collections import OrderedDict
from fnmatch import fnmatch
from os import path
from pathlib import Path
import re

import spydrnet as sdn

logger = logging.getLogger('spydrnet_logs')


class OpenFPGA_Tile01(object):

    def __init__(self, grid, netlist, library="work", top_module="fpga_top"):
        '''
        Init class

        args:
            netlist (sdn.netlist): Pass OpenFPGA core netlist
        '''
        self.fpga_size = grid
        self._netlist = netlist
        self._work = next(netlist.get_libraries(library))
        self._task_directory = netlist
        self._top_module = next(self._work.get_definitions(top_module))
        self._tile_name_patter = "tile_%d_%d_"
        netlist.top_instance = self._top_module

    @property
    def work(self):
        return self._work

    @property
    def top_module(self):
        return self._top_module

    def add_placement(self):
        pass

    def create_connection(self):
        pass

    def remove_undriven_nets(self):
        removed_cables = []
        for cable in self._top_module.get_cables("*undriven*"):
            removed_cables.append(cable.name)
            self._top_module.remove_cable(cable)
        return removed_cables

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

    def design_top_stat(self):
        '''
        Get statistics of the top module
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

    def save_netlist(self, patten="*",  location="."):
        '''
        Save verilog files
        '''
        for definition in self._work.get_definitions(patten):
            logger.info("Writing %s", definition.name)
            Path(location).mkdir(parents=True, exist_ok=True)
            sdn.compose(self._netlist,
                        filename=path.join(location, f"{definition.name}.v"),
                        skip_constrains=True,
                        definition_list=[definition.name],
                        write_blackbox=True)

    def create_grid_io_bus(self):
        sides = [("left", "top", "bottom"),
                 ("top", "left", "right"),
                 ("right", "top", "bottom"),
                 ("bottom", "left", "right")]

        #  =========  grid_io  =========
        for grid_io in self._work.get_definitions("grid_io*"):
            for s1, s2_1, s2_2 in sides:
                # Plan upper pins
                ports = list(grid_io.get_ports(
                    filter=lambda x: fnmatch(
                        x.name, f"{s1}*_pin_inpad_*upper")
                ))
                if ports:
                    ports = sorted(ports, key=lambda x: x.name)
                    grid_io.combine_ports(f"io_{s2_1}_{s1[0]}_in", ports)

                # Plan lower pins
                ports = list(grid_io.get_ports(
                    filter=lambda x: fnmatch(
                        x.name, f"{s1}*_pin_inpad_*lower")
                ))
                if ports:
                    ports = sorted(ports, key=lambda x: x.name)
                    grid_io.combine_ports(f"io_{s2_2}_{s1[0]}_in", ports)

                # Plan lower pins (Remaining in case of non duplicatded pins appear)
                ports = list(grid_io.get_ports(
                    filter=lambda x: fnmatch(x.name, f"{s1}*_pin_inpad_*")))
                if ports:
                    ports = sorted(ports, key=lambda x: x.name)
                    grid_io.combine_ports(f"io_{s1}_in", ports)

                # Plan input pins
                ports = list(grid_io.get_ports(
                    filter=lambda x: fnmatch(x.name, f"{s1}*_pin_outpad_*")))
                if ports:
                    ports = sorted(ports, key=lambda x: x.name)
                    grid_io.combine_ports(f"io_{s1}_out", ports)

    def create_grid_clb_bus(self):
        '''
        Convert CLB wires to Bus
        '''
        sides = [("left", "left_1", "left_2"),
                 ("top", "left", "right"),
                 ("right", "top", "bottom"),
                 ("bottom", "bottom_2", "bottom_1")]
        grid_clb = next(self._work.get_definitions("grid_clb*"))

        for port in grid_clb.get_ports("*pin_clk*"):
            grid_clb.remove_port(port)
        #  =========  grid_clb  =========
        for s1, s2_1, s2_2 in sides:
            # Plan upper pins
            ports = list(grid_clb.get_ports(
                filter=lambda x: fnmatch(x.name, f"{s1}*_pin_O_*upper")))
            if ports:
                ports = sorted(ports, key=lambda x: x.name)
                grid_clb.combine_ports(f"clb_{s2_1}_{s1[0]}_out", ports)

            # Plan lower pins
            ports = list(grid_clb.get_ports(
                filter=lambda x: fnmatch(x.name, f"{s1}*_pin_O_*lower")))
            if ports:
                ports = sorted(ports, key=lambda x: x.name)
                grid_clb.combine_ports(f"clb_{s2_2}_{s1[0]}_out", ports)

            # Plan lower pins (Remaining in case of non duplicatded pins appear)
            ports = list(grid_clb.get_ports(
                filter=lambda x: fnmatch(x.name, f"{s1}*_pin_O_*_")))
            if ports:
                ports = sorted(ports, key=lambda x: x.name)
                grid_clb.combine_ports(f"clb_{s1}_out", ports)

            # Plan input pins
            ports = list(grid_clb.get_ports(
                filter=lambda x: fnmatch(x.name, f"{s1}*_pin_I*")))
            if ports:
                ports = sorted(ports, key=lambda x: x.name)
                grid_clb.combine_ports(f"clb_{s1}_in", ports)

    def create_sb_bus(self):
        sides = ["top", "right", "bottom", "left"]
        for sb in self._work.get_definitions("sb_*"):
            for s1 in sides:
                for s2 in sides:
                    ports = list(sb.get_ports(
                        filter=lambda x: fnmatch(x.name, f"*{s1}_{s2}_grid_*_pin_O_*")))
                    if ports:
                        ports = sorted(ports, key=lambda x: x.name)
                        sb.combine_ports(f"sb_{s1}_{s2[0]}_in", ports)
                    ports = list(sb.get_ports(
                        filter=lambda x: fnmatch(x.name, f"*{s1}_{s2}_grid_*__pin_inpad_*")))
                    if ports:
                        ports = sorted(ports, key=lambda x: x.name)
                        sb.combine_ports(f"sb_{s1}_{s2[0]}_inpad", ports)

    def create_cb_bus(self):
        sides = ["top", "right", "bottom", "left"]
        for cbx in self._work.get_definitions("cbx_*"):
            for indx, s1 in enumerate(sides):
                ports = list(cbx.get_ports(
                    filter=lambda x: fnmatch(x.name, f"*{s1}_grid_*__pin_I_*")))
                if ports:
                    ports = sorted(ports, key=lambda x: x.name)
                    cbx.combine_ports(f"cb_{s1}_in", ports)

                ports = list(cbx.get_ports(
                    filter=lambda x: fnmatch(x.name, f"*{s1}_grid_*__pin_outpad_*")))
                if ports:
                    ports = sorted(ports, key=lambda x: x.name)
                    cbx.combine_ports(f"cb_{s1}_outpad", ports)

        for cby in self._work.get_definitions("cby_*"):
            for indx, s1 in enumerate(sides):
                ports = list(cby.get_ports(
                    filter=lambda x: fnmatch(x.name, f"*{s1}_grid_*__pin_I_*")))
                if ports:
                    ports = sorted(ports, key=lambda x: x.name)
                    cby.combine_ports(f"cb_{s1}_in", ports)

                ports = list(cby.get_ports(
                    filter=lambda x: fnmatch(x.name, f"*{s1}_grid_*__pin_outpad_*")))
                if ports:
                    ports = sorted(ports, key=lambda x: x.name)
                    cby.combine_ports(f"cb_{s1}_outpad", ports)

    def create_grid_clb_feedthroughs(self):
        '''
        Create feedthroughs for ``grid_clb``

        '''
        # TODO: Need more detal documentation
        left_ft0, left_ft1, bottom_ft0, bottom_ft1 = [], [], [], []
        clb = next(self._work.get_definitions("grid_clb"))

        for each in clb.references:
            cable = each.get_port_cables("clb_left_out")[0]
            x, y = map(int, re.match(
                r"grid_clb_(\w+)__(\w+)_", each.name).groups())
            through_inst = next(
                self._top_module.get_instances(f"cby_{x-1}__{y}_"))
            print(each.name, cable.name, through_inst.name)
            if through_inst.reference.name == "cby_0__1_":
                left_ft0.append((cable, (through_inst,)))
            elif through_inst.reference.name == "cby_1__1_":
                left_ft1.append((cable, (through_inst,)))
            else:
                print("Unexpected instance to merge")

            cable = each.get_port_cables("clb_bottom_out")[0]
            through_inst = next(
                self._top_module.get_instances(f"cbx_{x}__{y-1}_"))
            print(each.name, cable.name, through_inst.name)
            if through_inst.reference.name == "cbx_1__0_":
                bottom_ft0.append((cable, (through_inst,)))
            elif through_inst.reference.name == "cbx_1__1_":
                bottom_ft1.append((cable, (through_inst,)))
            else:
                print("Unexpected instance to merge")
            print("===================")

        _, new_ports = self._top_module.create_ft_multiple(left_ft0)
        new_ports[0][0].change_name("cb_right_grid_in")
        new_ports[0][1].change_name("cb_bottom_r_out")
        _, new_ports = self._top_module.create_ft_multiple(left_ft1)
        new_ports[0][0].change_name("cb_right_grid_in")
        new_ports[0][1].change_name("cb_bottom_r_out")
        _, new_ports = self._top_module.create_ft_multiple(bottom_ft0)
        new_ports[0][0].change_name("cb_top_grid_in")
        new_ports[0][1].change_name("cb_left_r_out")
        _, new_ports = self._top_module.create_ft_multiple(bottom_ft1)
        new_ports[0][0].change_name("cb_top_grid_in")
        new_ports[0][1].change_name("cb_left_r_out")

        next(clb.get_ports("clb_top_out")).change_name("clb_left_t_out")
        next(clb.get_ports("clb_right_out")).change_name("clb_bottom_r_out")

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
                clb = next(self._work.get_instances(f"grid_clb_{x}__{y}_"))
                cbx = next(self._work.get_instances(f"cbx_{x}__{y}_"))
                cby = next(self._work.get_instances(f"cby_{x}__{y}_"))
                sb = next(self._work.get_instances(f"sb_{x}__{y}_"))
                merge_module_list.append(((clb, cbx, cby, sb),
                                          f"tile_{x}__{y}_"))

        self._top_module.merge_multiple_instance(merge_module_list,
                                                 new_definition_name="tile")
        next(self._work.get_definitions("tile")).OptPins()

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
            clb = next(self._work.get_instances(f"grid_clb_1__{i}_"))
            cby0 = next(self._work.get_instances(f"cby_0__{i}_"))
            cby1 = next(self._work.get_instances(f"cby_1__{i}_"))
            cbx1 = next(self._work.get_instances(f"cbx_1__{i}_"))
            sb0 = next(self._work.get_instances(f"sb_0__{i}_"))
            sb1 = next(self._work.get_instances(f"sb_1__{i}_"))
            grid_io = next(self._work.get_instances(f"grid_io_left_0__{i}_"))
            instance_list.append(((clb, cby0, cby1, cbx1, sb0, sb1, grid_io),
                                  f"tile_1__{i}_"))

        self._top_module.merge_multiple_instance(instance_list,
                                                 new_definition_name="left_tile")
        next(self._work.get_definitions("left_tile")).OptPins()

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
            clb = next(self._work.get_instances(
                f"grid_clb_{self.fpga_size[0]}__{i}_"))
            cbx1 = next(self._work.get_instances(
                f"cbx_{self.fpga_size[0]}__{i}_"))
            cby0 = next(self._work.get_instances(
                f"cby_{self.fpga_size[0]}__{i}_"))
            sb0 = next(self._work.get_instances(
                f"sb_{self.fpga_size[0]}__{i}_"))
            grid_io = next(self._work.get_instances(
                f"grid_io_right_{self.fpga_size[0]+1}__{i}_"))
            instance_list.append(((clb, cbx1, cby0, sb0, grid_io),
                                  f"tile_{self.fpga_size[0]}__{i}_"))

        self._top_module.merge_multiple_instance(instance_list,
                                                 new_definition_name=f"right_tile")
        next(self._work.get_definitions("right_tile")).OptPins()

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
            clb = next(self._work.get_instances(
                f"grid_clb_{i}__{self.fpga_size[1]}_"))
            cbx = next(self._work.get_instances(
                f"cbx_{i}__{self.fpga_size[1]}_"))
            cby = next(self._work.get_instances(
                f"cby_{i}__{self.fpga_size[1]}_"))
            sb = next(self._work.get_instances(
                f"sb_{i}__{self.fpga_size[1]}_"))
            grid_io = next(self._work.get_instances(
                f"grid_io_top_{i}__{self.fpga_size[1]+1}_"))
            merge_module_list.append(((clb, cbx, cby, sb, grid_io),
                                      f"tile_{i}__{self.fpga_size[1]}_"))

        self.top_module.merge_multiple_instance(merge_module_list,
                                                new_definition_name="top_tile")
        next(self._work.get_definitions("top_tile")).OptPins()

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
            clb = next(self._work.get_instances(f"grid_clb_{i}__1_"))
            cbx0 = next(self._work.get_instances(f"cbx_{i}__0_"))
            cbx1 = next(self._work.get_instances(f"cbx_{i}__1_"))
            cby1 = next(self._work.get_instances(f"cby_{i}__1_"))
            sb0 = next(self._work.get_instances(f"sb_{i}__0_"))
            sb1 = next(self._work.get_instances(f"sb_{i}__1_"))
            grid_io = next(self._work.get_instances(f"grid_io_bottom_{i}__0_"))
            instance_list.append(((clb, cbx0, cbx1, cby1, sb0, sb1, grid_io),
                                  f"tile_{i}__1_"))

        self._top_module.merge_multiple_instance(instance_list,
                                                 new_definition_name=f"bottom_tile")
        next(self._work.get_definitions("bottom_tile")).OptPins()

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
        clb = next(self.work.get_instances(
            f"grid_clb_1__{self.fpga_size[1]}_"))
        cbx0 = next(self.work.get_instances(f"cbx_1__{self.fpga_size[1]}_"))
        cby0 = next(self.work.get_instances(f"cby_0__{self.fpga_size[1]}_"))
        cby1 = next(self.work.get_instances(f"cby_1__{self.fpga_size[1]}_"))
        sb0 = next(self.work.get_instances(f"sb_0__{self.fpga_size[1]}_"))
        sb1 = next(self.work.get_instances(f"sb_1__{self.fpga_size[1]}_"))
        grid_io_0 = next(self.work.get_instances(
            f"grid_io_top_1__{self.fpga_size[1]+1}_"))
        grid_io_1 = next(self.work.get_instances(
            f"grid_io_left_0__{self.fpga_size[1]}_"))
        merge_module_list.append(((clb, cbx0, cby0, cby1, sb0, sb1, grid_io_0, grid_io_1),
                                  f"tile_1__{self.fpga_size[1]}_"))
        self.top_module.merge_multiple_instance(merge_module_list,
                                                new_definition_name=f"top_left_tile")
        next(self.work.get_definitions("top_left_tile")).OptPins()

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
        clb = next(self._work.get_instances(
            f"grid_clb_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        cbx0 = next(self._work.get_instances(
            f"cbx_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        cby0 = next(self._work.get_instances(
            f"cby_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        sb0 = next(self._work.get_instances(
            f"sb_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        grid_io_0 = next(self._work.get_instances(
            f"grid_io_right_{self.fpga_size[0]+1}__{self.fpga_size[1]}_"))
        grid_io_1 = next(self._work.get_instances(
            f"grid_io_top_{self.fpga_size[0]}__{self.fpga_size[1]+1}_"))
        merge_module_list.append(((clb, cbx0, cby0, sb0, grid_io_0, grid_io_1),
                                  f"tile_{self.fpga_size[0]}__{self.fpga_size[1]}_"))
        self._top_module.merge_multiple_instance(merge_module_list,
                                                 new_definition_name=f"top_right_tile")
        next(self._work.get_definitions("top_right_tile")).OptPins()

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
        clb = next(self._work.get_instances("grid_clb_1__1_"))
        cbx0 = next(self._work.get_instances("cbx_1__0_"))
        cbx1 = next(self._work.get_instances("cbx_1__1_"))
        cby0 = next(self._work.get_instances("cby_0__1_"))
        cby1 = next(self._work.get_instances("cby_1__1_"))
        sb0 = next(self._work.get_instances("sb_0__0_"))
        sb1 = next(self._work.get_instances("sb_0__1_"))
        sb2 = next(self._work.get_instances("sb_1__0_"))
        sb3 = next(self._work.get_instances("sb_1__1_"))
        grid_io_0 = next(self._work.get_instances("grid_io_left_0__1_"))
        grid_io_1 = next(self._work.get_instances("grid_io_bottom_1__0_"))
        merge_module_list.append(((clb, cbx0, cbx1, cby0, cby1, sb0, sb1,
                                   sb2, sb3, grid_io_0, grid_io_1),
                                  "tile_1__1_"))
        self._top_module.merge_multiple_instance(merge_module_list,
                                                 new_definition_name=f"bottom_left_tile")

        next(self._work.get_definitions("bottom_left_tile")).OptPins()

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
        clb = next(self._work.get_instances(
            f"grid_clb_{self.fpga_size[0]}__1_"))
        cbx0 = next(self._work.get_instances(f"cbx_{self.fpga_size[0]}__0_"))
        cbx1 = next(self._work.get_instances(f"cbx_{self.fpga_size[0]}__1_"))
        cby0 = next(self._work.get_instances(f"cby_{self.fpga_size[0]}__1_"))
        sb0 = next(self._work.get_instances(f"sb_{self.fpga_size[0]}__0_"))
        sb1 = next(self._work.get_instances(f"sb_{self.fpga_size[0]}__1_"))
        grid_io_0 = next(self._work.get_instances(
            f"grid_io_bottom_{self.fpga_size[0]}__0_"))
        grid_io_1 = next(self._work.get_instances(
            f"grid_io_right_{self.fpga_size[0]+1}__1_"))
        merge_module_list.append(((clb, cbx0, cbx1, cby0, sb0, sb1, grid_io_0, grid_io_1),
                                  f"tile_{self.fpga_size[0]}__1_"))
        self._top_module.merge_multiple_instance(merge_module_list,
                                                 new_definition_name="bottom_right_tile")
        next(self._work.get_definitions("bottom_right_tile")).OptPins()
