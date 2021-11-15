import xml.etree.ElementTree as ET
from svgwrite import Drawing
from svgwrite import shapes
from svgwrite.container import Group
import logging

logger = logging.getLogger('spydrnet_logs')


class RoutingRender:
    def __init__(self, name, gsb_xml) -> None:
        self.name = name
        self.scale = 40
        self.spacing = self.scale*1
        self.gsb_xml = gsb_xml
        self.root = ET.parse(self.gsb_xml).getroot()
        self.extract_info()
        # Variables for SVG rendering
        self.dwg = Drawing()
        self.dwgbg = self.dwg.add(Group(id="bg"))
        self.core = self.dwg.add(Group(id="mainframe"))
        self.dwgText = self.core.add(Group(id="mainText",
                                           transform="scale(1,-1)"))
        self.dwgShapes = self.core.add(Group(id="mainShapes",
                                             transform="scale(1,-1)"))

    def update_dimentions(self, scale, spacing):
        """
        Updates scale and spacing dimensions
        """
        self.scale = int(scale) or self.scale
        self.spacing = int(spacing) or self.spacing

    def extract_info(self):
        """
        Extracts insformation from provided general switch box file
        """
        root = self.root
        self.chanx_l = root.findall("CHANX[@side='left']")
        self.chanx_l_len = len(self.chanx_l)
        self.chanx_r = root.findall("CHANX[@side='right']")
        self.chanx_r_len = len(self.chanx_r)
        self.chanx = self.chanx_l + self.chanx_r
        self.chanx_len = self.chanx_l_len + self.chanx_r_len

        self.chany_t = root.findall("CHANY[@side='top']")
        self.chany_t_len = len(self.chany_t)
        self.chany_b = root.findall("CHANY[@side='bottom']")
        self.chany_b_len = len(self.chany_b)
        self.chany = self.chany_t + self.chany_b
        self.chany_len = self.chany_t_len + self.chany_b_len

        self.ipin_l = root.findall("IPIN[@side='left']")
        self.ipin_l_len = len(self.ipin_l)
        self.ipin_r = root.findall("IPIN[@side='right']")
        self.ipin_r_len = len(self.ipin_r)
        self.ipin_t = root.findall("IPIN[@side='top']")
        self.ipin_t_len = len(self.ipin_t)
        self.ipin_b = root.findall("IPIN[@side='bottom']")
        self.ipin_b_len = len(self.ipin_b)

        # Left side OPins
        self.opin_l = root.findall(
            "*/driver_node[@type='OPIN'][@side='left']")
        self.opin_l_len = max([int(i.attrib["index"])
                               for i in self.opin_l] + [-1])+1
        self.opin_l_t = [
            e for e in self.opin_l if e.attrib["grid_side"] == "top"]
        self.opin_l_t_len = len(self.opin_l_t)
        self.opin_l_b = [
            e for e in self.opin_l if e.attrib["grid_side"] == "bottom"]
        self.opin_l_b_len = len(self.opin_l_b)

        # Right side OPins
        self.opin_r = root.findall(
            "*/driver_node[@type='OPIN'][@side='right']")
        self.opin_r_len = max([int(i.attrib["index"])
                               for i in self.opin_r] + [-1])+1
        self.opin_r_t = [
            e for e in self.opin_r if e.attrib["grid_side"] == "top"]
        self.opin_r_t_len = len(self.opin_r_t)
        self.opin_r_b = [
            e for e in self.opin_r if e.attrib["grid_side"] == "bottom"]
        self.opin_r_b_len = len(self.opin_r_b)

        # Top side OPins
        self.opin_t = root.findall("*/driver_node[@type='OPIN'][@side='top']")
        self.opin_t_len = max([int(i.attrib["index"])
                               for i in self.opin_t] + [-1])+1

        self.opin_t_l = [
            e for e in self.opin_t if e.attrib["grid_side"] == "left"]
        self.opin_t_l_len = len(self.opin_t_l)
        self.opin_t_r = [
            e for e in self.opin_t if e.attrib["grid_side"] == "right"]
        self.opin_t_r_len = len(self.opin_t_r)

        # bottom side OPins
        self.opin_b = root.findall(
            "*/driver_node[@type='OPIN'][@side='bottom']")
        self.opin_b_len = max([int(i.attrib["index"])
                               for i in self.opin_b] + [-1])+1
        self.opin_b_l = [
            e for e in self.opin_b if e.attrib["grid_side"] == "left"]
        self.opin_b_l_len = len(self.opin_b_l)
        self.opin_b_r = [
            e for e in self.opin_b if e.attrib["grid_side"] == "right"]
        self.opin_b_r_len = len(self.opin_b_r)

    @staticmethod
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

    def _add_channels(self):
        """
        Add channels in SVG image
        """
        marker_red = self._create_arrowhead('red')
        marker_green = self._create_arrowhead('green')

        x_min, x_max = 0, (self.chanx_len+1)*self.scale
        y_min, y_max = 0, (self.chany_len+1)*self.scale
        if self.ipin_t+self.ipin_b:
            x_min -= 2*self.spacing
            x_min -= (self.ipin_t+self.ipin_b)*self.scale
        if self.ipin_l+self.ipin_r:
            y_max += 2*self.spacing
            y_max += (self.ipin_l_len+self.ipin_r_len)*self.scale
        if self.opin_t_l_len+self.opin_t_r_len:
            y_max += 2*self.spacing
            y_max += self.opin_t_l_len+self.opin_t_r_len*self.scale

        logger.debug("%4d %4d %4d %4d ", x_min, x_max, y_min, y_max)
        for chan in range(1, 1+self.chanx_len):
            self.dwgShapes.add(shapes.Line(start=(x_min, chan*self.scale),
                                           end=(x_max, chan*self.scale), class_="channel"))
        for chan in range(1, 1+self.chany_len):
            self.dwgShapes.add(shapes.Line(start=(chan*self.scale, y_min),
                                           end=(chan*self.scale, y_max), class_="channel"))
        offset_y = (1+self.chany_len)*self.scale
        if self.ipin_l:
            offset_y += self.spacing
            for pins in range(self.ipin_l_len):
                self.dwgShapes.add(shapes.Line(
                    start=(x_max-self.scale, offset_y+(pins*self.scale)),
                    end=(x_min, offset_y+(pins*self.scale)),
                    marker_end=marker_red.get_funciri(),
                    class_="inpin"))
            offset_y += (self.ipin_l_len*self.scale)
        if self.opin_t_l_len:
            offset_y += self.spacing
            for pins, _ in enumerate(self.opin_t_l):
                self.dwgShapes.add(shapes.Line(
                    end=(x_max-self.scale, offset_y+(pins*self.scale)),
                    start=(x_min, offset_y+(pins*self.scale)),
                    marker_start=marker_green.get_funciri(),
                    class_="outpin"))
            offset_y += (self.opin_t_l_len*self.scale)
        if self.opin_t_r_len:
            offset_y += self.spacing
            for pins, _ in enumerate(self.opin_t_r):
                self.dwgShapes.add(shapes.Line(
                    start=(x_max, offset_y+(pins*self.scale)),
                    end=(x_min+self.scale, offset_y+(pins*self.scale)),
                    marker_start=marker_green.get_funciri(),
                    class_="outpin"))
            offset_y += (self.opin_t_r_len*self.scale)
        if self.ipin_r:
            offset_y += self.spacing
            for pins in range(self.ipin_l_len):
                self.dwgShapes.add(shapes.Line(
                    start=(x_min+self.scale, offset_y+(pins*self.scale)),
                    end=(x_max, offset_y+(pins*self.scale)),
                    marker_end=marker_red.get_funciri(),
                    class_="inpin"))

    def _add_switches(self):
        pass

    def render_switch_pattern(self):
        # Create groups in SVG image
        self._add_origin_marker()
        self._add_channels()

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
        viewbox = -0.5*width, -4.5*height, 2*width, 5*height
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

    def add_stylehseet(self):
        '''
        Adds custom stylesheet to the SVG image
        '''
        self.dwg.defs.add(self.dwg.style("""
                text{font-family: LATO; font-weight: 800; font-size: 5px;}
                .module_boundary{fill:#f4f0e6}
                .origin{stroke: red;stroke-width: 1;}
                .channel{stroke: grey;stroke-width: 4;}
                .inpin{stroke: red;stroke-width: 4;}
                .outpin{stroke: green;stroke-width: 4;}
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
