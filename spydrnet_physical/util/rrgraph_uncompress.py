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


def update_attr(element, attribs, skip_keys=(), upper_case_fields=()):
    for k, v in attribs.items():
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
    def _channels_bin2xml(channels, xml_root=None):
        if xml_root is None:
            xml_root = XML("<channels></channels>")
        # elements = []
        xml_root.append(
            update_attr(
                Element("channel"),
                channels.channel.to_dict()
            )
        )
        xml_root.extend(
            [
                update_attr(Element("x_list"), each.to_dict())
                for each in channels.xLists
            ]
        )
        xml_root.extend(
            [
                update_attr(Element("y_list"), each.to_dict())
                for each in channels.yLists
            ]
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
                name=str(segment_bin.name),
                length=str(segment_bin.length)
            )
            if not segment_bin.resType == "uxsdInvalid":
                segment_root.res_type= segment_bin.resType

            timing = update_attr(Element("timing"), segment_bin.timing.to_dict())
            segment_root.append(timing)
            xml_root.append(segment_root)
        return xml_root
