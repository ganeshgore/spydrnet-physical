
'''
This file creates different connection patterns for connectivity

The connection pattern format
# FROM_X, FROM_Y, TO_X, TO_Y


for external connections (its 45 degree clock wise ratation)
0, 0 : Left
None, 0 : bottom
None, None : Right
0, None : Top
'''
import math
from copy import deepcopy
from shutil import move
from typing import List

import spydrnet as sdn
import svgwrite
from svgwrite.container import Group


class ConnectPoint:
    ''' This store the individual connections points '''

    def __init__(self, from_x, from_y, to_x, to_y):
        from_x, from_y = int(from_x), int(from_y)
        to_x, to_y = int(to_x), int(to_y)
        assert not ((from_x == to_x) and (from_y == to_y)), \
            "Can not make connection to the same grid"
        assert ((from_x == to_x) and (from_y != to_y)) or \
               ((from_x != to_x) and (from_y == to_y)), \
            "Only horizontal or vertical connections are possible " + \
            f"{from_x}  {from_y} {to_x}  {to_y}"
        self.from_x, self.from_y = (from_x, from_y)
        self.to_x, self.to_y = (to_x, to_y)

        self.from_dir = ""
        self.to_dir = ""
        self._color = "black"
        self._update_direction()

    @property
    def distance(self):
        ''' return the connection distance '''
        return abs(self.from_x-self.to_x) + abs(self.from_y-self.to_y)

    @property
    def connection(self):
        ''' return all four connection points '''
        return (self.from_x, self.from_y, self.to_x, self.to_y)

    @property
    def full_connection(self):
        ''' return all four connection points '''
        return (self.from_x, self.from_y, self.to_x, self.to_y, self.from_dir, self.to_dir)

    @property
    def from_connection(self):
        ''' return from connection points '''
        return (self.from_x, self.from_y)

    @property
    def to_connection(self):
        ''' return to connection points '''
        return (self.to_x, self.to_y)

    @property
    def color(self):
        ''' return color of conneton '''
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
        return self._color

    def rotate_connection(self, angle, sizex=None, sizey=None):
        self.from_x, self.from_y = self._rotate_point(
            self.from_connection,
            angle=angle, sizex=sizex, sizey=sizey)
        self.to_x, self.to_y = self._rotate_point(
            self.to_connection,
            angle=angle, sizex=sizex, sizey=sizey)
        self._update_direction()

    def translate_connection(self, x, y):
        self.from_x, self.from_y = self.from_x + x, self.from_y+y
        self.to_x, self.to_y = self.to_x + x, self.to_y+y
        self._update_direction()

    def scale_connection(self, scale, anchor=(0, 0)):
        self.translate_connection(-1*anchor[0], -1*anchor[1])
        self.from_x, self.from_y = self.from_x * scale, self.from_y * scale
        self.to_x, self.to_y = self.to_x * scale, self.to_y * scale
        self.translate_connection(anchor[0], anchor[1])
        self._update_direction()

    def _update_direction(self):
        self.to_dir = self.direction()
        self.from_dir = self.direction(reverse=True)

    def direction(self, reverse=False):
        dx, dy = tuple(x-y for x, y in
                       zip(self.to_connection, self.from_connection))
        if dx == 0 and dy > 0:
            direction = "top"
        elif dx == 0 and dy < 0:
            direction = "bottom"
        elif dx > 0 and dy == 0:
            direction = "right"
        elif dx < 0 and dy == 0:
            direction = "left"
        else:
            direction = None
        if reverse:
            return direction
        else:
            return {"left": "right", "right": "left",
                    "top": "bottom", "bottom": "top"}[direction]

    @staticmethod
    def _rotate_point(point, angle, sizex=None, sizey=None):
        x, y = point
        if angle in (90, ):
            return(sizex-y+1, x)
        elif angle in (180, ):
            return(sizex-x+1, sizey-y+1)
        elif angle in (270, ):
            return(y, sizey-x+1)
        else:
            return point

    def __iter__(self):
        yield from self.connection

    def __str__(self) -> str:
        return "%5d %5d %5d %5d %s" % (self.from_x, self.from_y, self.to_x, self.to_y)

    def __mul__(self, scale):
        self.from_x *= scale
        self.from_y *= scale
        self.to_x *= scale
        self.to_y *= scale
        return self

    def __rmul__(self, scale):
        self.from_x *= scale
        self.from_y *= scale
        self.to_x *= scale
        self.to_y *= scale
        return self


class ConnectPointList:
    ''' This stores list of connection points  '''

    def __init__(self, sizex=None, sizey=None, point=None):
        self.sizex = sizex
        self.sizey = sizey
        self._points: List[ConnectPoint] = []
        self._cursor = []
        self._cursor_state = True
        if point:
            self.add_connect_point(point)

    @property
    def points(self):
        return self._points

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, point):
        self._cursor = point
        return self.cursor

    @property
    def get_x(self):
        ''' returns x location of cursor '''
        return self._cursor[0]

    @property
    def get_y(self):
        ''' returns y location of cursor '''
        return self._cursor[1]

    def set_color(self, color):
        ''' Set color to all the points in the connection list '''
        for each in self._points:
            each.color = color
        return self

    def hold_cursor(self):
        ''' Holds the cursor at current position '''
        self._cursor_state = False

    def release_cursor(self):
        ''' Rleases cursor and moves with each point addition '''
        self._cursor_state = True

    def flip(self, orientation="H", base=None):
        """ Flips all the points horizontally or vertically"""
        raise NotImplemented

    def sample_connections(self, max_distance=1):
        ''' This method splits all the connections longer that ``max_distance`` to
        at max ``max_distance`` length
        '''
        cursor_backup = self.cursor
        for indx, each in enumerate(self._points):
            if each.distance > max_distance:
                self.cursor = (each.from_x, each.from_y)
                for i in range(max_distance, each.distance, max_distance):
                    if each.from_dir == "right":
                        self.move_x(value=max_distance)
                    elif each.from_dir == "left":
                        self.move_x(value=-1*max_distance)
                    if each.from_dir == "top":
                        self.move_y(value=max_distance)
                    elif each.from_dir == "bottom":
                        self.move_y(value=-1*max_distance)
                each.from_x, each.from_y = self._cursor
        self.cursor = cursor_backup

    def crop_edges(self):
        ''' Crops all the connections going out of grid '''
        for point in self._points:
            for eachp in ('from_x', 'to_x'):
                pt = getattr(point, eachp)
                if pt < 0:
                    setattr(point, eachp, 0)
                if pt > self.sizex:
                    setattr(point, eachp, 0)
            for eachp in ('from_y', 'to_y'):
                pt = getattr(point, eachp)
                if pt < 0:
                    setattr(point, eachp, 0)
                if pt > self.sizey:
                    setattr(point, eachp, 0)

    def merge(self, connectlist):
        self._points.extend(connectlist._points)
        return self

    def scale(self, scale, anchor=(0, 0)):
        for point in self._points:
            point.scale_connection(scale, anchor)
        return self

    def translate(self, x, y):
        for point in self._points:
            point.translate_connection(x, y)
        return self

    def rotate(self, angle=0):
        angles = (0, 90, 180, 270, -90, -180, -270, 'CW', 'ACW')
        assert angle in angles, "Supports only %s degree ratations" % angles
        for point in self._points:
            point.rotate_connection(angle, sizex=self.sizex, sizey=self.sizey)
        return self

    def add_next_point(self, x, y):
        x_prev, y_prev = self._cursor
        point = ConnectPoint(x_prev, y_prev, x, y)
        self.add_connect_point(point)
        self._update_cursor()
        return point

    def move_x(self, value=1, steps=1):
        ''' Moves cursor in x direction by specified steps times by specified value'''
        x_prev, y_prev = self.cursor
        for _ in range(steps):
            point = ConnectPoint(x_prev, y_prev, x_prev+value, y_prev)
            self.add_connect_point(point)
            x_prev, y_prev = (x_prev+value, y_prev)
        self._update_cursor()
        return self.cursor

    def move_y(self, value=1, steps=1):
        ''' Moves cursor in y direction by specified steps times by specified value'''
        x_prev, y_prev = self.cursor
        for _ in range(steps):
            point = ConnectPoint(x_prev, y_prev, x_prev, y_prev+value)
            self.add_connect_point(point)
            x_prev, y_prev = (x_prev, y_prev+value)
        self._update_cursor()
        return self.cursor

    def _update_cursor(self):
        if self._cursor_state:
            self._cursor = self._points[-1].to_connection
        return self.cursor

    def __str__(self):
        lines = ""
        for p in self._points:
            lines += str(p)
            lines += "\n"
        return lines

    def add_connect_point(self, point):
        assert isinstance(point, ConnectPoint)
        self._points.append(point)
        self._update_cursor()
        return point

    def add_connection(self, from_x, from_y, to_x, to_y):
        point = ConnectPoint(from_x, from_y, to_x, to_y)
        self._points.append(point)
        self._update_cursor()
        return point

    def render_pattern(self, scale=20):
        '''
        This renderes connection points list in a SVG format

        args:
            connect (list): collection connection pattern

        returns:
            str(str): return svg string
        '''
        sizex = max([max(x1, x2) for x1, y1, x2, y2 in self._points])+1
        sizey = max([max(y1, y2) for x1, y1, x2, y2 in self._points])+1
        width = sizex*scale
        height = sizey*scale
        x_offset = 0
        y_offset = -1*height
        dwg = svgwrite.Drawing("_render.svg", size=(width, height))
        dwg.viewbox(x_offset, y_offset, width, height)

        dwgMarker = dwg.add(Group(id="markers",  transform="scale(1,-1)"))
        dwgMain = dwg.add(Group(id="main", transform="scale(1,-1)"))
        dwg.defs.add(dwg.style("""
                text{font-family: Verdana;}
                svgg{background-color:grey;}
                .connection{stroke-linecap:round; opacity: 0.7;}
                span{text-anchor: "middle"; alignment_baseline: "middle"}
                .gridLabels{fill: grey;font-style: italic;font-weight: 900}
                # core_boundary{stroke:grey; stroke_width:0.5;}
                .gridmarker{stroke:red; stroke_width:0.5;}
                """))
        DRMarker = dwg.marker(refX="30", refY="30",
                              viewBox="0 0 120 120",
                              markerUnits="strokeWidth",
                              markerWidth="8", markerHeight="10", orient="auto")
        DRMarker.add(dwg.path(d="M 0 0 L 60 30 L 0 60 z", fill="blue"))
        dwg.defs.add(DRMarker)
        for conn in self._points:
            conn = conn*scale
            dwgMain.add(dwg.line(start=conn.from_connection,
                                 end=conn.to_connection,
                                 stroke=conn.color,
                                 marker_end=DRMarker.get_funciri(),
                                 class_="connection"))
        return dwg

    def get_reference(self, x, y):
        '''
        Return reference for the given tile location
        '''
        return "PlaceholderModule"

    def get_top_instance(self, x, y):
        '''
        Return reference for the given tile location
        '''
        return "PlaceholderModule"

    def show_stats(self):
        '''
        Extracts the connectivity statistics for port and connection creation
        '''
        module_stat = {}
        for point in self._points:
            from_conn = self.get_reference(*point.from_connection)
            to_conn = self.get_reference(*point.to_connection)

            module_stat[from_conn] = module_stat.get(from_conn, {})
            module_stat[from_conn]["out"] = module_stat[from_conn].get(
                "out", {"left": 0, "right": 0, "top": 0, "bottom": 0})
            module_stat[from_conn]["out"][point.direction(reverse=True)] += 1

            module_stat[to_conn] = module_stat.get(to_conn, {})
            module_stat[to_conn]["in"] = module_stat[to_conn].get(
                "in", {"left": 0, "right": 0, "top": 0, "bottom": 0})
            module_stat[to_conn]["in"][point.direction(reverse=False)] += 1

        return module_stat

    def create_ft_ports(self, netlist, port_name: str):
        '''
        Create feedthrough port on the given module

        args:
            netlist (Netlist): netlist
            port (str): port name on each module
        '''

        for m_name, values in self.show_stats().items():
            if m_name == "top":
                continue
            module: sdn.Definition = next(netlist.get_definitions(m_name))
            port: sdn.Port = next(module.get_ports(port_name))

            prev_cable = None
            for inp in [k for k, v in values.get("in", {}).items() if v > 0]:
                module.create_port(f"{port.name}_{inp}_in",
                                   pins=port.size, direction=sdn.IN)
                cable = module.create_cable(f"{port.name}_{inp}_in",
                                            wires=port.size)
                if prev_cable:
                    prev_cable.assign_cable(cable)
                prev_cable = cable
            if prev_cable:
                prev_cable.assign_cable(next(port.get_cables()))

            prev_cable = None
            for outp in [k for k, v in values.get("out", {}).items() if v > 0]:
                module.create_port(f"{port.name}_{outp}_out",
                                   pins=port.size, direction=sdn.OUT)
                cable = module.create_cable(f"{port.name}_{outp}_out",
                                            wires=port.size)
                if prev_cable:
                    prev_cable.assign_cable(cable)
                prev_cable = cable
            if prev_cable:
                next(port.get_cables()).assign_cable(prev_cable)
            module.remove_port(port)

    def create_ft_connection(self, top_definition, signal_cable):
        ''' Create connections
        '''
        signal = signal_cable.name
        cable = top_definition.create_cable(signal+"_ft")
        for point in self._points:
            w = cable.create_wire()
            if 0 in point.from_connection:
                signal_cable.assign_cable(
                    cable, upper=w.get_index, lower=w.get_index)
            else:
                inst = self.get_top_instance(*point.from_connection)
                port_name = f"{signal}_{point.from_dir}_out"
                w.connect_pin(next(inst.get_port_pins(port_name)))

            if 0 in point.to_connection:
                signal_cable.assign_cable(
                    cable, upper=w.get_index, lower=w.get_index)
            else:
                inst = self.get_top_instance(*point.to_connection)
                w.connect_pin(next(inst.get_port_pins(
                    f"{signal}_{point.to_dir}_in")))

    def __iter__(self):
        yield from self._points

    def short_through(self, through_point):
        incoming = None
        outgoing = None
        for point in self._points:
            if point.from_connection == through_point:
                outgoing = point
            if point.to_connection == through_point:
                incoming = point
            if incoming and outgoing:
                break

        assert isinstance(
            incoming, ConnectPoint), "Incoming connection not found"
        assert isinstance(
            outgoing, ConnectPoint), "Outgoing connection not found"
        incoming.to_x, incoming.to_y = outgoing.to_connection
        self._points.remove(outgoing)


class ConnectionPattern:
    '''
    This creates a connection patterns (`ConnectPointList`) based on pre-defined rule

    '''

    def __init__(self, sizex, sizey):
        '''
        Initialise FPGA parameters

        args:
            sizex (int): Width of FPGA grid
            sizey (int): Size of FPGA grid
        '''
        self.sizex = sizex
        self.sizey = sizey
        self.xbias = 0
        self.ybias = 0
        self._connect = ConnectPointList(sizex=sizex, sizey=sizey)

    @ property
    def connections(self):
        return self._connect

    @ connections.setter
    def connections(self, value):
        self._connect = value
        return self._connect

    def reset(self):
        self._connect = ConnectPointList(sizex=self.sizex,
                                         sizey=self.sizey)

    @ staticmethod
    def _get_prime_factors(number):
        prime_factors = []
        while number % 2 == 0:
            prime_factors.append(2)
            number = number / 2

        for i in range(3, int(math.sqrt(number)) + 1, 2):
            while number % i == 0:
                prime_factors.append(int(i))
                number = number / i
        if number > 2:
            prime_factors.append(int(number))
        return prime_factors

    def auto_select(self):
        '''
        Auto implements the global tree with crop and scale operations
        '''
        NotImplementedError

    @staticmethod
    def get_htree(size, root=0, side=0, repeat=1):
        ''' Returns H-Tree of specific size '''
        points = ConnectPointList(sizex=size, sizey=size)
        size = size if size % 2 else (size-1)
        mid = (size+1)/2
        points.cursor = (mid, mid)
        for _ in range(repeat):
            points.release_cursor()
            points.move_x(value=1, steps=int(mid/2)+root)
            points.hold_cursor()
            points.move_y(value=1, steps=int(mid/2)+side)
            points.move_y(value=-1, steps=int(mid/2)+side)

        points.cursor = (mid, mid)
        for _ in range(repeat):
            points.release_cursor()
            points.move_x(value=-1, steps=int(mid/2)+root)
            points.hold_cursor()
            points.move_y(value=1, steps=int(mid/2)+side)
            points.move_y(value=-1, steps=int(mid/2)+side)
        return points

    def add_htree(self, n=3):
        '''
        Returns HTree pattern fo the given grid size
        '''
        assert (math.log2(n-1) % 1) == 0, "Support only (2^n)+1 width"
        self._connect.merge(self.get_htree(n))
        return self._connect

        dev_size = min(self.sizex, self.sizey)
        while n < dev_size:
            print(n)
            n = n*2
            self.get_fishbone()
        return self._connect
        # points = self._connect
        # x_center = ((self.sizex+1)*0.5)
        # y_center = ((self.sizey+1)*0.5)
        # print(x_center, y_center)

    def get_fishbone(self, x_margin=(0, 0), y_margin=(0, 0)):
        '''
        Returns fishbone pattern for the given grid size

        Spine is created at the center of the grid, to change bias when grid
        is symetric change ``xbias`` and ``ybias`` parameter

        x_margin(tuple(int, int)): Skips the repective grid connectivity
        y_margin(tuple(int, int)): Skips the repective grid connectivity
        '''
        points = self._connect
        x_center = ((self.sizex+1)*0.5)
        x_pt = math.ceil(x_center) if self.xbias else math.floor(x_center)
        y_pt = (1+y_margin[0])
        points.add_connection(x_pt, 0, x_pt, y_pt)
        points.cursor = (x_pt, y_pt)
        for indx in range(self.sizey-y_margin[1]):
            if not indx == 0:
                points.move_y()
            center = points.cursor
            while points.get_x < (self.sizex-x_margin[1]):
                points.move_x()
            points.cursor = center
            while points.get_x > (1 + x_margin[0]):
                points.move_x(-1)
            points.cursor = center
        return points

    def render_pattern(self, scale=20, title=None, add_module_labels=False):
        dwg = self._connect.render_pattern(scale)

        dwgMain = [e for e in dwg.elements if e.get_id() == "main"][0]
        dwgText = dwgMain.add(Group(id="text"))
        dwgMarker = [e for e in dwg.elements if e.get_id() == "markers"]

        if dwgMarker:
            dwgMarker = dwgMarker[0]
            for i in range(0, self.sizex+1):
                dwgMarker.add(dwg.line(start=((i+0.5)*scale, 0.5*scale),
                                       end=((i+0.5)*scale,
                                            (self.sizey+0.5)*scale),
                                       class_="gridmarker"))
            for i in range(0, self.sizey+1):
                dwgMarker.add(dwg.line(start=(0.5*scale, (i+0.5)*scale),
                                       end=((self.sizex+0.5) *
                                            scale, (i+0.5)*scale),
                                       class_="gridmarker"))

        # Add labels to the grid
        if add_module_labels:
            for x in range(1, 1+self.sizex):
                for y in range(1, 1+self.sizey):
                    txt = self._connect.get_top_instance(x, y).name
                    label = dwg.text("",
                                     font_size=self.sizey*scale*0.03,
                                     alignment_baseline="middle",
                                     class_="gridLabels",
                                     text_anchor="middle",
                                     transform="scale(1,-1)",
                                     insert=(x*scale, (-1*y*scale) + 0.25*scale))
                    label.add(dwg.tspan(txt, x=[x*scale]))
                    label.add(dwg.tspan(
                        "["+self._connect.get_reference(x, y)+"]",
                        font_size=self.sizey*scale*0.02,
                        x=[x*scale], dy=["2%", ]))
                    dwgText.add(label)

        # Add title to generated SVG image
        title = title or f" %d x %d FPGA " % (self.sizex, self.sizey)
        dwgText.add(dwg.text(title,
                             insert=((self.sizex+1)*scale*0.5, -1*-0.5*scale),
                             transform="scale(1,-1)",
                             class_="moduleLabel",
                             fill="black",
                             font_size=self.sizey*scale*0.1,
                             alignment_baseline="middle",
                             text_anchor="middle"))

        width = self.sizex*scale + (scale)
        height = self.sizey*scale + (3*scale)
        x_offset = 0
        y_offset = -1*height + (1.5*scale)
        dwg["width"] = width
        dwg["height"] = height
        dwg.viewbox(x_offset, y_offset, width, height)

        return dwg


if __name__ == "__main__":
    # conn_list = ConnectPointList(5, 5)
    # conn_list.add_connection(1, 1, 1, 2)
    # conn_list.add_connection(1, 2, 2, 2)
    # print(conn_list)
    # conn_list.render_pattern().save(pretty=True, indent=4)

    # fpga = ConnectionPattern(5, 5)
    # conn_list = fpga.get_fishbone()
    # print(conn_list)
    # conn_list.rotate(90)
    # fpga.render_pattern().save(pretty=True, indent=4)

    fpga = ConnectionPattern(5, 5)
    left_tree = fpga.connections
    left_tree = fpga.get_fishbone(x_margin=(0, 0))
    left_tree.scale(2, anchor=(1, 1))

    fpga = ConnectionPattern(10, 10)
    conn_list = fpga.connections
    conn_list.merge(left_tree)
    conn_list.crop_edges()
    conn_list.sample_connections()
    fpga.render_pattern().save(pretty=True, indent=4)
