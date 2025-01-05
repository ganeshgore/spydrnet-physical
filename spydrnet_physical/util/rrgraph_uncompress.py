#!/usr/bin/env python3

from lxml import etree


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


class rrgraph_bin2xml:

    @staticmethod
    def _updata_attr(
        element, attribs, attrib_map=None, skip_keys=(), upper_case_fields=()
    ):
        if attrib_map is None:
            attrib_map = {}
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

    @staticmethod
    def _channels_bin2xml(channels, xml_root=None):
        if xml_root is None:
            xml_root = etree.XML("<channels></channels>")
        print("channels_bin2xml")
        return xml_root

    @staticmethod
    def _switches_bin2xml(switches, xml_root=None):
        if xml_root is None:
            xml_root = etree.XML("<switches></switches>")
        for switch_bin in switches:
            switch_root = etree.Element(
                "switch",
                id=str(switch_bin.id),
                name=str(switch_bin.name),
                type=str(switch_bin.type),
            )
            switch_root.append(
                self._updata_attr(
                    etree.Element("timing"), switch_bin.timing.to_dict(), attrib_map
                ),
            )
            switch_root.append(
                self._updata_attr(
                    etree.Element("sizing"), switch_bin.sizing.to_dict(), attrib_map
                ),
            )
            xml_root.append(switch_root)
        return xml_root
