
module top(in, out);
    input [3:0]in;
    output [3:0]out;

    wire [1:0]mid11;
    wire [1:0]mid12;
    wire [1:0]mid21;
    wire [1:0]mid22;

    wire [1:0]inter0;
    wire [1:0]inter1;

    // Tile_1__1_
    module1 inst_1_11 (.in0(in[1]), .in1(in[0]), .out0(mid11[1]), .out1(mid11[0]));
    module2 inst_2_11 (.in0(mid11[1]), .in1(mid11[0]), .out0(inter0[1]), .out1(inter0[0]));

    // Tile_1__2_
    module1 inst_1_12 (.in0(in[3]), .in1(in[2]), .out0(mid12[1]), .out1(mid12[0]));
    module2 inst_2_12 (.in0(mid12[1]), .in1(mid12[0]), .out0(inter1[1]), .out1(inter1[0]));

    // Tile_2__1_
    module1 inst_1_21 (.in0(inter0[1]), .in1(inter0[0]), .out0(mid21[1]), .out1(mid21[0]));
    module2 inst_2_21 (.in0(mid21[1]), .in1(mid21[0]), .out0(out[1]), .out1(out[0]));

    // Tile_2__2_
    module1 inst_1_22 (.in0(inter1[1]), .in1(inter1[0]), .out0(mid22[1]), .out1(mid22[0]));
    module2 inst_2_22 (.in0(mid22[1]), .in1(mid22[0]), .out0(out[3]), .out1(out[2]));

endmodule

module module1(in0, in1, out0, out1);
    input in0;
    input in1;
    output out0;
    output out1;

endmodule

module module2(in0, in1, out0, out1);
    input in0;
    input in1;
    output out0;
    output out1;

endmodule

