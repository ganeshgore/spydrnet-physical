//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_top
(* WIDTH = 250, HEIGHT = 250, in0_X = 2, in0_Y = 10, in1_X = 2, in1_Y = 30, in3_X = 125.0, in3_Y = 125.0, bus_in_X = 2, bus_in_Y = 50, out0_X = 249, out0_Y = 230, bus_out_X = 249, bus_out_Y = 210 *)
module top
(
    in0,
    in1,
    in3,
    bus_in,
    out0,
    bus_out
);

(* SIDE = left, OFFSET = 10 *)
    input in0;
(* SIDE = left, OFFSET = 30 *)
    input in1;
(* SIDE = center, OFFSET = 0 *)
    input in3;
(* SIDE = left, OFFSET = 50 *)
    input [1:0]bus_in;
(* SIDE = right, OFFSET = 20 *)
    output out0;
(* SIDE = right, OFFSET = 40 *)
    output [1:0]bus_out;

    wire in0;
    wire in1;
    wire in3;
    wire [1:0]bus_in;
    wire out0;
    wire [1:0]bus_out;
    wire wire0;
    wire [1:0]wire_bus;

(* LOC_X = 50, LOC_Y = 50 *)
    module1 inst_1_0
    (
        .in0(in0),
        .in1(in1),
        .out(wire0)
    );
(* LOC_X = 50, LOC_Y = 150 *)
    module1 inst_1_1
    (
        .in0(wire0),
        .in1(in3),
        .out(out0)
    );
(* LOC_X = 150, LOC_Y = 50 *)
    module2 inst_2_0
    (
        .in0({in0, in1}),
        .in1({bus_in[1], bus_in[0]}),
        .out({wire_bus[1], wire_bus[0]})
    );
(* LOC_X = 150, LOC_Y = 150 *)
    module2 inst_2_1
    (
        .in0({wire_bus[1], wire_bus[0]}),
        .in1({wire_bus[1], wire_bus[0]}),
        .out({bus_out[1], bus_out[0]})
    );
endmodule

(* WIDTH = 50, HEIGHT = 60, SHAPE = cross, POINTS = [25, 25, 25, 25, 25, 25], in0_X = 50, in0_Y = 60, in1_X = 0, in1_Y = 35, out_X = 75, out_Y = 45 *)
module module1
(
    in0,
    in1,
    out
);

(* SIDE = top, OFFSET = 10, SIDE2 = right *)
    input in0;
(* SIDE = left, OFFSET = 10 *)
    input in1;
(* SIDE = right, OFFSET = 20 *)
    output out;

    wire in0;
    wire in1;
    wire out;

endmodule

(* WIDTH = 50, HEIGHT = 40, SHAPE = custom, POINTS = V 0 0 10 -10 10 30 -20 -20 *)
module module2
(
    in0,
    in1,
    out
);

(* SIDE = left, OFFSET = 10 *)
    input [1:0]in0;
(* SIDE = left, OFFSET = 30 *)
    input [1:0]in1;
(* SIDE = right, OFFSET = 20 *)
    output [1:0]out;

    wire [1:0]in0;
    wire [1:0]in1;
    wire [1:0]out;

endmodule

