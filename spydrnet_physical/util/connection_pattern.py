
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
import svgwrite
import math
from typing import List
from copy import deepcopy
from svgwrite.container import Group
import code


class ConnectPoint:
    ''' This store the individual connections points '''

    def __init__(self, from_x, from_y, to_x, to_y):
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y

    @property
    def connection(self):
        ''' return all four connection points '''
        return (self.from_x, self.from_y, self.to_x, self.to_y)

    @property
    def from_connection(self):
        ''' return from connection points '''
        return (self.from_x, self.from_y)

    @property
    def to_connection(self):
        ''' return to connection points '''
        return (self.to_x, self.to_y)

    def rotate_connection(self, angle, sizex=None, sizey=None):
        self.from_x, self.from_y = self._rotate_point(
            self.from_connection,
            angle=angle, sizex=sizex, sizey=sizey)
        self.to_x, self.to_y = self._rotate_point(
            self.to_connection,
            angle=angle, sizex=sizex, sizey=sizey)

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
        return "%5d %5d %5d %5d" % (self.from_x, self.from_y, self.to_x, self.to_y)

    def __mul__(self, scale):
        return ConnectPoint(scale*self.from_x, scale*self.from_y,
                            scale*self.to_x, scale*self.to_y)

    def __rmul__(self, scale):
        return ConnectPoint(scale*self.from_x, scale*self.from_y,
                            scale*self.to_x, scale*self.to_y)


class ConnectPointList:
    ''' This store list of connection points  '''

    def __init__(self, sizex=None, sizey=None, point=None):
        self.sizex = sizex
        self.sizey = sizey
        self._points: List[ConnectPoint] = []
        self._cursor = []
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
        return self._cursor[0]

    @property
    def get_y(self):
        return self._cursor[1]

    def flip(self):
        pass

    def rotate(self, angle=0):
        angles = (0, 90, 180, 270, -90, -180, -270, 'CW', 'ACW')
        assert angle in angles, "Supports only %s degree ratations" % angles
        for point in self._points:
            point.rotate_connection(angle, sizex=self.sizex, sizey=self.sizey)

    def add_next_point(self, x, y):
        x_prev, y_prev = self.points[-1].to_connection
        point = ConnectPoint(x_prev, y_prev, x, y)
        self.add_connect_point(point)
        self._update_cursor()
        return point

    def move_x(self, value=1):
        x_prev, y_prev = self.cursor
        point = ConnectPoint(x_prev, y_prev, x_prev+value, y_prev)
        self.cursor = (x_prev+value, y_prev)
        self.add_connect_point(point)
        self._update_cursor()
        return self.cursor

    def move_y(self, value=1):
        x_prev, y_prev = self.cursor
        point = ConnectPoint(x_prev, y_prev, x_prev, y_prev+value)
        self.cursor = (x_prev, y_prev+value)
        self.add_connect_point(point)
        self._update_cursor()
        return self.cursor

    def _update_cursor(self):
        self._cursor = self._points[-1].to_connection
        return self.cursor

    def __str__(self):
        lines = ""
        for p in self._points:
            lines += str(p)
            lines += "\n"
        return lines

    def add_connect_point(self, point):
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
        args:
            connect (list): collection connection pattern

        returns:
            str(str): return svg string
        '''
        sizex = max([max(x1, x2) for x1, y1, x2, y2 in self._points])+1
        sizey = max([max(x1, x2) for x1, y1, x2, y2 in self._points])+1

        svg = None
        # dwg = svgwrite.Drawing("_render.svg", style="border: 1px solid grey;")
        dwg = svgwrite.Drawing("_render.svg")
        dwg.viewbox(-5*scale, -1*(sizey+10)*scale,
                    (sizex+10)*scale, (sizey+10)*scale)

        dwgMarker = dwg.add(Group(id="markers",  transform="scale(1,-1)"))
        dwgMain = dwg.add(Group(id="main", transform="scale(1,-1)"))
        dwg.defs.add(dwg.style("""
                text{font-family: Verdana;}
                line{stroke: black;}
                #core_boundary{stroke:grey; stroke_width:0.5;}
                .marker{stroke:red; stroke_width:0.5;}
                """))
        for conn in self._points:
            conn = conn*scale
            dwgMain.add(dwg.line(start=conn.from_connection,
                                 end=conn.to_connection,
                                 class_="connection"))
        return dwg


class ConnectionPattern:
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

    @property
    def connections(self):
        return self._connect

    @connections.setter
    def connections(self, value):
        self._connect = value
        return self._connect

    def reset(self):
        self._connect = ConnectPointList(sizex=self.sizex,
                                         sizey=self.sizey)

    def get_htree(self):
        '''
        Returns HTree pattern fo the given grid size
        '''
        points = ConnectPointList()
        points.add_connection(1, 1, 1, 2)
        points.add_connection(10, 9, 10, 10)
        return points

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

    def render_pattern(self, scale=20, title=None):
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
                                       class_="marker"))
            for i in range(0, self.sizey+1):
                dwgMarker.add(dwg.line(start=(0.5*scale, (i+0.5)*scale),
                                       end=((self.sizex+0.5) *
                                            scale, (i+0.5)*scale),
                                       class_="marker"))
        title = title or f" %d x %d FPGA " % (self.sizex, self.sizey)
        dwgText.add(dwg.text(title,
                             insert=((self.sizex+1)*scale*0.5, -1*-0.5*scale),
                             transform="scale(1,-1)",
                             class_="moduleLabel",
                             fill="black",
                             font_size=self.sizey*scale*0.1,
                             alignment_baseline="middle",
                             text_anchor="middle"))
        dwg.viewbox(-1*scale, -1*(self.sizey+2)*scale,
                    (self.sizex+3)*scale, (self.sizey+3)*scale)
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
    conn_list = fpga.connections
    conn_list = fpga.get_fishbone()
    conn_list.rotate(0)
    fpga.render_pattern().save(pretty=True, indent=4)
