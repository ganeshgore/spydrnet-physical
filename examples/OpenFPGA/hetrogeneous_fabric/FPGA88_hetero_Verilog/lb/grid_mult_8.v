//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for physical tile: mult_8]
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

// ----- BEGIN Grid Verilog module: grid_mult_8 -----
//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for grid_mult_8 -----
module grid_mult_8(top_width_0_height_0_subtile_0__pin_a_0_,
                   top_width_0_height_0_subtile_0__pin_b_0_,
                   top_width_0_height_0_subtile_0__pin_clk_0_,
                   top_width_0_height_1_subtile_0__pin_a_1_,
                   top_width_0_height_1_subtile_0__pin_b_1_,
                   right_width_0_height_0_subtile_0__pin_a_2_,
                   right_width_0_height_0_subtile_0__pin_b_2_,
                   right_width_0_height_1_subtile_0__pin_a_3_,
                   right_width_0_height_1_subtile_0__pin_b_3_,
                   bottom_width_0_height_0_subtile_0__pin_a_4_,
                   bottom_width_0_height_0_subtile_0__pin_b_4_,
                   bottom_width_0_height_1_subtile_0__pin_a_5_,
                   bottom_width_0_height_1_subtile_0__pin_b_5_,
                   left_width_0_height_0_subtile_0__pin_a_6_,
                   left_width_0_height_0_subtile_0__pin_b_6_,
                   left_width_0_height_1_subtile_0__pin_a_7_,
                   left_width_0_height_1_subtile_0__pin_b_7_,
                   top_width_0_height_0_subtile_0__pin_out_0_,
                   top_width_0_height_0_subtile_0__pin_out_8_,
                   top_width_0_height_1_subtile_0__pin_out_1_,
                   top_width_0_height_1_subtile_0__pin_out_9_,
                   right_width_0_height_0_subtile_0__pin_out_2_,
                   right_width_0_height_0_subtile_0__pin_out_10_,
                   right_width_0_height_1_subtile_0__pin_out_3_,
                   right_width_0_height_1_subtile_0__pin_out_11_,
                   bottom_width_0_height_0_subtile_0__pin_out_4_,
                   bottom_width_0_height_0_subtile_0__pin_out_12_,
                   bottom_width_0_height_1_subtile_0__pin_out_5_,
                   bottom_width_0_height_1_subtile_0__pin_out_13_,
                   left_width_0_height_0_subtile_0__pin_out_6_,
                   left_width_0_height_0_subtile_0__pin_out_14_,
                   left_width_0_height_1_subtile_0__pin_out_7_,
                   left_width_0_height_1_subtile_0__pin_out_15_);
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_a_0_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_b_0_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_clk_0_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_1_subtile_0__pin_a_1_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_1_subtile_0__pin_b_1_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_a_2_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_b_2_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_1_subtile_0__pin_a_3_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_1_subtile_0__pin_b_3_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_a_4_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_b_4_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_1_subtile_0__pin_a_5_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_1_subtile_0__pin_b_5_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_a_6_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_b_6_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_1_subtile_0__pin_a_7_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_1_subtile_0__pin_b_7_;
//----- OUTPUT PORTS -----
output [0:0] top_width_0_height_0_subtile_0__pin_out_0_;
//----- OUTPUT PORTS -----
output [0:0] top_width_0_height_0_subtile_0__pin_out_8_;
//----- OUTPUT PORTS -----
output [0:0] top_width_0_height_1_subtile_0__pin_out_1_;
//----- OUTPUT PORTS -----
output [0:0] top_width_0_height_1_subtile_0__pin_out_9_;
//----- OUTPUT PORTS -----
output [0:0] right_width_0_height_0_subtile_0__pin_out_2_;
//----- OUTPUT PORTS -----
output [0:0] right_width_0_height_0_subtile_0__pin_out_10_;
//----- OUTPUT PORTS -----
output [0:0] right_width_0_height_1_subtile_0__pin_out_3_;
//----- OUTPUT PORTS -----
output [0:0] right_width_0_height_1_subtile_0__pin_out_11_;
//----- OUTPUT PORTS -----
output [0:0] bottom_width_0_height_0_subtile_0__pin_out_4_;
//----- OUTPUT PORTS -----
output [0:0] bottom_width_0_height_0_subtile_0__pin_out_12_;
//----- OUTPUT PORTS -----
output [0:0] bottom_width_0_height_1_subtile_0__pin_out_5_;
//----- OUTPUT PORTS -----
output [0:0] bottom_width_0_height_1_subtile_0__pin_out_13_;
//----- OUTPUT PORTS -----
output [0:0] left_width_0_height_0_subtile_0__pin_out_6_;
//----- OUTPUT PORTS -----
output [0:0] left_width_0_height_0_subtile_0__pin_out_14_;
//----- OUTPUT PORTS -----
output [0:0] left_width_0_height_1_subtile_0__pin_out_7_;
//----- OUTPUT PORTS -----
output [0:0] left_width_0_height_1_subtile_0__pin_out_15_;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	logical_tile_mult_8_mode_mult_8_ logical_tile_mult_8_mode_mult_8__0 (
		.mult_8_a({top_width_0_height_0_subtile_0__pin_a_0_, top_width_0_height_1_subtile_0__pin_a_1_, right_width_0_height_0_subtile_0__pin_a_2_, right_width_0_height_1_subtile_0__pin_a_3_, bottom_width_0_height_0_subtile_0__pin_a_4_, bottom_width_0_height_1_subtile_0__pin_a_5_, left_width_0_height_0_subtile_0__pin_a_6_, left_width_0_height_1_subtile_0__pin_a_7_}),
		.mult_8_b({top_width_0_height_0_subtile_0__pin_b_0_, top_width_0_height_1_subtile_0__pin_b_1_, right_width_0_height_0_subtile_0__pin_b_2_, right_width_0_height_1_subtile_0__pin_b_3_, bottom_width_0_height_0_subtile_0__pin_b_4_, bottom_width_0_height_1_subtile_0__pin_b_5_, left_width_0_height_0_subtile_0__pin_b_6_, left_width_0_height_1_subtile_0__pin_b_7_}),
		.mult_8_clk(top_width_0_height_0_subtile_0__pin_clk_0_),
		.mult_8_out({top_width_0_height_0_subtile_0__pin_out_0_, top_width_0_height_1_subtile_0__pin_out_1_, right_width_0_height_0_subtile_0__pin_out_2_, right_width_0_height_1_subtile_0__pin_out_3_, bottom_width_0_height_0_subtile_0__pin_out_4_, bottom_width_0_height_1_subtile_0__pin_out_5_, left_width_0_height_0_subtile_0__pin_out_6_, left_width_0_height_1_subtile_0__pin_out_7_, top_width_0_height_0_subtile_0__pin_out_8_, top_width_0_height_1_subtile_0__pin_out_9_, right_width_0_height_0_subtile_0__pin_out_10_, right_width_0_height_1_subtile_0__pin_out_11_, bottom_width_0_height_0_subtile_0__pin_out_12_, bottom_width_0_height_1_subtile_0__pin_out_13_, left_width_0_height_0_subtile_0__pin_out_14_, left_width_0_height_1_subtile_0__pin_out_15_}));

endmodule
// ----- END Verilog module for grid_mult_8 -----

//----- Default net type -----
// `default_nettype none



// ----- END Grid Verilog module: grid_mult_8 -----

