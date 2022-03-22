"""
This script implements simple floorplanning visualisation using SVG images.

The visualizer uses the information stored in each verilog object (as a PROP)
to perform shaping and placement of each block.
but there is no explicit routing performed,
all the edges are connected from point to point.

Detail of properties on different objects

**On Definitions**

``SHAPE`` =  Shape of the module [`Rect` (Default), `RectL`]

``WIDTH`` and ``HEIGHT`` = The rectangular dimension of the module (if Shape is `Rect`)

``A``, ``B`` , ``C`` , ``D`` , ``E``, ``F``  =
Dimensions of the rectilinear block (if shape is `RectL`)

.. rst-class:: ascii

::

                    d
                ┌──────────┐
                │          │
               c│          │
            b   │          │   e
         ┌──────┘          └──────┐
         │                        │
        a│           0            │
         │                        │
         └──────┐          ┌──────┘
                │          │
               f│          │
                │          │
                └──────────┘
                RectL Shape


**On Instances**

``LOC_X`` and ``LOC_Y`` = Location of the component with respect to its parrent


**On Ports**:

``SIDE``:
Shape sice where module port is placed [left/right/bottom/top]

``SIDE2``:
Optional and valid only when shape in RectL [left/right/bottom/top]

``OFFSET``:
Offset from the origin of that side
First point on respective side in clockwise direction is considered as origin


.. rst-class:: ascii

::

                       top/top
                     ┌──────────┐
            top/left │          | top/right
                     │          │
           left/top  │          │ right/top
              ┌──────┘          └──────┐
              │                        │
    left/left │           0            │ right/right
              │                        │
              └──────┐          ┌──────┘
        left/bottom  │          │ right/bottom
                     │          │
         bottom/left │          | bottom/right
                     └──────────┘
                    bottom/bottom

        Representing SIDE/SIDE2 parameters



**TODO** Add Some sort of a cordinate transformation which scaleX and scaleY.
All the inputs are in mutliple of SC_HEIGHT and SC_WIDTH, default value
of these variables is set to 1



"""

import logging
import os

import spydrnet as sdn
from matplotlib.pyplot import text
from spydrnet.ir.outerpin import OuterPin
from svgwrite import Drawing
from svgwrite.container import Group, Symbol
from svgwrite.shapes import Polyline

logger = logging.getLogger('spydrnet_logs')
base_dir = os.path.dirname(os.path.abspath(__file__))
PROJ_BASE_DIR = os.path.abspath(os.path.join(base_dir, ".."))

PROP = "VERILOG.InlineConstraints"

PIN_H = 4
PIN_W = 4

TOP_PIN = 1
BOTTOM_PIN = 2
LEFT_PIN = 3
RIGHT_PIN = 4

STYLE_SHEET = """
            text{font-family: Verdana; font-size: 5px;}
            .module_boundary{stroke:grey; stroke-width:1;opacity: 0.8}
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
        """


class FloorPlanViz:
    '''
    Implmenetation of SVG Visualiser `floorplan_visualizer <reference/visualization/floorplan_visualizer.rst>`_ 
    '''

    def __init__(self, definition, viewbox=(0, 0, 1000, 1000)):
        """
        Initialise the class with definition to render.

        Optionally, provide the Height and Width if its not set on the definition
        itself
        """
        self.module = definition
        self.def_list = {}  # Stores symbol refrences
        self.view_w = 0  # This variable tracks the maximum width of the SVG
        self.view_h = 0  # This variable tracks the maximum height of the SVG
        self.skip_pins = True

        self.custom_style = None
        # Create SVG drawing
        self.dwg = Drawing()
        self.dwg.viewbox(*viewbox)
        # Create groups in SVG image
        self.dwgbg = self.dwg.add(Group(id="bg"))
        self.core = self.dwg.add(Group(id="mainframe"))
        t_prop = {"transform": "scale(1,-1)"}
        self.dwgShapes = self.core.add(Group(id="mainShapes", **t_prop))
        self.dwgText = self.core.add(Group(id="mainText", **t_prop))
        self.dwgEdges = self.core.add(Group(id="edges", **t_prop))


    @property
    def custom_style_sheet(self):
        '''
        Return custom styles added in this visualiazer
        '''
        return self.custom_style

    @custom_style_sheet.setter
    def custom_style_sheet(self, value):
        '''
        Adds custom styles in this visualizer
        '''
        self.custom_style = value

    def compose(self, skip_connections=False,
                skip_pins=False,
                filter_cables=(lambda x: True)) -> Drawing:
        '''
        Entry point to generate final SVG file

        args:
            skip_connections(bool) : Skip rednering connections beetween modules
            skip_pins(bool) :Skip rendering modules pins  
            filter_cables(Callable): A callable function which filters the connections to redner
        '''
        # Create symbol for top-module and add in svg
        self.skip_pins = skip_pins
        self.add_symbol(self.module)
        self.add_top_block(self.module)

        # Iterate over all the instaces and place
        for child in self.module.children:
            self.add_symbol(child.reference)
            self.add_block(child)

        if skip_connections:
            return
        # create connections
        for cable in self.module.get_cables():
            if not filter_cables(cable):
                continue
            if cable.size:
                points = []
                # Extract all connection points
                for p in cable.wires[0].pins:
                    x, y = 0, 0
                    if isinstance(p, OuterPin):
                        x = int(p.instance.data[PROP].get("LOC_X", 0))
                        y = int(p.instance.data[PROP].get("LOC_Y", 0))
                        m = p.instance.reference
                        x += int(m.data[PROP].get(f"{p.port.name}_X", 0))
                        y += int(m.data[PROP].get(f"{p.port.name}_Y", 0))
                    else:
                        x = int(self.module.data[PROP].get(
                            f"{p.port.name}_X", 0))
                        y = int(self.module.data[PROP].get(
                            f"{p.port.name}_Y", 0))
                    points.append((x, y))
                # if connections found connect them in sequence
                if(points):
                    self.dwgEdges.add(
                        Polyline(points, fill="none",
                                 class_="edge",
                                 stroke="black",
                                 onmousemove=f"showTooltip(evt, '{cable.name}');",
                                 onmouseout="hideTooltip();",
                                 stroke_width="1"))
        return self.dwg

    def add_top_block(self, top_module):
        """
        Adds top level block in the design 
        """
        name = top_module.name
        defDict = self.def_list[name]
        self.dwgShapes.add(self.dwg.use(defDict["instance"],
                                        class_=f"topModule",
                                        insert=(0, 0)))
        self.dwgText.add(self.dwg.text(defDict["name"],
                                       insert=(defDict["width"]*0.5,
                                               -1*defDict["height"]*0.1),
                                       fill="black",
                                       transform="scale(1,-1)",
                                       alignment_baseline="middle",
                                       text_anchor="middle"))
        self._update_viewbox(defDict["width"], defDict["height"])

    def add_symbol(self, module):
        """
        Inserts symbols in the SVG file
        """
        if "ASSIG" in module.name:
            return
        if self.def_list.get(module.name, None):
            return self.def_list[module.name]
        shape = module.data[PROP].get("SHAPE", "rect")
        if shape.lower() == "rectl":
            new_def = self._add_rect_linear_symbol(module)
        else:
            new_def = self._add_rect_symbol(module)
        self.dwg.defs.add(new_def)
        return new_def

    def add_block(self, instance):
        """
        Iterates over each instance and adds them in SVG file
        """
        name = instance.reference.name
        if "ASSIG" in name:
            return
        defDict = self.def_list[name]

        loc_x = int(instance.data[PROP].get("LOC_X", 0))
        loc_y = int(instance.data[PROP].get("LOC_Y", 0))

        self.dwgShapes.add(self.dwg.use(defDict["instance"],
                                        class_=f"{instance.name}",
                                        insert=(loc_x, loc_y)))

        module_name = self.dwg.tspan(text=f"[{instance.reference.name}]",
                                     insert=self._get_label_location(instance),
                                     dy=["1.2em", ])
        
        module_text = self.dwg.text(f"{instance.name}",
                                    insert=self._get_label_location(instance),
                                    transform="scale(1,-1)",
                                    fill="black",
                                    alignment_baseline="middle",
                                    text_anchor="middle")
        module_text.add(module_name)
        
        module_label = instance.reference.data[PROP].get('LABEL', None)
        if module_label:
            module_text.add(self.dwg.tspan(
                insert=self._get_label_location(instance),
                text=f"{module_label}",
                dy=["2.4em", ]))

        self.dwgText.add(module_text)

    def _get_label_location(self, instance) -> tuple:
        '''
        Return the label location given the verilog instance 

        Always in the center of the shape
        '''
        defDict = self.def_list[instance.reference.name]
        loc_x = int(instance.data[PROP].get("LOC_X", 0))
        loc_y = int(instance.data[PROP].get("LOC_Y", 0))
        loc_x += defDict["width"]*0.5
        loc_y += defDict["height"]*0.5
        loc_y *= -1
        return (loc_x, loc_y)

    # ===================================================
    #        Methods for shapes and pin addition
    # ===================================================
    def _add_rect_symbol(self, module: sdn.Definition) -> None:
        width = int(module.data[PROP].get("WIDTH", 10))
        height = int(module.data[PROP].get("HEIGHT", 10))
        COLOR = module.data[PROP].get("COLOR", "#f4f0e6")
        new_def = self.dwg.symbol(id=module.name)
        self.def_list[module.name] = {
            "name": module.name,
            "instance": new_def,
            "shape": "rect",
            "points": None,
            "width": width,
            "height": height,
        }
        new_def.add(self.dwg.rect(insert=(1, 1),
                                  size=(width-1, height-1),
                                  fill=COLOR,
                                  class_=f"module_boundary {module.name}"))
        if not self.skip_pins:
            self._add_rect_symbol_pins(module, new_def)
        return new_def

    def _add_rect_linear_symbol_pins(self, module: sdn.Definition, new_def: Symbol) -> None:
        '''
        Adds ``rect_linear`` modules in the SVG symbol list
        '''
        a, b, c, d, e, f = map(int, module.data[PROP].get("POINTS", [10]*6))
        width = b+d+e
        height = a+c+f

        for port in module.ports:
            p = port.name
            SIDE = port.data[PROP].get(f"SIDE", "center")
            SIDE2 = port.data[PROP].get(f"SIDE2", "center")
            OFFSET = int(port.data[PROP].get(f"OFFSET", 0))

            LOC_X, LOC_Y, PIN_DIR = {
                "left": {
                    "top": (OFFSET, a+f, TOP_PIN),
                    "bottom": (OFFSET, f, BOTTOM_PIN),
                    "center": (0, f+OFFSET, LEFT_PIN),
                },
                "right": {
                    "top": (b+d+OFFSET, a+f, TOP_PIN),
                    "bottom": (b+d+OFFSET, f, BOTTOM_PIN),
                    "center": (width, f+OFFSET, RIGHT_PIN),
                },
                "bottom": {
                    "left": (b, OFFSET, LEFT_PIN),
                    "right": (b+d, OFFSET, RIGHT_PIN),
                    "center": (b+OFFSET, 0, BOTTOM_PIN),
                },
                "top":  {
                    "left": (b, a+f+OFFSET, LEFT_PIN),
                    "right": (b+d, a+f+OFFSET, RIGHT_PIN),
                    "center": (b+OFFSET, height, TOP_PIN),
                },
                "center": {
                    "center": (width*0.5, height*0.5, TOP_PIN)
                }}[SIDE][SIDE2]

            pin_w, pin_h, mult = (PIN_W, PIN_H, -1) if PIN_DIR in [LEFT_PIN, RIGHT_PIN] \
                else (PIN_H, PIN_W, 1)

            new_def.add(self.dwg.rect(insert=(LOC_X-pin_w*0.5, LOC_Y-pin_h*0.5),
                                      size=(pin_w, pin_h),
                                      class_=f"module_pin {str(port.direction).split('.')[-1].lower()}_pin",
                                      onmousemove=f"showTooltip(evt, '{port.name}');",
                                      onmouseout="hideTooltip();",
                                      stroke_width=0))
            new_def.add(self.dwg.text(port.name,
                                      insert=(LOC_X-pin_w*0.5,
                                              mult * (LOC_Y-pin_h*0.5)),
                                      class_=f"pin {SIDE}_pin {SIDE2}_pin",))

            module.data[PROP][f"{p}_X"] = LOC_X
            module.data[PROP][f"{p}_Y"] = LOC_Y

    def _add_rect_linear_symbol(self, module: sdn.Definition) -> None:
        a, b, c, d, e, f = map(int, module.data[PROP].get("POINTS", [10]*6))
        COLOR = module.data[PROP].get("COLOR", "#f4f0e6")
        new_def = self.dwg.symbol(id=module.name)
        self.def_list[module.name] = {
            "name": module.name,
            "instance": new_def,
            "shape": "rectl",
            "a": a, "b": b, "c": c,
            "d": d, "e": e, "f": f,
            "width": b+d+e,
            "height": a+c+f,
        }
        path = f"M {b} 0 v {f} h {-1*b} v {a} h {b} "
        path += f" v {c} h {d} v {-1*c} h {e} v {-1*a} "
        path += f" h {-1*e} v {-1*f} Z"
        path += f" Z"
        logger.debug("")
        new_def.add(self.dwg.path(d=path,
                                  fill=COLOR,
                                  class_=f"module_boundary {module.name}"))
        if not self.skip_pins:
            self._add_rect_linear_symbol_pins(module, new_def)
        return new_def

    def _add_rect_symbol_pins(self, module: sdn.Definition, new_def: Symbol) -> None:
        '''
        Adds pins on the rectangular shpapes
        '''
        width = int(module.data[PROP].get("WIDTH", 10))
        height = int(module.data[PROP].get("HEIGHT", 10))
        for port in module.ports:
            p = port.name
            SIDE = port.data[PROP].get(f"SIDE", [])
            OFFSET = int(port.data[PROP].get(f"OFFSET", 0))

            if 'left' in SIDE:
                LOC_X, LOC_Y = 2, OFFSET
                pin_w, pin_h = PIN_W, PIN_H
                mult = -1
            elif 'right' in SIDE:
                LOC_X, LOC_Y = width-1, height-OFFSET
                pin_w, pin_h = PIN_W, PIN_H
                mult = -1
            elif 'bottom' in SIDE:
                LOC_X, LOC_Y = width-OFFSET+1, 2
                pin_w, pin_h = PIN_H, PIN_W
                mult = 1
            elif 'top' in SIDE:
                LOC_X, LOC_Y = width-OFFSET+1, height-1-PIN_W
                pin_w, pin_h = PIN_H, PIN_W
                mult = 1
            else:
                LOC_X, LOC_Y = width/2, height/2
                pin_w, pin_h = PIN_W, PIN_H
                mult = -1
            new_def.add(self.dwg.rect(insert=(LOC_X-pin_w*0.5, LOC_Y-pin_h*0.5),
                                      size=(pin_w, pin_h),
                                      class_=f"module_pin {str(port.direction).split('.')[-1].lower()}_pin",
                                      onmousemove=f"showTooltip(evt, '{port.name}');",
                                      onmouseout="hideTooltip();",
                                      stroke_width=0))
            new_def.add(self.dwg.text(port.name,
                                      insert=(LOC_X-pin_w*0.5, mult *
                                              (LOC_Y-pin_h*0.5)),
                                      class_=f"pin {SIDE}_pin",))

            # transform=f"translate({OFF_X}, {OFF_Y}) rotate({ROT}) " + "scale(1,-1)",
            module.data[PROP][f"{p}_X"] = LOC_X
            module.data[PROP][f"{p}_Y"] = LOC_Y

    # ===================================================
    #              SVG Rendering Related
    # ===================================================

    def _update_viewbox(self, x, y):
        '''
        Updates the view box x and y value provided before saving image

        '''
        self.view_w = self.view_w if self.view_w > x else x
        self.view_h = self.view_h if self.view_h > y else y

    def add_stylehseet(self):
        '''
        Adds custom stylesheet to the SVG image
        '''
        self.dwg.defs.add(self.dwg.style(STYLE_SHEET))
        if self.custom_style:
            self.dwg.defs.add(self.dwg.style(self.custom_style))

    def _add_background(self, bgColor="#FFF"):
        self.dwgbg.add(self.dwg.rect(insert=(-25, -25),
                                     size=(self.view_w+50,
                                           self.view_h+50),
                                     id=f"background",
                                     fill=bgColor,
                                     stroke_width=0))
        self.dwg.viewbox(-50, -1*(self.view_h+100),
                         self.view_w+100, self.view_h+100)

    def get_svg(self):
        '''
        Returns SVG string of the current floorplan
        '''
        self.add_stylehseet()
        self._add_background()
        return self.dwg

    def get_html(self):
        '''
        Adds the SVG image to HTML page which supports zoom and pan control using d3.js
        '''
        self.get_svg()
        static_root = os.path.join(PROJ_BASE_DIR, "support_files")
        with open(os.path.join(static_root, "html_templates",
                               "svg_render.html"), "rb") as fp:
            content = fp.read()

        script = """function load_svg() {
            d3.select("#svgViewer").html(`%s`)}""" % self.dwg.tostring()

        content = content.replace(
            'onload="init_websocket();"'.encode(),
            'onload="load_svg();"'.encode(),
        )
        content = content.replace(
            '// <ADDITIONAL JS>'.encode(),
            script.encode(),
        )
        return content
