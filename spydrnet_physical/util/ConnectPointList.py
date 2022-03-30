
import math
from copy import deepcopy
from shutil import move
from typing import List
import logging

import networkx as nx
import spydrnet as sdn
import svgwrite
from spydrnet_physical.util import ConnectPoint
from svgwrite.container import Group

DEFAULT_COLOR = " black"

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


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
        return self._cursor

    @property
    def get_x(self):
        ''' returns x location of cursor '''
        return self._cursor[0]

    @property
    def get_y(self):
        ''' returns y location of cursor '''
        return self._cursor[1]

    def set_cursor(self, x, y):
        self._cursor = (x, y)
        return self

    def set_color(self, color):
        ''' Set color to all the points in the connection list '''
        for each in self._points:
            each.color = color
        return self

    def store_points(self, filename):
        ''' Stores all points and its attributes in csv format in the file '''
        raise NotImplementedError

    def validate_connectivity(self):
        """
        This fucntion checks following

        * If there is any connection coming outside from range (0-sizex+1) or (0-sizey+1)
        * If there is any redundant connections
        """
        raise NotImplementedError

    def load_points(self, filename):
        ''' Loads all points and its attributes from the given csv file 

        Format: from_x, from_y, to_x, to_y, level, color
        '''
        raise NotImplementedError

    def search_from_point(self, point):
        for pt in self._points:
            if (pt.from_connection == point):
                return pt

    def search_to_point(self, point):
        for pt in self._points:
            if (pt.to_connection == point):
                return pt

    def push_connection_down(self, point):
        if isinstance(point, tuple):
            point = self.search_to_point(point)
        point.level = "down"
        return point

    def pull_connection_up(self, point):
        if isinstance(point, tuple):
            point = self.search_from_point(point)
        point.level = "up"
        return point

    def make_top_connection(self, point):
        if isinstance(point, tuple):
            point = self.search_from_point(point)
        point.level = "top"
        return point

    def reset_level(self, point):
        assert isinstance(point, ConnectPoint), \
            "point should be instance of ConnectPoint class not " + type(point)
        point.level = "same"

    def hold_cursor(self):
        ''' Holds the cursor at current position '''
        self._cursor_state = False

    def release_cursor(self):
        ''' Rleases cursor and moves with each point addition '''
        self._cursor_state = True

    def flip(self, orientation="H", base=None):
        """ Flips all the points horizontally or vertically"""
        for point in self._points:
            point.flip_connection(orientation)
        return self

    def sample_connections(self, max_distance=1):
        ''' This method splits all the connections longer that ``max_distance`` to
        at max ``max_distance`` length
        '''
        cursor_backup = self._cursor
        for indx, each in enumerate(self._points):
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
        graph = nx.DiGraph(directed=True)
        node = 0
        for conn in self._points:
            from_node = f"_%d_%d_" % conn.from_connection
            to_node = f"_%d_%d_" % conn.to_connection
            graph.add_edge(from_node, to_node)
        return graph

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

    def move_cursor_x(self, value=1):
        self._cursor = self._cursor[0]+value, self._cursor[1]

    def move_cursor_y(self, value=1):
        self._cursor = self._cursor[0], self._cursor[1]+value

    def move_x(self, value=1, steps=1, color=DEFAULT_COLOR):
        ''' Moves cursor in x direction by specified steps times by specified value'''
        x_prev, y_prev = self._cursor
        for _ in range(steps):
            point = ConnectPoint(x_prev, y_prev, x_prev+value, y_prev)
            point.color = color
            self.add_connect_point(point)
            x_prev, y_prev = (x_prev+value, y_prev)
        self._update_cursor()
        return self

    def move_y(self, value=1, steps=1, color=DEFAULT_COLOR):
        ''' Moves cursor in y direction by specified steps times by specified value'''
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
                .connection{stroke-linecap:round; opacity: 0.7; stroke-width:1.2;}
                span{text-anchor: "middle"; alignment_baseline: "middle"}
                .gridLabels{fill: grey;font-style: italic;font-weight: 900}
                .down{stroke-dasharray: 5;}
                .up{stroke-dasharray: 5;}
                .gridmarker{stroke:red; stroke-width:0.2; opacity: 0.7;}
                """))
        DRMarker = dwg.marker(refX="30", refY="30",
                              viewBox="0 0 120 120",
                              markerUnits="strokeWidth",
                              markerWidth="5", markerHeight="10", orient="auto")
        DRMarker.add(dwg.path(d="M 0 0 L 60 30 L 0 60 z", fill="blue"))
        dwg.defs.add(DRMarker)
        for conn in self._points:
            conn_new = conn*scale
            dwgMain.add(dwg.line(start=conn_new.from_connection,
                                 end=conn_new.to_connection,
                                 stroke=conn.color,
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
            logger.exception("Instance not found " + instance_name)

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
        format_str = "{:15s} | {:>3} {:>3} {:>3} {:>3} | {:>3} {:>3} {:>3} {:>3}"
        default = {
            "left": 0, "right": 0, "top": 0, "bottom": 0
        }
        output.append("= "*26)
        output.append("{:15s} | {:^15} | {:^15}".format('Module', "In", "Out"))
        output.append(format_str.format('Module',
                                        "L", "R", "T", "B",
                                        "L", "R", "T", "B"))
        output.append("= "*26)
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
            with open(filename, "w") as fp:
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

        return mstat

    def create_ft_ports(self, netlist: sdn.Netlist, port_name: str, cable: sdn.Cable):
        '''
        Create feedthrough port on the given module

        args:
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
            if point.level == "up":
                continue
            w = cable.create_wire()
            if (0 in point.from_connection) or \
                (self.sizex+1 == point.from_connection[0]) or \
                    (self.sizey+1 == point.from_connection[1]):
                signal_cable.assign_cable(cable,
                                          upper=w.get_index,
                                          lower=w.get_index)
            elif point.level == "top":
                signal_cable.assign_cable(top_cable)
            else:
                inst = self.get_top_instance(netlist, *point.from_connection)
                port_name = f"{signal}_{point.from_dir}_out"
                w.connect_pin(next(inst.get_port_pins(port_name)))

            if 0 in point.to_connection or \
                    (self.sizex+1 == point.to_connection[0]) or \
                    (self.sizey+1 == point.to_connection[1]):
                signal_cable.assign_cable(
                    cable, upper=w.get_index, lower=w.get_index)
            else:
                inst = self.get_top_instance(netlist, *point.to_connection)
                port_name = {
                    "same": f"{signal}_{point.to_dir}_in",
                    "top": f"{signal}_{point.to_dir}_in",
                    "down": f"{down_port}_{point.to_dir}_in"}[point.level]
                w.connect_pin(next(inst.get_port_pins(port_name)))

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
