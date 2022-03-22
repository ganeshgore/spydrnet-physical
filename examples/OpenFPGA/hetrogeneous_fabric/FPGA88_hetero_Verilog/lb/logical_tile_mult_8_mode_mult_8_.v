//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for pb_type: mult_8
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

// ----- BEGIN Physical programmable logic block Verilog module: mult_8 -----
//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for logical_tile_mult_8_mode_mult_8_ -----
module logical_tile_mult_8_mode_mult_8_(mult_8_a,
                                        mult_8_b,
                                        mult_8_clk,
                                        mult_8_out);
//----- INPUT PORTS -----
input [0:7] mult_8_a;
//----- INPUT PORTS -----
input [0:7] mult_8_b;
//----- INPUT PORTS -----
input [0:0] mult_8_clk;
//----- OUTPUT PORTS -----
output [0:15] mult_8_out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

endmodule
// ----- END Verilog module for logical_tile_mult_8_mode_mult_8_ -----

//----- Default net type -----
// `default_nettype none



// ----- END Physical programmable logic block Verilog module: mult_8 -----
