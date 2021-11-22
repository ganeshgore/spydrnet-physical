import logging
import xml.etree.ElementTree as ET

from svgwrite import Drawing, shapes
from svgwrite.container import Group
from svgwrite.text import Text

logger = logging.getLogger('spydrnet_logs')


class RoutingRender:
    def __init__(self, name, gsb_xml) -> None:
        self.name = name
        self.scale = 40
        self.spacing = self.scale*2
        self.gsb_xml = gsb_xml
        self.root = ET.parse(self.gsb_xml).getroot()
        self.extract_info()
        # Variables for SVG rendering
        self.dwg = Drawing()
        self.dwgbg = self.dwg.add(Group(id="bg"))
        self.region = self.dwg.add(Group(id="region", transform="scale(1,-1)"))
        self.core = self.dwg.add(Group(id="mainframe"))
        self.dwgShapes = self.core.add(Group(id="mainShapes",
                                             transform="scale(1,-1)"))
        self.switches = self.core.add(Group(id="switches",
                                            transform="scale(1,-1)"))
        self.dwgText = self.core.add(Group(id="mainText",
                                           transform="scale(1,-1)"))
        self.marker_red = self._create_arrowhead('red')
        self.marker_green = self._create_arrowhead('green')
        self.marker_blue = self._create_arrowhead('blue')
        self.marker_terminate = self._create_termination('blue')

    def update_dimensions(self, scale, spacing):
        """
        Updates scale and spacing dimensions
        """
        self.scale = int(scale) or self.scale
        self.spacing = int(spacing) or self.spacing

    @staticmethod
    def _get_max_index(ele):
        return max([int(i.attrib["index"])for i in ele] + [-1])+1

    @staticmethod
    def set_bit(x, indx):
        x[int(indx)] = 'x'

    @staticmethod
    def set_vbit(x, indx):
        x[int(indx)] = 'l' if int(indx) % 2 else "r"

    @staticmethod
    def set_hbit(x, indx):
        x[int(indx)] = 't' if int(indx) % 2 else "b"

    def report_ipins(self, side):
        format_str = "{:^6s} {:^6s} {:^45s} {:^45s} "
        print("= = "*25)
        print(format_str.format("index", "Mux", "ChanX", "Chany"))
        print("= = "*25)
        items = {"left": self.ipin_l,
                 "right": self.ipin_r,
                 "top": self.ipin_t,
                 "bottom": self.ipin_b}[side]
        for chan in items:
            ChanX = ['_']*self.chanx_len
            _ = [self.set_vbit(ChanX, e.attrib['index'])
                 for e in chan.findall('./driver_node[@type="CHANX"]')]
            ChanY = ['_']*self.chany_len
            _ = [self.set_hbit(ChanY, e.attrib['index'])
                 for e in chan.findall('./driver_node[@type="CHANY"]')]
            print(format_str.format(
                chan.attrib["index"],
                chan.attrib["mux_size"],
                ''.join(ChanX),
                ''.join(ChanY)))

    def report_channel_connection(self, side):
        """
        This print the channel information of given SB in speific direction
        """
        format_str = "{:^6s} {:^6s} {:^45s} {:^45s} {:^10s} {:^10s} {:^10s} {:^10s}"
        print("= = "*40)
        print(format_str.format("index", "Mux", "ChanX", "Chany",
                                "OPIN_L", "OPIN_R", "OPIN_T", "OPIN_B"))
        print("= = "*40)

        items = {"left": self.chanx_l, "right": self.chanx_r,
                 "top": self.chany_t, "bottom": self.chany_b}[side]
        for chan in items:
            ChanX = ['_']*self.chanx_len
            _ = [self.set_vbit(ChanX, e.attrib['index'])
                 for e in chan.findall('./driver_node[@type="CHANX"]')]
            ChanY = ['_']*self.chany_len
            _ = [self.set_hbit(ChanY, e.attrib['index'])
                 for e in chan.findall('./driver_node[@type="CHANY"]')]
            OPIN_L = ['_']*self.opin_l_len
            _ = [self.set_bit(OPIN_L, e.attrib['index'])
                 for e in chan.findall('./driver_node[@type="OPIN"][@side="left"]')]
            OPIN_R = ['_']*self.opin_l_len
            _ = [self.set_bit(OPIN_R, e.attrib['index'])
                 for e in chan.findall('./driver_node[@type="OPIN"][@side="right"]')]
            OPIN_T = ['_']*self.opin_l_len
            _ = [self.set_bit(OPIN_T, e.attrib['index'])
                 for e in chan.findall('./driver_node[@type="OPIN"][@side="top"]')]
            OPIN_B = ['_']*self.opin_l_len
            _ = [self.set_bit(OPIN_B, e.attrib['index'])
                 for e in chan.findall('./driver_node[@type="OPIN"][@side="bottom"]')]
            print(format_str.format(
                chan.attrib["index"],
                chan.attrib["mux_size"],
                ''.join(ChanX),
                ''.join(ChanY),
                ''.join(OPIN_L),
                ''.join(OPIN_R),
                ''.join(OPIN_T),
                ''.join(OPIN_B)))

    def extract_info(self):
        """
        Extracts insformation from provided general switch box file
        """
        root = self.root
        self.chanx_l = root.findall("CHANX[@side='left']")
        self.chanx_l_len = len(self.chanx_l)
        self.chanx_r = root.findall("CHANX[@side='right']")
        self.chanx_r_len = len(self.chanx_r)
        self.chanx = sorted(root.findall("CHANX"),
                            key=lambda x: int(x.attrib['index']))
        self.chanx_len = self.chanx_l_len + self.chanx_r_len

        self.chany_t = root.findall("CHANY[@side='top']")
        self.chany_t_len = len(self.chany_t)
        self.chany_b = root.findall("CHANY[@side='bottom']")
        self.chany_b_len = len(self.chany_b)
        self.chany = sorted(root.findall("CHANY"),
                            key=lambda x: int(x.attrib['index']))
        self.chany_len = self.chany_t_len + self.chany_b_len

        self.ipin_l = root.findall("IPIN[@side='left']")
        self.ipin_l_len = self._get_max_index(self.ipin_l)
        self.ipin_r = root.findall("IPIN[@side='right']")
        self.ipin_r_len = self._get_max_index(self.ipin_r)
        self.ipin_t = root.findall("IPIN[@side='top']")
        self.ipin_t_len = self._get_max_index(self.ipin_t)
        self.ipin_b = root.findall("IPIN[@side='bottom']")
        self.ipin_b_len = self._get_max_index(self.ipin_b)

        # Collect Feedthrough
        self.ft_left = [chan for chan in self.chanx_l if len(
            chan.getchildren()) == 1]
        self.ft_left_len = len(set((e.attrib["index"] for e in self.ft_left)))
        self.ft_right = [chan for chan in self.chanx_r if len(
            chan.getchildren()) == 1]
        self.ft_right_len = len(
            set((e.attrib["index"] for e in self.ft_right)))
        self.ft_top = [chan for chan in self.chany_t if len(
            chan.getchildren()) == 1]
        self.ft_top_len = len(set((e.attrib["index"] for e in self.ft_top)))
        self.ft_bottom = [chan for chan in self.chany_b if len(
            chan.getchildren()) == 1]
        self.ft_bottom_len = len(
            set((e.attrib["index"] for e in self.ft_bottom)))

        # Collect Terminating connections
        self.term_left = [chan for chan in self.chanx_l if len(
            chan.getchildren()) > 1]
        self.term_left_len = len(
            set((e.attrib["index"] for e in self.term_left)))
        self.term_right = [chan for chan in self.chanx_r if len(
            chan.getchildren()) > 1]
        self.term_right_len = len(
            set((e.attrib["index"] for e in self.term_right)))
        self.term_top = [chan for chan in self.chany_t if len(
            chan.getchildren()) > 1]
        self.term_top_len = len(
            set((e.attrib["index"] for e in self.term_top)))
        self.term_bottom = [chan for chan in self.chany_b if len(
            chan.getchildren()) > 1]
        self.term_bottom_len = len(
            set((e.attrib["index"] for e in self.term_bottom)))

        # Left side OPins
        self.opin_l = root.findall(
            "*/driver_node[@type='OPIN'][@side='left']")
        self.opin_l_len = max([int(i.attrib["index"])
                               for i in self.opin_l] + [-1])+1
        self.opin_l_t = [
            e for e in self.opin_l if e.attrib["grid_side"] == "top"]
        self.opin_l_t_len = self._get_max_index(self.opin_l_t)
        self.opin_l_b = [
            e for e in self.opin_l if e.attrib["grid_side"] == "bottom"]
        self.opin_l_b_len = self._get_max_index(self.opin_l_b)

        # Right side OPins
        self.opin_r = root.findall(
            "*/driver_node[@type='OPIN'][@side='right']")
        self.opin_r_len = max([int(i.attrib["index"])
                               for i in self.opin_r] + [-1])+1
        self.opin_r_t = [
            e for e in self.opin_r if e.attrib["grid_side"] == "top"]
        self.opin_r_t_len = self._get_max_index(self.opin_r_t)
        self.opin_r_b = [
            e for e in self.opin_r if e.attrib["grid_side"] == "bottom"]
        self.opin_r_b_len = self._get_max_index(self.opin_r_b)

        # Top side OPins
        self.opin_t = root.findall("*/driver_node[@type='OPIN'][@side='top']")
        self.opin_t_len = max([int(i.attrib["index"])
                               for i in self.opin_t] + [-1])+1

        self.opin_t_l = [
            e for e in self.opin_t if e.attrib["grid_side"] == "left"]
        self.opin_t_l_len = self._get_max_index(self.opin_t_l)
        self.opin_t_r = [
            e for e in self.opin_t if e.attrib["grid_side"] == "right"]
        self.opin_t_r_len = self._get_max_index(self.opin_t_r)

        # bottom side OPins
        self.opin_b = root.findall(
            "*/driver_node[@type='OPIN'][@side='bottom']")
        self.opin_b_len = max([int(i.attrib["index"])
                               for i in self.opin_b] + [-1])+1
        self.opin_b_l = [
            e for e in self.opin_b if e.attrib["grid_side"] == "left"]
        self.opin_b_l_len = self._get_max_index(self.opin_b_l)
        self.opin_b_r = [
            e for e in self.opin_b if e.attrib["grid_side"] == "right"]
        self.opin_b_r_len = self._get_max_index(self.opin_b_r)

    @ staticmethod
    def print_stat_header():
        """
        Prints header for statistics information

        module
        chanx_l  chanx_r  chany_t  chany_b
        ipin_t   ipin_b   ipin_r   ipin_l
        opin_l   opin_r   opin_t   opin_b
        """
        print("=="*80)
        print("%15s %8s %8s %8s %8s %8s %8s %8s %8s %15s %15s %15s %15s" %
              ('module',
               'chanx_l', 'chanx_r', 'chany_t', 'chany_b',
               'ipin_t', 'ipin_b', 'ipin_r', 'ipin_l',
               'opin_l', 'opin_r', 'opin_t', 'opin_b'))
        print("=="*80)

    def get_stats(self, print_header=False, noprint=False):
        """
        Prints switch box statistics
        """
        if print_header:
            self.print_stat_header()
        msg = ("%15s %8s %8s %8s %8s %8s %8s %8s %8s %15s %15s %15s %15s" %
               (self.name,
                self.chanx_l_len, self.chanx_r_len,
                self.chany_t_len, self.chany_b_len,
                self.ipin_t_len, self.ipin_b_len,
                self.ipin_r_len, self.ipin_l_len,
                f"{self.opin_t_len:3} [{self.opin_t_l_len:3},{self.opin_t_r_len:3}]",
                f"{self.opin_b_len:3} [{self.opin_b_l_len:3},{self.opin_b_r_len:3}]",
                f"{self.opin_r_len:3} [{self.opin_r_t_len:3},{self.opin_r_b_len:3}]",
                f"{self.opin_l_len:3} [{self.opin_l_t_len:3},{self.opin_l_b_len:3}]"))
        if not noprint:
            print(msg)
        return msg

    def add_left_channels(self):
        """
        Creates horizontal channels
        """
        # Channels
        term_indx = 0
        offset = self.y_min_0+self.spacing+self.scale
        for chan, ele in enumerate(self.chanx):
            if chan in [int(e.attrib["index"]) for e in self.chanx_l]:
                # Right to left channels
                if chan in [int(e.attrib["index"]) for e in self.ft_left]:
                    # Passthrough cables
                    self.dwgShapes.add(shapes.Line(start=(self.x_max_4, offset),
                                                   end=(self.x_min_4, offset),
                                                   marker_start=self.marker_red.get_funciri(),
                                                   marker_end=self.marker_red.get_funciri(),
                                                   class_="channel rl_chan"))
                    self.dwgText.add(Text(ele.getchildren()[0].attrib["index"],
                                          transform="scale(1,-1)",
                                          class_="rl_text",
                                          insert=(self.x_max_3, -1*offset)))
                    self.dwgText.add(Text(ele.attrib["index"],
                                          transform="scale(1,-1)",
                                          class_="rl_text",
                                          insert=(self.x_min_3, -1*offset)))
                else:
                    # Terminating cable
                    self.dwgShapes.add(shapes.Line(start=(self.x_max_4, offset),
                                                   end=(self.x_min_2, offset),
                                                   marker_start=self.marker_red.get_funciri(),
                                                   marker_end=self.marker_red.get_funciri(),
                                                   class_="channel rl_chan"))

                    # Add connecting Vertical line
                    x_line = self.x_min_1 - term_indx*self.scale - self.spacing
                    y_line = self.y_min_0 - term_indx*self.scale - self.spacing
                    self.dwgShapes.add(shapes.Line(start=(x_line, self.y_max_0),
                                                   end=(x_line, y_line),
                                                   marker_start=self.marker_red.get_funciri(),
                                                   marker_end=self.marker_terminate.get_funciri(),
                                                   class_="channel rl_chan"))
                    # Add connecting horizontal line
                    self.dwgShapes.add(shapes.Line(start=(self.x_max_0, y_line),
                                                   end=(self.x_min_4, y_line),
                                                   marker_start=self.marker_red.get_funciri(),
                                                   marker_end=self.marker_red.get_funciri(),
                                                   class_="channel rl_chan"))
                    self._add_short_at(x_line, y_line)
                    # Add Text
                    self.dwgText.add(Text(self.term_right[term_indx].attrib["index"],
                                          transform="scale(1,-1)",
                                          class_="rl_text",
                                          insert=(self.x_max_3, -1*offset)))
                    self.dwgText.add(Text(ele.attrib["index"],
                                          transform="scale(1,-1)",
                                          class_="rl_text",
                                          insert=(self.x_min_3, -1*y_line)))

                    # Add Switches
                    print(f"---> {ele.attrib['index']}")
                    for switch in ele.getchildren():
                        sw_type = switch.attrib["type"]
                        side = switch.attrib["side"]
                        index = int(switch.attrib["index"])
                        grid_side = switch.attrib.get("grid_side", "")
                        if sw_type == "CHANX":
                            self._add_switch_at(
                                x_line,
                                ((index+1)*self.scale) + 2*self.spacing)
                        elif sw_type == "CHANY":
                            self._add_switch_at(
                                ((index+1)*self.scale) + 2*self.spacing,
                                y_line)

                    term_indx += 1

            offset += self.scale

    def add_right_channels(self):
        """
        Creates horizontal channels
        """
        # Channels
        term_indx = 0
        offset = self.y_min_0+self.spacing+self.scale
        for chan, ele in enumerate(self.chanx):
            if chan in [int(e.attrib["index"]) for e in self.chanx_r]:
                # Right to left channels
                if chan in [int(e.attrib["index"]) for e in self.ft_right]:
                    # Passthrough cables
                    self.dwgShapes.add(shapes.Line(start=(self.x_min_4, offset),
                                                   end=(self.x_max_4, offset),
                                                   marker_start=self.marker_blue.get_funciri(),
                                                   marker_end=self.marker_blue.get_funciri(),
                                                   class_="channel lr_chan"))
                    self.dwgText.add(Text(ele.getchildren()[0].attrib["index"],
                                          transform="scale(1,-1)",
                                          class_="lr_text",
                                          insert=(self.x_max_3, -1*offset)))
                    self.dwgText.add(Text(ele.attrib["index"],
                                          transform="scale(1,-1)",
                                          class_="lr_text",
                                          insert=(self.x_min_3, -1*offset)))
                else:
                    # Terminating cable
                    self.dwgShapes.add(shapes.Line(start=(self.x_min_4, offset),
                                                   end=(self.x_max_2, offset),
                                                   marker_start=self.marker_blue.get_funciri(),
                                                   marker_end=self.marker_blue.get_funciri(),
                                                   class_="channel lr_chan"))

                    # Add connecting Vertical line
                    x_line = self.x_max_1 + term_indx*self.scale + self.spacing
                    y_line = self.y_max_0 + term_indx*self.scale + self.spacing
                    self.dwgShapes.add(shapes.Line(start=(x_line, self.y_min_1),
                                                   end=(x_line, y_line),
                                                   marker_start=self.marker_blue.get_funciri(),
                                                   marker_end=self.marker_terminate.get_funciri(),
                                                   class_="channel lr_chan"))
                    # Add connecting horizontal line
                    self.dwgShapes.add(shapes.Line(start=(self.x_min_0, y_line),
                                                   end=(self.x_max_4, y_line),
                                                   marker_start=self.marker_blue.get_funciri(),
                                                   marker_end=self.marker_blue.get_funciri(),
                                                   class_="channel lr_chan"))
                    self._add_short_at(x_line, y_line)

                    # Add Text
                    self.dwgText.add(Text(self.term_left[term_indx].attrib["index"],
                                          transform="scale(1,-1)",
                                          class_="lr_text",
                                          insert=(self.x_min_3, -1*offset)))
                    self.dwgText.add(Text(ele.attrib["index"],
                                          transform="scale(1,-1)",
                                          class_="lr_text",
                                          insert=(self.x_max_3, -1*y_line)))

                    # Add Switches
                    print(f"---> {ele.attrib['index']}")
                    for switch in ele.getchildren():
                        sw_type = switch.attrib["type"]
                        side = switch.attrib["side"]
                        index = int(switch.attrib["index"])
                        grid_side = switch.attrib.get("grid_side", "")
                        if sw_type == "CHANX":
                            self._add_switch_at(
                                x_line,
                                ((index+1)*self.scale) + 2*self.spacing)
                        elif sw_type == "CHANY":
                            self._add_switch_at(
                                ((index+1)*self.scale) + 2*self.spacing,
                                y_line)
                    term_indx += 1

            offset += self.scale

    def add_top_channel(self):
        # Channels
        term_indx = 0
        offset = self.x_min_0+self.spacing+self.scale
        for chan, ele in enumerate(self.chany):
            # Botttom to top channels
            if chan in [int(e.attrib["index"]) for e in self.chany_t]:
                if chan in [int(e.attrib["index"]) for e in self.ft_top]:
                    # Passthrough cables
                    self.dwgShapes.add(shapes.Line(start=(offset, self.y_min_4),
                                                   end=(offset, self.y_max_4),
                                                   marker_start=self.marker_red.get_funciri(),
                                                   marker_end=self.marker_red.get_funciri(),
                                                   class_="channel rl_chan"))
                    self.dwgText.add(Text(ele.getchildren()[0].attrib["index"],
                                          transform="scale(1,-1)",
                                          class_='bt_text',
                                          insert=(offset, -1*self.y_min_3)))
                    self.dwgText.add(Text(ele.attrib["index"],
                                          transform="scale(1,-1)",
                                          class_='bt_text',
                                          insert=(offset, -1*self.y_max_3)))
                else:
                    # Terminating cable
                    self.dwgShapes.add(shapes.Line(start=(offset, self.y_min_4),
                                                   end=(offset, self.y_max_1),
                                                   marker_start=self.marker_red.get_funciri(),
                                                   marker_end=self.marker_red.get_funciri(),
                                                   class_="channel rl_chan"))
                    self.dwgText.add(Text(self.term_bottom[term_indx].attrib["index"],
                                          transform="scale(1,-1)",
                                          class_='bt_text',
                                          insert=(offset, -1*self.y_min_3)))

                    # Add connecting horizontal line
                    x_line = self.x_min_0 - term_indx*self.scale - self.spacing
                    y_line = self.y_max_1 + term_indx*self.scale + self.spacing
                    self.dwgShapes.add(shapes.Line(start=(x_line, y_line),
                                                   end=(self.x_max_2, y_line),
                                                   marker_start=self.marker_terminate.get_funciri(),
                                                   marker_end=self.marker_terminate.get_funciri(),
                                                   class_="channel bt_chan"))
                    # Add connecting vertical line
                    self.dwgShapes.add(shapes.Line(start=(x_line, self.y_min_1),
                                                   end=(x_line, self.y_max_4),
                                                   marker_start=self.marker_terminate.get_funciri(),
                                                   marker_end=self.marker_red.get_funciri(),
                                                   class_="channel bt_chan"))

                    self._add_short_at(x_line, y_line)

                    # Add Text
                    self.dwgText.add(Text(ele.attrib["index"],
                                          transform="scale(1,-1)",
                                          class_="bt_text",
                                          insert=(x_line, -1*self.y_max_3)))

                    # Add Switches
                    print(f"---> {ele.attrib['index']}")
                    for switch in ele.getchildren():
                        sw_type = switch.attrib["type"]
                        side = switch.attrib["side"]
                        index = int(switch.attrib["index"])
                        grid_side = switch.attrib.get("grid_side", "")
                        if sw_type == "CHANX":
                            self._add_switch_at(
                                x_line,
                                ((index+1)*self.scale) + 2*self.spacing)
                        elif sw_type == "CHANY":
                            self._add_switch_at(
                                ((index+1)*self.scale) + 2*self.spacing,
                                y_line)
                    term_indx += 1

            offset += self.scale

    def add_bottom_channel(self):
        # Channels
        term_indx = 0
        offset = self.x_min_0+self.spacing+self.scale
        for chan, ele in enumerate(self.chany):
            # Botttom to top channels
            if chan in [int(e.attrib["index"]) for e in self.chany_b]:
                if chan in [int(e.attrib["index"]) for e in self.ft_bottom]:
                    # Passthrough cables
                    self.dwgShapes.add(shapes.Line(start=(offset, self.y_max_4),
                                                   end=(offset, self.y_min_4),
                                                   marker_start=self.marker_blue.get_funciri(),
                                                   marker_end=self.marker_blue.get_funciri(),
                                                   class_="channel tb_chan"))
                    self.dwgText.add(Text(ele.getchildren()[0].attrib["index"],
                                          transform="scale(1,-1)",
                                          class_='tb_text',
                                          insert=(offset, -1*self.y_max_3)))
                    self.dwgText.add(Text(ele.attrib["index"],
                                          transform="scale(1,-1)",
                                          class_='tb_text',
                                          insert=(offset, -1*self.y_min_3)))
                else:
                    # Terminating cable
                    self.dwgShapes.add(shapes.Line(start=(offset, self.y_max_4),
                                                   end=(offset, self.y_min_1),
                                                   marker_start=self.marker_blue.get_funciri(),
                                                   marker_end=self.marker_blue.get_funciri(),
                                                   class_="channel tb_chan"))
                    self.dwgText.add(Text(self.term_top[term_indx].attrib["index"],
                                          transform="scale(1,-1)",
                                          class_='tb_text',
                                          insert=(offset, -1*self.y_max_3)))

                    # Add connecting horizontal line
                    x_line = self.x_max_1 - term_indx*self.scale - self.spacing
                    y_line = self.y_min_1 - term_indx*self.scale - self.spacing
                    self.dwgShapes.add(shapes.Line(start=(x_line, y_line),
                                                   end=(self.x_min_0, y_line),
                                                   marker_start=self.marker_terminate.get_funciri(),
                                                   marker_end=self.marker_terminate.get_funciri(),
                                                   class_="channel tb_chan"))
                    # Add connecting vertical line
                    self.dwgShapes.add(shapes.Line(start=(x_line, self.y_max_1),
                                                   end=(x_line, self.y_min_4),
                                                   marker_start=self.marker_terminate.get_funciri(),
                                                   marker_end=self.marker_blue.get_funciri(),
                                                   class_="channel tb_chan"))
                    self._add_short_at(x_line, y_line)

                    # Add Text
                    self.dwgText.add(Text(ele.attrib["index"],
                                          transform="scale(1,-1)",
                                          class_="tb_text",
                                          insert=(x_line, -1*self.y_min_3)))

                    # Add Switches
                    print(f"---> {ele.attrib['index']}")
                    for switch in ele.getchildren():
                        sw_type = switch.attrib["type"]
                        side = switch.attrib["side"]
                        index = int(switch.attrib["index"])
                        grid_side = switch.attrib.get("grid_side", "")
                        if sw_type == "CHANX":
                            self._add_switch_at(
                                x_line,
                                ((index+1)*self.scale) + 2*self.spacing)
                        elif sw_type == "CHANY":
                            self._add_switch_at(
                                ((index+1)*self.scale) + 2*self.spacing,
                                y_line)
                    term_indx += 1

            offset += self.scale

    def _add_switch_at(self, x, y):
        self.switches.add(shapes.Circle(center=(x, y), r=10, class_="switch"))

    def _add_short_at(self, x, y):
        self.switches.add(shapes.Circle(center=(x, y), r=10, class_="short"))

    def _add_partitions(self):
        min_terminating = min(self.ft_left_len, self.ft_right_len,
                              self.ft_top_len, self.ft_bottom_len)

        width = self.chanx_len*self.scale + 2*self.spacing
        width1 = width + 2*(self.chanx_l_len-min_terminating)*self.scale \
            + 2*self.spacing
        width2 = width1 + 2*(self.chanx_l_len-min_terminating)*self.scale \
            + 2*self.spacing
        width3 = width2 + 2*(self.chanx_l_len-min_terminating)*self.scale
        width4 = width3 + (self.ipin_l_len+self.ipin_r_len)*self.scale

        height = self.chany_len*self.scale + 2*self.spacing
        height1 = height + 2*(self.chany_t_len-min_terminating)*self.scale \
            + 2*self.spacing
        height2 = height1 + 2*(self.chany_t_len-min_terminating)*self.scale \
            + 2*self.spacing
        height3 = height2 + 2*(self.chany_t_len-min_terminating)*self.scale
        height4 = height3 + (self.ipin_t_len+self.ipin_b_len)*self.scale

        insert_pt = -0.5*(width4-width), -0.5*(height4-height)
        self.x_min_4, self.y_min_4 = insert_pt
        self.x_min_4 += (self.ipin_r_len-self.ipin_l_len)*self.scale
        self.y_min_4 += (self.ipin_t_len-self.ipin_b_len)*self.scale
        self.x_max_4, self.y_max_4 = self.x_min_4+width4, self.y_min_4+height4

        insert_pt = -0.5*(width3-width), -0.5*(height3-height)
        self.x_min_3, self.y_min_3 = insert_pt
        self.x_max_3, self.y_max_3 = self.x_min_3+width3, self.y_min_3+height3

        insert_pt = -0.5*(width2-width), -0.5*(height2-height)
        self.x_min_2, self.y_min_2 = insert_pt
        self.x_max_2, self.y_max_2 = self.x_min_2+width2, self.y_min_2+height2

        insert_pt = -0.5*(width1-width), -0.5*(height1-height)
        self.x_min_1, self.y_min_1 = insert_pt
        self.x_max_1, self.y_max_1 = self.x_min_1+width1, self.y_min_1+height1

        self.x_min_0, self.y_min_0 = 0, 0
        self.x_max_0, self.y_max_0 = width, height

        self.region.add(shapes.Rect(insert=(self.x_min_3, self.y_min_4),
                                    size=(width3, height4),
                                    class_="boundry"))
        self.region.add(shapes.Rect(insert=(self.x_min_4, self.y_min_3),
                                    size=(width4, height3),
                                    class_="boundry"))
        self.region.add(shapes.Rect(insert=(self.x_min_3, self.y_min_3),
                                    size=(width3, height3),
                                    class_="region4"))
        self.region.add(shapes.Rect(insert=(self.x_min_2, self.y_min_2),
                                    size=(width2, height2),
                                    class_="region3"))
        self.region.add(shapes.Rect(insert=(self.x_min_1, self.y_min_1),
                                    size=(width1, height1),
                                    class_="region2"))
        self.region.add(shapes.Rect(insert=(0, 0),
                                    size=(width, height),
                                    class_="region1"))
        self.width = width
        self.width1 = width1
        self.width2 = width2
        self.width3 = width3
        self.width4 = width4
        self.height = height
        self.height1 = height1
        self.height2 = height2
        self.height3 = height3
        self.height4 = height4

    def _add_switches(self):
        for chan, ele in enumerate(self.chanx):
            for switch in ele.getchildren():
                sw_type = switch.attrib["type"]
                side = switch.attrib["side"]
                index = int(switch.attrib["index"])
                grid_side = switch.attrib.get("grid_side", "")
                if sw_type == "CHANX":
                    pass
                elif sw_type == "CHANY":
                    pass
        pass
        # for chan_indx, chan in enumerate(self.ipin_t):
        #     for switch in chan.getchildren():
        #         sw_type = switch.attrib["type"]
        #         side = switch.attrib["side"]
        #         index = int(switch.attrib["index"])

        #         if sw_type.startswith("CHANX"):
        #             cx = (index+1)*self.scale + self.spacing
        #             cy = ((chan_indx)+(self.chany_len+1)) * \
        #                 self.scale + self.spacing
        #             self.switches.add(shapes.Circle(
        #                 center=(cx, cy), r=10, class_="switch"
        #             ))

    def render_switch_pattern(self):
        # Create groups in SVG image
        self._add_partitions()
        self._add_origin_marker()
        # ====================================
        #         Create channels
        # ====================================
        self.add_left_channels()
        # self.add_right_channels()
        self.add_top_channel()
        # self.add_bottom_channel()

        # add_channels(dwgShapes, root)

    def _add_origin_marker(self):
        self.dwgbg.add(shapes.Line(start=(0, 1*self.scale),
                                   end=(0, -1*self.scale),
                                   class_="origin"))
        self.dwgbg.add(shapes.Line(start=(1*self.scale, 0),
                                   end=(-1*self.scale, 0),
                                   class_="origin"))

    def save(self, filename=None):
        """ Save SVG file"""
        self.add_stylehseet()
        filename = filename or "_"+self.name+".svg"
        width, height = self.chanx_len*self.scale, self.chany_len*self.scale
        viewbox = -0.5*width, -3*height, 3*width, 6*height
        self.dwg.viewbox(*viewbox)
        logger.debug(f"Saving svg {filename}")
        self.dwg.saveas(filename, pretty=True)

    def _create_arrowhead(self, hex_color):
        DRMarker = self.dwg.marker(refX="30", refY="30",
                                   viewBox="0 0 120 120",
                                   markerUnits="strokeWidth",
                                   markerWidth="8", markerHeight="10", orient="auto")
        DRMarker.add(self.dwg.path(d="M 0 0 L 60 30 L 0 60 z", fill=hex_color))
        self.dwg.defs.add(DRMarker)
        return DRMarker

    def _create_termination(self, hex_color):
        DRMarker = self.dwg.marker(refX="0", refY="0",
                                   viewBox="-10 -30 20 60",
                                   markerUnits="strokeWidth",
                                   markerWidth="4", markerHeight="10", orient="auto")
        DRMarker.add(shapes.Rect(insert=(-5, -15), height="30",
                                 width="10", fill=hex_color))
        self.dwg.defs.add(DRMarker)
        return DRMarker

    def add_stylehseet(self):
        '''
        Adds custom stylesheet to the SVG image
        '''
        self.dwg.defs.add(self.dwg.style("""
                text{font-family: LATO; font-weight: 800; font-size: 25px;}
                .module_boundary{fill:#f4f0e6}
                .origin{stroke: red; stroke-width: 1;}
                .channel{stroke: grey; stroke-width: 4;}
                .switch{stroke: black; fill:blue; stroke-width: 0;}
                .short{stroke: black; fill:black; stroke-width: 0;}
                .inpin{stroke: red;stroke-width: 4;}
                .outpin{stroke: green;stroke-width: 4;}
                .rl_chan{stroke: red;}
                .lr_chan{stroke: blue;}
                .lr_text{fill: blue;}
                .rl_text{fill: red;}
                .bt_chan{stroke: red;}
                .bt_text{fill: red;}
                .tb_chan{stroke: blue;}
                .tb_text{fill: blue;}
                .region1{fill: #CCE7D4;}
                .region2{fill: #F8AC92;}
                .region3{fill: #C4E7EB;}
                .region4{fill: #F5F3C9;}
                .boundry{stroke: red;stroke-width: 10;fill: none;opacity: 10%;}
                .left_pin{
                    fill:blue;
                    text-anchor: start;
                    transform: translate(5px, 00px) scale(1,-1);}
                .right_pin{
                    fill:blue;
                    text-anchor: end;
                    transform: translate(-5px, 00px) scale(1,-1);}
                .bottom_pin{
                    fill:blue;
                    transform-box: fill-box;
                    transform-origin: start;
                    text-anchor: start;
                    transform: translate(0px, 10px) rotate(90deg) scale(1,-1);}
                .top_pin{
                    fill:blue;
                    transform-box: fill-box;
                    transform-origin: bottom left;
                    text-anchor: start;
                    transform: translate(0px, -3px) rotate(-90deg) scale(1,-1);}
                .in_pin{fill: red;}
                .out_pin{fill: blue;}
            """))
