"""
"""
import logging
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
from fnmatch import fnmatch
from collections import Counter

import spydrnet as sdn
import svgwrite
from spydrnet_physical.util import FPGAGridGen

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")


class FabricKeyGenCCFF:
    """This stores list of connection points"""

    fkey: list = [[]]
    bits_mapping: dict = {}

    def __init__(self, fpga_grid=None, design_name=None, arch_file=None, layout=None):

        if not fpga_grid:
            self.design_name = design_name
            self.arch_file = arch_file
            self.layout = layout
            fpga_grid = FPGAGridGen(
                design_name="", arch_file=arch_file, release_root="", layout=layout
            )
            fpga_grid.enumerate_grid()
            fpga_grid.render_layout()

        self.fpga_grid = fpga_grid
        self.dwg = fpga_grid.dwg
        self.dwg_shapes = fpga_grid.dwg_shapes
        self.dwg_text = fpga_grid.dwg_text

    def validate_key(
        self,
        skip_duplicate_checks=False,
        skip_missing_checks=False,
        skip_extra_instance_checks=False,
    ):
        """
        This method validates the generated fabric key against bitsream distribution file
        It requies bitstream_distribution file loaded before execution.
        Following checks has been performs

        1. If there is a duplicated key in the current database
        2. If there is missing instance in the current database
        3. If there is an extra instance in the current database

        """
        assert (
            len(self.bits_mapping) > 0
        ), "Can not validate keu please load bitsream distribution file first"

        # Check for duplicate
        if not skip_duplicate_checks:
            flatlist = [item[-1] for sublist in self.fkey for item in sublist]
            for key, value in Counter(flatlist).items():
                if value > 1:
                    logger.warning("Duplicate key found %s, %d times", key, value)

        # Check for missing instance
        instance_list = self.bits_mapping.keys()
        if not skip_missing_checks:
            for instance in set(instance_list).difference(flatlist):
                logger.warning("Instance missing %s", instance)

        # Check for extra instance
        if not skip_extra_instance_checks:
            for instance in set(flatlist).difference(instance_list):
                logger.warning("Extra instance found %s", instance)

    def save_fabric_key(self, filename):
        """
        Saves the fabric key as XML

        Args:
            filename (str): Fabric key filename
        """
        start = 0
        key = ET.Element("fabric_key")
        for index, region_elements in enumerate(self.fkey):
            region = ET.SubElement(key, "region", {"id": str(index)})
            for each in region_elements:
                inst_name = each[-1]
                if not (inst_name.startswith("cb") or inst_name.startswith("sb")):
                    inst_name = "grid_" + inst_name
                ET.SubElement(region, "key", {"id": str(start), "alias": inst_name})
                start += 1
        with open(filename, "w", encoding="UTF-8") as fptr:
            rough_string = ET.tostring(key, "utf-8")
            reparsed = minidom.parseString(rough_string)
            fptr.write(reparsed.toprettyxml(indent="  "))

    @staticmethod
    def instance_to_coordinate(instance_name, regex=None):
        """
        This method returns the cordinates from the instance name
        """
        regex = regex or r".*_([0-9]+)__([0-9]+)_"
        match = re.match(regex, instance_name)
        return match.group(1), match.group(2)

    def create_serpentine_connection(self, start="bl"):
        """
        This method creates the a single fabric key pattern for the entire ]
        FPGA device. Starting from bottom left to top right
        """
        for xpt in range(0, (self.fpga_grid.get_width() * 2) + 3, 2):
            for ypt in range((self.fpga_grid.get_height() * 2) + 3):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                self.fkey[0] += [(xpt, ypt, inst_name)]
            for ypt in range((self.fpga_grid.get_height() * 2) + 3)[::-1]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt + 1, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                self.fkey[0] += [(xpt + 1, ypt, inst_name)]

    def read_bistream_distribution(self, filename):
        """
        This method read the bitsream distribution file and
        maintains mapping for the final bitsream length calculation
        """
        root = ET.parse(filename)
        for eachblock in root.findall(".//block/block"):
            name = eachblock.attrib["name"].replace("grid_", "")
            self.bits_mapping[name] = int(eachblock.attrib["number_of_bits"])

    def bitstream_stats(self):
        """
        Return the statistics of the bitstream generated
        """
        stats = {}
        for indx, region in enumerate(self.fkey):
            length = 0
            for block in region:
                inst_name = block[-1]
                length += int(self.bits_mapping[inst_name])
            stats[f"region_{indx}"] = length
        return stats

    def create_fabric_key(self, pattern=None):
        """
        Main fucntion to create fabric key

        Args:
            pattern (str): Type of fabric key pattern
        """
        if pattern == "serpentine":
            self.create_serpentine_connection()
        else:
            self.create_serpentine_connection()
        return self.fkey

    def render_svg(self, filename, skip_instance=""):
        """
        This method renders the fabric key on the given FPGA grid

        Args:
            design_name (str): Design name
            filename (str): name of the SVG file to store
            show_grid_io (str): name of the SVG file to store
            skip_instance (str): Regex match string to skip instances
        """
        dwg = self.dwg

        marker = dwg.marker(
            refX="30",
            refY="30",
            viewBox="0 0 120 120",
            markerUnits="strokeWidth",
            markerWidth="8",
            markerHeight="10",
            orient="auto",
        )
        marker.add(dwg.path(d="M 0 0 L 60 30 L 0 60 z", fill="blue"))
        dwg.defs.add(marker)

        mapping = {}
        for element in self.dwg_text.elements:
            mapping[element.text] = (
                float(element.attribs["x"]),
                -1 * float(element.attribs["y"]),
            )

        for indx, each_region in enumerate(self.fkey):
            points = []
            for each_instance in each_region:
                if fnmatch(each_instance[-1], skip_instance):
                    continue
                try:
                    points += map(str, mapping[each_instance[-1]])
                except KeyError:
                    logger.warning(
                        "%s instance placement not found, while rendering CCFF",
                        each_instance[-1],
                    )
            self.dwg_shapes.add(
                dwg.path(
                    d=f"M {points[0]} {points[1]} " + " ".join(points),
                    fill="none",
                    class_ = f"region_{indx}",
                    marker_mid=marker.get_funciri(),
                    marker_end=marker.get_funciri(),
                    stroke_width="0.4px",
                    stroke="red",
                )
            )

        if filename:
            self.dwg.saveas(filename, pretty=True, indent=4)
            print(f"SVG file saved as {filename}")
        return self.dwg
