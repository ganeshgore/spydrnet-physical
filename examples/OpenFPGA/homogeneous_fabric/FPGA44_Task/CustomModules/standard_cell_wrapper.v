
// module CCDFF (D, Q, clk, reset);
//     input D;
//     output Q;
//     input clk;
//     input reset;

//     QDFFRBNUCLDX1A DFF ( .Q(Q), .D(D), .CK(clk), .RB(reset) );
// endmodule

module DFF (D, Q, clk, reset);
    input D;
    output Q;
    input clk;
    input reset;

    QDFFRBNUCLDX1A DFF ( .Q(Q), .D(D), .CK(clk), .RB(reset) );
endmodule

module MUX2_X1(A0, A1, S, Y);
    input A0;
    input A1;
    input S;
    output Y;
    MUX2CKUCLDX1 MUX2_X0 ( .A(A0), .B(A1), .S(S), .O(Y));
endmodule

module MUX4_X1(A0, A1, A2, A3, S, Y);
    input A0;
    input A1;
    input A2;
    input A3;
    input [1:0]S;
    output Y;
    MUX4V2UCLDX1 MUX4_X0 ( .A(A0), .B(A1), .C(A2), .D(A3), .S0(S[0]), .S1(S[1]), .O(Y));
endmodule

module mux2_wrapper(A0, A1, S, X);
    input A0;
    input A1;
    input S;
    output X;
    MUX2CKUCLDX1 MUX2_X0 ( .A(A0), .B(A1), .S(S), .O(X));
endmodule

module AND2_X1(A, B, Y);
    input A;
    input B;
    output Y;
    AN2CKUCLDX1 AND (.I1(A), .I2(B), .O(Y));
endmodule

module NAND2_X1(A, B, Y);
    input A;
    input B;
    output Y;
    ND2BPNUCLDX1 AND (.I1(A), .I2(B), .O(Y));
endmodule

module AND2_ISOL_X1(A, B, Y);
    input A;
    input B;
    output Y;
    A2ISOUCLDX1 AND (.I(A), .SLB(B), .O(Y));
endmodule

module OR2_X1(A, B, Y);
    input A;
    input B;
    output Y;
    OR2CKUCLDX1 OR (.I1(A), .I2(B), .O(Y));
endmodule

module OR2_ISOL_X1(A, B, Y);
    input A;
    input B;
    output Y;
    O2ISOUCLDX1 OR (.I(A), .SL(B), .O(Y));
endmodule

module INV_X1(A, Y);
    input A;
    output Y;
    INVUCLDX11 INV (.I(A), .O(Y));
endmodule

module BUF_X0(A, Y);
    input A;
    output Y;
    assign Y = A;
endmodule

module BUF_X1(A, Y);
    input A;
    output Y;
    BUFCKUCLDX1 BUF (.I(A), .O(Y));
endmodule

module BUF_X2(A, Y);
    input A;
    output Y;
    BUFCKUCLDX2 BUF (.I(A), .O(Y));
endmodule

module BUF_X4(A, Y);
    input A;
    output Y;
    BUFCKUCLDX4 BUF (.I(A), .O(Y));
endmodule

module BUF_X8(A, Y);
    input A;
    output Y;
    BUFCKUCLDX8 BUF (.I(A), .O(Y));
endmodule


module BUFCLK_X1(A, Y);
    input A;
    output Y;
    BUFCKUCLDX1 BUF (.I(A), .O(Y));
endmodule

module BUFCLK_X2(A, Y);
    input A;
    output Y;
    BUFCKUCLDX2 BUF (.I(A), .O(Y));
endmodule

module BUFCLK_X4(A, Y);
    input A;
    output Y;
    BUFCKUCLDX4 BUF (.I(A), .O(Y));
endmodule

module BUFCLK_X8(A, Y);
    input A;
    output Y;
    BUFCKUCLDX8 BUF (.I(A), .O(Y));
endmodule

