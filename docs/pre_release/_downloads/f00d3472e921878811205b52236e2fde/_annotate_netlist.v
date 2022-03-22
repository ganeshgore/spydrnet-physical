//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_top
(* WIDTH = 250, HEIGHT = 250, in0_X = 2, in0_Y = 10, in1_X = 2, in1_Y = 30, bus_in_X = 2, bus_in_Y = 50, out0_X = 249, out0_Y = 230, bus_out_X = 249, bus_out_Y = 210 *)
module top
(
    in0,
    in1,
    bus_in,
    out0,
    bus_out
);

(* SIDE = left, OFFSET = 10 *)
    input in0;
(* SIDE = left, OFFSET = 30 *)
    input in1;
(* SIDE = left, OFFSET = 50 *)
    input [1:0]bus_in;
(* SIDE = right, OFFSET = 20 *)
    output out0;
(* SIDE = right, OFFSET = 40 *)
    output [1:0]bus_out;

    wire in0;
    wire in1;
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
        .in1(in0),
        .out(out0)
    );
(* LOC_X = 150, LOC_Y = 50 *)
    module2 inst_2_0
    (
        .in0({in0, in1}),
        .in1(bus_in),
        .out(wire_bus)
    );
(* LOC_X = 150, LOC_Y = 150 *)
    module2 inst_2_1
    (
        .in0(wire_bus),
        .in1(wire_bus),
        .out(bus_out)
    );
endmodule

(* WIDTH = 50, HEIGHT = 60, SHAPE = RectL, POINTS = [25, 25, 25, 25, 25, 25], in0_X = 50, in0_Y = 60, in1_X = 0, in1_Y = 35, out_X = 75, out_Y = 45 *)
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

(* WIDTH = 50, HEIGHT = 40, in0_X = 2, in0_Y = 10, in1_X = 2, in1_Y = 30, out_X = 49, out_Y = 20 *)
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

