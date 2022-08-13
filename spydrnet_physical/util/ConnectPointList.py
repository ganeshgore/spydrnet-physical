'''
'''
import csv
import math
import logging
from collections import OrderedDict
from typing import List
from xml.dom import minidom

import networkx as nx
import spydrnet as sdn
import svgwrite
from spydrnet_physical.util import ConnectPoint
from svgwrite.container import Group

DEFAULT_COLOR = " black"

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='DEBUG')


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
        "Returns list of ConnectionPoints"
        return self._points

    @property
    def cursor(self):
        "Returns current location of cursor"
        return self._cursor

    @cursor.setter
    def cursor(self, point):
        '''
        Cursor is placed at the specified point

        Args:
            point (int, int): (x,y) coordinates where cursor is to be placed
        '''
        self._cursor = point
        return self._cursor

    @property
    def get_x(self):
        " Returns location of cursor "
        return self._cursor[0]

    @property
    def get_y(self):
        ''' returns y location of cursor '''
        return self._cursor[1]

    def set_cursor(self, x, y):
        '''
        Sets cursor at given x, y coordinate

        Args:
            x (int): point on the x-axis where cursor is to be placed
            y (int): point on the y-axis where cursor is to be placed

        Returns:
            self: self ConnectionPointList object
        '''
        self._cursor = (x, y)
        return self

    def set_color(self, color):
        '''
        Set color to all the points in the connection list

        Args:
            color (str): Specify a color for connect point list e.g 'red', 'blue', 'green', etc.

        '''
        for each in self._points:
            each.color = color
        return self

    def store_points(self, filename):
        ''' Stores all points and its attributes in csv format in the file '''
        with open(filename, "w", encoding="UTF-8") as file_ptr:
            file_ptr.write("# Generated using SpyDrNet-physical plugin\n")
            file_ptr.write("# fr_x  fr_y  to_x  to_y  type\n")
            file_ptr.write("= = "*10 +"\n")
            for point in  self.points:
                file_ptr.write(str(point)+"\n")


    def validate_connectivity(self):
        """
        This fucntion checks following

        * If there is any connection coming outside from range (0-sizex+1) or (0-sizey+1)
        * If there is any redundant connections
        """
        # Check if signal enter module multiple times
        logger.info("Checking consistency of the connection file")
        point : ConnectPoint
        in_mapping = [[0 for _ in range(self.sizey+2)] for _ in range(self.sizex+2)]
        for point in self._points:
            if point.to_x >= self.sizex+2:
                logger.warning("Pointx out of range %d", point.to_x)
                continue
            if point.to_y >= self.sizey+2:
                logger.warning("Pointy out of range %d", point.to_y)
                continue
            if in_mapping[point.to_x][point.to_y]:
                logger.warning("Multiple input for instance (%d %d)",
                                *point.to_connection)
            in_mapping[point.to_x][point.to_y] = 1

    def load_points(self, filename, append=False, delimiter=" ", skiplines=3):
        '''
        Loads all points and its attributes from the given csv file

        Format: from_x, from_y, to_x, to_y, level, color
        '''
        if not append:
            _ = [self._points.pop(0) for _ in list(self._points)]
        with open(filename, encoding="UTF-8") as pts_file:
            spamreader = csv.reader(pts_file, delimiter=delimiter, skipinitialspace=True)
            _ = [next(spamreader) for _ in range(skiplines)]
            for row in spamreader:
                point = self.add_connection(*row[:4])
                if "top" in row[-1]:
                    self.make_top_connection(point)
                if "down" in row[-1]:
                    self.push_connection_down(point)
                if "up" in row[-1]:
                    self.pull_connection_up(point)


    def load_points_from_svg(self, filename, grid=6.9*2, group="markers", append=False,
                        same_color="black", down_color="red", up_color="green"):
        '''
        This method loads points from the SVG file.
        enabling UI based designing of connection file.
        '''
        root = minidom.parse(filename)
        if not append:
            _ = [self._points.pop(0) for _ in list(self._points)]

        x_grid = []
        y_grid = []
        for conn in root.getElementsByTagName("line"):
            if "gridmarker" in conn.getAttribute('class'):
                x1 = float(conn.getAttribute("x1"))
                x2 = float(conn.getAttribute("x2"))
                y1 = float(conn.getAttribute("y1"))
                y2 = float(conn.getAttribute("y2"))
                if y1 == y2:
                    y_grid.append(y1)
                if x1 == x2:
                    x_grid.append(x1)
        x_grid = sorted(x_grid)
        y_grid = sorted(y_grid)
        x_origin = x_grid[0]
        y_origin = y_grid[0]
        # x_grid= min([ abs(a-b) for a,b in zip(x_grid[:-1], x_grid[1:])])
        # y_grid= min([ abs(a-b) for a,b in zip(y_grid[:-1], y_grid[1:])])

        x_grid = (max(x_grid)-min(x_grid))/(self.sizex)
        y_grid = (max(y_grid)-min(y_grid))/(self.sizey)
        logger.info("Computed grid size is  %.2f x %.2f", x_grid, y_grid)
        logger.info("origin  %.2f x %.2f", x_origin, y_origin)

        logger.debug("x1                 x2                 y1                 y2")
        for conn in root.getElementsByTagName("line"):
            conn_class = conn.getAttribute('class')
            if "connection" in conn_class:
                x1 = 1 + math.floor(((float(conn.getAttribute("x1")))-(x_origin))/x_grid)
                x2 = 1 + math.floor(((float(conn.getAttribute("x2")))-(x_origin))/x_grid)
                y1 = 1 + math.floor(((float(conn.getAttribute("y1")))-(y_origin))/y_grid)
                y2 = 1 + math.floor(((float(conn.getAttribute("y2")))-(y_origin))/y_grid)

                if abs(y1 - y2) > abs(x1 - x2):
                    direction = "top" if y2 > y1 else "bottom"
                elif abs(x1 - x2) > abs(y1 - y2):
                    direction = "right" if x2 > x1 else "left"
                else:
                    logger.warning("Can not identify the connection direction %s [Dx %.2f, Dy %.2f]",
                        conn.attributes.items(),abs(x1 - x2),abs(y1 - y2))
                    continue
                conn_type = "up" if "up" in conn_class else "down" \
                                if "down" in conn_class else "same"
                points_info = f"{x1:8.2f}[{conn.getAttribute('x1'):8s}]  " + \
                      f"{y1:8.2f}[{conn.getAttribute('y1'):8s}]  " + \
                      f"{x2:8.2f}[{conn.getAttribute('x2'):8s}]  " + \
                      f"{y2:8.2f}[{conn.getAttribute('y2'):8s}]  " + \
                      f"-> {direction:>8s}[{conn_type:^4s}]"
                try:
                    point = self.add_connection(abs(x1), self.sizey+1-abs(y1),
                        abs(x2), self.sizey+1-abs(y2))
                    logger.debug("%s Added", points_info)
                except AssertionError as error:
                    logger.debug("%s Skipped (%8s, %8s) : %s", points_info,
                        conn.getAttribute("x1"), conn.getAttribute("y1"), error)
                if "top" in conn_class:
                    self.make_top_connection(point)
                if "down" in conn_class:
                    self.push_connection_down(point)
                if "up" in conn_class:
                    self.pull_connection_up(point)

        # raise NotImplementedError


    def search_from_point(self, point):
        '''
        Search for connection going out of this point

        Note: Returns the first point

        Args:
            point (tuple): Point to search

        Returns:
            ConnectionPoint:
        '''
        for pts in self._points:
            if (pts.from_connection == point):
                return pts
        return None

    def search_to_point(self, point):
        '''
        Search for connection coming into this point

        Note: Returns the first point

        Args:
            point (tuple): Point to search

        Returns:
            ConnectionPoint:
        '''
        for pts in self._points:
            if (pts.to_connection == point):
                return pts
        return None

    def push_connection_down(self, point):
        '''
        Push given connection one-level down

        'Push down' connection indicates that this connection is going down from
        the current level

        Args:
            point (tuple): Connetion point to push down

        Returns:
            ConnectionPoint:
        '''
        if isinstance(point, tuple):
            point = self.search_to_point(point)
        point.level = "down"
        return point

    def pull_connection_up(self, point):
        '''
        Pull given connections one-level up

        'Pull up' connection indicates that this connection is coming from
        one level above this level

        Args:
            point (tuple): Connetion point to pull up
        '''
        if isinstance(point, tuple):
            point = self.search_from_point(point)
        point.level = "up"
        return point

    def make_top_connection(self, point):
        '''
        Make connection with the top layer

        Args:
            point (tuple): Connetion point to push down

        Returns:
            ConnectionPoint:
        '''
        if isinstance(point, tuple):
            point = self.search_from_point(point)
        point.level = "top"
        return point

    def reset_level(self, point):
        '''
        Resets the level of the connections

        Args:
            point (ConnectPoint): It is a ConnectPoint object
        '''
        assert isinstance(point, ConnectPoint), \
            "point should be instance of ConnectPoint class not " + type(point)
        point.level = "same"

    def hold_cursor(self):
        ''' Holds the cursor at current position '''
        self._cursor_state = False

    def release_cursor(self):
        ''' Releases cursor and moves with each point addition '''
        self._cursor_state = True

    def flip(self, orientation="H"):
        '''
        Flips all the points horizontally or vertically

        Args:
            orientation: "H" or "V" (default="H")
        '''
        for point in self._points:
            point.flip_connection(orientation)
        return self

    def sample_connections(self, max_distance=1):
        '''
        This method splits all the connections longer that ``max_distance`` to
        at max ``max_distance`` length

        Args:
            max_distance (int): int to sample the connection at this value
        '''
        cursor_backup = self._cursor
        for _, each in enumerate(self._points):
            if each.distance > max_distance:
                self._cursor = (each.from_x, each.from_y)
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
        self._cursor = cursor_backup

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

    def trim_borders(self):
        for point in self._points[::-1]:
            if (point.from_x > self.sizex) or (point.to_x > self.sizex) \
                    or (point.from_y > self.sizey) or (point.to_y > self.sizey):
                self._points.remove(point)
            if (point.from_x < 1) or (point.to_x < 1) \
                    or (point.from_y < 1) or (point.to_y < 1):
                self._points.remove(point)
        return self

    def create_graph(self):
        """
        Returns networksx object of the given connection point list

        Returns:
            nx.DiGraph:  Returns networkx object of the given ConnectionPointList

        """
        graph = nx.DiGraph(directed=True)
        for conn in self._points:
            from_node = "_%d_%d_" % conn.from_connection
            to_node = "_%d_%d_" % conn.to_connection
            graph.add_edge(from_node, to_node)
        return graph

    def merge(self, connectlist):
        '''
        Merges different ConnectPointList together into one Connect Point List

        Args:
            connectlist (ConnectPointList): provide with a ConnectPointList

        Returns:
            ConnectPointList: Return self object
        '''
        self._points.extend(connectlist.points)
        return self

    def scale(self, scale, anchor=(0, 0)):
        '''
        Scales the connect point list from an anchor position

        Args:
            scale: scale at which ConnectPointList is expanded
            anchor: (x,y) coordinates of an anchor point

        Returns:
            ConnectPointList: Return self object
        '''
        for point in self._points:
            point.scale_connection(scale, anchor)
        return self

    def translate(self, x, y):
        '''
        Moves the connect point list in x y coordinates

        Args:
            x(int): Steps in x-axis
            y(int): Steps in y-axis
        '''
        for point in self._points:
            point.translate_connection(x, y)
        return self

    def rotate(self, angle=0):
        '''
        Rotates the connect point list at right angles

        Args:
            angle (int): degree of rotations (0, 90, 180, 270, -90, -180, -270)

        Returns:
            ConnectPointList: Return self object
        '''
        angles = (0, 90, 180, 270, -90, -180, -270, 'CW', 'ACW')
        assert angle in angles, "Supports only %s degree rotations" % angles
        for point in self._points:
            point.rotate_connection(angle, sizex=self.sizex, sizey=self.sizey)
        return self

    def add_next_point(self, x, y):
        '''
        Adds the next point in the connect point list

        Args:
            x: next point x-axis coordinate
            y: next point y-axis coordinate

        Returns:
            ConnectPoint: Return new added point
        '''
        x_prev, y_prev = self._cursor
        point = ConnectPoint(x_prev, y_prev, x, y)
        self.add_connect_point(point)
        self._update_cursor()
        return point

    def move_cursor_x(self, value=1):
        '''
        Places the cursor on the specified x coordinate without connection

        Args:
            value: steps cursor moves in the x-axis
        '''
        self._cursor = self._cursor[0]+value, self._cursor[1]

    def move_cursor_y(self, value=1):
        '''
        Places the cursor on the specified y coordinate without connection

        Args:
            value: steps cursor moves in the y-axis
        '''
        self._cursor = self._cursor[0], self._cursor[1]+value

    def move_x(self, value=1, steps=1, color=DEFAULT_COLOR):
        ''' Moves cursor in x direction by specified steps times by specified value

        Args:
            value: specified value by which cursor moves in the x-axis
            steps: times cursor is moved
            color: specify the color of this connection e.g red, blue, green, etc.

        Returns:
            ConnectPointList: Return self object
        '''
        x_prev, y_prev = self._cursor
        for _ in range(steps):
            point = ConnectPoint(x_prev, y_prev, x_prev+value, y_prev)
            point.color = color
            self.add_connect_point(point)
            x_prev, y_prev = (x_prev+value, y_prev)
        self._update_cursor()
        return self

    def move_y(self, value=1, steps=1, color=DEFAULT_COLOR):
        '''
        Moves cursor in y direction by specified steps times by specified value

        Args:
            value: specified value by which cursor moves in the y-axis
            steps: times cursor is moved
            color: specify the color of this connection e.g red, blue, green, etc.

        Returns:
            self: return self object
        '''
        x_prev, y_prev = self._cursor
        for _ in range(steps):
            point = ConnectPoint(x_prev, y_prev, x_prev, y_prev+value)
            point.color = color
            self.add_connect_point(point)
            x_prev, y_prev = (x_prev, y_prev+value)
        self._update_cursor()
        return self

    def _update_cursor(self):
        if self._cursor_state:
            self._cursor = self._points[-1].to_connection
        return self._cursor

    def __str__(self):
        lines = ""
        for p in self._points:
            lines += str(p)
            lines += "\n"
        return lines

    def add_connect_point(self, point):
        '''
        Adds a connect point in the connect point list

        Args:
            point (ConnectPoint): It is a cConnectPoint object

        Returns:
            ConnectPoint: Returns new ConnectPoint
        '''

        assert isinstance(point, ConnectPoint)
        self._points.append(point)
        self._update_cursor()
        return point

    def add_connection(self, from_x, from_y, to_x, to_y):
        '''
        Creates a new connection at the given from and to points
        and add it to the connect point list

        Args:
            from_x (int): point on x coordinate from which connection starts
            from_y (int): point on y coordinate from which connection starts
            to_x (int): point on x coordinate where connection ends
            to_y (int): point on y coordinate where connection ends

        Returns:
            ConnectionPoint: New ConnectionPoint object
        '''
        point = ConnectPoint(from_x, from_y, to_x, to_y)
        self._points.append(point)
        self._update_cursor()
        return point

    def render_pattern(self, scale=20):
        '''
        This renderes connection points list in a SVG format

        Args:
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
                .connection{stroke-linecap:round; opacity: 0.7; stroke-width:1.2;}
                span{text-anchor: "middle"; alignment_baseline: "middle"}
                .gridLabels{fill: grey;font-style: italic;font-weight: 900}
                .down{stroke-dasharray: 5;}
                .up{stroke-dasharray: 5;}
                .top{stroke-dasharray: 5;}
                .gridmarker{stroke:red; stroke-width:0.2; opacity: 0.7;}
                """))
        # Add arrow marker
        DRMarker = dwg.marker(refX="30", refY="30",
                              viewBox="0 0 120 120",
                              markerUnits="strokeWidth",
                              markerWidth="5", markerHeight="10", orient="auto")
        DRMarker.add(dwg.path(d="M 0 0 L 60 30 L 0 60 z", fill="blue"))
        dwg.defs.add(DRMarker)

        # Add buffer marker
        buff_marker = dwg.marker(refX="30", refY="30",
                                 viewBox="0 0 120 120",
                                 markerUnits="strokeWidth",
                                 markerWidth="5", markerHeight="10", orient="auto")
        buff_marker.add(dwg.circle(center=(0, 0), r=60, fill="red"))
        dwg.defs.add(buff_marker)
        for conn in self._points:
            conn_new = conn*scale
            dwgMain.add(dwg.line(start=tuple(map(round, conn_new.from_connection)),
                                 end=tuple(map(round, conn_new.to_connection)),
                                 stroke=conn.color,
                                 marker_mid=buff_marker.get_funciri(),
                                 marker_end=DRMarker.get_funciri(),
                                 class_=f"connection {conn.level}"))
        return dwg

    def get_reference(self, netlist, x, y):
        '''
        Return reference for the given tile location
        '''
        inst = self.get_top_instance(netlist, x, y)
        return inst.reference.name if isinstance(inst, sdn.Instance) else inst

    def get_top_instance(self, netlist: sdn.Netlist, x, y):
        '''
        Return reference for the given tile location

        Returns:
            sdn.Instance: Returns SpyDrNet instance
        '''
        if 0 in (x, y):
            return "top"
        instance_name = self.get_top_instance_name(x, y)
        try:
            return next(netlist.top_instance.reference.get_instances(instance_name))
        except StopIteration:
            logger.exception("Instance not found %s", instance_name)

    def get_top_instance_name(self, x, y):
        '''
        Returns the instance from top_level design

        Returns:
            str: Instance name
        '''
        return "PlaceholderModule"

    def print_port_stat(self, netlist, filename=None):
        '''
        This print ports generation statistics
        '''
        stat = self.show_stats(netlist)
        output = []
        format_str = "{:25s} | {:>3} {:>3} {:>3} {:>3} | {:>3} {:>3} {:>3} {:>3}"
        default = {
            "left": 0, "right": 0, "top": 0, "bottom": 0
        }
        output.append("= "*32)
        output.append("{:25s} | {:^15} | {:^15}".format('Module', "In", "Out"))
        output.append(format_str.format('Module',
                                        "L", "R", "T", "B",
                                        "L", "R", "T", "B"))
        output.append("= "*32)
        for module, mstat in stat.items():
            output.append(format_str.format(
                module,
                mstat.get("in", default)["left"] or '-',
                mstat.get("in", default)["right"] or '-',
                mstat.get("in", default)["top"] or '-',
                mstat.get("in", default)["bottom"] or '-',
                mstat.get("out", default)["left"] or '-',
                mstat.get("out", default)["right"] or '-',
                mstat.get("out", default)["top"] or '-',
                mstat.get("out", default)["bottom"] or '-'))
        if filename:
            with open(filename, "w", encoding="UTF-8") as fp:
                fp.write("\n".join(output))
        return output

    def show_stats(self, netlist):
        '''
        Extracts the connectivity statistics for port and connection creation
        '''
        mstat = {}
        for point in self._points:

            if point.level in ["same", "down"]:
                from_conn = self.get_reference(netlist, *point.from_connection)
                mstat[from_conn] = mstat.get(from_conn, {})
                mstat[from_conn]["out"] = mstat[from_conn].get(
                    "out", {"left": 0, "right": 0, "top": 0, "bottom": 0})
                mstat[from_conn]["out"][point.direction(reverse=True)] += 1
            if point.level in ["same", "up", "top"]:
                to_conn = self.get_reference(netlist, *point.to_connection)
                mstat[to_conn] = mstat.get(to_conn, {})
                mstat[to_conn]["in"] = mstat[to_conn].get(
                    "in", {"left": 0, "right": 0, "top": 0, "bottom": 0})
                mstat[to_conn]["in"][point.direction(reverse=False)] += 1

        return OrderedDict((module, mstat[module]) for module in sorted(mstat))

    def create_ft_ports(self, netlist: sdn.Netlist, port_name: str, cable: sdn.Cable):
        '''
        Create feedthrough port on the given module

        Args:
            netlist (Netlist): netlist
            port (str): port name on each module
        '''

        for m_name, values in self.show_stats(netlist).items():
            if m_name == "top":
                continue
            # Get current module
            module: sdn.Definition = next(netlist.get_definitions(m_name))
            # Get the signal port if it exist in the cirrect module
            port: sdn.Port = next(module.get_ports(port_name), None)

            # Create input ports on the module
            prev_cable = None
            # rotate anti-clockwise and create input connections
            for inp in [k for k, v in values.get("in", {}).items() if v > 0]:
                module.create_port(f"{port_name}_{inp}_in",
                                   pins=cable.size, direction=sdn.IN)
                cable = module.create_cable(f"{port_name}_{inp}_in",
                                            wires=cable.size)
                if prev_cable:
                    prev_cable.assign_cable(cable)
                prev_cable = cable

            # if the port exist (which means signal is used in this port)
            # Create assignement statement fo the signal
            signal_net = prev_cable
            if prev_cable and port:
                prev_cable.assign_cable(next(port.get_cables()))
                signal_net = next(port.get_cables())

            prev_cable = None
            # rotate clockwise and create output connections
            for outp in [k for k, v in values.get("out", {}).items() if v > 0][::-1]:
                module.create_port(f"{port_name}_{outp}_out",
                                   pins=cable.size, direction=sdn.OUT)
                cable = module.create_cable(f"{port_name}_{outp}_out",
                                            wires=cable.size)
                if prev_cable:
                    cable.assign_cable(prev_cable)
                prev_cable = cable
            if prev_cable:
                signal_net.assign_cable(prev_cable)
            if port:
                module.remove_port(port)

    def create_ft_connection(self, netlist: sdn.Netlist, signal_cable: sdn.Instance,
                             down_port=None, up_port=None, top_cable=None):
        ''' Performs top level connection using connection file

        Args:
            netlist(sdn.Netlist): Top level netlist
            signal_cable(str): Current level signal port
            down_port(str) : Name of down level port
        '''
        signal = signal_cable.name
        cable = netlist.top_instance.reference.create_cable(signal+"_ft")
        for point in self._points:
            logger.debug("Evaluating Point %s", point)
            if point.level == "up":
                continue
            w = cable.create_wire()
            if point.level == "top":
                top_cable.assign_cable(cable,
                                       upper=len(cable.wires),
                                       lower=len(cable.wires)-1)
            elif (0 in point.from_connection) or \
                (self.sizex+1 == point.from_connection[0]) or \
                    (self.sizey+1 == point.from_connection[1]):
                signal_cable.assign_cable(cable,
                                          upper=w.get_index,
                                          lower=w.get_index)
            else:
                inst = self.get_top_instance(netlist, *point.from_connection)
                port_name = f"{signal}_{point.from_dir}_out"
                try:
                    w.connect_pin(next(inst.get_port_pins(port_name)))
                except AssertionError:
                    logger.warning("%s -> %s", inst.name,
                        next(inst.get_port_pins(port_name)).port.name)
                    w = next(inst.get_port_pins(port_name)).wire

            if 0 in point.to_connection or \
                    (self.sizex+1 == point.to_connection[0]) or \
                    (self.sizey+1 == point.to_connection[1]):
                signal_cable.assign_cable(
                    cable, upper=w.get_index, lower=w.get_index)
            else:
                inst = self.get_top_instance(netlist, *point.to_connection)
                if point.level in ["same", "down"]:
                    assert signal, "Singal is not defined for %s connection" % point.level
                port_name = {
                    "same": f"{signal}_{point.to_dir}_in",
                    "top": f"{signal}_{point.to_dir}_in",
                    "down": f"{down_port}_{point.to_dir}_in"}[point.level]
                logger.debug("Connecting to pin %s", port_name)
                w.connect_pin(next(inst.get_port_pins(port_name)))
        if len(cable.wires) > 0:
            netlist.top_instance.reference.remove_cable(cable)

    def print_instance_grid_map(self):
        """ Prints mapping beetween grid cordinates and top level instances """
        for y in range(self.sizey, 0, -1):
            for x in range(1, self.sizex+1):
                print(f"{self.get_top_instance_name(x, y):15}", end=" ")
            print("")

    def print_reference_grid_map(self, netlist: sdn.Netlist):
        """ Prints mapping beetween grid cordinates and top level instance refereneces """
        for y in range(self.sizey, 0, -1):
            for x in range(1, self.sizex+1):
                print(f"{self.get_reference(netlist, x, y):15}", end=" ")
            print("")

    def __iter__(self):
        yield from self._points

    def short_through(self, through_point):
        '''
        Short all the incoming connections to this point with outgoing connections

        Note: Connects the last found incoming and outgoing point in the list

        Args:
            through_point (tuple): point to short through
        '''
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
