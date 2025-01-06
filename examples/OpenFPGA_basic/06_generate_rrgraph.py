"""
===========================================
Generate RRGraph from VPR architecture file
===========================================

"""


from spydrnet_physical.util import rrgraph

rrgraph_bin = rrgraph("vpr-rendered.xml", 160, "FPGA44")
rrgraph_bin.write_rrgraph_xml("_rrgraph_generated.xml")
