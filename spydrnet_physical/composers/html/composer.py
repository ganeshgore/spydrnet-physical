from collections import deque, OrderedDict
from spydrnet.ir import instance
from spydrnet.ir.outerpin import OuterPin
from spydrnet.util import selection
from spydrnet.ir.port import Port
from spydrnet.ir.cable import Cable
import json
from itertools import chain
from spydrnet.ir.innerpin import InnerPin
from copy import deepcopy
from collections import OrderedDict
import spydrnet.parsers.verilog.verilog_tokens as vt
from spydrnet_physical.composers.html.SpyDrNetEncoder import SpyDrNetJSONEncoder


def InputFilter(x): return x.direction == Port.Direction.IN


def OutputFilter(x): return (x.direction == Port.Direction.OUT) or (
    x.direction == Port.Direction.INOUT)


class HTMLComposer:

    def __init__(self, definition_list=None, write_blackbox=False):
        self.file = None
        self.direction_string_map = dict()
        self.direction_string_map[Port.Direction.IN] = "INPUT"
        self.direction_string_map[Port.Direction.OUT] = "OUTPUT"
        self.direction_string_map[Port.Direction.INOUT] = "INPUT"
        self.direction_side_map = dict()
        self.direction_side_map[Port.Direction.IN] = "WEST"
        self.direction_side_map[Port.Direction.OUT] = "EAST"
        self.direction_side_map[Port.Direction.INOUT] = "WEST"
        self.depth = 2
        self.write_blackbox = write_blackbox
        self.definition_list = definition_list
        self.ElkJSON = ''
        self.edgeID = 1
        self.ModuleList = {}
        self.top_instance = None

    def run(self, ir, file_out="out.v"):
        """ Main method to run composer """
        self.file = file_out
        self._compose(ir)

    def _get_default_module_template(self, name, defName):
        od = OrderedDict()
        od["id"] = name
        od["ports"] = []
        od["_children"] = []
        od["_edges"] = []
        od["hwMeta"] = {"bodyText": defName, "cls": "Process", }
        od["properties"] = {
            "org.eclipse.elk.layered.mergeEdges": 1,
            "org.eclipse.elk.portConstraints": "FIXED_SIDE"
        }
        return od

    def _get_default_port_template(self, portInstance):
        od = OrderedDict()
        od["id"] = portInstance.name
        od["direction"] = self.direction_string_map[portInstance.direction]
        od["hwMeta"] = {"name": portInstance.name}
        od["properties"] = {
            "index": 1,
            "side": self.direction_side_map[portInstance.direction]
        }
        return od

    def _get_default_net_template(self, cable_name):
        od = OrderedDict()
        od["id"] = cable_name
        od["hwMeta"] = {"name": cable_name, "cssClass": "link-style0"}
        od["sources"] = []
        od["targets"] = []
        return od

    def _create_top_frame(self):
        od = OrderedDict()
        od["id"] = "top_frame"
        od["ports"] = []
        od["children"] = []
        od["edges"] = []
        od["hwMeta"] = {}
        od["properties"] = {
            "org.eclipse.elk.layered.mergeEdges": 1,
            "org.eclipse.elk.portConstraints": "FIXED_SIDE"
        }
        return od

    def _create_top_block(self, name="unnamed"):
        od = OrderedDict()
        od["id"] = self.top_instance
        od["ports"] = []
        od["_children"] = []
        od["_edges"] = []
        od["hwMeta"] = {"bodyText": self.top_instance,
                        "cls": "Process"}
        od["properties"] = {
            "org.eclipse.elk.layered.mergeEdges": 1,
            "org.eclipse.elk.portConstraints": "FIXED_SIDE"
        }
        return od

    def _create_component_body(self, hinstance, node):
        """ This creates the component body with input and Output ports
        children and edges kept empty to fill up later
        """
        instance = hinstance.item

        for eachPort in chain(instance.get_ports(filter=InputFilter), instance.get_ports(filter=OutputFilter)):
            portNode = self._get_default_port_template(eachPort)
            portNode["id"] = hinstance.name + "/" + portNode["id"]
            node["ports"].append(portNode)

    def _create_top_component_tree(self, netlist, curr_pointer, depth):
        if depth > self.depth:
            return
        for eachTopLInst in netlist.get_hinstances():
            node = self._get_default_module_template(
                eachTopLInst.name,
                eachTopLInst.item.name)
            self._create_component_body(eachTopLInst, node)
            curr_pointer["_children"].append(node)
            # for child in eachTopLInst.get_hinstances():
            self._create_top_component_tree(eachTopLInst, node, depth+1)
        self._add_edges(netlist, curr_pointer)

    def _add_edges(self, netlist, curr_pointer):
        for eachCable in netlist.get_hcables():
            hWires = list(eachCable.get_hwires())
            edge = self._get_default_net_template(eachCable.name)
            if eachCable.item.size == 0:
                continue
            elif (eachCable.item.size == 1) or eachCable.item.check_concat():
                edge["id"] = self.edgeID
                self.edgeID += 1
                for indx, eachPin in enumerate(hWires[0].get_hpins()):
                    if eachCable.item.size > 1:
                        edge["hwMeta"]["cssClass"] = "link-style1"
                    ePinN = eachPin.item.port.name if isinstance(
                        eachPin.item, InnerPin) else eachPin.item.inner_pin.port.name
                    source = "/".join(eachPin.name.split("/")
                                      [:-1]) or self.top_instance

                    if indx == 0:
                        edge["sources"].append([source, source+"/"+ePinN])
                    else:
                        edge["targets"].append([source, source+"/"+ePinN])

                curr_pointer["_edges"].append(edge)

    def _create_top_level_ports(self, port, node):
        topPortNode = self._get_default_module_template(port.name, port.name)
        portNode = self._get_default_port_template(port)
        topPortNode["hwMeta"]['isExternalPort'] = True
        topPortNodePort = portNode
        topPortNodePort["hwMeta"]["name"] = ""
        topPortNodePort["direction"] = self.direction_string_map[Port.Direction.OUT if (
            port.direction == Port.Direction.IN) else Port.Direction.IN]
        topPortNodePort["properties"]["side"] = "WEST" if topPortNodePort["properties"]["side"] == "EAST" else "EAST"
        topPortNode["ports"].append(topPortNodePort)
        topPortNode["id"] += "_port"
        node["children"].append(topPortNode)
        topPortConn = self._get_default_net_template(f"{port.name}_conn")
        topPortConn["sources"].append(
            [self.top_instance, f"{self.top_instance}/{port.name}"])
        topPortConn["targets"].append([f"{port.name}_port", port.name])
        node["edges"].append(topPortConn)

    def _compose(self, netlist):
        """ Identifies the top level instance """
        instance = netlist.top_instance
        self.top_instance = instance.name
        assert instance != None, " Missing top instance "
        self.ElkJSON = self._create_top_frame()
        TopNode = self._create_top_block(instance.name)
        self.ElkJSON["children"].append(TopNode)

        for eachPort in chain(instance.get_ports(filter=InputFilter), instance.get_ports(filter=OutputFilter)):
            portNode = self._get_default_port_template(eachPort)
            portNode["id"] = self.top_instance + "/" + portNode["id"]
            TopNode["ports"].append(portNode)
            self._create_top_level_ports(eachPort, self.ElkJSON)

        self._create_top_component_tree(netlist, TopNode, 1)
        self.ElkJSON["hwMeta"]["maxId"] = self.edgeID
        self._write_html()

    def _write_json(self):
        return str(json.dumps(self.ElkJSON, cls=SpyDrNetJSONEncoder,
                              sort_keys=False, indent=2))

    def _write_html(self):
        fp = open(self.file, "w")
        fp.write("""
        <!DOCTYPE html><html><head>
        <meta charset="utf-8">
        <title>SpyDrNet Schematic Render</title>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.0.2/d3.js"></script>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/elkjs@0.7.0/lib/elk.bundled.js"></script>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/d3-hwschematic@0.1.6/dist/d3-hwschematic.js"></script>
        <link href="https://cdn.jsdelivr.net/npm/d3-hwschematic@0.1.6/dist/d3-hwschematic.css" rel="stylesheet">
        <style> body { margin: 0; background-color: white; } </style> </head>
        <body>
            <button type="button" onclick="download();">Download JSON</button>
            <svg id="scheme-placeholder"></svg>
            <script>
                var currentFileName = "";
                const getCircularReplacer = () => {
                const seen = new WeakSet();
                return (key, value) => {
                    if (typeof value === "object" && value !== null) {
                    if (seen.has(value)) { return;}
                    seen.add(value);}
                    return value;};};

                function download() {
                    var element = document.createElement('a');
                    element.setAttribute('href', 'data:text/plain;charset=utf-8,' +
                    encodeURIComponent(JSON.stringify(hwSchematic.layouter.graph, getCircularReplacer(), 2)));
                    element.setAttribute('download', currentFileName.replace(".json", "_mapped.json"));
                    element.style.display = 'none';
                    document.body.appendChild(element);
                    element.click();
                    document.body.removeChild(element);
                }
                function viewport() {
                    var e = window, a = 'inner';
                    if (!('innerWidth' in window)) {
                        a = 'client';
                        e = document.documentElement || document.body;
                    }
                    return { width: e[a + 'Width'], height: e[a + 'Height']}
                }

                var width = viewport().width,
                    height = viewport().height;

                var svg = d3.select("#scheme-placeholder")
                    .attr("width", width)
                    .attr("height", height);

                var orig = document.body.onresize;
                document.body.onresize = function(ev) {
                    if (orig)
                        orig(ev);

                    var w = viewport();
                    svg.attr("width", w.width);
                    svg.attr("height", w.height);
                }

                var hwSchematic = new d3.HwSchematic(svg);
                hwSchematic._PERF = true;
                var zoom = d3.zoom();
                zoom.on("zoom", function applyTransform(ev) {
                    hwSchematic.root.attr("transform", ev.transform)
                });

                // disable zoom on doubleclick
                // because it interferes with component expanding/collapsing
                svg.call(zoom)
                .on("dblclick.zoom", null)
        \n""")
        fp.write("hwSchematic.bindData(\n")
        fp.write(self._write_json())
        fp.write(");")
        fp.write(f"var currentFileName = '{self.top_instance}.json';")
        fp.write("""
        </script>
        </body>
        </html>
        """)
        fp.close()

    def write_block(self):
        """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Elkjs-SVG</title>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.0.2/d3.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/elkjs@0.7.0/lib/elk.bundled.js"></script>
    <script type="text/javascript" src="https://bundle.run/elkjs-svg@0.2.1"></script>
    <style>
        svg {
            display: block;
            margin: auto;
        }

        body {
            margin: 0;
            background-color: white;
        }
    </style>
</head>

<body>
    <div id="svg-wrapper"></div>
    <script>

        function viewport() {
            var e = window,
                a = 'inner';
            if (!('innerWidth' in window)) {
                a = 'client';
                e = document.documentElement || document.body;
            }
            return {
                width: e[a + 'Width'],
                height: e[a + 'Height']
            }
        }

        var width = viewport().width;
        var height = viewport().height;

        const graph = {
            "id": "root",
            "layoutOptions": {
                "elk.algorithm": "rectpacking"
            },
            "children": [
                { "id": "n1", "width": 30, "height": 30 },
                { "id": "n2", "width": 30, "height": 30 },
                { "id": "n3", "width": 30, "height": 30 }
            ],
            "edges": [
                { "id": "e1", "sources": ["n1"], "targets": ["n2"] },
                { "id": "e2", "sources": ["n1"], "targets": ["n3"] }
            ]
        };
        const elk = new ELK()
        var d3SVG;
        elk.layout(graph)
            .then(data => {
                var renderer = new elkjsSvg.Renderer();
                var svg = renderer.toSvg(data);
                // var newsvg = document.getElementsByTagName("body");
                var newsvg = document.getElementById("svg-wrapper");
                newsvg.innerHTML += svg;

                d3SVG = d3.select('svg')
                    .attr("width", 1051)
                    .attr("height", 969)
                    .attr("preserveAspectRatio", "xMidYMin")
                    .call(zoom);

            });

        var orig = document.body.onresize;
        document.body.onresize = function (ev) {
            if (orig)
                orig(ev);

            var w = viewport();
            svg.attr("width", w.width);
            svg.attr("height", w.height);
        }

        var zoom = d3.zoom();
        zoom.on("zoom", function applyTransform(ev) {
            console.log(ev.transform);
            console.log(d3SVG.select("g"));
            d3SVG.select("g").attr("transform", ev.transform);
        });

    </script>
</body>
</html>
        """
