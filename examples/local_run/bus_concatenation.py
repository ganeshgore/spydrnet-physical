

import spydrnet as sdn

with open("_temp.v", "w", encoding="UTF-8") as tmp:
    tmp.write('''
    module sample();

    wire [2:0] mode;
    wire [5:0] n39;

    module1 inst1 (.b_i({n39[3], mode}));

    endmodule
    ''')

netlist = sdn.parse("_temp.v")
top = netlist.top_instance
module = next(top.get_definitions("sample"))
mpins = next(next(module.get_definitions("module1")).get_ports("b_i")).pins
pins = next(module.get_instances("inst1")).pins
n39 = next(module.get_cables("n39")).wires[0]
mode_wires = next(module.get_cables("mode")).wires

sdn.compose(netlist, "_temp_rewrite.v",
            skip_constraints=True, write_blackbox=False)
