//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for primitive pb_type: ff
//	Author: Xifan TANG
//	Organization: University of Utah
//	Date: Thu Oct 28 13:17:18 2021
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
`default_nettype wire

// ----- Verilog module for logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff -----
module logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff(reset,
                                                                               clk,
                                                                               ff_D,
                                                                               ff_Q,
                                                                               ff_clk);
//----- GLOBAL PORTS -----
input [0:0] reset;
//----- GLOBAL PORTS -----
input [0:0] clk;
//----- INPUT PORTS -----
input [0:0] ff_D;
//----- OUTPUT PORTS -----
output [0:0] ff_Q;
//----- CLOCK PORTS -----
input [0:0] ff_clk;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	DFF DFF_0_ (
		.reset(reset),
		.clk(clk),
		.D(ff_D),
		.Q(ff_Q));

endmodule
// ----- END Verilog module for logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff -----

//----- Default net type -----
`default_nettype none



