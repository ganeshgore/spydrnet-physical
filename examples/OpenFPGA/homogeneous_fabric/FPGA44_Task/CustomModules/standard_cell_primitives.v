

`celldefine
module CCDFF (RESET_B, CFGE, D, Q, CFGQN, CFGQ, CLK);
  input RESET_B;
  input CFGE;
  input D;
  output Q;
  output CFGQN;
  output CFGQ;
  input CLK;
);

endmodule
`endcelldefine

`celldefine
module DFF (D, Q, clk, reset);
    input D;
    output Q;
    input clk;
    input reset;

endmodule
`endcelldefine

`celldefine
module MUX2_X1(A0, A1, S, Y);
    input A0;
    input A1;
    input S;
    output Y;
endmodule
`endcelldefine

`celldefine
module MUX4_X1(A0, A1, A2, A3, S, Y);
    input A0;
    input A1;
    input A2;
    input A3;
    input [1:0]S;
    output Y;
endmodule
`endcelldefine

`celldefine
module mux2_wrapper(A0, A1, S, X);
    input A0;
    input A1;
    input S;
    output X;
endmodule
`endcelldefine

`celldefine
module AND2_X1(A, B, Y);
    input A;
    input B;
    output Y;
endmodule
`endcelldefine

`celldefine
module NAND2_X1(A, B, Y);
    input A;
    input B;
    output Y;
endmodule
`endcelldefine

`celldefine
module AND2_ISOL_X1(A, B, Y);
    input A;
    input B;
    output Y;
endmodule
`endcelldefine

`celldefine
module OR2_X1(A, B, Y);
    input A;
    input B;
    output Y;
endmodule
`endcelldefine

`celldefine
module OR2_ISOL_X1(A, B, Y);
    input A;
    input B;
    output Y;
endmodule
`endcelldefine

`celldefine
module INV_X1(A, Y);
    input A;
    output Y;
endmodule
`endcelldefine

`celldefine
module BUF_X0(A, Y);
    input A;
    output Y;
    assign Y = A;
endmodule
`endcelldefine

`celldefine
module BUF_X1(A, Y);
    input A;
    output Y;
endmodule
`endcelldefine

`celldefine
module BUF_X2(A, Y);
    input A;
    output Y;
endmodule
`endcelldefine

`celldefine
module BUF_X4(A, Y);
    input A;
    output Y;
endmodule
`endcelldefine

`celldefine
module BUF_X8(A, Y);
    input A;
    output Y;
endmodule
`endcelldefine


`celldefine
module BUFCLK_X1(A, Y);
    input A;
    output Y;
endmodule
`endcelldefine

`celldefine
module BUFCLK_X2(A, Y);
    input A;
    output Y;
endmodule
`endcelldefine

`celldefine
module BUFCLK_X4(A, Y);
    input A;
    output Y;
endmodule
`endcelldefine

`celldefine
module BUFCLK_X8(A, Y);
    input A;
    output Y;
endmodule
`endcelldefine

