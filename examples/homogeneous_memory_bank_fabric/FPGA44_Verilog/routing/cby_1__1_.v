//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for Unique Connection Blocks[1][1]
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for cby_1__1_ -----
module cby_1__1_(chany_bottom_in,
                 chany_top_in,
                 bl,
                 wl,
                 chany_bottom_out,
                 chany_top_out,
                 right_grid_left_width_0_height_0_subtile_0__pin_I_3_,
                 right_grid_left_width_0_height_0_subtile_0__pin_I_7_,
                 right_grid_left_width_0_height_0_subtile_0__pin_I_11_,
                 right_grid_left_width_0_height_0_subtile_0__pin_I_15_,
                 right_grid_left_width_0_height_0_subtile_0__pin_I_19_,
                 right_grid_left_width_0_height_0_subtile_0__pin_I_23_,
                 right_grid_left_width_0_height_0_subtile_0__pin_I_27_,
                 right_grid_left_width_0_height_0_subtile_0__pin_I_31_,
                 right_grid_left_width_0_height_0_subtile_0__pin_I_35_,
                 right_grid_left_width_0_height_0_subtile_0__pin_I_39_,
                 left_grid_right_width_0_height_0_subtile_0__pin_I_1_,
                 left_grid_right_width_0_height_0_subtile_0__pin_I_5_,
                 left_grid_right_width_0_height_0_subtile_0__pin_I_9_,
                 left_grid_right_width_0_height_0_subtile_0__pin_I_13_,
                 left_grid_right_width_0_height_0_subtile_0__pin_I_17_,
                 left_grid_right_width_0_height_0_subtile_0__pin_I_21_,
                 left_grid_right_width_0_height_0_subtile_0__pin_I_25_,
                 left_grid_right_width_0_height_0_subtile_0__pin_I_29_,
                 left_grid_right_width_0_height_0_subtile_0__pin_I_33_,
                 left_grid_right_width_0_height_0_subtile_0__pin_I_37_);
//----- INPUT PORTS -----
input [0:19] chany_bottom_in;
//----- INPUT PORTS -----
input [0:19] chany_top_in;
//----- INPUT PORTS -----
input [0:8] bl;
//----- INPUT PORTS -----
input [0:8] wl;
//----- OUTPUT PORTS -----
output [0:19] chany_bottom_out;
//----- OUTPUT PORTS -----
output [0:19] chany_top_out;
//----- OUTPUT PORTS -----
output [0:0] right_grid_left_width_0_height_0_subtile_0__pin_I_3_;
//----- OUTPUT PORTS -----
output [0:0] right_grid_left_width_0_height_0_subtile_0__pin_I_7_;
//----- OUTPUT PORTS -----
output [0:0] right_grid_left_width_0_height_0_subtile_0__pin_I_11_;
//----- OUTPUT PORTS -----
output [0:0] right_grid_left_width_0_height_0_subtile_0__pin_I_15_;
//----- OUTPUT PORTS -----
output [0:0] right_grid_left_width_0_height_0_subtile_0__pin_I_19_;
//----- OUTPUT PORTS -----
output [0:0] right_grid_left_width_0_height_0_subtile_0__pin_I_23_;
//----- OUTPUT PORTS -----
output [0:0] right_grid_left_width_0_height_0_subtile_0__pin_I_27_;
//----- OUTPUT PORTS -----
output [0:0] right_grid_left_width_0_height_0_subtile_0__pin_I_31_;
//----- OUTPUT PORTS -----
output [0:0] right_grid_left_width_0_height_0_subtile_0__pin_I_35_;
//----- OUTPUT PORTS -----
output [0:0] right_grid_left_width_0_height_0_subtile_0__pin_I_39_;
//----- OUTPUT PORTS -----
output [0:0] left_grid_right_width_0_height_0_subtile_0__pin_I_1_;
//----- OUTPUT PORTS -----
output [0:0] left_grid_right_width_0_height_0_subtile_0__pin_I_5_;
//----- OUTPUT PORTS -----
output [0:0] left_grid_right_width_0_height_0_subtile_0__pin_I_9_;
//----- OUTPUT PORTS -----
output [0:0] left_grid_right_width_0_height_0_subtile_0__pin_I_13_;
//----- OUTPUT PORTS -----
output [0:0] left_grid_right_width_0_height_0_subtile_0__pin_I_17_;
//----- OUTPUT PORTS -----
output [0:0] left_grid_right_width_0_height_0_subtile_0__pin_I_21_;
//----- OUTPUT PORTS -----
output [0:0] left_grid_right_width_0_height_0_subtile_0__pin_I_25_;
//----- OUTPUT PORTS -----
output [0:0] left_grid_right_width_0_height_0_subtile_0__pin_I_29_;
//----- OUTPUT PORTS -----
output [0:0] left_grid_right_width_0_height_0_subtile_0__pin_I_33_;
//----- OUTPUT PORTS -----
output [0:0] left_grid_right_width_0_height_0_subtile_0__pin_I_37_;

//----- BEGIN Registered ports -----
//----- END Registered ports -----


wire [0:3] mux2_size8_0_sram;
wire [0:3] mux2_size8_0_sram_inv;
wire [0:3] mux2_size8_10_sram;
wire [0:3] mux2_size8_10_sram_inv;
wire [0:3] mux2_size8_11_sram;
wire [0:3] mux2_size8_11_sram_inv;
wire [0:3] mux2_size8_12_sram;
wire [0:3] mux2_size8_12_sram_inv;
wire [0:3] mux2_size8_13_sram;
wire [0:3] mux2_size8_13_sram_inv;
wire [0:3] mux2_size8_14_sram;
wire [0:3] mux2_size8_14_sram_inv;
wire [0:3] mux2_size8_15_sram;
wire [0:3] mux2_size8_15_sram_inv;
wire [0:3] mux2_size8_16_sram;
wire [0:3] mux2_size8_16_sram_inv;
wire [0:3] mux2_size8_17_sram;
wire [0:3] mux2_size8_17_sram_inv;
wire [0:3] mux2_size8_18_sram;
wire [0:3] mux2_size8_18_sram_inv;
wire [0:3] mux2_size8_19_sram;
wire [0:3] mux2_size8_19_sram_inv;
wire [0:3] mux2_size8_1_sram;
wire [0:3] mux2_size8_1_sram_inv;
wire [0:3] mux2_size8_2_sram;
wire [0:3] mux2_size8_2_sram_inv;
wire [0:3] mux2_size8_3_sram;
wire [0:3] mux2_size8_3_sram_inv;
wire [0:3] mux2_size8_4_sram;
wire [0:3] mux2_size8_4_sram_inv;
wire [0:3] mux2_size8_5_sram;
wire [0:3] mux2_size8_5_sram_inv;
wire [0:3] mux2_size8_6_sram;
wire [0:3] mux2_size8_6_sram_inv;
wire [0:3] mux2_size8_7_sram;
wire [0:3] mux2_size8_7_sram_inv;
wire [0:3] mux2_size8_8_sram;
wire [0:3] mux2_size8_8_sram_inv;
wire [0:3] mux2_size8_9_sram;
wire [0:3] mux2_size8_9_sram_inv;

// ----- BEGIN Local short connections -----
// ----- Local connection due to Wire 0 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[0] = chany_bottom_in[0];
// ----- Local connection due to Wire 1 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[1] = chany_bottom_in[1];
// ----- Local connection due to Wire 2 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[2] = chany_bottom_in[2];
// ----- Local connection due to Wire 3 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[3] = chany_bottom_in[3];
// ----- Local connection due to Wire 4 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[4] = chany_bottom_in[4];
// ----- Local connection due to Wire 5 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[5] = chany_bottom_in[5];
// ----- Local connection due to Wire 6 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[6] = chany_bottom_in[6];
// ----- Local connection due to Wire 7 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[7] = chany_bottom_in[7];
// ----- Local connection due to Wire 8 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[8] = chany_bottom_in[8];
// ----- Local connection due to Wire 9 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[9] = chany_bottom_in[9];
// ----- Local connection due to Wire 10 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[10] = chany_bottom_in[10];
// ----- Local connection due to Wire 11 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[11] = chany_bottom_in[11];
// ----- Local connection due to Wire 12 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[12] = chany_bottom_in[12];
// ----- Local connection due to Wire 13 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[13] = chany_bottom_in[13];
// ----- Local connection due to Wire 14 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[14] = chany_bottom_in[14];
// ----- Local connection due to Wire 15 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[15] = chany_bottom_in[15];
// ----- Local connection due to Wire 16 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[16] = chany_bottom_in[16];
// ----- Local connection due to Wire 17 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[17] = chany_bottom_in[17];
// ----- Local connection due to Wire 18 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[18] = chany_bottom_in[18];
// ----- Local connection due to Wire 19 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[19] = chany_bottom_in[19];
// ----- Local connection due to Wire 20 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[0] = chany_top_in[0];
// ----- Local connection due to Wire 21 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[1] = chany_top_in[1];
// ----- Local connection due to Wire 22 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[2] = chany_top_in[2];
// ----- Local connection due to Wire 23 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[3] = chany_top_in[3];
// ----- Local connection due to Wire 24 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[4] = chany_top_in[4];
// ----- Local connection due to Wire 25 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[5] = chany_top_in[5];
// ----- Local connection due to Wire 26 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[6] = chany_top_in[6];
// ----- Local connection due to Wire 27 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[7] = chany_top_in[7];
// ----- Local connection due to Wire 28 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[8] = chany_top_in[8];
// ----- Local connection due to Wire 29 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[9] = chany_top_in[9];
// ----- Local connection due to Wire 30 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[10] = chany_top_in[10];
// ----- Local connection due to Wire 31 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[11] = chany_top_in[11];
// ----- Local connection due to Wire 32 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[12] = chany_top_in[12];
// ----- Local connection due to Wire 33 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[13] = chany_top_in[13];
// ----- Local connection due to Wire 34 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[14] = chany_top_in[14];
// ----- Local connection due to Wire 35 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[15] = chany_top_in[15];
// ----- Local connection due to Wire 36 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[16] = chany_top_in[16];
// ----- Local connection due to Wire 37 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[17] = chany_top_in[17];
// ----- Local connection due to Wire 38 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[18] = chany_top_in[18];
// ----- Local connection due to Wire 39 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[19] = chany_top_in[19];
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	mux2_size8 mux_left_ipin_0 (
		.in({chany_bottom_in[0], chany_top_in[0], chany_bottom_in[6], chany_top_in[6], chany_bottom_in[12], chany_top_in[12], chany_bottom_in[18], chany_top_in[18]}),
		.sram(mux2_size8_0_sram[0:3]),
		.sram_inv(mux2_size8_0_sram_inv[0:3]),
		.out(right_grid_left_width_0_height_0_subtile_0__pin_I_3_));

	mux2_size8 mux_left_ipin_1 (
		.in({chany_bottom_in[1], chany_top_in[1], chany_bottom_in[7], chany_top_in[7], chany_bottom_in[13], chany_top_in[13], chany_bottom_in[19], chany_top_in[19]}),
		.sram(mux2_size8_1_sram[0:3]),
		.sram_inv(mux2_size8_1_sram_inv[0:3]),
		.out(right_grid_left_width_0_height_0_subtile_0__pin_I_7_));

	mux2_size8 mux_left_ipin_2 (
		.in({chany_bottom_in[0], chany_top_in[0], chany_bottom_in[2], chany_top_in[2], chany_bottom_in[8], chany_top_in[8], chany_bottom_in[14], chany_top_in[14]}),
		.sram(mux2_size8_2_sram[0:3]),
		.sram_inv(mux2_size8_2_sram_inv[0:3]),
		.out(right_grid_left_width_0_height_0_subtile_0__pin_I_11_));

	mux2_size8 mux_left_ipin_3 (
		.in({chany_bottom_in[1], chany_top_in[1], chany_bottom_in[3], chany_top_in[3], chany_bottom_in[9], chany_top_in[9], chany_bottom_in[15], chany_top_in[15]}),
		.sram(mux2_size8_3_sram[0:3]),
		.sram_inv(mux2_size8_3_sram_inv[0:3]),
		.out(right_grid_left_width_0_height_0_subtile_0__pin_I_15_));

	mux2_size8 mux_left_ipin_4 (
		.in({chany_bottom_in[2], chany_top_in[2], chany_bottom_in[4], chany_top_in[4], chany_bottom_in[10], chany_top_in[10], chany_bottom_in[16], chany_top_in[16]}),
		.sram(mux2_size8_4_sram[0:3]),
		.sram_inv(mux2_size8_4_sram_inv[0:3]),
		.out(right_grid_left_width_0_height_0_subtile_0__pin_I_19_));

	mux2_size8 mux_left_ipin_5 (
		.in({chany_bottom_in[3], chany_top_in[3], chany_bottom_in[5], chany_top_in[5], chany_bottom_in[11], chany_top_in[11], chany_bottom_in[17], chany_top_in[17]}),
		.sram(mux2_size8_5_sram[0:3]),
		.sram_inv(mux2_size8_5_sram_inv[0:3]),
		.out(right_grid_left_width_0_height_0_subtile_0__pin_I_23_));

	mux2_size8 mux_left_ipin_6 (
		.in({chany_bottom_in[4], chany_top_in[4], chany_bottom_in[6], chany_top_in[6], chany_bottom_in[12], chany_top_in[12], chany_bottom_in[18], chany_top_in[18]}),
		.sram(mux2_size8_6_sram[0:3]),
		.sram_inv(mux2_size8_6_sram_inv[0:3]),
		.out(right_grid_left_width_0_height_0_subtile_0__pin_I_27_));

	mux2_size8 mux_left_ipin_7 (
		.in({chany_bottom_in[5], chany_top_in[5], chany_bottom_in[7], chany_top_in[7], chany_bottom_in[13], chany_top_in[13], chany_bottom_in[19], chany_top_in[19]}),
		.sram(mux2_size8_7_sram[0:3]),
		.sram_inv(mux2_size8_7_sram_inv[0:3]),
		.out(right_grid_left_width_0_height_0_subtile_0__pin_I_31_));

	mux2_size8 mux_left_ipin_8 (
		.in({chany_bottom_in[0], chany_top_in[0], chany_bottom_in[6], chany_top_in[6], chany_bottom_in[8], chany_top_in[8], chany_bottom_in[14], chany_top_in[14]}),
		.sram(mux2_size8_8_sram[0:3]),
		.sram_inv(mux2_size8_8_sram_inv[0:3]),
		.out(right_grid_left_width_0_height_0_subtile_0__pin_I_35_));

	mux2_size8 mux_left_ipin_9 (
		.in({chany_bottom_in[1], chany_top_in[1], chany_bottom_in[7], chany_top_in[7], chany_bottom_in[9], chany_top_in[9], chany_bottom_in[15], chany_top_in[15]}),
		.sram(mux2_size8_9_sram[0:3]),
		.sram_inv(mux2_size8_9_sram_inv[0:3]),
		.out(right_grid_left_width_0_height_0_subtile_0__pin_I_39_));

	mux2_size8 mux_right_ipin_0 (
		.in({chany_bottom_in[2], chany_top_in[2], chany_bottom_in[8], chany_top_in[8], chany_bottom_in[10], chany_top_in[10], chany_bottom_in[16], chany_top_in[16]}),
		.sram(mux2_size8_10_sram[0:3]),
		.sram_inv(mux2_size8_10_sram_inv[0:3]),
		.out(left_grid_right_width_0_height_0_subtile_0__pin_I_1_));

	mux2_size8 mux_right_ipin_1 (
		.in({chany_bottom_in[3], chany_top_in[3], chany_bottom_in[9], chany_top_in[9], chany_bottom_in[11], chany_top_in[11], chany_bottom_in[17], chany_top_in[17]}),
		.sram(mux2_size8_11_sram[0:3]),
		.sram_inv(mux2_size8_11_sram_inv[0:3]),
		.out(left_grid_right_width_0_height_0_subtile_0__pin_I_5_));

	mux2_size8 mux_right_ipin_2 (
		.in({chany_bottom_in[4], chany_top_in[4], chany_bottom_in[10], chany_top_in[10], chany_bottom_in[12], chany_top_in[12], chany_bottom_in[18], chany_top_in[18]}),
		.sram(mux2_size8_12_sram[0:3]),
		.sram_inv(mux2_size8_12_sram_inv[0:3]),
		.out(left_grid_right_width_0_height_0_subtile_0__pin_I_9_));

	mux2_size8 mux_right_ipin_3 (
		.in({chany_bottom_in[5], chany_top_in[5], chany_bottom_in[11], chany_top_in[11], chany_bottom_in[13], chany_top_in[13], chany_bottom_in[19], chany_top_in[19]}),
		.sram(mux2_size8_13_sram[0:3]),
		.sram_inv(mux2_size8_13_sram_inv[0:3]),
		.out(left_grid_right_width_0_height_0_subtile_0__pin_I_13_));

	mux2_size8 mux_right_ipin_4 (
		.in({chany_bottom_in[0], chany_top_in[0], chany_bottom_in[6], chany_top_in[6], chany_bottom_in[12], chany_top_in[12], chany_bottom_in[14], chany_top_in[14]}),
		.sram(mux2_size8_14_sram[0:3]),
		.sram_inv(mux2_size8_14_sram_inv[0:3]),
		.out(left_grid_right_width_0_height_0_subtile_0__pin_I_17_));

	mux2_size8 mux_right_ipin_5 (
		.in({chany_bottom_in[1], chany_top_in[1], chany_bottom_in[7], chany_top_in[7], chany_bottom_in[13], chany_top_in[13], chany_bottom_in[15], chany_top_in[15]}),
		.sram(mux2_size8_15_sram[0:3]),
		.sram_inv(mux2_size8_15_sram_inv[0:3]),
		.out(left_grid_right_width_0_height_0_subtile_0__pin_I_21_));

	mux2_size8 mux_right_ipin_6 (
		.in({chany_bottom_in[2], chany_top_in[2], chany_bottom_in[8], chany_top_in[8], chany_bottom_in[14], chany_top_in[14], chany_bottom_in[16], chany_top_in[16]}),
		.sram(mux2_size8_16_sram[0:3]),
		.sram_inv(mux2_size8_16_sram_inv[0:3]),
		.out(left_grid_right_width_0_height_0_subtile_0__pin_I_25_));

	mux2_size8 mux_right_ipin_7 (
		.in({chany_bottom_in[3], chany_top_in[3], chany_bottom_in[9], chany_top_in[9], chany_bottom_in[15], chany_top_in[15], chany_bottom_in[17], chany_top_in[17]}),
		.sram(mux2_size8_17_sram[0:3]),
		.sram_inv(mux2_size8_17_sram_inv[0:3]),
		.out(left_grid_right_width_0_height_0_subtile_0__pin_I_29_));

	mux2_size8 mux_right_ipin_8 (
		.in({chany_bottom_in[4], chany_top_in[4], chany_bottom_in[10], chany_top_in[10], chany_bottom_in[16], chany_top_in[16], chany_bottom_in[18], chany_top_in[18]}),
		.sram(mux2_size8_18_sram[0:3]),
		.sram_inv(mux2_size8_18_sram_inv[0:3]),
		.out(left_grid_right_width_0_height_0_subtile_0__pin_I_33_));

	mux2_size8 mux_right_ipin_9 (
		.in({chany_bottom_in[5], chany_top_in[5], chany_bottom_in[11], chany_top_in[11], chany_bottom_in[17], chany_top_in[17], chany_bottom_in[19], chany_top_in[19]}),
		.sram(mux2_size8_19_sram[0:3]),
		.sram_inv(mux2_size8_19_sram_inv[0:3]),
		.out(left_grid_right_width_0_height_0_subtile_0__pin_I_37_));

	mux2_size8_mem mem_left_ipin_0 (
		.bl(bl[0:3]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_0_sram[0:3]),
		.mem_outb(mux2_size8_0_sram_inv[0:3]));

	mux2_size8_mem mem_left_ipin_1 (
		.bl(bl[4:7]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_1_sram[0:3]),
		.mem_outb(mux2_size8_1_sram_inv[0:3]));

	mux2_size8_mem mem_left_ipin_2 (
		.bl({bl[8], bl[0:2]}),
		.wl({wl[0:1], wl[1], wl[1]}),
		.mem_out(mux2_size8_2_sram[0:3]),
		.mem_outb(mux2_size8_2_sram_inv[0:3]));

	mux2_size8_mem mem_left_ipin_3 (
		.bl(bl[3:6]),
		.wl({wl[1], wl[1], wl[1], wl[1]}),
		.mem_out(mux2_size8_3_sram[0:3]),
		.mem_outb(mux2_size8_3_sram_inv[0:3]));

	mux2_size8_mem mem_left_ipin_4 (
		.bl({bl[7:8], bl[0:1]}),
		.wl({wl[1], wl[1:2], wl[2]}),
		.mem_out(mux2_size8_4_sram[0:3]),
		.mem_outb(mux2_size8_4_sram_inv[0:3]));

	mux2_size8_mem mem_left_ipin_5 (
		.bl(bl[2:5]),
		.wl({wl[2], wl[2], wl[2], wl[2]}),
		.mem_out(mux2_size8_5_sram[0:3]),
		.mem_outb(mux2_size8_5_sram_inv[0:3]));

	mux2_size8_mem mem_left_ipin_6 (
		.bl({bl[6:8], bl[0]}),
		.wl({wl[2], wl[2], wl[2:3]}),
		.mem_out(mux2_size8_6_sram[0:3]),
		.mem_outb(mux2_size8_6_sram_inv[0:3]));

	mux2_size8_mem mem_left_ipin_7 (
		.bl(bl[1:4]),
		.wl({wl[3], wl[3], wl[3], wl[3]}),
		.mem_out(mux2_size8_7_sram[0:3]),
		.mem_outb(mux2_size8_7_sram_inv[0:3]));

	mux2_size8_mem mem_left_ipin_8 (
		.bl(bl[5:8]),
		.wl({wl[3], wl[3], wl[3], wl[3]}),
		.mem_out(mux2_size8_8_sram[0:3]),
		.mem_outb(mux2_size8_8_sram_inv[0:3]));

	mux2_size8_mem mem_left_ipin_9 (
		.bl(bl[0:3]),
		.wl({wl[4], wl[4], wl[4], wl[4]}),
		.mem_out(mux2_size8_9_sram[0:3]),
		.mem_outb(mux2_size8_9_sram_inv[0:3]));

	mux2_size8_mem mem_right_ipin_0 (
		.bl(bl[4:7]),
		.wl({wl[4], wl[4], wl[4], wl[4]}),
		.mem_out(mux2_size8_10_sram[0:3]),
		.mem_outb(mux2_size8_10_sram_inv[0:3]));

	mux2_size8_mem mem_right_ipin_1 (
		.bl({bl[8], bl[0:2]}),
		.wl({wl[4:5], wl[5], wl[5]}),
		.mem_out(mux2_size8_11_sram[0:3]),
		.mem_outb(mux2_size8_11_sram_inv[0:3]));

	mux2_size8_mem mem_right_ipin_2 (
		.bl(bl[3:6]),
		.wl({wl[5], wl[5], wl[5], wl[5]}),
		.mem_out(mux2_size8_12_sram[0:3]),
		.mem_outb(mux2_size8_12_sram_inv[0:3]));

	mux2_size8_mem mem_right_ipin_3 (
		.bl({bl[7:8], bl[0:1]}),
		.wl({wl[5], wl[5:6], wl[6]}),
		.mem_out(mux2_size8_13_sram[0:3]),
		.mem_outb(mux2_size8_13_sram_inv[0:3]));

	mux2_size8_mem mem_right_ipin_4 (
		.bl(bl[2:5]),
		.wl({wl[6], wl[6], wl[6], wl[6]}),
		.mem_out(mux2_size8_14_sram[0:3]),
		.mem_outb(mux2_size8_14_sram_inv[0:3]));

	mux2_size8_mem mem_right_ipin_5 (
		.bl({bl[6:8], bl[0]}),
		.wl({wl[6], wl[6], wl[6:7]}),
		.mem_out(mux2_size8_15_sram[0:3]),
		.mem_outb(mux2_size8_15_sram_inv[0:3]));

	mux2_size8_mem mem_right_ipin_6 (
		.bl(bl[1:4]),
		.wl({wl[7], wl[7], wl[7], wl[7]}),
		.mem_out(mux2_size8_16_sram[0:3]),
		.mem_outb(mux2_size8_16_sram_inv[0:3]));

	mux2_size8_mem mem_right_ipin_7 (
		.bl(bl[5:8]),
		.wl({wl[7], wl[7], wl[7], wl[7]}),
		.mem_out(mux2_size8_17_sram[0:3]),
		.mem_outb(mux2_size8_17_sram_inv[0:3]));

	mux2_size8_mem mem_right_ipin_8 (
		.bl(bl[0:3]),
		.wl({wl[8], wl[8], wl[8], wl[8]}),
		.mem_out(mux2_size8_18_sram[0:3]),
		.mem_outb(mux2_size8_18_sram_inv[0:3]));

	mux2_size8_mem mem_right_ipin_9 (
		.bl(bl[4:7]),
		.wl({wl[8], wl[8], wl[8], wl[8]}),
		.mem_out(mux2_size8_19_sram[0:3]),
		.mem_outb(mux2_size8_19_sram_inv[0:3]));

endmodule
// ----- END Verilog module for cby_1__1_ -----

//----- Default net type -----
// `default_nettype none




