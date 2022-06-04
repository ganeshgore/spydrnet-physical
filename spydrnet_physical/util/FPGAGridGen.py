# ##############################################################################
# Tool: OpenFPGA-Physical
# Script: FPGAGridGen.py
################################################################################
"""
FPGAGridGen
-------------

This scripts read the layout section of the VPR architecture file and
create a 2D matrix of the FPGA grid.
"""

import argparse
import logging
import math

import svgwrite
from svgwrite.container import Group
from spydrnet_physical.util.openfpga_arch import OpenFPGA_Arch
from spydrnet_physical.ir.shaping_utils import shaping_utils

logger = logging.getLogger("spydrnet_logs")


def formatter(prog):
    return argparse.HelpFormatter(prog, max_help_position=60)


help_msg = {"design_name": "Design name, Generally in FPGAxxxx_xxxx format"}


UP_ARROW = chr(8593)  # ↑
RIGHT_ARROW = chr(8594)  # →


def main() -> None:
    """
    Execute when this file called as a script
    """
    args = parse_argument()
    grid = FPGAGridGen(args.design_name, args.arch_file,
                       args.layout, args.release_root)
    grid.enumerate_grid()
    grid.print_grid()


def parse_argument() -> argparse.Namespace:
    """
    Parse commnad line arguement
    """
    parser = argparse.ArgumentParser(formatter_class=formatter)
    parser.add_argument(
        "--design_name", help="Design name, Generally in FPGAxxxx_xxxx format"
    )
    parser.add_argument(
        "--arch_file",
        type=str,
        help="VPR architecture file, It should atleast contain on fixed_layout",
    )
    parser.add_argument(
        "--layout",
        type=str,
        default=None,
        help="Specific layout name to render from the provided XML file",
    )
    parser.add_argument(
        "--release_root",
        type=str,
        default=None,
        help="Location to store pickled object of the 2D FPGA grid matrix",
    )
    return parser.parse_args()


CSS_STYLE = '''
.boundary{stroke:grey; fill:none; stroke-width:0.2}
text{font-family: Lato; font-size:1.2px;}
symbol[id="cbx"] * { fill:#d9d9f3; stroke-width:0.1; stroke:black;}
symbol[id="cby"] * { fill:#a8d0db; stroke-width:0.1; stroke:black;}
symbol[id*="sb"] * { fill:#ceefe4; stroke-width:0.1; stroke:black;}
rect[class="lb"] { fill:#f4f0e6; stroke-width:0.1; stroke:black; }
'''


class FPGAGridGen:
    """This class generates the 2D lsit of the FPGA grid,
    based on the provided VPR architecture file.
    This class generate two grid

    **self.grid** : This is logic blocks grid including IOs (NxM)

    **self.full_grid** : This is complete grid with a logic and routing blocks (N-1)x(M-1)

    Where NxM is width and height of the FPGA, including IO

    **Example execution**:

    .. code-block:: bash

        python FPGAGridGen.py --design_name FPGA66_flex --layout dp
                --arch_file example_files/vpr_arch_render_demo.xml

    **Expected Output**:

    .. code-block:: text

          EMPTY     io_top     io_top     io_top     io_top     io_top     io_top     EMPTY
         io_left     clb        clb        clb        clb        clb        clb      io_right
         io_left     clb        clb        clb        clb        clb        clb      io_right
         io_left    ram9k        →        ram9k        →        ram9k        →       io_right
         io_left     clb        clb        clb        clb        clb        clb      io_right
         io_left     dsp         →         dsp         →         dsp         →       io_right
         io_left     clb        clb        clb        clb        clb        clb      io_right
          EMPTY   io_bottom  io_bottom  io_bottom  io_bottom  io_bottom  io_bottom    EMPTY

    """

    design_name = ""
    """str: Design name"""

    grid = None
    """list(list): 2-Dimentional grid for logic blocks grid[0] bottom most row"""

    full_grid = None
    """list(list): 2-Dimentional grid for logic block and routing elements"""

    fpga_arch = None
    """OpenFPGA_Arch: Instance of OpenFPGA_Arch class"""

    def __init__(self, design_name, arch_file, layout, release_root=None) -> None:
        """
        Initiliaze the FPGA grid generator class

        args:
            design_name  (str): Design name
            arch_file    (str): Path to architecture file
            layout       (str): Fixed layout selection from architecture file
            release_root (str): Directory to output binaries
        """
        self.design_name = design_name
        self.release_root = release_root
        self.fpga_arch = OpenFPGA_Arch(arch_file, None, layout=layout)
        # Parse values
        self.clb = None
        self.root = self.fpga_arch.vpr_arch
        self.layout = self.root.find(f".//fixed_layout[@name='{layout}']")
        assert layout, "Specified layout not found in the architecture file"
        self.width = self.fpga_arch.width
        self.height = self.fpga_arch.height
        self.grid = [[0 for _ in range(self.width)]
                     for _ in range(self.height)]
        self.full_grid = [
            [0 for _ in range(2 * (self.width) - 1)]
            for _ in range(2 * (self.height) - 1)
        ]
        self.RIGHT_ARROW = RIGHT_ARROW
        self.UP_ARROW = UP_ARROW

    def get_width(self):
        """Get width of FPGA"""
        return self.width - 2

    def get_height(self):
        """Get height of FPGA"""
        return self.height - 2

    def print_grid(self, grid="grid"):
        """
        Prints logic block grid
        """
        grid = self.grid if grid == "grid" else self.full_grid
        output = ""
        for row in grid[::-1]:
            for y in row:
                output += f"{y:^10} "
            output += "\n"
        print(output)
        return output

    def get_block(self, x, y):
        """
        This method returns the module present in specific x and y
        cordinate. The return value contains module name and
        adjusted X and Y cordianates

        the cordiante origin starts from the first element of top most list
        and first element of the first element of list of list
        """
        value = self.grid[y][x]
        while value in [self.RIGHT_ARROW, self.UP_ARROW]:
            if value == self.UP_ARROW:
                y -= 1
            if value == self.RIGHT_ARROW:
                x -= 1
            if x < 0 and y < 0:
                x, y = 0, 0
                break
            value = self.grid[y][x]
        return value, x, y

    def get_top_instance(self, x, y):
        """
        This method generates the grid instance information given the
        cordinate points
        """
        grid_lbl = self.get_block(int(x / 2), int(y / 2))
        if y == 0 or ((self.height * 2) - 2 == y):
            return (
                "EMPTY"
                if ((x % 2) or grid_lbl[0] == "EMPTY")
                else ("%s_%d__%d_" % grid_lbl)
            )
        if x == 0 or ((self.width * 2) - 2 == x):
            return (
                "EMPTY"
                if ((y % 2) or grid_lbl[0] == "EMPTY")
                else ("%s_%d__%d_" % grid_lbl)
            )
        if (x % 2 == 0) and (y % 2 == 0):
            return "%s_%d__%d_" % grid_lbl
        module = {
            True: "sb",
            (x % 2 == 1) and (y % 2 == 0): "cby",
            (x % 2 == 0) and (y % 2 == 1): "cbx",
        }[True]
        xi, yi = int(x / 2), int(y / 2)
        # TODO : Square modules are not supported yet
        if module == "sb":
            if (self.get_block(xi + 1, yi + 1) == self.get_block(xi + 1, yi)) and (
                self.get_block(xi + 1, yi + 1) == self.get_block(xi, yi + 1)
            ):
                grid_lbl = self.get_block(xi, yi)
                return "%s_%d__%d_" % grid_lbl
        if module == "cby":
            if self.get_block(xi, yi) == self.get_block(xi + 1, yi):
                grid_lbl = self.get_block(xi, yi)
                return "%s_%d__%d_" % grid_lbl
        if module == "cbx":
            if self.grid[yi + 1][xi] in [self.UP_ARROW]:
                grid_lbl = self.get_block(xi, yi)
                return "%s_%d__%d_" % grid_lbl
        return f"{module}_{int(x/2)}__{int(y/2)}_"

    @staticmethod
    def _resolve_string(ele, param, default, variables={}):
        """
        Parses the startx, starty, repeatx and repeaty variables to integer

        Variables are passed in `variables` variable,
        generally ``W`` and ``H`` values
        """
        val = ele.attrib.get(param, str(default))
        if val.isnumeric():
            return int(val)
        else:
            val = val.replace("W", "{W}")
            val = val.replace("H", "{H}")
            return int(eval(val.format(**variables)))

    def _set_value(self, x, y, value, width=1, height=1):
        """
        Sets value in the FPGA grid
        """
        try:
            for xi in range(0, width):
                for yi in range(0, height):
                    self.grid[y + yi][x + xi] = (
                        value
                        if (xi, yi) == (0, 0)
                        else RIGHT_ARROW
                        if yi == 0
                        else UP_ARROW
                    )
            return 1
        except IndexError:
            logger.warning("Trying to set grid location (%s %s)", x, y)
            return 0

    def add_fill(self, ele):
        """
        Fill the grid with given element

        Args:
            ele (ET): Accepts Element Tree (element) as a input

        """
        ele_type = ele.attrib["type"]
        self.clb = ele_type
        ele_w, ele_h = self.fpga_arch.tiles[ele_type]
        for x in range(0, self.width, ele_w):
            for y in range(0, self.height, ele_h):
                self._set_value(x, y, ele_type, ele_w, ele_h)

    def add_perimeter(self, ele):
        """
        Add given element on the periphery of the grid

        Args:
            ele (ET): Accepts Element Tree (element) as a input

        """
        ele_type = ele.attrib["type"]
        ele_w, ele_h = self.fpga_arch.tiles[ele_type]

        for y in [0, self.fpga_arch.height - 1]:
            for x in range(0, self.fpga_arch.width):
                self._set_value(x, y, ele_type, ele_w, ele_h)
        for x in [0, self.fpga_arch.width - 1]:
            for y in range(0, self.fpga_arch.height):
                self._set_value(x, y, ele_type, ele_w, ele_h)

    def add_corners(self, ele):
        """
        Add given element on the corners of the grid

        Args:
            ele (ET): Accepts Element Tree (element) as a input

        """
        ele_type = ele.attrib["type"]
        ele_w, ele_h = self.fpga_arch.tiles[ele_type]
        self._set_value(0, 0, ele_type)
        self._set_value(0, self.height - 1, ele_type)
        self._set_value(self.width - 1, 0, ele_type)
        self._set_value(self.width - 1, self.height -
                        1, ele_type, ele_w, ele_h)

    def add_single(self, ele):
        """
        Add given element to the specifica location of the grid

        Args:
            ele (ET): Accepts Element Tree (element) as a input
            ele.x (int): x locations to insert
            ele.y (int): y locations to insert

        """
        ele_type = ele.attrib["type"]
        ele_w, ele_h = self.fpga_arch.tiles[ele_type]
        x = int(ele.attrib["x"])
        y = int(ele.attrib["y"])
        self._set_value(x - 1, y - 1, ele_type, ele_w, ele_h)

    def add_row(self, ele):
        ele_type = ele.attrib["type"]
        ele_w, ele_h = self.fpga_arch.tiles[ele_type]
        var = {
            "w": ele_w,
            "h": ele_h,
            "W": self.fpga_arch.width,
            "H": self.fpga_arch.height,
        }
        startx = self._resolve_string(ele, "startx", ele_w, var)
        incrx = self._resolve_string(ele, "incrx", ele_w, var)
        starty = self._resolve_string(ele, "starty", 1, var)
        repy = self._resolve_string(ele, "repeaty", self.fpga_arch.height, var)
        for x in range(startx, self.width, incrx):
            for y in range(starty, self.height, repy):
                self._set_value(x, y, ele_type, ele_w, ele_h)

    def add_col(self, ele):
        ele_type = ele.attrib["type"]
        ele_w, ele_h = self.fpga_arch.tiles[ele_type]
        var = {
            "w": ele_w,
            "h": ele_h,
            "W": self.fpga_arch.width,
            "H": self.fpga_arch.height,
        }
        startx = self._resolve_string(ele, "startx", 0, var)
        repeatx = self._resolve_string(
            ele, "repeatx", self.fpga_arch.width, var)
        starty = self._resolve_string(ele, "starty", 1, var)
        incry = self._resolve_string(ele, "incry", ele_h, var)
        for x in range(startx, self.width, repeatx):
            for y in range(starty, self.height, incry):
                self._set_value(x, y, ele_type, ele_w, ele_h)

    def add_region(self, ele):
        ele_type = ele.attrib["type"]
        ele_w, ele_h = self.fpga_arch.tiles[ele_type]
        var = {
            "w": ele_w,
            "h": ele_h,
            "W": self.fpga_arch.width,
            "H": self.fpga_arch.height,
        }
        startx = self._resolve_string(ele, "startx", 0, var)
        endx = self._resolve_string(ele, "endx", self.fpga_arch.width, var)
        incrx = self._resolve_string(ele, "incrx", ele_w, var)
        repeatx = self._resolve_string(
            ele, "repeatx", self.fpga_arch.width, var)
        starty = self._resolve_string(ele, "starty", 0, var)
        endy = self._resolve_string(ele, "endy", self.fpga_arch.height, var)
        incry = self._resolve_string(ele, "incry", ele_h, var)
        repeaty = self._resolve_string(
            ele, "repeaty", self.fpga_arch.height, var)

        for xstep in range(0, self.width, repeatx):
            for ystep in range(0, self.height, repeaty):
                for x in range(startx, endx, incrx):
                    for y in range(starty, endy, incry):
                        self._set_value(xstep + x, ystep + y,
                                        ele_type, ele_w, ele_h)

    def enumerate_grid(self):
        """
        Enumerates the FPGA grid

        Returns:
           (list(list(str))): Returns 2D grid
        """
        for element in sorted(self.layout, key=lambda x: int(x.attrib["priority"])):
            tag = element.tag.lower()
            if tag == "fill":
                logger.debug("Adding Fill")
                self.add_fill(element)
            elif tag == "corners":
                logger.debug("Adding Corners")
                self.add_corners(element)
            elif tag == "single":
                logger.debug("Adding Single")
                self.add_single(element)
            elif tag == "perimeter":
                logger.debug("Adding Perimeter")
                self.add_perimeter(element)
            elif tag == "row":
                logger.debug("Adding Row")
                self.add_row(element)
            elif tag == "col":
                logger.debug("Adding Col")
                self.add_col(element)
            elif tag == "region":
                logger.debug("Adding region")
                self.add_region(element)
            else:
                continue
        self._enumerate_full_grid()
        return self.grid

    def _enumerate_full_grid(self):
        arrows = (self.RIGHT_ARROW, self.UP_ARROW)
        for y in range((self.height*2) - 1):
            for x in range((self.width*2) - 1):
                grid_lbl = self.grid[math.floor(y/2)][math.floor(x/2)]
                grid_lbl_r = self.grid[math.floor(y/2)][math.floor(x/2)+1] \
                    if (x+2) < self.width*2 else None
                grid_lbl_l = self.grid[math.floor(y/2)][math.floor(x/2)] \
                    if x > 0 else None
                grid_lbl_t = self.grid[math.floor(y/2)+1][math.floor(x/2)] \
                    if (y+2) < self.height*2 else None
                grid_lbl_b = self.grid[math.floor(y/2)][math.floor(x/2)] \
                    if y > 0 else None
                # print(
                #     f"{x:4} {y:4} {str(grid_lbl):10} " +
                #     f"{str(grid_lbl_t):10} {str(grid_lbl_b):10} " +
                #     f"{str(grid_lbl_l):10} {str(grid_lbl_r):10}")
                module = {
                    True: self.UP_ARROW if ((grid_lbl_r in arrows) and (grid_lbl_t in arrows)) else "sb",
                    (x % 2 == 1) and (y % 2 == 0): grid_lbl_r if (grid_lbl_r == self.RIGHT_ARROW) else self.UP_ARROW
                    if ((grid_lbl_l == self.UP_ARROW) and (grid_lbl_r == self.UP_ARROW)) else "cbx",
                    (x % 2 == 0) and (y % 2 == 1): grid_lbl_t if (grid_lbl_t == self.UP_ARROW) else "cby",
                    (x % 2 == 0) and (y % 2 == 0): grid_lbl,
                    (x == 0) and (y % 2 == 1): "EMPTY",
                    (x == ((self.width-1)*2)) and (y % 2 == 1): "EMPTY",
                    (x % 2 == 1) and (y == 0): "EMPTY",
                    (x % 2 == 1) and (y == ((self.height-1)*2)): "EMPTY",
                }[True]
                self.full_grid[y][x] = module

    def validate_grid(self):
        """
        Checks for the correctness of the grid
            - if right and up arrows are placed correctly in the grid
            - if the boundry blocks has correct grid value
        """
        left_edge = [row[0] for row in self.grid]
        bottom_edge = self.grid[0]
        if RIGHT_ARROW in left_edge:
            raise ValueError("Found right arrow on left edge")

        if UP_ARROW in bottom_edge:
            raise ValueError("Found up arrow on bottom edge")

    @staticmethod
    def _default_shaping_param():
        '''
        Returns default shaping parameters for rendering
        '''
        return {"grid": [10, 5],
                "clb": [10, 10],
                "cbx": [8.5, 2.5, 2, 0],
                "cby": [2.5, 8.5, 0, 2],
                "sb": [2.5, 2, 2, 2.5, 2, 2, -2, -2]}

    def add_render_symbols(self, dwg, params):
        sym_map = {}
        rect_symbols = {
            "cbx": params["cbx"],
            "cby": params["cby"],
        }
        for tile, size in self.fpga_arch.pb_types.items():
            rect_symbols[tile] = [(12.5*pt if pt == 1
                                  else (15*(pt-1)+12.5)) for pt in size] + [0, 0]
        for module, dims in rect_symbols.items():
            symbol = dwg.symbol(id=module)
            class_tag = 'routing' if module in ('cbx', 'cby') else "lb"
            symbol.add(dwg.rect(size=dims[:2], class_=class_tag,
                                insert=dims[2:]))
            dwg.defs.add(symbol)
            sym_map[module] = {"symbol": symbol,
                               "center": (dims[0]/2 + dims[2],
                                          dims[1]/2 + dims[3])}
        cb_map = {
            #        a, b, c, d, e, f
            "sb":   [2.5, 2, 2, 2.5, 2, 2, 0, 0],
            "sb00": [2.5, 2, 2, 2.5, 2, 2, -2, -2],  # ┿
            "sb01": [2.5, 0, 2, 2.5, 2, 0, 0, 0],  # ┗
            "sb02": [2.5, 0, 2, 2.5, 2, 2, 0, -2],  # ┝
            "sb03": [2.5, 0, 0, 2.5, 2, 2, 0, -2],  # ┏
            "sb04": [2.5, 2, 0, 2.5, 2, 2, -2, -2],  # ┯
            "sb05": [2.5, 2, 0, 2.5, 0, 2, -2, -2],  # ┓
            "sb06": [2.5, 2, 2, 2.5, 0, 2, -2, -2],  # ┫
            "sb07": [2.5, 2, 2, 2.5, 0, 0, -2, 0],  # ┛
            "sb08": [2.5, 2, 2, 2.5, 2, 0, -2, 0],  # ┷
            "sb09": [2.5, 0, 2, 2.5, 0, 2, 0, -2],  # ┃
            "sb10": [2.5, 2, 0, 2.5, 2, 0, -2, 0],  # ━
        }
        for module, dims in cb_map.items():
            a, b, c, d, e, f, x, y = dims
            symbol = dwg.symbol(id=module)
            symbol["x"] = x
            symbol["y"] = y
            symbol.add(dwg.path(d=f"M {b} 0 " +
                                f"v {f} h {-1*b} " +
                                f"v {a} h {b} v {c} h {d} " +
                                f"v {-1*c} h {e} v {-1*a} h {-1*e} " +
                                f"v {-1*f}" +
                                " z"))
            dwg.defs.add(symbol)
            sym_map[module] = {"symbol": symbol,
                               "center": ((d)/2, (a)/2)}
        return sym_map

    def _unique(self, sequence):
        seen = set()
        u = [x for x in sequence if not (x in seen or seen.add(x))]
        return [val for sublist in u for val in sublist]

    def merge_symbol(self, inst_list, new_symbol_name):
        points = []

        def add_point(direction, distance):
            if direction == "h":
                new_pt = (points[-1][0] + distance, points[-1][1])
            if direction == "v":
                new_pt = (points[-1][0], points[-1][1] + distance)
            points.append(new_pt)

        for each in inst_list:
            inst = self.get_instance(each)
            symbol = self.get_symbol_of_instance(each)
            pt = (inst.attribs["x"], inst.attribs["y"])
            if symbol.elements[0].elementname == "rect":
                ele = symbol.elements[0]
                attrib = ele.attribs
                points.append((pt[0]+attrib.get("x", 0),
                              pt[1]+attrib.get("y", 0)))
                add_point("v", float(attrib["height"]))
                add_point("h", float(attrib["width"]))
                add_point("v", -1*float(attrib["height"]))
            elif symbol.elements[0].elementname == "path":
                ele = symbol.elements[0]
                pts = ele.attribs["d"].split()
                points.append((pt[0]+pts[1],
                              pt[1]+pts[2]))
                for direction, distance in zip(pts[3:-1:2], pts[4:-1:2]):
                    add_point(direction, float(distance))
            else:
                logger.error("Can not extract point from tag")
        _, points = shaping_utils.get_shapes_outline(points)
        print(points)
        path_points = shaping_utils.points_to_path(points)
        pt = path_points.lower().split()
        svg_path = ""
        for eachpt in zip(pt[3::2], pt[4::2]):
            svg_path += "v {} h {} ".format(*eachpt) if pt[0] == "v" else \
                "h {} v {} ".format(*eachpt)
        symbol = self.dwg.symbol(id=new_symbol_name)
        symbol.add(self.dwg.path(d=f"M {pt[1]} {pt[2]} {svg_path} z"))
        self.dwg.defs.add(symbol)
        self.dwg_shapes.add(self.dwg.use(symbol, insert=points[0]))
        return symbol

    def add_style(self, style):
        for ele in self.dwg.defs.elements:
            if ele.attribs.get('type', "") == 'text/css':
                ele.append(style)

    def get_instance(self, instance_name):
        for ele in self.dwg_shapes.elements:
            if instance_name in ele.attribs.get("id", ""):
                return ele

    def get_symbol_of_instance(self, instance_name):
        symbol = self.get_instance(instance_name)
        return self.get_symbol(symbol["xlink:href"][1:])

    def get_symbol(self, symbol_name):
        for ele in self.dwg.defs.elements:
            if symbol_name in ele.attribs.get("id", ""):
                return ele

    def render_layout(self, filename=None):
        '''
        Renders the given layout
        '''
        filename = filename or "_render.svg"
        params = self._default_shaping_param()
        bbox = (0, 0, 15*(self.width)-5, 15*(self.height)-5)
        dwg = svgwrite.Drawing(filename, bbox[2:], debug=False)
        dwg.viewbox(0, -1*bbox[3], bbox[2], bbox[3])
        dwg.defs.add(dwg.style(CSS_STYLE))
        symbol_map = self.add_render_symbols(dwg, params)

        # Createing instances
        dwg_main = dwg.add(Group(id="main", transform="scale(1,-1)"))
        dwg_main.add(dwg.rect(size=bbox[2:],
                              id="core_boundary",
                              class_="boundary"))
        dwg_shapes = dwg_main.add(Group(id="main_shapes"))
        dwg_text = dwg_main.add(Group(id="main_text"))

        visited = []
        for x_pt in range(1, (2*self.width)-2):
            for y_pt in range(1, (2*self.height)-2):
                module = self.get_top_instance(x_pt, y_pt)
                inst_name = module
                if module in visited:
                    continue
                visited.append(module)
                module = "_".join(module.split("_")[:-4])
                if "sb" in module:
                    left = self.get_top_instance(x_pt-1, y_pt).split("_")[0]
                    right = self.get_top_instance(x_pt+1, y_pt).split("_")[0]
                    bottom = self.get_top_instance(x_pt, y_pt-1).split("_")[0]
                    top = self.get_top_instance(x_pt, y_pt+1).split("_")[0]
                    left = left if left in ('cbx', 'cby') else "EMPTY"
                    right = right if right in ('cbx', 'cby') else "EMPTY"
                    bottom = bottom if bottom in ('cbx', 'cby') else "EMPTY"
                    top = top if top in ('cbx', 'cby') else "EMPTY"
                    if (left, right, bottom, top) == ("cbx", "cbx", "cby", "cby"):
                        symbol = "sb00"
                    elif (left, right, bottom, top) == ("EMPTY", "cbx", "cby", "cby"):
                        symbol = "sb02"
                    elif (left, right, bottom, top) == ("EMPTY", "EMPTY", "cby", "cby"):
                        symbol = "sb09"
                    elif (left, right, bottom, top) == ("cbx", "cbx", "EMPTY", "EMPTY"):
                        symbol = "sb10"
                    elif (left, right, bottom) == ("cbx", "cbx", "cby"):
                        symbol = "sb04"
                    elif (left, top, bottom) == ("cbx", "cby", "cby"):
                        symbol = "sb06"
                    elif (left, right, top) == ("cbx", "cbx", "cby"):
                        symbol = "sb08"
                    elif (left, top) == ("cbx", "cby"):
                        symbol = "sb07"
                    elif (left, bottom) == ("cbx", "cby"):
                        symbol = "sb05"
                    elif (right, top) == ("cbx",  "cby"):
                        symbol = "sb01"
                    elif (right, bottom) == ("cbx",  "cby"):
                        symbol = "sb03"
                    else:
                        symbol = module
                else:
                    symbol = module

                x_pt_new = (x_pt/2)*15 if (x_pt % 2) == 0 else (x_pt/2)*15 + 5
                y_pt_new = (y_pt/2)*15 if (y_pt % 2) == 0 else (y_pt/2)*15 + 5
                # dwg_shapes.add(dwg.circle(r=0.02, stroke="red",
                #                center=(x_pt_new, y_pt_new)))
                xct, yct = symbol_map[symbol]["center"]
                dwg_text.add(dwg.text(inst_name, insert=(x_pt_new+xct, (y_pt_new+yct)*-1),
                                      transform="scale(1,-1)",
                                      alignment_baseline="middle",
                                      text_anchor="middle"))
                if symbol:
                    dwg_shapes.add(dwg.use(symbol_map[symbol]["symbol"],
                                           id=inst_name,
                                           insert=(x_pt_new, y_pt_new)))
                else:
                    print(module)
        dwg.save(pretty=True, indent=4)
        self.dwg = dwg
        self.dwg_shapes = dwg_shapes
        self.dwg_text = dwg_text
        return dwg


if __name__ == "__main__":
    main()
