
module top(in0, in1, out0);
    input in0;
    input in1;
    output out0;

    wire wire0;

    module1 inst_1_0 (.in0(in0), .in1(in1), .out(wire0));
    module1 inst_1_1 (.in0(wire0), .in1(in0), .out(out0));

endmodule

module module1(in0, in1, out);
    input in0;
    input in1;
    output out;

    wire internal;

    module2 module2_0 (.in0(in0), .in1(in1), .out(internal));
    module2 module2_1 (.in0(in1), .in1(internal), .out(out));

endmodule


`celldefine
module module2(in0, in1, out);
    input in0;
    input in1;
    output out;

endmodule
`endcelldefine
