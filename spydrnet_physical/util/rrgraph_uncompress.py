#!/usr/bin/env python3

from lxml.etree import XML, Element


attrib_map = {
    "xMax": "x_max",
    "xMin": "x_min",
    "yMax": "y_max",
    "yMin": "y_min",
    "resType": "res_type",
    "chanWidthMax": "chan_width_max",
    "bufSize": "buf_size",
    "muxTransSize": "mux_trans_size",
    "cPerMeter": "C_per_meter",
    "rPerMeter": "R_per_meter",
    "blockTypeId": "block_type_id",
    "heightOffset": "height_offset",
    "widthOffset": "width_offset",
    "c": "C",
    "r": "R",
    "cinternal": "Cinternal",
    "cin": "Cin",
    "cout": "Cout",
    "tdel": "Tdel",
    "srcNode": "src_node",
    "sinkNode": "sink_node",
    "switchId": "switch_id",
    "segmentId": "segment_id",
}

default_values = ["0", "0.0", "uxsdInvalid"]
skip_if_default = [
    "cin",
    "cinternal",
    "r",
    "c",
    "cout",
    "tdel",
    "cPerMeter",
    "rPerMeter",
]


def update_attr(element, attribs, skip_keys=(), upper_case_fields=()):
    for k, v in attribs.items():
        if (str(k) in skip_if_default) and (v in default_values):
            continue
        if (str(k) in skip_if_default) and isinstance(v, float):
            if float(v) <= 0:
                continue
        if str(v) != "uxsdInvalid":
            if not k in skip_keys:
                element.attrib[attrib_map.get(k, k)] = (
                    str(v) if not k in upper_case_fields else str(v).upper()
                )
                if element.attrib[attrib_map.get(k, k)].endswith(".0"):
                    element.attrib[attrib_map.get(k, k)] = element.attrib[
                        attrib_map.get(k, k)
                    ][:-2]
                if "e-" in element.attrib[attrib_map.get(k, k)]:
                    element.attrib[attrib_map.get(k, k)] = (
                        f"{float(element.attrib[attrib_map.get(k, k)]):.8e}"
                    )
    return element


class rrgraph_bin2xml:

    @staticmethod
    def _grid_bin2xml(grids, xml_root=None):
        if xml_root is None:
            xml_root = XML("<grid></grid>")
        xml_root.extend(
            [update_attr(Element("grid_loc"), g_loc.to_dict()) for g_loc in grids]
        )
        return xml_root

    @staticmethod
    def _channels_bin2xml(channels, xml_root=None):
        if xml_root is None:
            xml_root = XML("<channels></channels>")
        # elements = []
        xml_root.append(update_attr(Element("channel"), channels.channel.to_dict()))
        xml_root.extend(
            [update_attr(Element("x_list"), each.to_dict()) for each in channels.xLists]
        )
        xml_root.extend(
            [update_attr(Element("y_list"), each.to_dict()) for each in channels.yLists]
        )
        return xml_root

    @staticmethod
    def _switches_bin2xml(switches, xml_root=None):
        if xml_root is None:
            xml_root = XML("<switches></switches>")
        for switch_bin in switches:
            switch_root = Element(
                "switch",
                id=str(switch_bin.id),
                name=str(switch_bin.name),
                type=str(switch_bin.type),
            )
            timing = update_attr(Element("timing"), switch_bin.timing.to_dict())
            switch_root.append(timing)
            sizing = update_attr(Element("sizing"), switch_bin.sizing.to_dict())
            switch_root.append(sizing)
            xml_root.append(switch_root)
        return xml_root

    @staticmethod
    def _segments_bin2xml(segments, xml_root=None):
        if xml_root is None:
            xml_root = XML("<segments></segments>")
        for segment_bin in segments:
            segment_root = Element(
                "segment",
                id=str(segment_bin.id),
                length=str(segment_bin.length),
                name=str(segment_bin.name),
            )
            if not segment_bin.resType == "uxsdInvalid":
                segment_root.attrib["res_type"] = str(segment_bin.resType).upper()

            timing = update_attr(Element("timing"), segment_bin.timing.to_dict())
            segment_root.append(timing)
            xml_root.append(segment_root)
        return xml_root

    @staticmethod
    def _block_types_bin2xml(block_types, xml_root=None):
        if xml_root is None:
            xml_root = XML("<block_types></block_types>")
        for block_type in block_types:
            block_types_root = Element(
                "block_type",
                height=str(block_type.height),
                id=str(block_type.id),
                name=str(block_type.name),
                width=str(block_type.width),
            )

            for pin_class_ux in block_type.pinClasses:
                pin_class = update_attr(
                    Element("pin_class"),
                    pin_class_ux.to_dict(),
                    ("pins"),
                    upper_case_fields=("type"),
                )
                for p in pin_class_ux.pins:
                    pin = update_attr(Element("pin"), p.to_dict(), ("value"))
                    pin.text = p.value
                    pin_class.append(pin)
                block_types_root.append(pin_class)
            xml_root.append(block_types_root)
        return xml_root

    @staticmethod
    def _nodes_bin2xml(nodes, xml_root=None):
        if xml_root is None:
            xml_root = XML("<rr_nodes></rr_nodes>")

        for node_ux in nodes:
            node = update_attr(
                Element("node"),
                node_ux.to_dict(),
                ("loc", "timing", "segment"),
                upper_case_fields=("type"),
            )
            if node.attrib.get("direction", None):
                node.attrib["direction"] = (
                    node.attrib["direction"].upper().replace("DIR", "_DIR")
                )
            loc = update_attr(
                Element("loc"),
                node_ux.loc.to_dict(),
                upper_case_fields=("side"),
            )
            node.append(loc)
            if node_ux.timing.r != 0 or node_ux.timing.c != 0:
                node.append(update_attr(Element("timing"), node_ux.timing.to_dict()))
            if str(node_ux.type).startswith("chan"):
                node.append(update_attr(Element("segment"), node_ux.segment.to_dict()))
            xml_root.append(node)
        return xml_root

    @staticmethod
    def _edges_bin2xml(edges, xml_root=None):
        if xml_root is None:
            xml_root = XML("<rr_edges></rr_edges>")

        xml_root.extend(
            [
                update_attr(
                    Element("edge"),
                    edge_ux.to_dict(),
                    ("metadata"),
                )
                for edge_ux in edges
            ]
        )
        return xml_root
