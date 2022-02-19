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
BUFTUCLDX1 BUF_IN  ( .O(PAD), .I(outpad), .E(DIR) );
BUFTUCLDX1 BUF_OUT ( .O(inpad), .I(PAD), .E(DIRB) );

endmodule

