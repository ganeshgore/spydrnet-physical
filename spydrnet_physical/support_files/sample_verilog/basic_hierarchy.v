
module top(in0, in1, in3, bus_in, out0, bus_out);
    input in0;
    input in1;
    input in3;
    input [1:0]bus_in;
    output out0;
    output [1:0]bus_out;

    wire wire0;
    wire [1:0]wire_bus;

    module1 inst_1_0 (.in0(in0), .in1(in1), .out(wire0));
    module1 inst_1_1 (.in0(wire0), .in1(in3), .out(out0));

    module2 inst_2_0 (.in0({in0, in1}), .in1(bus_in), .out(wire_bus));
    module2 inst_2_1 (.in0(wire_bus), .in1(wire_bus), .out(bus_out));

endmodule

module module1(in0, in1, out);
    input in0;
    input in1;
    output out;

endmodule

module module2(in0, in1, out);
    input [1:0]in0;
    input [1:0]in1;
    output [1:0]out;

endmodule

