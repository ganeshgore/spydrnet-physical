
# import pathlib
# import xml.etree.ElementTree as ET
# from glob import glob
# from bitstring import Bits, BitArray, BitStream


# exit()

# print(Bits(length=12).bin)
# print(Bits(length=12)[2:3])

# s = BitArray(length=10)
# print(s.bin)
# s.overwrite('0b100', 4)
# print(s.bin)
# print(s[:5].bin)
# s.reverse()
# print(s.bin)


# # import yaml

# # bitstream_files = "../homogeneous_fabric/split_bitstreams"
# # gsb_files = "../homogeneous_fabric/FPGA44_gsb"
# # instance_map = "../homogeneous_fabric/top_hierarchy.yml"


# # instances = glob(f"{bitstream_files}/sb*/*0__0*.xml")[0]

# # tree = ET.parse(instances)
# # root = tree.getroot()

# # elements = root.findall(".//hierarchy/..")
# # elements = sorted(elements, key=lambda x: "_".join(
# #     x.attrib["name"].split("_")[-1::-2]))

# # for ele in root.findall(".//hierarchy/.."):
# #     # print(".".join([e.attrib["name"]
# #     #       for e in ele.findall(".//instance")]), end="")
# #     print("{:>4d}   {:<20s}".format(
# #         len(ele.findall(".//bit")),
# #         ele.attrib["name"]))


# # How to Bitsream design kit

# fpga_bdk = load_bdk(fabric_indenpendent_bitstream,
#                     general_switchbox_directory,
#                     vpr_architecture_file,
#                     openfpga_architecture_file)

# fpga_bdk.get_modules()   # List all the unique modules in the design
# fpga_bdk.get_instances()  # Get all configurable instances in all the module
# fpga_bdk.reset_all()     # Resets all the bit in the current fabric
# fpga_bdk.set_default()   # Sets all bits to default setting

# cbx11 = fpga_bdk.get_instance("cbx_1__1_")

# # This will list all the bitstream segments in the current instance
# cbx11.list_bit_segemets()
# cbx11.type                # This returns routing or pb_type keyword

# # If routing module (CB and SBs)
# # List all the outputs/drivers of the current routing block "<side>_<indx>"
# cbx11.outputs()
# cbx11.inputs()            # List all the inputs of the current routing block "<side>_<indx>"
# # List all the inputs connected to the given output pins
# cbx11.get_output("<output_pin>").inputs()
# # List all the outputs connected to the given input pins
# cbx11.get_output("<input_pins>").outputs()
# # Sets the bitstream segment value for the current module
# cbx11.get_output("<output_pin>").select_input("<input_pin>")

# # If Physical blocks
# clb = fpga_bdk.get_instance("grid_clb_1__1_")
# clb.type  # pb_type

# clb.list_connection()       # lists collection of crossbars/local_routing in the pb_type
# clb.list_blocks()           # lists collection of blocks in side the pb_type


# # Cross bar configuration
# # list outputs to the crossbar "<block>_<indx>_<pin>_<indx>"
# clb.get_connection("").outputs()
# crobbbar_out = clb.get_connection("").get_output("<block>_<indx>_<pin>_<indx>")
# crobbbar_out.inputs()  # list inputs to the given output crossbar pin
# crobbbar_out.select_input("Input Pin Name")


# # PB_type configuration
# clb.list_blocks()
