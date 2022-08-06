import spydrnet as sdn
import spydrnet_physical as sdnphy

with open("_const_module.v", "w", encoding="UTF-8") as fp:
    fp.write(
        """
    module const_module(const0_out, const1_out);
        output const0_out;
        output const1_out;

        assign const0_out = 1'b0;
        assign const1_out = 1'b1;
    endmodule
    """
    )


netlist = sdn.parse("_const_module.v")
top = netlist.top_instance.reference
netlist.compose("_const_module_out.v", skip_constraints=True)

with open("_const_module_out.v", "r", encoding="UTF-8") as fp:
    print("".join(fp.readlines()))
