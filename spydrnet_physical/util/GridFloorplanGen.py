
from svgwrite import Drawing
from svgwrite.container import Group

STYLE_SHEET = """
            line{stroke-width: 1; stroke: red;}
            .origin{fill:black}
            .grid_boundary{stroke-width: 1; stroke: grey; fill:lightgrey}
            """


class GridFloorplanGen:
    '''
    This class genrates generic floorplan for the grided design
    This is agnostics to the netlist or the design and just 
    consideres the grid size.

    paramters:

      GRID_X(int) : X-direction pitch
      GRID_Y(int) : Y-direction pitch
      grid_x_points(list(int)) : x-sample points on grid
      grid_y_points(list(int)) : y-sample points on grid
      grid_x_width(list(int)) : Each column widths
      grid_y_height(list(int)) : Each row height

    .. rst-class: ascii

    ::

        <--GRID_X-->
        +----------+----------+----------+----------+
        |          |          |          |          |
        |          |          |          |          |
        |          |          |          |          |
        +-------------------------------------------+
        |          |          |          |          |
        |          |          |          |          |
        |          |          |          |          |
        +-------------------------------------------+
        |          |          |          |          |
        |          |          |          |          |
        |          |          |          |          |
        +-------------------------------------------+
        |          |          |          |          |
        |          |          |          |          |
        |          |          |          |          |
        +-------------------------------------------+   ᐱ
        |          |          |          |          |   |
        |          |          |          |          | GRID_Y
        |          |          |          |          |   |
        +----------+----------+----------+----------+   ᐯ 

                    Grid Representation 

    '''

    def __init__(self, size_x, size_y) -> None:
        self.size_x = size_x
        self.size_y = size_y

        self.grid_x = 100
        self.grid_y = 100

        self.grid_x_width = [self.grid_x]*self.size_x
        self.grid_y_height = [self.grid_y]*self.size_y

        self.grid_x_points = [0]*(self.size_x+1)
        self.grid_y_points = [0]*(self.size_y+1)

        self.update_points()

    @property
    def width(self):
        return (self.grid_x_points[-1]-self.grid_x_points[0])

    @property
    def height(self):
        return (self.grid_y_points[-1]-self.grid_y_points[0])

    @property
    def offset_x(self):
        return self.grid_x_points[0]

    @property
    def offset_y(self):
        return self.grid_y_points[0]

    @offset_x.setter
    def offset_x(self, value):
        self.grid_x_points[0] = value
        self.update_points()
        return self.grid_x_points

    @offset_y.setter
    def offset_y(self, value):
        self.grid_y_points[0] = value
        self.update_points()
        return self.grid_y_points

    def create_grid(self):
        pass

    def set_column_width(self, col_number, value):
        """ Indexing starts from the bottom left corner """
        assert col_number != 0, "Indexing starts from 1"
        self.grid_x_width[col_number-1 if col_number >
                          0 else col_number] = value
        self.update_points()

    def set_row_height(self, row_number, value):
        """ Indexing starts from the bottom left corner """
        assert row_number != 0, "Indexing starts from 1"
        self.grid_y_height[row_number-1 if row_number >
                           0 else row_number] = value
        self.update_points()

    def update_points(self):
        for indx, width in enumerate(self.grid_x_width):
            self.grid_x_points[indx+1] = self.grid_x_points[indx] + width
        for indx, height in enumerate(self.grid_y_height):
            self.grid_y_points[indx+1] = self.grid_y_points[indx] + height

    def __str__(self) -> str:
        return " ".join(map(str, self.grid_x_points)) + \
            "\n" + " ".join(map(str, self.grid_y_points))

    def render_grid(self, filename=None) -> Drawing:
        # Default margin for the render
        margin_x = 100
        margin_y = 100

        # initialize SVGWRITE Drawing object
        dwg = Drawing(size=(self.width+(2*margin_x),
                            self.height+(2*margin_y)),
                      style="background:#F0F0F0")
        t_prop = {"transform": "scale(1,-1)"}
        dwgShapes = dwg.add(Group(id="mainShapes", **t_prop))
        dwg.defs.add(dwg.style(STYLE_SHEET))
        dwg.viewbox(self.grid_x_points[0]-margin_x,
                    -1*(self.grid_y_points[0]+margin_y+self.height),
                    self.width+(margin_x*2),
                    self.height+(margin_y*2))

        # Add main frame
        dwgShapes.add(dwg.rect(
            insert=(self.offset_x, self.offset_y),
            size=(self.width, self.height),
            class_="grid_boundary"))

        # Add horizontal lines
        for eachrow in self.grid_y_points:
            dwgShapes.add(dwg.line(start=(self.offset_x, eachrow),
                                   end=(self.offset_x+self.width, eachrow)))
        # Add vertical lines
        for eachcol in self.grid_x_points:
            dwgShapes.add(dwg.line(start=(eachcol, self.offset_y),
                                   end=(eachcol, self.offset_y+self.height)))
        dwg.add(dwg.rect(insert=(0, 0), size=(10, 10), class_="origin"))
        return dwg
