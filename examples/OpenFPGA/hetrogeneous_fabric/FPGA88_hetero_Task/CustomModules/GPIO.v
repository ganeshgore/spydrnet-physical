`timescale 1ns/1ps

// //-----------------------------------------------------
// // Simple GPIO Module
// //-----------------------------------------------------
module GPIO (PAD, DIR, outpad, inpad);

inout PAD;
input DIR;
input outpad;
output inpad;

INV_X1     INV     ( .A(DIR), .Y(DIRB) );
BUFT_X1 BUF_IN  ( .Y(PAD), .A(outpad), .E(DIR) );
BUFT_X1 BUF_OUT ( .Y(inpad), .A(PAD), .E(DIRB) );

endmodule

