'''
'''

from copy import deepcopy


DEFAULT_COLOR = " black"


class ConnectPoint:
    '''
    This class stores information of each connection made in the grid.

    Each connection is strictly either vertical or horizontal,
    the diagonal connections are invalid. Following properties
    are store with each connection
    '''

    def __init__(self, from_x, from_y, to_x, to_y, color=DEFAULT_COLOR,
                 level="same"):
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
        self._level = level
        self._color = color
        self._buffer = False
        self._update_direction()

    @property
    def level(self):
        ''' Returns connection level '''
        return self._level

    @property
    def connection(self):
        ''' Return ``from`` and ``to`` connection points ()
        (``from_x``, ``from_y``, ``to_x``, ``to_y``)'''
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
    def distance(self):
        ''' return the connection distance '''
        return abs(self.from_x-self.to_x) + abs(self.from_y-self.to_y)

    @property
    def color(self):
        ''' return color of connection '''
        return self._color

    @property
    def is_buffered(self):
        ''' Returns connection level '''
        return bool(self._buffer)

    # @set_buffer.setter
    # def set_buffer(self):
    #     self._buffer = True

    # @remove_buffer.setter
    # def remove_buffer(self):
    #     self._buffer = False

    @from_connection.setter
    def from_connection(self, points):
        self.from_x, self.from_y = points
        return (self.from_x, self.from_y)

    @to_connection.setter
    def to_connection(self, points):
        self.to_x, self.to_y = points
        return (self.to_x, self.to_y)

    @color.setter
    def color(self, color):
        self._color = color
        return self._color

    @level.setter
    def level(self, value):
        ''' Sets connection level '''
        self._level = value
        return self._level

    def move(self, x=0, y=0):
        self.from_x += x
        self.from_y += y
        self.to_x += x
        self.to_y += y
        return self

    def flip_connection(self, orientation):
        '''
        This methods flips the connection depending upon the orientation,
        Valid arguments (V, H, v, h)

        Args:
            orientation (str): The orientation can be vertical or horizontal
        '''
        if orientation.lower() == "v":
            self.from_y *= -1
            self.to_y *= -1
        elif orientation.lower() == "h":
            self.from_x *= -1
            self.to_x *= -1
        else:
            raise Exception(orientation + " Orinetation is not supported" +
                            "Supported arguments (V, H, v, h)")

    def rotate_connection(self, angle, sizex=None, sizey=None):
        self.from_x, self.from_y = self._rotate_point(
            self.from_connection,
            angle=angle, sizex=sizex, sizey=sizey)
        self.to_x, self.to_y = self._rotate_point(
            self.to_connection,
            angle=angle, sizex=sizex, sizey=sizey)
        self._update_direction()

    def translate_connection(self, x, y):
        '''
        Translates the connection by given x and y value

        Args:
            x(int): Horizontal shift in the connection
            y(int): Vertical shift in the connection
        '''
        self.from_x, self.from_y = self.from_x + x, self.from_y+y
        self.to_x, self.to_y = self.to_x + x, self.to_y+y
        self._update_direction()

    def scale_connection(self, scale, anchor=(0, 0)):
        '''
        Scale up the connection by multipying the connection_from
        and connection_to coordinates with the scaling factor.

        This methd used to expand the exiting conenction

        Args:
            scale(int): Scale by which connection will be enlarged
        '''
        self.translate_connection(-1*anchor[0], -1*anchor[1])
        self.from_x, self.from_y = self.from_x * scale, self.from_y * scale
        self.to_x, self.to_y = self.to_x * scale, self.to_y * scale
        self.translate_connection(anchor[0], anchor[1])
        self._update_direction()

    def _update_direction(self):
        self.to_dir = self.direction()
        self.from_dir = self.direction(reverse=True)

    def direction(self, reverse=False):
        '''
        This method extracts the direction of the connection.

        Direction is derived by subtracting the x and y coordinates 
        of the to and from connection and 
        if the value of X is 0 and the value of Y is:
        >1 direction = Top <1 direction = Bottom
        and if the value of Y is 0 and X is
        >1 direction = Right <1 direction = Left
        It returns the actual and reversed (if reverse = True) direction of the connect point.

        Args:
            reverse(bool): Reverse the connection (default=false)

        Returns:
            str: Returns one of these strings ['right', 'left', 'bottom', 'top']

        '''
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
        '''
        Rotates the connection point by the given angle

        Args:
            angle (int): Valid angles are (0, 90, 180, 270, 360, -90, -180, -270, -360)

        Returns:
            tuple : (x, y) 

        '''
        x, y = point
        angle = (360 + int(angle)) if int(angle) < 0 else int(angle)
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

    def __str__(self):
        return "%5d %5d %5d %5d [%s]" % \
            (self.from_x, self.from_y, self.to_x, self.to_y, self._level)

    def __mul__(self, scale):
        '''
        Returns to and from coordinates after multipluing 
        them with the scaling factor
        '''
        pt = deepcopy(self)
        pt.from_connection = (scale*self.from_x, scale*self.from_y)
        pt.to_connection = (scale*self.to_x, scale*self.to_y)
        return pt

    def __rmul__(self, scale):
        '''
        Returns to and from coordinates after multipluing 
        them with the scaling factor
        '''
        pt = deepcopy(self)
        pt.from_connection = (scale*self.from_x, scale*self.from_y)
        pt.to_connection = (scale*self.to_x, scale*self.to_y)
        return pt
