//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for Unique Connection Blocks[1][1]
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for cbx_1__1_ -----
module cbx_1__1_(chanx_left_in,
                 chanx_right_in,
                 bl,
                 wl,
                 chanx_left_out,
                 chanx_right_out,
                 top_grid_bottom_width_0_height_0_subtile_0__pin_I_2_,
                 top_grid_bottom_width_0_height_0_subtile_0__pin_I_6_,
                 top_grid_bottom_width_0_height_0_subtile_0__pin_I_10_,
                 top_grid_bottom_width_0_height_0_subtile_0__pin_I_14_,
                 top_grid_bottom_width_0_height_0_subtile_0__pin_I_18_,
                 top_grid_bottom_width_0_height_0_subtile_0__pin_I_22_,
                 top_grid_bottom_width_0_height_0_subtile_0__pin_I_26_,
                 top_grid_bottom_width_0_height_0_subtile_0__pin_I_30_,
                 top_grid_bottom_width_0_height_0_subtile_0__pin_I_34_,
                 top_grid_bottom_width_0_height_0_subtile_0__pin_I_38_,
                 bottom_grid_top_width_0_height_0_subtile_0__pin_I_0_,
                 bottom_grid_top_width_0_height_0_subtile_0__pin_I_4_,
                 bottom_grid_top_width_0_height_0_subtile_0__pin_I_8_,
                 bottom_grid_top_width_0_height_0_subtile_0__pin_I_12_,
                 bottom_grid_top_width_0_height_0_subtile_0__pin_I_16_,
                 bottom_grid_top_width_0_height_0_subtile_0__pin_I_20_,
                 bottom_grid_top_width_0_height_0_subtile_0__pin_I_24_,
                 bottom_grid_top_width_0_height_0_subtile_0__pin_I_28_,
                 bottom_grid_top_width_0_height_0_subtile_0__pin_I_32_,
                 bottom_grid_top_width_0_height_0_subtile_0__pin_I_36_);
//----- INPUT PORTS -----
input [0:19] chanx_left_in;
//----- INPUT PORTS -----
input [0:19] chanx_right_in;
//----- INPUT PORTS -----
input [0:79] bl;
//----- INPUT PORTS -----
input [0:79] wl;
//----- OUTPUT PORTS -----
output [0:19] chanx_left_out;
//----- OUTPUT PORTS -----
output [0:19] chanx_right_out;
//----- OUTPUT PORTS -----
output [0:0] top_grid_bottom_width_0_height_0_subtile_0__pin_I_2_;
//----- OUTPUT PORTS -----
output [0:0] top_grid_bottom_width_0_height_0_subtile_0__pin_I_6_;
//----- OUTPUT PORTS -----
output [0:0] top_grid_bottom_width_0_height_0_subtile_0__pin_I_10_;
//----- OUTPUT PORTS -----
output [0:0] top_grid_bottom_width_0_height_0_subtile_0__pin_I_14_;
//----- OUTPUT PORTS -----
output [0:0] top_grid_bottom_width_0_height_0_subtile_0__pin_I_18_;
//----- OUTPUT PORTS -----
output [0:0] top_grid_bottom_width_0_height_0_subtile_0__pin_I_22_;
//----- OUTPUT PORTS -----
output [0:0] top_grid_bottom_width_0_height_0_subtile_0__pin_I_26_;
//----- OUTPUT PORTS -----
output [0:0] top_grid_bottom_width_0_height_0_subtile_0__pin_I_30_;
//----- OUTPUT PORTS -----
output [0:0] top_grid_bottom_width_0_height_0_subtile_0__pin_I_34_;
//----- OUTPUT PORTS -----
output [0:0] top_grid_bottom_width_0_height_0_subtile_0__pin_I_38_;
//----- OUTPUT PORTS -----
output [0:0] bottom_grid_top_width_0_height_0_subtile_0__pin_I_0_;
//----- OUTPUT PORTS -----
output [0:0] bottom_grid_top_width_0_height_0_subtile_0__pin_I_4_;
//----- OUTPUT PORTS -----
output [0:0] bottom_grid_top_width_0_height_0_subtile_0__pin_I_8_;
//----- OUTPUT PORTS -----
output [0:0] bottom_grid_top_width_0_height_0_subtile_0__pin_I_12_;
//----- OUTPUT PORTS -----
output [0:0] bottom_grid_top_width_0_height_0_subtile_0__pin_I_16_;
//----- OUTPUT PORTS -----
output [0:0] bottom_grid_top_width_0_height_0_subtile_0__pin_I_20_;
//----- OUTPUT PORTS -----
output [0:0] bottom_grid_top_width_0_height_0_subtile_0__pin_I_24_;
//----- OUTPUT PORTS -----
output [0:0] bottom_grid_top_width_0_height_0_subtile_0__pin_I_28_;
//----- OUTPUT PORTS -----
output [0:0] bottom_grid_top_width_0_height_0_subtile_0__pin_I_32_;
//----- OUTPUT PORTS -----
output [0:0] bottom_grid_top_width_0_height_0_subtile_0__pin_I_36_;

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
	assign chanx_right_out[0] = chanx_left_in[0];
// ----- Local connection due to Wire 1 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[1] = chanx_left_in[1];
// ----- Local connection due to Wire 2 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[2] = chanx_left_in[2];
// ----- Local connection due to Wire 3 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[3] = chanx_left_in[3];
// ----- Local connection due to Wire 4 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[4] = chanx_left_in[4];
// ----- Local connection due to Wire 5 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[5] = chanx_left_in[5];
// ----- Local connection due to Wire 6 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[6] = chanx_left_in[6];
// ----- Local connection due to Wire 7 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[7] = chanx_left_in[7];
// ----- Local connection due to Wire 8 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[8] = chanx_left_in[8];
// ----- Local connection due to Wire 9 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[9] = chanx_left_in[9];
// ----- Local connection due to Wire 10 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[10] = chanx_left_in[10];
// ----- Local connection due to Wire 11 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[11] = chanx_left_in[11];
// ----- Local connection due to Wire 12 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[12] = chanx_left_in[12];
// ----- Local connection due to Wire 13 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[13] = chanx_left_in[13];
// ----- Local connection due to Wire 14 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[14] = chanx_left_in[14];
// ----- Local connection due to Wire 15 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[15] = chanx_left_in[15];
// ----- Local connection due to Wire 16 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[16] = chanx_left_in[16];
// ----- Local connection due to Wire 17 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[17] = chanx_left_in[17];
// ----- Local connection due to Wire 18 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[18] = chanx_left_in[18];
// ----- Local connection due to Wire 19 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[19] = chanx_left_in[19];
// ----- Local connection due to Wire 20 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[0] = chanx_right_in[0];
// ----- Local connection due to Wire 21 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[1] = chanx_right_in[1];
// ----- Local connection due to Wire 22 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[2] = chanx_right_in[2];
// ----- Local connection due to Wire 23 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[3] = chanx_right_in[3];
// ----- Local connection due to Wire 24 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[4] = chanx_right_in[4];
// ----- Local connection due to Wire 25 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[5] = chanx_right_in[5];
// ----- Local connection due to Wire 26 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[6] = chanx_right_in[6];
// ----- Local connection due to Wire 27 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[7] = chanx_right_in[7];
// ----- Local connection due to Wire 28 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[8] = chanx_right_in[8];
// ----- Local connection due to Wire 29 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[9] = chanx_right_in[9];
// ----- Local connection due to Wire 30 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[10] = chanx_right_in[10];
// ----- Local connection due to Wire 31 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[11] = chanx_right_in[11];
// ----- Local connection due to Wire 32 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[12] = chanx_right_in[12];
// ----- Local connection due to Wire 33 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[13] = chanx_right_in[13];
// ----- Local connection due to Wire 34 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[14] = chanx_right_in[14];
// ----- Local connection due to Wire 35 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[15] = chanx_right_in[15];
// ----- Local connection due to Wire 36 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[16] = chanx_right_in[16];
// ----- Local connection due to Wire 37 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[17] = chanx_right_in[17];
// ----- Local connection due to Wire 38 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[18] = chanx_right_in[18];
// ----- Local connection due to Wire 39 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_left_out[19] = chanx_right_in[19];
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	mux2_size8 mux_bottom_ipin_0 (
		.in({chanx_left_in[0], chanx_right_in[0], chanx_left_in[6], chanx_right_in[6], chanx_left_in[12], chanx_right_in[12], chanx_left_in[18], chanx_right_in[18]}),
		.sram(mux2_size8_0_sram[0:3]),
		.sram_inv(mux2_size8_0_sram_inv[0:3]),
		.out(top_grid_bottom_width_0_height_0_subtile_0__pin_I_2_));

	mux2_size8 mux_bottom_ipin_1 (
		.in({chanx_left_in[1], chanx_right_in[1], chanx_left_in[7], chanx_right_in[7], chanx_left_in[13], chanx_right_in[13], chanx_left_in[19], chanx_right_in[19]}),
		.sram(mux2_size8_1_sram[0:3]),
		.sram_inv(mux2_size8_1_sram_inv[0:3]),
		.out(top_grid_bottom_width_0_height_0_subtile_0__pin_I_6_));

	mux2_size8 mux_bottom_ipin_2 (
		.in({chanx_left_in[0], chanx_right_in[0], chanx_left_in[2], chanx_right_in[2], chanx_left_in[8], chanx_right_in[8], chanx_left_in[14], chanx_right_in[14]}),
		.sram(mux2_size8_2_sram[0:3]),
		.sram_inv(mux2_size8_2_sram_inv[0:3]),
		.out(top_grid_bottom_width_0_height_0_subtile_0__pin_I_10_));

	mux2_size8 mux_bottom_ipin_3 (
		.in({chanx_left_in[1], chanx_right_in[1], chanx_left_in[3], chanx_right_in[3], chanx_left_in[9], chanx_right_in[9], chanx_left_in[15], chanx_right_in[15]}),
		.sram(mux2_size8_3_sram[0:3]),
		.sram_inv(mux2_size8_3_sram_inv[0:3]),
		.out(top_grid_bottom_width_0_height_0_subtile_0__pin_I_14_));

	mux2_size8 mux_bottom_ipin_4 (
		.in({chanx_left_in[2], chanx_right_in[2], chanx_left_in[4], chanx_right_in[4], chanx_left_in[10], chanx_right_in[10], chanx_left_in[16], chanx_right_in[16]}),
		.sram(mux2_size8_4_sram[0:3]),
		.sram_inv(mux2_size8_4_sram_inv[0:3]),
		.out(top_grid_bottom_width_0_height_0_subtile_0__pin_I_18_));

	mux2_size8 mux_bottom_ipin_5 (
		.in({chanx_left_in[3], chanx_right_in[3], chanx_left_in[5], chanx_right_in[5], chanx_left_in[11], chanx_right_in[11], chanx_left_in[17], chanx_right_in[17]}),
		.sram(mux2_size8_5_sram[0:3]),
		.sram_inv(mux2_size8_5_sram_inv[0:3]),
		.out(top_grid_bottom_width_0_height_0_subtile_0__pin_I_22_));

	mux2_size8 mux_bottom_ipin_6 (
		.in({chanx_left_in[4], chanx_right_in[4], chanx_left_in[6], chanx_right_in[6], chanx_left_in[12], chanx_right_in[12], chanx_left_in[18], chanx_right_in[18]}),
		.sram(mux2_size8_6_sram[0:3]),
		.sram_inv(mux2_size8_6_sram_inv[0:3]),
		.out(top_grid_bottom_width_0_height_0_subtile_0__pin_I_26_));

	mux2_size8 mux_bottom_ipin_7 (
		.in({chanx_left_in[5], chanx_right_in[5], chanx_left_in[7], chanx_right_in[7], chanx_left_in[13], chanx_right_in[13], chanx_left_in[19], chanx_right_in[19]}),
		.sram(mux2_size8_7_sram[0:3]),
		.sram_inv(mux2_size8_7_sram_inv[0:3]),
		.out(top_grid_bottom_width_0_height_0_subtile_0__pin_I_30_));

	mux2_size8 mux_bottom_ipin_8 (
		.in({chanx_left_in[0], chanx_right_in[0], chanx_left_in[6], chanx_right_in[6], chanx_left_in[8], chanx_right_in[8], chanx_left_in[14], chanx_right_in[14]}),
		.sram(mux2_size8_8_sram[0:3]),
		.sram_inv(mux2_size8_8_sram_inv[0:3]),
		.out(top_grid_bottom_width_0_height_0_subtile_0__pin_I_34_));

	mux2_size8 mux_bottom_ipin_9 (
		.in({chanx_left_in[1], chanx_right_in[1], chanx_left_in[7], chanx_right_in[7], chanx_left_in[9], chanx_right_in[9], chanx_left_in[15], chanx_right_in[15]}),
		.sram(mux2_size8_9_sram[0:3]),
		.sram_inv(mux2_size8_9_sram_inv[0:3]),
		.out(top_grid_bottom_width_0_height_0_subtile_0__pin_I_38_));

	mux2_size8 mux_top_ipin_0 (
		.in({chanx_left_in[2], chanx_right_in[2], chanx_left_in[8], chanx_right_in[8], chanx_left_in[10], chanx_right_in[10], chanx_left_in[16], chanx_right_in[16]}),
		.sram(mux2_size8_10_sram[0:3]),
		.sram_inv(mux2_size8_10_sram_inv[0:3]),
		.out(bottom_grid_top_width_0_height_0_subtile_0__pin_I_0_));

	mux2_size8 mux_top_ipin_1 (
		.in({chanx_left_in[3], chanx_right_in[3], chanx_left_in[9], chanx_right_in[9], chanx_left_in[11], chanx_right_in[11], chanx_left_in[17], chanx_right_in[17]}),
		.sram(mux2_size8_11_sram[0:3]),
		.sram_inv(mux2_size8_11_sram_inv[0:3]),
		.out(bottom_grid_top_width_0_height_0_subtile_0__pin_I_4_));

	mux2_size8 mux_top_ipin_2 (
		.in({chanx_left_in[4], chanx_right_in[4], chanx_left_in[10], chanx_right_in[10], chanx_left_in[12], chanx_right_in[12], chanx_left_in[18], chanx_right_in[18]}),
		.sram(mux2_size8_12_sram[0:3]),
		.sram_inv(mux2_size8_12_sram_inv[0:3]),
		.out(bottom_grid_top_width_0_height_0_subtile_0__pin_I_8_));

	mux2_size8 mux_top_ipin_3 (
		.in({chanx_left_in[5], chanx_right_in[5], chanx_left_in[11], chanx_right_in[11], chanx_left_in[13], chanx_right_in[13], chanx_left_in[19], chanx_right_in[19]}),
		.sram(mux2_size8_13_sram[0:3]),
		.sram_inv(mux2_size8_13_sram_inv[0:3]),
		.out(bottom_grid_top_width_0_height_0_subtile_0__pin_I_12_));

	mux2_size8 mux_top_ipin_4 (
		.in({chanx_left_in[0], chanx_right_in[0], chanx_left_in[6], chanx_right_in[6], chanx_left_in[12], chanx_right_in[12], chanx_left_in[14], chanx_right_in[14]}),
		.sram(mux2_size8_14_sram[0:3]),
		.sram_inv(mux2_size8_14_sram_inv[0:3]),
		.out(bottom_grid_top_width_0_height_0_subtile_0__pin_I_16_));

	mux2_size8 mux_top_ipin_5 (
		.in({chanx_left_in[1], chanx_right_in[1], chanx_left_in[7], chanx_right_in[7], chanx_left_in[13], chanx_right_in[13], chanx_left_in[15], chanx_right_in[15]}),
		.sram(mux2_size8_15_sram[0:3]),
		.sram_inv(mux2_size8_15_sram_inv[0:3]),
		.out(bottom_grid_top_width_0_height_0_subtile_0__pin_I_20_));

	mux2_size8 mux_top_ipin_6 (
		.in({chanx_left_in[2], chanx_right_in[2], chanx_left_in[8], chanx_right_in[8], chanx_left_in[14], chanx_right_in[14], chanx_left_in[16], chanx_right_in[16]}),
		.sram(mux2_size8_16_sram[0:3]),
		.sram_inv(mux2_size8_16_sram_inv[0:3]),
		.out(bottom_grid_top_width_0_height_0_subtile_0__pin_I_24_));

	mux2_size8 mux_top_ipin_7 (
		.in({chanx_left_in[3], chanx_right_in[3], chanx_left_in[9], chanx_right_in[9], chanx_left_in[15], chanx_right_in[15], chanx_left_in[17], chanx_right_in[17]}),
		.sram(mux2_size8_17_sram[0:3]),
		.sram_inv(mux2_size8_17_sram_inv[0:3]),
		.out(bottom_grid_top_width_0_height_0_subtile_0__pin_I_28_));

	mux2_size8 mux_top_ipin_8 (
		.in({chanx_left_in[4], chanx_right_in[4], chanx_left_in[10], chanx_right_in[10], chanx_left_in[16], chanx_right_in[16], chanx_left_in[18], chanx_right_in[18]}),
		.sram(mux2_size8_18_sram[0:3]),
		.sram_inv(mux2_size8_18_sram_inv[0:3]),
		.out(bottom_grid_top_width_0_height_0_subtile_0__pin_I_32_));

	mux2_size8 mux_top_ipin_9 (
		.in({chanx_left_in[5], chanx_right_in[5], chanx_left_in[11], chanx_right_in[11], chanx_left_in[17], chanx_right_in[17], chanx_left_in[19], chanx_right_in[19]}),
		.sram(mux2_size8_19_sram[0:3]),
		.sram_inv(mux2_size8_19_sram_inv[0:3]),
		.out(bottom_grid_top_width_0_height_0_subtile_0__pin_I_36_));

	mux2_size8_mem mem_bottom_ipin_0 (
		.bl(bl[0:3]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_0_sram[0:3]),
		.mem_outb(mux2_size8_0_sram_inv[0:3]));

	mux2_size8_mem mem_bottom_ipin_1 (
		.bl(bl[4:7]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_1_sram[0:3]),
		.mem_outb(mux2_size8_1_sram_inv[0:3]));

	mux2_size8_mem mem_bottom_ipin_2 (
		.bl(bl[8:11]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_2_sram[0:3]),
		.mem_outb(mux2_size8_2_sram_inv[0:3]));

	mux2_size8_mem mem_bottom_ipin_3 (
		.bl(bl[12:15]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_3_sram[0:3]),
		.mem_outb(mux2_size8_3_sram_inv[0:3]));

	mux2_size8_mem mem_bottom_ipin_4 (
		.bl(bl[16:19]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_4_sram[0:3]),
		.mem_outb(mux2_size8_4_sram_inv[0:3]));

	mux2_size8_mem mem_bottom_ipin_5 (
		.bl(bl[20:23]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_5_sram[0:3]),
		.mem_outb(mux2_size8_5_sram_inv[0:3]));

	mux2_size8_mem mem_bottom_ipin_6 (
		.bl(bl[24:27]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_6_sram[0:3]),
		.mem_outb(mux2_size8_6_sram_inv[0:3]));

	mux2_size8_mem mem_bottom_ipin_7 (
		.bl(bl[28:31]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_7_sram[0:3]),
		.mem_outb(mux2_size8_7_sram_inv[0:3]));

	mux2_size8_mem mem_bottom_ipin_8 (
		.bl(bl[32:35]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_8_sram[0:3]),
		.mem_outb(mux2_size8_8_sram_inv[0:3]));

	mux2_size8_mem mem_bottom_ipin_9 (
		.bl(bl[36:39]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_9_sram[0:3]),
		.mem_outb(mux2_size8_9_sram_inv[0:3]));

	mux2_size8_mem mem_top_ipin_0 (
		.bl(bl[40:43]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_10_sram[0:3]),
		.mem_outb(mux2_size8_10_sram_inv[0:3]));

	mux2_size8_mem mem_top_ipin_1 (
		.bl(bl[44:47]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_11_sram[0:3]),
		.mem_outb(mux2_size8_11_sram_inv[0:3]));

	mux2_size8_mem mem_top_ipin_2 (
		.bl(bl[48:51]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_12_sram[0:3]),
		.mem_outb(mux2_size8_12_sram_inv[0:3]));

	mux2_size8_mem mem_top_ipin_3 (
		.bl(bl[52:55]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_13_sram[0:3]),
		.mem_outb(mux2_size8_13_sram_inv[0:3]));

	mux2_size8_mem mem_top_ipin_4 (
		.bl(bl[56:59]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_14_sram[0:3]),
		.mem_outb(mux2_size8_14_sram_inv[0:3]));

	mux2_size8_mem mem_top_ipin_5 (
		.bl(bl[60:63]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_15_sram[0:3]),
		.mem_outb(mux2_size8_15_sram_inv[0:3]));

	mux2_size8_mem mem_top_ipin_6 (
		.bl(bl[64:67]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_16_sram[0:3]),
		.mem_outb(mux2_size8_16_sram_inv[0:3]));

	mux2_size8_mem mem_top_ipin_7 (
		.bl(bl[68:71]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_17_sram[0:3]),
		.mem_outb(mux2_size8_17_sram_inv[0:3]));

	mux2_size8_mem mem_top_ipin_8 (
		.bl(bl[72:75]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_18_sram[0:3]),
		.mem_outb(mux2_size8_18_sram_inv[0:3]));

	mux2_size8_mem mem_top_ipin_9 (
		.bl(bl[76:79]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size8_19_sram[0:3]),
		.mem_outb(mux2_size8_19_sram_inv[0:3]));

endmodule
// ----- END Verilog module for cbx_1__1_ -----

//----- Default net type -----
// `default_nettype none




