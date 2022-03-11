//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for physical tile: clb]
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

// ----- BEGIN Grid Verilog module: grid_clb -----
//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for grid_clb -----
module grid_clb(cfg_done,
                prog_reset,
                prog_clk,
                reset,
                clk,
                top_width_0_height_0_subtile_0__pin_I_0_,
                top_width_0_height_0_subtile_0__pin_I_4_,
                top_width_0_height_0_subtile_0__pin_I_8_,
                top_width_0_height_0_subtile_0__pin_I_12_,
                top_width_0_height_0_subtile_0__pin_I_16_,
                top_width_0_height_0_subtile_0__pin_I_20_,
                top_width_0_height_0_subtile_0__pin_I_24_,
                top_width_0_height_0_subtile_0__pin_I_28_,
                top_width_0_height_0_subtile_0__pin_I_32_,
                top_width_0_height_0_subtile_0__pin_I_36_,
                right_width_0_height_0_subtile_0__pin_I_1_,
                right_width_0_height_0_subtile_0__pin_I_5_,
                right_width_0_height_0_subtile_0__pin_I_9_,
                right_width_0_height_0_subtile_0__pin_I_13_,
                right_width_0_height_0_subtile_0__pin_I_17_,
                right_width_0_height_0_subtile_0__pin_I_21_,
                right_width_0_height_0_subtile_0__pin_I_25_,
                right_width_0_height_0_subtile_0__pin_I_29_,
                right_width_0_height_0_subtile_0__pin_I_33_,
                right_width_0_height_0_subtile_0__pin_I_37_,
                bottom_width_0_height_0_subtile_0__pin_I_2_,
                bottom_width_0_height_0_subtile_0__pin_I_6_,
                bottom_width_0_height_0_subtile_0__pin_I_10_,
                bottom_width_0_height_0_subtile_0__pin_I_14_,
                bottom_width_0_height_0_subtile_0__pin_I_18_,
                bottom_width_0_height_0_subtile_0__pin_I_22_,
                bottom_width_0_height_0_subtile_0__pin_I_26_,
                bottom_width_0_height_0_subtile_0__pin_I_30_,
                bottom_width_0_height_0_subtile_0__pin_I_34_,
                bottom_width_0_height_0_subtile_0__pin_I_38_,
                bottom_width_0_height_0_subtile_0__pin_clk_0_,
                left_width_0_height_0_subtile_0__pin_I_3_,
                left_width_0_height_0_subtile_0__pin_I_7_,
                left_width_0_height_0_subtile_0__pin_I_11_,
                left_width_0_height_0_subtile_0__pin_I_15_,
                left_width_0_height_0_subtile_0__pin_I_19_,
                left_width_0_height_0_subtile_0__pin_I_23_,
                left_width_0_height_0_subtile_0__pin_I_27_,
                left_width_0_height_0_subtile_0__pin_I_31_,
                left_width_0_height_0_subtile_0__pin_I_35_,
                left_width_0_height_0_subtile_0__pin_I_39_,
                ccff_head,
                top_width_0_height_0_subtile_0__pin_O_0_,
                top_width_0_height_0_subtile_0__pin_O_4_,
                top_width_0_height_0_subtile_0__pin_O_8_,
                right_width_0_height_0_subtile_0__pin_O_1_,
                right_width_0_height_0_subtile_0__pin_O_5_,
                right_width_0_height_0_subtile_0__pin_O_9_,
                bottom_width_0_height_0_subtile_0__pin_O_2_,
                bottom_width_0_height_0_subtile_0__pin_O_6_,
                left_width_0_height_0_subtile_0__pin_O_3_,
                left_width_0_height_0_subtile_0__pin_O_7_,
                ccff_tail);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- GLOBAL PORTS -----
input [0:0] reset;
//----- GLOBAL PORTS -----
input [0:0] clk;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_I_0_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_I_4_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_I_8_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_I_12_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_I_16_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_I_20_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_I_24_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_I_28_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_I_32_;
//----- INPUT PORTS -----
input [0:0] top_width_0_height_0_subtile_0__pin_I_36_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_I_1_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_I_5_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_I_9_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_I_13_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_I_17_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_I_21_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_I_25_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_I_29_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_I_33_;
//----- INPUT PORTS -----
input [0:0] right_width_0_height_0_subtile_0__pin_I_37_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_I_2_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_I_6_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_I_10_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_I_14_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_I_18_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_I_22_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_I_26_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_I_30_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_I_34_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_I_38_;
//----- INPUT PORTS -----
input [0:0] bottom_width_0_height_0_subtile_0__pin_clk_0_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_I_3_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_I_7_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_I_11_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_I_15_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_I_19_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_I_23_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_I_27_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_I_31_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_I_35_;
//----- INPUT PORTS -----
input [0:0] left_width_0_height_0_subtile_0__pin_I_39_;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] top_width_0_height_0_subtile_0__pin_O_0_;
//----- OUTPUT PORTS -----
output [0:0] top_width_0_height_0_subtile_0__pin_O_4_;
//----- OUTPUT PORTS -----
output [0:0] top_width_0_height_0_subtile_0__pin_O_8_;
//----- OUTPUT PORTS -----
output [0:0] right_width_0_height_0_subtile_0__pin_O_1_;
//----- OUTPUT PORTS -----
output [0:0] right_width_0_height_0_subtile_0__pin_O_5_;
//----- OUTPUT PORTS -----
output [0:0] right_width_0_height_0_subtile_0__pin_O_9_;
//----- OUTPUT PORTS -----
output [0:0] bottom_width_0_height_0_subtile_0__pin_O_2_;
//----- OUTPUT PORTS -----
output [0:0] bottom_width_0_height_0_subtile_0__pin_O_6_;
//----- OUTPUT PORTS -----
output [0:0] left_width_0_height_0_subtile_0__pin_O_3_;
//----- OUTPUT PORTS -----
output [0:0] left_width_0_height_0_subtile_0__pin_O_7_;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	logical_tile_clb_mode_clb_ logical_tile_clb_mode_clb__0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.clb_I({top_width_0_height_0_subtile_0__pin_I_0_, right_width_0_height_0_subtile_0__pin_I_1_, bottom_width_0_height_0_subtile_0__pin_I_2_, left_width_0_height_0_subtile_0__pin_I_3_, top_width_0_height_0_subtile_0__pin_I_4_, right_width_0_height_0_subtile_0__pin_I_5_, bottom_width_0_height_0_subtile_0__pin_I_6_, left_width_0_height_0_subtile_0__pin_I_7_, top_width_0_height_0_subtile_0__pin_I_8_, right_width_0_height_0_subtile_0__pin_I_9_, bottom_width_0_height_0_subtile_0__pin_I_10_, left_width_0_height_0_subtile_0__pin_I_11_, top_width_0_height_0_subtile_0__pin_I_12_, right_width_0_height_0_subtile_0__pin_I_13_, bottom_width_0_height_0_subtile_0__pin_I_14_, left_width_0_height_0_subtile_0__pin_I_15_, top_width_0_height_0_subtile_0__pin_I_16_, right_width_0_height_0_subtile_0__pin_I_17_, bottom_width_0_height_0_subtile_0__pin_I_18_, left_width_0_height_0_subtile_0__pin_I_19_, top_width_0_height_0_subtile_0__pin_I_20_, right_width_0_height_0_subtile_0__pin_I_21_, bottom_width_0_height_0_subtile_0__pin_I_22_, left_width_0_height_0_subtile_0__pin_I_23_, top_width_0_height_0_subtile_0__pin_I_24_, right_width_0_height_0_subtile_0__pin_I_25_, bottom_width_0_height_0_subtile_0__pin_I_26_, left_width_0_height_0_subtile_0__pin_I_27_, top_width_0_height_0_subtile_0__pin_I_28_, right_width_0_height_0_subtile_0__pin_I_29_, bottom_width_0_height_0_subtile_0__pin_I_30_, left_width_0_height_0_subtile_0__pin_I_31_, top_width_0_height_0_subtile_0__pin_I_32_, right_width_0_height_0_subtile_0__pin_I_33_, bottom_width_0_height_0_subtile_0__pin_I_34_, left_width_0_height_0_subtile_0__pin_I_35_, top_width_0_height_0_subtile_0__pin_I_36_, right_width_0_height_0_subtile_0__pin_I_37_, bottom_width_0_height_0_subtile_0__pin_I_38_, left_width_0_height_0_subtile_0__pin_I_39_}),
		.clb_clk(bottom_width_0_height_0_subtile_0__pin_clk_0_),
		.ccff_head(ccff_head),
		.clb_O({top_width_0_height_0_subtile_0__pin_O_0_, right_width_0_height_0_subtile_0__pin_O_1_, bottom_width_0_height_0_subtile_0__pin_O_2_, left_width_0_height_0_subtile_0__pin_O_3_, top_width_0_height_0_subtile_0__pin_O_4_, right_width_0_height_0_subtile_0__pin_O_5_, bottom_width_0_height_0_subtile_0__pin_O_6_, left_width_0_height_0_subtile_0__pin_O_7_, top_width_0_height_0_subtile_0__pin_O_8_, right_width_0_height_0_subtile_0__pin_O_9_}),
		.ccff_tail(ccff_tail));

endmodule
// ----- END Verilog module for grid_clb -----

//----- Default net type -----
// `default_nettype none



// ----- END Grid Verilog module: grid_clb -----

