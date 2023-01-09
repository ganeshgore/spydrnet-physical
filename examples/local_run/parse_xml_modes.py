"""
Simple VPR custom .net generator
"""
from xml.dom.minidom import parseString
from xml.dom import minidom


arch_snippet = """
    <mode name="dff">
        <pb_type name="dff" blif_model=".subckt dff" num_pb="1">
            <input name="D" num_pins="1" port_class="D"/>
            <output name="Q" num_pins="1" port_class="Q"/>
            <clock name="C" num_pins="1" port_class="clock"/>
            <T_setup value="${FF_T_SETUP}" port="dff.D" clock="C"/>
            <T_clock_to_Q max="${FF_T_CLK2Q}" port="dff.Q" clock="C"/>
        </pb_type>
        <interconnect>
            <direct name="direct1" input="ff.D" output="dff.D"/>
            <direct name="direct2" input="ff.C" output="dff.C"/>
            <direct name="direct3" input="dff.Q" output="ff.Q"/>
        </interconnect>
    </mode>
"""

root = parseString(arch_snippet)

netFile = minidom.Document()
xml = netFile.createElement("root")
netFile.appendChild(xml)

print(netFile.toprettyxml())


# print(dir(root))
# print(root.nodeName)
# print(root.childNodes[0].nodeName)
