import logging
import xml.etree.ElementTree as ET

from pprint import pprint
from svgwrite import Drawing, shapes
from svgwrite.container import Group
from svgwrite.mixins import XLink
from svgwrite.text import Text
import numpy as np

logger = logging.getLogger("spydrnet_logs")


class base_renderer:
    """
    This is a base class for ``cb_renderer`` and ``sb_renderer``
    """

    def __init__(self, name, gsb_xml, scale=40, spacing=None) -> None:
        self.name = name
        self.scale = scale
        self.spacing = spacing if spacing else self.scale * 2
        self.root = (
            gsb_xml if isinstance(gsb_xml, ET.Element) else ET.parse(gsb_xml).getroot()
        )
        self.extract_info()

    @staticmethod
    def _get_label(x):
        """
        returns attribute  ``<side>_<index>`` as a string
        """
        return f"{x.attrib['side']}_{int(x.attrib['index'])}"

    def extract_info(self):
        """
        This should be extended in the specific element rendering class
        """
        raise NotImplementedError

    def _setup_svg(self):
        # Variables for SVG rendering
        self.dwg = Drawing()
        self.dwgbg = self.dwg.add(Group(id="bg"))
        self.region = self.dwg.add(Group(id="region", transform="scale(1,-1)"))
        self.core = self.dwg.add(Group(id="mainframe"))
        self.dwgShapes = self.core.add(Group(id="mainShapes", transform="scale(1,-1)"))
        self.switches = self.core.add(Group(id="switches", transform="scale(1,-1)"))
        self.dwgText = self.core.add(Group(id="mainText", transform="scale(1,-1)"))
        self.marker_red = self._create_arrowhead("red")
        self.marker_green = self._create_arrowhead("green")
        self.marker_blue = self._create_arrowhead("blue")
        self.marker_terminate = self._create_termination("blue")
        return self.dwg

    def save(self, filename=None, viewbox=None):
        """Save SVG file"""
        self._add_stylehseet()
        filename = filename or "_" + self.name + ".svg"
        margin = 200
        # width, height = self.x_max_4-self.x_min_4, self.y_max_4-self.y_min_4
        # viewbox = viewbox or (self.x_min_4-margin, -1*(self.y_max_4+margin),
        #                       width+2*margin, height+2*margin)
        # self.dwg.viewbox(*viewbox)
        logger.debug(f"Saving svg {filename}")
        self.dwg.saveas(filename, pretty=True)

    def _create_termination(self, hex_color):
        DRMarker = self.dwg.marker(
            refX="0",
            refY="0",
            viewBox="-10 -30 20 60",
            markerUnits="strokeWidth",
            markerWidth="4",
            markerHeight="10",
            orient="auto",
        )
        DRMarker.add(
            shapes.Rect(insert=(-5, -15), height="30", width="10", fill=hex_color)
        )
        self.dwg.defs.add(DRMarker)
        return DRMarker

    def _create_arrowhead(self, hex_color):
        DRMarker = self.dwg.marker(
            refX="30",
            refY="30",
            viewBox="0 0 120 120",
            markerUnits="strokeWidth",
            markerWidth="8",
            markerHeight="10",
            orient="auto",
        )
        DRMarker.add(self.dwg.path(d="M 0 0 L 60 30 L 0 60 z", fill=hex_color))
        self.dwg.defs.add(DRMarker)
        return DRMarker

    def _add_stylehseet(self):
        """
        Adds custom stylesheet to the SVG image
        """
        self.dwg.defs.add(
            self.dwg.style(
                """
                text{font-family: LATO; font-weight: 800; font-size: 25px;}
                svg{outline: 1px solid grey; outline-offset: -2px;}
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
                .OPIN{fill: green;}
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
                .in_pin{fill: blue !important;}
                .out_pin{fill: red !important;}
            """
            )
        )


class sb_renderer(base_renderer):
    """
    Renders the switch box information from GSB (Generic Switch Box) file
    """

    def extract_info(self) -> None:
        """
        Extracts all parameters

        .. csv-table:: Channel Variables
            :widths: 25, 100

            chan_out        , All output channels
            chanx_[l/r]_in  , Horizontal left and right incoming channels
            chany_[t/b]_in  , Vertical top and bottom incoming channels
            opin_l[l/r/t/b] , Incoming grid output channels
        """
        self.chan_out = sorted(
            self.root.findall("CHANX") + self.root.findall("CHANY"),
            key=lambda x: f"{x.attrib['side']}_{int(x.attrib['index']):03}",
        )
        self.chan_out_l = len(self.chan_out)

        self.chanx_l_in = sorted(
            self.root.findall(".//INPUT/CHANX/driver_node[@side='left']"),
            key=lambda x: int(x.attrib["index"]),
        )
        self.chanx_r_in = sorted(
            self.root.findall(".//INPUT/CHANX/driver_node[@side='right']"),
            key=lambda x: int(x.attrib["index"]),
        )
        self.chany_t_in = sorted(
            self.root.findall(".//INPUT/CHANY/driver_node[@side='top']"),
            key=lambda x: int(x.attrib["index"]),
        )
        self.chany_b_in = sorted(
            self.root.findall(".//INPUT/CHANY/driver_node[@side='bottom']"),
            key=lambda x: int(x.attrib["index"]),
        )

        self.opin_l = sorted(
            self.root.findall(".//INPUT/OPIN/driver_node[@side='left']"),
            key=lambda x: int(x.attrib["index"]),
        )
        self.opin_r = sorted(
            self.root.findall(".//INPUT/OPIN/driver_node[@side='right']"),
            key=lambda x: int(x.attrib["index"]),
        )
        self.opin_t = sorted(
            self.root.findall(".//INPUT/OPIN/driver_node[@side='top']"),
            key=lambda x: int(x.attrib["index"]),
        )
        self.opin_b = sorted(
            self.root.findall(".//INPUT/OPIN/driver_node[@side='bottom']"),
            key=lambda x: int(x.attrib["index"]),
        )

        self.channels = self.root.attrib["type"].lower()
        assert self.channels == "sb", "XML file does not contain Switch box information"

    def _create_header(self, in_pin):
        """
        Create headers for printing information
        """
        index_label_map, loc = {}, 0
        header, conn_str = "", ""
        for side, side_chann in {
            "chany_bottom": self.chany_b_in,
            "chanx_left": self.chanx_l_in,
            "chanx_right": self.chanx_r_in,
            "chany_top": self.chany_t_in,
            "opin_bottom": self.opin_b,
            "opin_left": self.opin_l,
            "opin_right": self.opin_r,
            "opin_top": self.opin_t,
        }.items():
            if not side in in_pin:
                continue
            margin = 2 if len(side_chann) > 7 else 7
            i = len(side_chann) + 2 * margin
            loc += margin
            conn_str += " " * margin
            header += side.center(i)
            for x in side_chann:
                index_label_map[
                    f"{x.attrib['type'].lower()}_" + self._get_label(x)
                ] = loc
                loc += 1
                conn_str += "."
            loc += margin
            conn_str += " " * margin
        return header, conn_str, index_label_map

    def report_connectivity(
        self, pin_map={}, in_pin=None, out_pin=None, filter_direct=False
    ):
        """
        Report connectivity of each driver mux

        parameters
        ----------

        filter_direct (bool): Skips printing of direct feedtrhough connections
        in_pin
        out_pin
        """
        out_pin = out_pin or ["left", "right", "top", "bottom"]
        out_pin = [out_pin] if isinstance(out_pin, str) else out_pin
        in_pin = in_pin or [
            "chanx_left",
            "chanx_right",
            "chany_top",
            "chany_bottom",
            "opin_left",
            "opin_right",
            "opin_top",
            "opin_bottom",
        ]
        in_pin = [in_pin] if isinstance(in_pin, str) else in_pin

        header, conn_str, index_label_map = self._create_header(in_pin)
        index_label_map.update(pin_map)

        print(f"{' ':11}{header}")
        for eachPin in self.chan_out:
            direct = "-" if eachPin.attrib["mux_size"] == "0" else " "
            if filter_direct and direct == "-":
                continue
            if not eachPin.attrib["side"] in out_pin:
                continue
            print(f"{self._get_label(eachPin):10}{direct:1}", end="")
            conn = list(conn_str)
            for eachconn in eachPin:
                if (
                    not f"{eachconn.attrib['type'].lower()}_{eachconn.attrib['side']}"
                    in in_pin
                ):
                    continue
                conn[
                    index_label_map[
                        f"{eachconn.attrib['type'].lower()}_"
                        + self._get_label(eachconn)
                    ]
                ] = "x"
            print("".join(conn), end="")
            print("")
        print("")


class cb_renderer(base_renderer):
    """
    This class renders the conenction box information
    """

    def extract_info(self) -> None:
        """
        .. csv-table:: Channel Variables
            :widths: 25, 100

            ipin_l     , IPIN (Output) Pin toward left direction
            ipin_l_len , Number of output pins towards left direction
        """
        self.ipin = sorted(
            self.root.findall("IPIN"),
            key=lambda x: f"{x.attrib['side']}_{x.attrib['index']}",
        )
        self.ipin_l = len(self.ipin)
        logger.debug("Found %d Ipins", self.ipin_l)
        self.chan = sorted(
            {node.attrib["index"] for node in self.root.findall(".//*/driver_node")}
        )

        self.chan_l = len(self.chan)
        logger.debug("Found %d Channels", self.chan_l)
        self.channels = self.root.tag.lower()
        assert (
            "cb" in self.channels
        ), "XML file does not contain connection box information"

    def report_ipins(self):
        """
        Reports IPIN information

        parameters
        ----------

        pMap: Pin map information if position needs to modified {pin_label: location}
            example: {'top_1': 2, 'left_1': 1 }

        """
        print(
            f"{' ':13}  "
            + "|    " * int(np.floor(self.chan_l / (2 * 5)))
            + "  "
            + "|    " * int(np.floor(self.chan_l / (2 * 5)))
        )
        for each_pin in self.ipin:
            print(
                f"{each_pin.attrib['side']:>10} " + f"{each_pin.attrib['index']:4}",
                end="",
            )
            conn_map = ["-"] * self.chan_l
            for conn in each_pin:
                conn_map[int(conn.attrib["index"])] = "x"

            print("".join(conn_map[::2]), end="  ")
            print("".join(conn_map[1::2]), end="")
            print(f" {conn_map.count('x'):3}")


class RoutingRender:
    """
    This class illustrates the FPGA switch box and connection box based on the
    given GSB xml files.

    **General Variables**

    Args:
        self.name: Name of the module
        self.scale: General scale for rendering connectivity
        self.spacing: Margin beetween each section
        self.root: Parsed XML Root element

    .. csv-table:: Channel Variables
       :widths: 25, 75

       self.chanx           ,Unique list of elements horizontal channels
       self.chanx_l         ,Unique list of elements left incoming chanx channels
       self.chanx_l_len     ,length of ``chanx_l``
       self.chanx_r         ,Unique list of elements right incoming chanx channels
       self.chanx_r_len     ,length of ``chanx_r``

       self.chanx_l_drivers ,New generated left outgoing channels with feedthrough
       self.chanx_l_ft      ,Left outgoing channels with feedthrough
       self.chanx_l_out_map ,Mapping of ft/driver index with offset on the left side

       self.ipin_l          ,Unique list of elements outgoing from connection box on left side
       self.ipin_l_len      ,Length of ``ipin_l``

       self.opin_l          ,Unique list of elements incoming from left side
       self.opin_l_len      ,Length of ``opin_l``
       self.opin_l_t        ,Unique list of elements incoming from left top side
       self.opin_l_t_len    ,Length of ``opin_l_t``
       self.opin_l_b        ,Unique list of elements incoming from left bottom side
       self.opin_l_b_len    ,Length of ``opin_l_b``



    """

    def __init__(self, name, gsb_xml, scale=40, spacing=None) -> None:
        """
        Initialise the rendering class

        args:
            name (str): Name of the connection box
            gsb_xml (str): XML file path to read
        """
        self.name = name
        self.scale = scale
        self.spacing = spacing if spacing else self.scale * 2
        self.root = (
            gsb_xml if isinstance(gsb_xml, ET.Element) else ET.parse(gsb_xml).getroot()
        )
        self.extract_info()

    def update_dimensions(self, scale, spacing):
        """
        Updates scale and spacing dimensions
        """
        self.scale = int(scale) or self.scale
        self.spacing = int(spacing) or self.spacing

    @staticmethod
    def render_ipin(sw):
        size = sw.shape
        format_str = "{:<6} {:<6} {:^%d} " % size[1]
        print("=" * (size[1] + 16))
        print(format_str.format("INDX", "MUX", "CONNECTIONS"))
        print("=" * (size[1] + 16))
        print(
            format_str.format(
                "", "", "".join(["{:<4}|".format(i) for i in range(0, size[1], 5)])
            )
        )
        for indx, row in enumerate(sw):
            count = row.size - list(row).count("_")
            print(format_str.format(indx, count, "".join(row)))

    @staticmethod
    def _filter_attrib(eles, attrib, value):
        return [e for e in eles if e.attrib[attrib] == value]

    @staticmethod
    def _get_driver_node(root, p, type, side):
        return root.findall(f"{p}/driver_node[@type='{type}'][@side='{side}']")

    @staticmethod
    def _get_max_index(ele):
        return len({int(i.attrib["index"]): "" for i in ele}.keys())

    @staticmethod
    def _set_bit(x, indx, symbol="x"):
        x[int(indx)] = symbol

    @staticmethod
    def _set_vbit(x, indx):
        x[int(indx)] = "l" if int(indx) % 2 else "r"

    @staticmethod
    def _set_hbit(x, indx):
        x[int(indx)] = "t" if int(indx) % 2 else "b"

    @staticmethod
    def _print_stat_header():
        """
        Prints header for statistics information

        module
        chanx_l  chanx_r  chany_t  chany_b
        ipin_t   ipin_b   ipin_r   ipin_l
        opin_l   opin_r   opin_t   opin_b
        """
        print("==" * 80)
        print(
            "%15s %8s %8s %8s %8s %8s %8s %8s %8s %15s %15s %15s %15s"
            % (
                "module",
                "chanx_l",
                "chanx_r",
                "chany_t",
                "chany_b",
                "ipin_l",
                "ipin_r",
                "ipin_t",
                "ipin_b",
                "opin_l",
                "opin_r",
                "opin_t",
                "opin_b",
            )
        )
        print("==" * 80)

    def report_ipins(self, side, show=True):
        format_str = "{:^6s} {:^6s} {:^45s} "
        items = {
            "left": self.ipin_l,
            "right": self.ipin_r,
            "top": self.ipin_t,
            "bottom": self.ipin_b,
        }[side]
        arr = np.empty(
            shape=[0, self.chanx_len if side in ["top", "bottom"] else self.chany_len],
            dtype=np.str,
        )
        for chan in items:
            ChanX = ["_"] * self.chanx_len
            _ = [
                self._set_bit(ChanX, e.attrib["index"])
                for e in chan.findall('./driver_node[@type="CHANX"]')
            ]
            ChanY = ["_"] * self.chany_len
            _ = [
                self._set_bit(ChanY, e.attrib["index"])
                for e in chan.findall('./driver_node[@type="CHANY"]')
            ]
            flags = ChanX if side in ["top", "bottom"] else ChanY
            arr = np.vstack([arr, flags])
        if show:
            self.render_ipin(arr)
        return arr

    def report_incoming_channels(self, side):
        """
        This prints incoming channels in the given switch box
        from the given direction
        ``index, Mux, ChanX, Chany, OPIN_L, OPIN_R, OPIN_T, OPIN_B``
        """
        format_str = "{:^6s} {:^6s} {:^45s} {:^45s} {:^10s} {:^10s} {:^10s} {:^10s}"
        print("= = " * 40)
        print(
            format_str.format(
                "index", "Mux", "ChanX", "Chany", "OPIN_L", "OPIN_R", "OPIN_T", "OPIN_B"
            )
        )
        print("= = " * 40)

        items = {
            "left": self.chanx_l,
            "right": self.chanx_r,
            "top": self.chany_t,
            "bottom": self.chany_b,
        }[side]
        for chan in items:
            ChanX = ["_"] * self.chanx_len
            _ = [
                self._set_vbit(ChanX, e.attrib["index"])
                for e in chan.findall('./driver_node[@type="CHANX"]')
            ]
            ChanY = ["_"] * self.chany_len
            ChanY = ["_"] * 40
            _ = [
                self._set_hbit(ChanY, e.attrib["index"])
                for e in chan.findall('./driver_node[@type="CHANY"]')
            ]
            # OPIN_L = ['_']*self.opin_l_len
            # _ = [self._set_bit(OPIN_L, e.attrib['index'])
            #      for e in chan.findall('./driver_node[@type="OPIN"][@side="left"]')]
            # OPIN_R = ['_']*self.opin_l_len
            # _ = [self._set_bit(OPIN_R, e.attrib['index'])
            #      for e in chan.findall('./driver_node[@type="OPIN"][@side="right"]')]
            # OPIN_T = ['_']*self.opin_l_len
            # _ = [self._set_bit(OPIN_T, e.attrib['index'])
            #      for e in chan.findall('./driver_node[@type="OPIN"][@side="top"]')]
            # OPIN_B = ['_']*self.opin_l_len
            # _ = [self._set_bit(OPIN_B, e.attrib['index'])
            #      for e in chan.findall('./driver_node[@type="OPIN"][@side="bottom"]')]
            OPIN_L = ["_", "_"]
            OPIN_R = ["_", "_"]
            OPIN_T = ["_", "_"]
            OPIN_B = ["_", "_"]
            print(
                format_str.format(
                    chan.attrib["index"],
                    chan.attrib["mux_size"],
                    "".join(ChanX),
                    "".join(ChanY),
                    "".join(OPIN_L),
                    "".join(OPIN_R),
                    "".join(OPIN_T),
                    "".join(OPIN_B),
                )
            )

    def report_outgoing_channels(self, side):
        """
        This prints the channel information of given switch box
        for a given direction channels
        """
        format_str = "{:^6s} {:^6s} {:^45s} {:^45s} {:^10s} {:^10s} {:^10s} {:^10s}"
        print("= = " * 40)
        print(
            format_str.format(
                "index", "Mux", "ChanX", "Chany", "OPIN_L", "OPIN_R", "OPIN_T", "OPIN_B"
            )
        )
        print("= = " * 40)

        items = {
            "left": self.chanx_l,
            "right": self.chanx_r,
            "top": self.chany_t,
            "bottom": self.chany_b,
        }[side]
        for chan in items:
            ChanX = ["_"] * self.chanx_len
            _ = [
                self._set_vbit(ChanX, e.attrib["index"])
                for e in chan.findall('./driver_node[@type="CHANX"]')
            ]
            ChanY = ["_"] * self.chany_len
            _ = [
                self._set_hbit(ChanY, e.attrib["index"])
                for e in chan.findall('./driver_node[@type="CHANY"]')
            ]
            OPIN_L = ["_"] * self.opin_l_len
            _ = [
                self._set_bit(OPIN_L, e.attrib["index"])
                for e in chan.findall('./driver_node[@type="OPIN"][@side="left"]')
            ]
            OPIN_R = ["_"] * self.opin_l_len
            _ = [
                self._set_bit(OPIN_R, e.attrib["index"])
                for e in chan.findall('./driver_node[@type="OPIN"][@side="right"]')
            ]
            OPIN_T = ["_"] * self.opin_l_len
            _ = [
                self._set_bit(OPIN_T, e.attrib["index"])
                for e in chan.findall('./driver_node[@type="OPIN"][@side="top"]')
            ]
            OPIN_B = ["_"] * self.opin_l_len
            _ = [
                self._set_bit(OPIN_B, e.attrib["index"])
                for e in chan.findall('./driver_node[@type="OPIN"][@side="bottom"]')
            ]
            print(
                format_str.format(
                    chan.attrib["index"],
                    chan.attrib["mux_size"],
                    "".join(ChanX),
                    "".join(ChanY),
                    "".join(OPIN_L),
                    "".join(OPIN_R),
                    "".join(OPIN_T),
                    "".join(OPIN_B),
                )
            )

    def extract_info(self):
        """
        Extracts insformation from provided general switch box file
        """
        root = self.root
        self.chanx = sorted(root.findall("CHANX"), key=lambda x: int(x.attrib["index"]))
        self.chanx_len = len(self.chanx)
        self.chanx_l = root.findall("CHANX[@side='left']")
        self.chanx_l_len = len(self.chanx_l)
        self.chanx_r = root.findall("CHANX[@side='right']")
        self.chanx_r_len = len(self.chanx_r)

        self.chanx_l_out_map = [0] * self.chanx_len
        self.chanx_r_out_map = [0] * self.chanx_len
        self.chanx_drivers = self.chanx_l + self.chanx_r
        self.chanx_drivers = root.findall(
            './/CHANX/driver_node[@type="CHANX"]'
        ) + root.findall('.//CHANY/driver_node[@type="CHANX"]')

        self.chany_t = root.findall("CHANY[@side='top']")
        self.chany_t_len = len(self.chany_t)
        self.chany_b = root.findall("CHANY[@side='bottom']")
        self.chany_b_len = len(self.chany_b)
        self.chany = sorted(root.findall("CHANY"), key=lambda x: int(x.attrib["index"]))
        self.chany_len = self.chany_t_len + self.chany_b_len
        self.chany_t_out_map = [0] * self.chany_len
        self.chany_b_out_map = [0] * self.chany_len
        self.chany_drivers = self.chany_t + self.chany_b
        self.chany_drivers = root.findall(
            './/CHANY/driver_node[@type="CHANY"]'
        ) + root.findall('.//CHANX/driver_node[@type="CHANY"]')

        self.ipin_l = root.findall("IPIN[@side='left']")
        self.ipin_l_len = self._get_max_index(self.ipin_l)
        self.ipin_r = root.findall("IPIN[@side='right']")
        self.ipin_r_len = self._get_max_index(self.ipin_r)
        self.ipin_t = root.findall("IPIN[@side='top']")
        self.ipin_t_len = self._get_max_index(self.ipin_t)
        self.ipin_b = root.findall("IPIN[@side='bottom']")
        self.ipin_b_len = self._get_max_index(self.ipin_b)

        # Collect Feedthrough
        self.ft_left = [chan for chan in self.chanx_l if len(list(chan)) == 1]
        self.ft_left_len = len(set((e.attrib["index"] for e in self.ft_left)))
        self.ft_right = [chan for chan in self.chanx_r if len(list(chan)) == 1]
        self.ft_right_len = len(set((e.attrib["index"] for e in self.ft_right)))
        self.ft_top = [chan for chan in self.chany_t if len(list(chan)) == 1]
        self.ft_top_len = len(set((e.attrib["index"] for e in self.ft_top)))
        self.ft_bottom = [chan for chan in self.chany_b if len(list(chan)) == 1]
        self.ft_bottom_len = len(set((e.attrib["index"] for e in self.ft_bottom)))

        # Left side OPins
        self.opin_l = self._get_driver_node(root, "*", "OPIN", "left")
        self.opin_l_len = self._get_max_index(self.opin_l)
        self.opin_l_t = self._filter_attrib(self.opin_l, "grid_side", "top")
        self.opin_l_t_len = self._get_max_index(self.opin_l_t)
        self.opin_l_b = self._filter_attrib(self.opin_l, "grid_side", "bottom")
        self.opin_l_b_len = self._get_max_index(self.opin_l_b)

        # right side OPins
        self.opin_r = self._get_driver_node(root, "*", "OPIN", "right")
        self.opin_r_len = self._get_max_index(self.opin_r)
        self.opin_r_t = self._filter_attrib(self.opin_r, "grid_side", "top")
        self.opin_r_t_len = self._get_max_index(self.opin_r_t)
        self.opin_r_b = self._filter_attrib(self.opin_r, "grid_side", "bottom")
        self.opin_r_b_len = self._get_max_index(self.opin_r_b)

        # top side OPins
        self.opin_t = self._get_driver_node(root, "*", "OPIN", "top")
        self.opin_t_len = self._get_max_index(self.opin_t)
        self.opin_t_l = self._filter_attrib(self.opin_t, "grid_side", "left")
        self.opin_t_l_len = self._get_max_index(self.opin_t_l)
        self.opin_t_r = self._filter_attrib(self.opin_t, "grid_side", "right")
        self.opin_t_r_len = self._get_max_index(self.opin_t_r)

        # Bottom side OPins
        self.opin_b = self._get_driver_node(root, "*", "OPIN", "bottom")
        self.opin_b_len = self._get_max_index(self.opin_b)
        self.opin_b_l = self._filter_attrib(self.opin_b, "grid_side", "left")
        self.opin_b_l_len = self._get_max_index(self.opin_b_l)
        self.opin_b_r = self._filter_attrib(self.opin_b, "grid_side", "right")
        self.opin_b_r_len = self._get_max_index(self.opin_b_r)

    def get_stats(self, print_header=False, noprint=False):
        """
        Prints switch box statistics
        """
        if print_header:
            self._print_stat_header()
        msg = "%15s %8s %8s %8s %8s %8s %8s %8s %8s %15s %15s %15s %15s" % (
            self.name,
            self.chanx_l_len,
            self.chanx_r_len,
            self.chany_t_len,
            self.chany_b_len,
            self.ipin_l_len,
            self.ipin_r_len,
            self.ipin_t_len,
            self.ipin_b_len,
            f"{self.opin_l_len:3} [{self.opin_l_t_len:3},{self.opin_l_b_len:3}]",
            f"{self.opin_r_len:3} [{self.opin_r_t_len:3},{self.opin_r_b_len:3}]",
            f"{self.opin_t_len:3} [{self.opin_t_l_len:3},{self.opin_t_r_len:3}]",
            f"{self.opin_b_len:3} [{self.opin_b_l_len:3},{self.opin_b_r_len:3}]",
        )
        if not noprint:
            print(msg)
        return msg

    def save(self, filename=None, viewbox=None):
        """Save SVG file"""
        self._add_stylehseet()
        filename = filename or "_" + self.name + ".svg"
        margin = 200
        width, height = self.x_max_4 - self.x_min_4, self.y_max_4 - self.y_min_4
        viewbox = viewbox or (
            self.x_min_4 - margin,
            -1 * (self.y_max_4 + margin),
            width + 2 * margin,
            height + 2 * margin,
        )
        self.dwg.viewbox(*viewbox)
        logger.debug(f"Saving svg {filename}")
        self.dwg.saveas(filename, pretty=True)

    def _add_left_connection_box(self, pinmap=None, channel_map=None):
        self.chanx_l_out_map = []
        left_drivers = [e.attrib["index"] for e in self.chanx_l]
        for index in range(self.chanx_len):
            offset = self.x_min_0 + self.spacing + pinmap(index) * self.scale
            self.chanx_l_out_map.append(offset)
            marker = self.marker_blue
            start = (self.y_min_4, offset)
            end = (self.y_min_3, offset)
            class_ = "lr"
            if str(index) in left_drivers:
                marker = self.marker_red
                start, end = end, start
                class_ = "rl"
            self.dwgShapes.add(
                shapes.Line(
                    start=start,
                    end=end,
                    marker_end=marker.get_funciri(),
                    class_=f"channel {class_}_chan",
                )
            )
            self.dwgText.add(
                Text(
                    index,
                    transform="scale(1,-1)",
                    class_=f"{class_}_text",
                    insert=(start[0], -1 * start[-1]),
                )
            )
            self.dwgText.add(
                Text(
                    index,
                    transform="scale(1,-1)",
                    class_=f"{class_}_text",
                    insert=(end[0], -1 * end[-1]),
                )
            )
        self._add_ipins(side="left", channel_map=channel_map)

    def _add_top_connection_box(self, pinmap=None, channel_map=None):
        self.chany_t_out_map = []
        left_drivers = [e.attrib["index"] for e in self.chany_t]
        for index in range(self.chany_len):
            offset = self.y_min_0 + self.spacing + pinmap(index) * self.scale
            self.chany_t_out_map.append(offset)
            marker = self.marker_blue
            start = (offset, self.x_max_4)
            end = (offset, self.x_max_3)
            class_ = "lr"
            if str(index) in left_drivers:
                marker = self.marker_red
                start, end = end, start
                class_ = "rl"
            self.dwgShapes.add(
                shapes.Line(
                    start=start,
                    end=end,
                    marker_end=marker.get_funciri(),
                    class_=f"channel {class_}_chan",
                )
            )
            self.dwgText.add(
                Text(
                    index,
                    transform="scale(1,-1)",
                    class_=f"{class_}_text",
                    insert=(start[0], -1 * start[-1]),
                )
            )
            self.dwgText.add(
                Text(
                    index,
                    transform="scale(1,-1)",
                    class_=f"{class_}_text",
                    insert=(end[0], -1 * end[-1]),
                )
            )
        self._add_ipins(side="top", channel_map=channel_map)

    def render_connection_box(self, side, pinmap=None, channel_map=None, filename=None):
        """
        Render connections box in SVG format
        """
        self._setup_svg()
        self._add_origin_marker()
        pinmap = pinmap or (lambda x: x)
        if side == "top":
            self._add_top_connection_box(pinmap=pinmap, channel_map=channel_map)
        else:
            self._add_left_connection_box(pinmap=pinmap, channel_map=channel_map)
        if filename:
            margin = 200
            width = (
                (self.x_max_4 - self.x_min_4)
                if side == "top"
                else (self.x_max_4 - self.x_max_3)
            )
            height = (
                (self.y_max_4 - self.y_min_4)
                if side == "left"
                else (self.y_max_4 - self.y_max_3)
            )
            llx = self.x_min_4 - margin
            lly = self.y_max_4 + margin
            viewbox = (llx, -1 * lly, width + (2 * margin), height + (2 * margin))
            self.save(filename, viewbox=viewbox)

    def render_switch_pattern(self):
        """
        Create SVG object rendering all the switchs from switch box
        """
        self._setup_svg()
        self.add_partitions()
        self._add_origin_marker()
        self._add_channels()
        self._add_opins()
        # ====================================
        #         Create channels
        # ====================================
        self._add_left_channels()
        self._add_right_channels()
        self._add_top_channels()
        self._add_bottom_channels()
        # ====================================
        #         Added Input Pins
        # ====================================
        self._add_ipins(side="left")
        self._add_ipins(side="top")

    def _add_left_channels(self):
        """
        Creates horizontal channels
        """
        term_indx = 0
        for ele in self.chanx_l:
            chan = int(ele.attrib["index"])
            # Right to left channels
            if not chan in [int(e.attrib["index"]) for e in self.ft_left]:
                # Add connecting Vertical line
                x_line = self.x_min_1 - term_indx * self.scale - self.spacing
                y_line = self.y_min_0 - term_indx * self.scale - self.spacing
                self.dwgShapes.add(
                    shapes.Line(
                        start=(x_line, self.y_max_0),
                        end=(x_line, y_line),
                        marker_start=self.marker_red.get_funciri(),
                        marker_end=self.marker_terminate.get_funciri(),
                        class_="channel rl_chan",
                    )
                )
                # Add connecting horizontal line
                self.dwgShapes.add(
                    shapes.Line(
                        start=(self.x_max_0, y_line),
                        end=(self.x_min_4, y_line),
                        marker_start=self.marker_red.get_funciri(),
                        class_="channel rl_chan",
                    )
                )
                self._add_short_at(x_line, y_line)

                # Add Text
                self.dwgText.add(
                    Text(
                        ele.attrib["index"],
                        transform="scale(1,-1)",
                        class_="rl_text",
                        insert=(self.x_min_4, -1 * y_line),
                    )
                )

                self.chanx_l_out_map[int(ele.attrib["index"])] = y_line
                # Add Switches
                for switch in list(ele):
                    sw_type = switch.attrib["type"]
                    side = switch.attrib["side"]
                    index = int(switch.attrib["index"])
                    grid_side = switch.attrib.get("grid_side", "")
                    offset = index * self.scale
                    if sw_type == "CHANX":
                        self._add_switch_at(
                            x_line, self.x_min_0 + offset + self.spacing
                        )
                    elif sw_type == "CHANY":
                        self._add_switch_at(
                            self.y_min_0 + offset + self.spacing, y_line
                        )
                    elif sw_type == "OPIN":
                        self._add_switch_at(
                            self.x_min_2 - offset - self.spacing, y_line
                        )
                term_indx += 1

    def _add_right_channels(self):
        """
        Creates horizontal channels
        """
        term_indx = 0
        offset_0 = self.y_max_0 - self.spacing - self.scale
        for ele in self.chanx_r:
            chan = int(ele.attrib["index"])
            offset = offset_0 + int(ele.attrib["index"]) * self.scale
            # left to right channels
            if not chan in [int(e.attrib["index"]) for e in self.ft_right]:
                # Add connecting Vertical line
                x_line = self.x_max_1 + term_indx * self.scale + self.spacing
                y_line = self.y_max_0 + term_indx * self.scale + self.spacing
                self.dwgShapes.add(
                    shapes.Line(
                        start=(x_line, self.y_min_0),
                        end=(x_line, y_line),
                        marker_start=self.marker_blue.get_funciri(),
                        marker_end=self.marker_terminate.get_funciri(),
                        class_="channel lr_chan",
                    )
                )
                # Add connecting horizontal line
                self.dwgShapes.add(
                    shapes.Line(
                        start=(self.x_min_0, y_line),
                        end=(self.x_max_4, y_line),
                        marker_start=self.marker_terminate.get_funciri(),
                        marker_end=self.marker_blue.get_funciri(),
                        class_="channel lr_chan",
                    )
                )
                self._add_short_at(x_line, y_line)

                # Add Text
                self.dwgText.add(
                    Text(
                        ele.attrib["index"],
                        transform="scale(1,-1)",
                        class_="lr_text",
                        insert=(self.x_max_4, -1 * y_line),
                    )
                )
                self.chanx_r_out_map[int(ele.attrib["index"])] = x_line
                # Add Switches
                for switch in list(ele):
                    sw_type = switch.attrib["type"]
                    side = switch.attrib["side"]
                    index = int(switch.attrib["index"])
                    grid_side = switch.attrib.get("grid_side", "")
                    offset = index * self.scale
                    if sw_type == "CHANX":
                        self._add_switch_at(
                            x_line, self.x_min_0 + offset + self.spacing
                        )
                    elif sw_type == "CHANY":
                        self._add_switch_at(
                            self.y_min_0 + offset + self.spacing, y_line
                        )
                    elif sw_type == "OPIN":
                        self._add_switch_at(
                            self.x_max_2 + offset + self.spacing, y_line
                        )
                term_indx += 1

    def _add_top_channels(self):
        """
        Creates horizontal channels
        """
        term_indx = 0
        for ele in self.chany_t:
            chan = int(ele.attrib["index"])
            # left to right channels
            if not chan in [int(e.attrib["index"]) for e in self.ft_top]:
                # Add connecting Vertical line
                x_line = self.x_min_0 - term_indx * self.scale - self.spacing
                y_line = self.y_max_1 + term_indx * self.scale + self.spacing
                self.dwgShapes.add(
                    shapes.Line(
                        start=(x_line, self.y_min_0),
                        end=(x_line, self.y_max_4),
                        marker_start=self.marker_terminate.get_funciri(),
                        marker_end=self.marker_blue.get_funciri(),
                        class_="channel lr_chan",
                    )
                )
                # Add connecting horizontal line
                self.dwgShapes.add(
                    shapes.Line(
                        start=(x_line, y_line),
                        end=(self.x_max_0, y_line),
                        marker_start=self.marker_terminate.get_funciri(),
                        marker_end=self.marker_terminate.get_funciri(),
                        class_="channel lr_chan",
                    )
                )
                self._add_short_at(x_line, y_line)

                # Add Text
                self.dwgText.add(
                    Text(
                        ele.attrib["index"],
                        transform="scale(1,-1)",
                        class_="lr_text",
                        insert=(x_line, -1 * self.y_max_4),
                    )
                )

                # Add Switches
                for switch in list(ele):
                    sw_type = switch.attrib["type"]
                    side = switch.attrib["side"]
                    index = int(switch.attrib["index"])
                    grid_side = switch.attrib.get("grid_side", "")
                    offset = index * self.scale
                    if sw_type == "CHANX":
                        self._add_switch_at(
                            x_line, self.x_min_0 + offset + self.spacing
                        )
                    elif sw_type == "CHANY":
                        self._add_switch_at(
                            self.y_min_0 + offset + self.spacing, y_line
                        )
                    elif sw_type == "OPIN":
                        self._add_switch_at(
                            x_line, self.y_max_2 + offset + self.spacing
                        )
                term_indx += 1

    def _add_bottom_channels(self):
        """
        Creates horizontal channels
        """
        term_indx = 0
        for ele in self.chany_b:
            chan = int(ele.attrib["index"])
            # left to right channels
            if not chan in [int(e.attrib["index"]) for e in self.ft_bottom]:
                # Add connecting Vertical line
                x_line = self.x_max_0 + term_indx * self.scale + self.spacing
                y_line = self.y_min_1 - term_indx * self.scale - self.spacing
                self.dwgShapes.add(
                    shapes.Line(
                        start=(x_line, self.y_max_0),
                        end=(x_line, self.y_min_4),
                        marker_start=self.marker_terminate.get_funciri(),
                        marker_end=self.marker_blue.get_funciri(),
                        class_="channel lr_chan",
                    )
                )
                # Add connecting horizontal line
                self.dwgShapes.add(
                    shapes.Line(
                        start=(x_line, y_line),
                        end=(self.x_min_0, y_line),
                        marker_start=self.marker_terminate.get_funciri(),
                        marker_end=self.marker_terminate.get_funciri(),
                        class_="channel lr_chan",
                    )
                )
                self._add_short_at(x_line, y_line)

                # Add Text
                self.dwgText.add(
                    Text(
                        ele.attrib["index"],
                        transform="scale(1,-1)",
                        class_="lr_text",
                        insert=(x_line, -1 * self.y_min_4),
                    )
                )

                # Add Switches
                for switch in list(ele):
                    sw_type = switch.attrib["type"]
                    side = switch.attrib["side"]
                    index = int(switch.attrib["index"])
                    grid_side = switch.attrib.get("grid_side", "")
                    offset = index * self.scale
                    if sw_type == "CHANX":
                        self._add_switch_at(
                            x_line, self.x_min_0 + offset + self.spacing
                        )
                    elif sw_type == "CHANY":
                        self._add_switch_at(
                            self.y_min_0 + offset + self.spacing, y_line
                        )
                    elif sw_type == "OPIN":
                        self._add_switch_at(
                            x_line, self.y_min_2 - offset - self.spacing
                        )
                term_indx += 1

    def _add_channels(self):
        """
        Adds horizontal driver lines
        """
        pass_through = {
            "%s%d"
            % (ele[0].attrib["side"], int(ele[0].attrib["index"])): int(
                ele.attrib["index"]
            )
            for ele in self.ft_left + self.ft_right + self.ft_top + self.ft_bottom
        }
        visited_pins = list()
        for ele in self.chanx_drivers + self.chany_drivers:
            index = int(ele.attrib["index"])
            side = ele.attrib["side"]
            offset_x = self.x_min_0 + self.spacing + index * self.scale
            offset_y = self.y_min_0 + self.spacing + index * self.scale

            curr_pin = "%s%d" % (side, index)
            if curr_pin in visited_pins:
                continue
            # Create side specific parameters
            if side == "left":
                marker = self.marker_blue
                class_name = "lr"
                offset = offset_x
                start = (self.x_min_4, offset)
                end = (
                    self.x_max_4 if pass_through.get(curr_pin, None) else self.x_max_2,
                    offset,
                )
                if pass_through.get(curr_pin, None):
                    self.chanx_r_out_map[pass_through[curr_pin]] = offset
                self.chanx_l_out_map[index] = offset
            elif side == "right":
                marker = self.marker_red
                class_name = "rl"
                offset = offset_x
                start = (self.x_max_4, offset)
                end = (
                    self.x_min_4 if pass_through.get(curr_pin, None) else self.x_min_2,
                    offset,
                )
                if pass_through.get(curr_pin, None):
                    self.chanx_l_out_map[pass_through[curr_pin]] = offset
                self.chanx_r_out_map[index] = offset
            elif side == "top":
                marker = self.marker_blue
                class_name = "tb"
                offset = offset_y
                start = (offset, self.y_max_4)
                end = (
                    offset,
                    self.y_min_4 if pass_through.get(curr_pin, None) else self.y_min_2,
                )
                if pass_through.get(curr_pin, None):
                    self.chany_b_out_map[pass_through[curr_pin]] = offset
                self.chany_t_out_map[index] = offset
            elif side == "bottom":
                marker = self.marker_red
                class_name = "bt"
                offset = offset_y
                start = (offset, self.y_min_4)
                end = (
                    offset,
                    self.y_max_4 if pass_through.get(curr_pin, None) else self.y_max_2,
                )
                if pass_through.get(curr_pin, None):
                    self.chany_t_out_map[pass_through[curr_pin]] = offset
                self.chany_b_out_map[index] = offset

            self.dwgShapes.add(
                shapes.Line(
                    start=start,
                    end=end,
                    marker_start=marker.get_funciri(),
                    marker_end=marker.get_funciri(),
                    class_=f"channel {class_name}_chan",
                )
            )
            self.dwgText.add(
                Text(
                    index,
                    transform="scale(1,-1)",
                    class_=f"in_pin {class_name}_text",
                    insert=(start[0], -1 * start[-1]),
                )
            )

            if pass_through.get(curr_pin, None):
                self.dwgText.add(
                    Text(
                        pass_through[curr_pin],
                        transform="scale(1,-1)",
                        class_=f"out_pin {class_name}_text",
                        insert=(end[0], -1 * end[-1]),
                    )
                )
            visited_pins.append(curr_pin)

    def _add_ipins(self, side="left", channel_map=None):
        channel_map = channel_map or (lambda side, x: x)
        if side == "left":
            ipins = self.ipin_t + self.ipin_b
        else:
            ipins = self.ipin_r + self.ipin_l
        for ele in ipins:
            index = int(ele.attrib["index"])
            side = ele.attrib["side"]
            marker = self.marker_red
            offset = self.spacing + channel_map(side, index) * self.scale

            if side in "top":
                start = (self.x_min_3 - offset, self.y_min_2)
                end = (self.x_min_3 - offset, self.y_max_3)
            elif side in "bottom":
                start = (self.x_min_4 + offset, self.y_max_2)
                end = (self.x_min_4 + offset, self.y_min_3)
            elif side in "left":
                start = (self.x_max_2, self.y_max_3 + offset)
                end = (self.x_min_3, self.y_max_3 + offset)
            elif side in "right":
                start = (self.x_min_2, self.y_max_4 - offset)
                end = (self.x_max_3, self.y_max_4 - offset)

            self.dwgShapes.add(
                shapes.Line(
                    start=start,
                    end=end,
                    marker_start=marker.get_funciri(),
                    marker_end=marker.get_funciri(),
                    class_="channel",
                )
            )
            self.dwgText.add(
                Text(
                    index,
                    transform="scale(1,-1)",
                    class_=f"OPIN",
                    insert=(end[0], -1 * end[-1]),
                )
            )

            # Add Switches
            for switch in list(ele):
                index = int(switch.attrib["index"])
                offset = (
                    self.chanx_l_out_map[index]
                    if side in ["top", "bottom"]
                    else self.chany_t_out_map[index]
                )
                if side in ["top", "bottom"]:
                    self._add_switch_at(start[0], offset)
                elif side in ["left", "right"]:
                    self._add_switch_at(offset, start[1])

    def _add_opins(self):

        for ele in self.opin_l + self.opin_r + self.opin_t + self.opin_b:
            index = int(ele.attrib["index"])
            side = ele.attrib["side"]
            grid_side = ele.attrib["grid_side"]

            offset = self.spacing + (index) * self.scale

            if side in ["left", "right"]:
                start = (
                    self.x_min_2 - offset if side == "left" else self.x_max_2 + offset,
                    self.y_min_4 if grid_side == "top" else self.y_min_1,
                )
                end = (
                    self.x_min_2 - offset if side == "left" else self.x_max_2 + offset,
                    self.y_max_1 if grid_side == "top" else self.y_max_4,
                )
                if grid_side == "bottom":
                    start, end = end, start
                marker = self.marker_red
            elif side in ["top", "bottom"]:
                start = (
                    self.x_max_4 if grid_side == "left" else self.x_min_4,
                    self.y_min_2 - offset
                    if side == "bottom"
                    else self.y_max_2 + offset,
                )
                end = (
                    self.x_min_2 if grid_side == "left" else self.x_max_2,
                    self.y_min_2 - offset
                    if side == "bottom"
                    else self.y_max_2 + offset,
                )
                marker = self.marker_red
            self.dwgShapes.add(
                shapes.Line(
                    start=start,
                    end=end,
                    marker_start=marker.get_funciri(),
                    marker_end=marker.get_funciri(),
                    class_="channel",
                )
            )
            self.dwgText.add(
                Text(
                    index,
                    transform="scale(1,-1)",
                    class_=f"OPIN",
                    insert=(start[0], -1 * start[-1]),
                )
            )

    def _add_switch_at(self, x, y):
        self.switches.add(shapes.Circle(center=(x, y), r=10, class_="switch"))

    def _add_short_at(self, x, y):
        self.switches.add(shapes.Circle(center=(x, y), r=10, class_="short"))

    def add_partitions(self):
        """
        This function creates initial floorplan for rendering switch boxes
            ┌───────────────────────────────┐
            │                               │
            │ ┌───────────────────────────┐ │
            │ │                           │ │
            │ │  ┌──────────────────────┐ │ │
            │ │  │                      │ │ │
            │ │  │ ┌──────────────────┐ │ │ │
            │ │  │ │                  │ │ │ │
            │ │  │ │Channel_CrossOver │ │ │ │
            │ │  │ │                  │ │ │ │
            │ │  │ └──────────────────┘ │ │ │
            │ │  │   Driver_Channels_1  │ │ │
            │ │  └──────────────────────┘ │ │
            │ │      Driver_Channels_2    │ │
            │ └───────────────────────────┘ │
            │            OPINs_1            │
            └───────────────────────────────┘

        ``Channel_CrossOver`` and ``Driver_Channels_1`` section always exists.
        ``Driver_Channels_2`` on specific site can be skipped if there are no
        channels drivers in that direction
        """
        min_terminating = min(
            self.ft_left_len, self.ft_right_len, self.ft_top_len, self.ft_bottom_len
        )

        # Width, Height Calculation for
        width = self.chanx_len * self.scale + 2 * self.spacing
        height = self.chany_len * self.scale + 2 * self.spacing

        # width1 height1 calculation
        width1 = width + 2 * (self.chanx_l_len - min_terminating) * self.scale
        width1 += 2 * self.spacing
        height1 = height + 2 * (self.chany_t_len - min_terminating) * self.scale
        height1 += 2 * self.spacing

        # width1 height1 calculation
        width2 = (
            width1
            + 2 * (self.chanx_l_len - min_terminating) * self.scale
            + 2 * self.spacing
        )
        height2 = (
            height1
            + 2 * (self.chany_t_len - min_terminating) * self.scale
            + 2 * self.spacing
        )

        # width1 height1 calculation
        width3 = width2 + 2 * (self.chanx_l_len - min_terminating) * self.scale
        width3 += 2 * self.spacing
        height3 = height2 + 2 * (self.chany_t_len - min_terminating) * self.scale
        height3 += 2 * self.spacing

        # width1 height1 calculation
        width4 = width3 + 2 * (self.ipin_l_len + self.ipin_r_len) * self.scale
        width4 += 4 * self.spacing
        height4 = height3 + 2 * (self.ipin_t_len + self.ipin_b_len) * self.scale
        height4 += 4 * self.spacing

        insert_pt = -0.5 * (width4 - width), -0.5 * (height4 - height)
        self.x_min_4, self.y_min_4 = insert_pt
        self.x_min_4 += (self.ipin_r_len - self.ipin_l_len) * self.scale
        self.y_min_4 += (self.ipin_t_len - self.ipin_b_len) * self.scale
        self.x_max_4, self.y_max_4 = self.x_min_4 + width4, self.y_min_4 + height4

        insert_pt = -0.5 * (width3 - width), -0.5 * (height3 - height)
        self.x_min_3, self.y_min_3 = insert_pt
        self.x_max_3, self.y_max_3 = self.x_min_3 + width3, self.y_min_3 + height3

        insert_pt = -0.5 * (width2 - width), -0.5 * (height2 - height)
        self.x_min_2, self.y_min_2 = insert_pt
        self.x_max_2, self.y_max_2 = self.x_min_2 + width2, self.y_min_2 + height2

        insert_pt = -0.5 * (width1 - width), -0.5 * (height1 - height)
        self.x_min_1, self.y_min_1 = insert_pt
        self.x_max_1, self.y_max_1 = self.x_min_1 + width1, self.y_min_1 + height1

        self.x_min_0, self.y_min_0 = 0, 0
        self.x_max_0, self.y_max_0 = width, height

        self.region.add(
            shapes.Rect(
                insert=(self.x_min_3, self.y_min_4),
                size=(width3, height4),
                class_="boundry",
            )
        )
        self.region.add(
            shapes.Rect(
                insert=(self.x_min_4, self.y_min_3),
                size=(width4, height3),
                class_="boundry",
            )
        )
        self.region.add(
            shapes.Rect(
                insert=(self.x_min_3, self.y_min_3),
                size=(width3, height3),
                class_="region4",
            )
        )
        self.region.add(
            shapes.Rect(
                insert=(self.x_min_2, self.y_min_2),
                size=(width2, height2),
                class_="region3",
            )
        )
        self.region.add(
            shapes.Rect(
                insert=(self.x_min_1, self.y_min_1),
                size=(width1, height1),
                class_="region2",
            )
        )
        self.region.add(
            shapes.Rect(insert=(0, 0), size=(width, height), class_="region1")
        )

    def _add_origin_marker(self):
        self.dwgbg.add(
            shapes.Line(
                start=(0, 1 * self.scale), end=(0, -1 * self.scale), class_="origin"
            )
        )
        self.dwgbg.add(
            shapes.Line(
                start=(1 * self.scale, 0), end=(-1 * self.scale, 0), class_="origin"
            )
        )

    def _create_arrowhead(self, hex_color):
        DRMarker = self.dwg.marker(
            refX="30",
            refY="30",
            viewBox="0 0 120 120",
            markerUnits="strokeWidth",
            markerWidth="8",
            markerHeight="10",
            orient="auto",
        )
        DRMarker.add(self.dwg.path(d="M 0 0 L 60 30 L 0 60 z", fill=hex_color))
        self.dwg.defs.add(DRMarker)
        return DRMarker

    def _create_termination(self, hex_color):
        DRMarker = self.dwg.marker(
            refX="0",
            refY="0",
            viewBox="-10 -30 20 60",
            markerUnits="strokeWidth",
            markerWidth="4",
            markerHeight="10",
            orient="auto",
        )
        DRMarker.add(
            shapes.Rect(insert=(-5, -15), height="30", width="10", fill=hex_color)
        )
        self.dwg.defs.add(DRMarker)
        return DRMarker

    def _add_stylehseet(self):
        """
        Adds custom stylesheet to the SVG image
        """
        self.dwg.defs.add(
            self.dwg.style(
                """
                text{font-family: LATO; font-weight: 800; font-size: 25px;}
                svg{outline: 1px solid grey; outline-offset: -2px;}
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
                .OPIN{fill: green;}
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
                .in_pin{fill: blue !important;}
                .out_pin{fill: red !important;}
            """
            )
        )

    def _setup_svg(self):
        # Variables for SVG rendering
        self.dwg = Drawing()
        self.dwgbg = self.dwg.add(Group(id="bg"))
        self.region = self.dwg.add(Group(id="region", transform="scale(1,-1)"))
        self.core = self.dwg.add(Group(id="mainframe"))
        self.dwgShapes = self.core.add(Group(id="mainShapes", transform="scale(1,-1)"))
        self.switches = self.core.add(Group(id="switches", transform="scale(1,-1)"))
        self.dwgText = self.core.add(Group(id="mainText", transform="scale(1,-1)"))
        self.marker_red = self._create_arrowhead("red")
        self.marker_green = self._create_arrowhead("green")
        self.marker_blue = self._create_arrowhead("blue")
        self.marker_terminate = self._create_termination("blue")
