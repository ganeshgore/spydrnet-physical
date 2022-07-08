"""
This file contain the class which performs  the bitsream manipulation
"""
import numpy as np
import pandas as pd
import xml.etree.ElementTree as etree
from collections import namedtuple, OrderedDict
from pprint import pprint


class block_bitstream:
    """
    This class store bistream for each block
    """
    pass


class BitstreamManager:
    """

    """

    instance_map = {}
    """
    A dictionary containing the module name instances of those definitions
    """
    _regions = []
    """
    Store the list of list, and each element contains tuple of
    (module_name, instance_name)
    """

    bit_man = {}
    """
    A dictionary of lists with the bitstream values

    .. code-block::

        {
            "module_name" : {
                "elements": {
                    "each_element" : (higher_index, lower_indx)
                },
                "bitstream": {
                    "instance_name" : [<<as shown below>>]
                }
            }
        }


    .. rst-class:: ascii

    ::

                   bits ---->>
        ------------------------------------
         I |
         N |
         S |
         T |
         A |
         N |
         C |
         E |

        Each element is (unique_id, value)

    """

    Bit = namedtuple("Bit", "id value")

    def __init__(self, fabric_key, bitstream) -> None:
        """
        Bitstream manipulation class

        Args:
            bistream: Fabric inpdendendent bitstream
        """
        self.fabric_key = etree.parse(fabric_key).getroot()
        self.bitstream = etree.parse(bitstream).getroot()
        self._get_instance_map()
        self.load_bitstream()

    @property
    def regions(self):
        """
        Returns number of regions in the current bitstream
        """
        return len(self._regions)

    def _get_instance_map(self):
        """
        Extracts the tp level configuration regions
        """
        regions = self.fabric_key.findall("region")
        self._regions = [[] for _ in range(len(regions))]
        for indx, each_region in enumerate(regions):
            for each_instance in each_region:
                name = each_instance.attrib["name"]
                alias = each_instance.attrib["alias"]
                self.instance_map[name] = self.instance_map.get(name, [])
                self.instance_map[name].append(alias)
                self._regions[indx].append((name, alias))

    def _get_module_of_instance(self, instance_name):
        """
        Returns the module name of the given instance
        """
        for module_name, instances in self.instance_map.items():
            if instance_name in instances:
                return module_name
        return None

    def load_bitstream(self):
        """
        This method loads the bitstreams in the internal varaibles
        """
        for each_region in self.bitstream.findall("region"):
            bitcount = 1  # Counts number of bits in each mdoule
            element_count = 0
            pre_module_name = None
            for bits in each_region:
                unique_id = int(bits.attrib["id"])
                bit = bool(int(bits.attrib["value"]))
                bpath = bits.attrib["path"]

                # Derive variables
                instance = bpath.split(".")[1]
                module_name = self._get_module_of_instance(instance)

                # Enumerate data
                self.bit_man[module_name] = mod = \
                    self.bit_man.get(module_name, {
                        "elements": OrderedDict(),
                        "instances": {},
                    })

                mod["instances"][instance] = mod["instances"].get(instance, [])
                mod["instances"][instance].append(self.Bit(unique_id, bit))

                if not (pre_module_name == module_name):
                    bitcount = 0
                    element_count = 0
                    prev_bitcount = 0

                if "mem_out[0]" in bpath:
                    reg_path = '.'.join(bpath.split('.')[2:-1])
                    if not reg_path in self.bit_man[module_name]["elements"].keys():
                        mod["elements"][reg_path] = (bitcount, prev_bitcount)
                    prev_bitcount = bitcount
                    element_count += 1
                pre_module_name = module_name
                bitcount += 1

    def get_module_elements(self, module_name):
        pprint(self.bit_man[module_name]["elements"])

    def print_bitstream_of_module(self, module_name, value="hex"):
        for inst_name, bits in self.bit_man[module_name]["instances"].items():
            bit_str = "".join(["1" if b.value else "0" for b in bits])
            if value == 'hex':
                print(inst_name, hex(int(bit_str, 2)))
            else:
                print(inst_name, bit_str)

    def create_fabric_bitstream(self, filename):
        with open(filename, "w", encoding="UTF-8") as fp_ptr:
            fp_ptr.write("# Fabric bitstream auto-generated\n")

    def get_unique_memory_elements(self):
        pass
