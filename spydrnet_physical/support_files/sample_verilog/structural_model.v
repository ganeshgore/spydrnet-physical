
module top(in0, in1, in3, clk, bus_in, out0, bus_out);
    input in0;
    input in1;
    input in3;
    input clk;
    input [1:0]bus_in;
    output out0;
    output [1:0]bus_out;

    wire wire0;
    wire [1:0]wire_bus;

    fifo U1 (.clk(clk));
    ram U2 (.clk(clk));
    counter U3 (.clk(clk));

endmodule

module fifo(in0, in1, clk, out);
    input in0;
    input in1;
    input clk;
    output out;

endmodule

module ram(clk, rst, we, en, data, address, out);
    input clk, rst, out, en;
    input [3:0]data;
    input [3:0]address;
    output [7:0]out;

endmodule

module counter(clk, rst, out);
    input clk;
    input rst;
    output [7:0]out;

endmodule

