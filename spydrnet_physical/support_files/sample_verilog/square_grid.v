
module top(in, out);
    input [3:0]in;
    output [3:0]out;

    wire [3:0] row1;
    wire [3:0] row2;
    wire [3:0] row3;
    wire [3:0] row4;

    // Tile_1__*_
    module1 inst_1_11 (.in0(in[0]), .out0(row1[0]));
    module1 inst_1_21 (.in0(row1[0]), .out0(row1[1]));
    module1 inst_1_31 (.in0(row1[1]), .out0(row1[2]));
    module1 inst_1_41 (.in0(row1[2]), .out0(out[0]));

    // Tile_2__*_
    module1 inst_1_12 (.in0(in[1]), .out0(row2[0]));
    module1 inst_1_22 (.in0(row2[0]), .out0(row2[1]));
    module1 inst_1_32 (.in0(row2[1]), .out0(row2[2]));
    module1 inst_1_42 (.in0(row2[2]), .out0(out[1]));

    // Tile_3__*_
    module1 inst_1_13 (.in0(in[2]), .out0(row3[0]));
    module1 inst_1_23 (.in0(row3[0]), .out0(row3[1]));
    module1 inst_1_33 (.in0(row3[1]), .out0(row3[2]));
    module1 inst_1_43 (.in0(row3[2]), .out0(out[2]));

    // Tile_4__*_
    module1 inst_1_14 (.in0(in[3]), .out0(row4[0]));
    module1 inst_1_24 (.in0(row4[0]), .out0(row4[1]));
    module1 inst_1_34 (.in0(row4[1]), .out0(row4[2]));
    module1 inst_1_44 (.in0(row4[2]), .out0(out[3]));

endmodule

module module1(in0, clk, out0);
    input in0;
    input clk;
    output out0;

    wire in0;
    wire clk;
    wire out0;

endmodule