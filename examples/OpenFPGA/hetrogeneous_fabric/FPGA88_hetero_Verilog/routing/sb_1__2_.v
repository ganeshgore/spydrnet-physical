//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for Unique Switch Blocks[1][2]
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for sb_1__2_ -----
module sb_1__2_(cfg_done,
                prog_reset,
                prog_clk,
                chany_top_in,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_,
                top_right_grid_left_width_0_height_0_subtile_0__pin_out_6_,
                top_right_grid_left_width_0_height_0_subtile_0__pin_out_14_,
                chanx_right_in,
                right_top_grid_bottom_width_0_height_0_subtile_0__pin_out_4_,
                right_top_grid_bottom_width_0_height_0_subtile_0__pin_out_12_,
                right_bottom_grid_top_width_0_height_1_subtile_0__pin_out_1_,
                right_bottom_grid_top_width_0_height_1_subtile_0__pin_out_9_,
                chany_bottom_in,
                bottom_right_grid_left_width_0_height_1_subtile_0__pin_out_7_,
                bottom_right_grid_left_width_0_height_1_subtile_0__pin_out_15_,
                bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_1_,
                bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_5_,
                bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_9_,
                chanx_left_in,
                left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_,
                left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_,
                left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_0_,
                left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_4_,
                left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_8_,
                ccff_head,
                chany_top_out,
                chanx_right_out,
                chany_bottom_out,
                chanx_left_out,
                ccff_tail);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:19] chany_top_in;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_0__pin_out_6_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_0__pin_out_14_;
//----- INPUT PORTS -----
input [0:19] chanx_right_in;
//----- INPUT PORTS -----
input [0:0] right_top_grid_bottom_width_0_height_0_subtile_0__pin_out_4_;
//----- INPUT PORTS -----
input [0:0] right_top_grid_bottom_width_0_height_0_subtile_0__pin_out_12_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_1_subtile_0__pin_out_1_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_1_subtile_0__pin_out_9_;
//----- INPUT PORTS -----
input [0:19] chany_bottom_in;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_1_subtile_0__pin_out_7_;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_1_subtile_0__pin_out_15_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_1_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_5_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_9_;
//----- INPUT PORTS -----
input [0:19] chanx_left_in;
//----- INPUT PORTS -----
input [0:0] left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_;
//----- INPUT PORTS -----
input [0:0] left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_0_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_4_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_8_;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:19] chany_top_out;
//----- OUTPUT PORTS -----
output [0:19] chanx_right_out;
//----- OUTPUT PORTS -----
output [0:19] chany_bottom_out;
//----- OUTPUT PORTS -----
output [0:19] chanx_left_out;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;

//----- BEGIN Registered ports -----
//----- END Registered ports -----


wire [0:3] mux2_size11_0_sram;
wire [0:3] mux2_size11_0_sram_inv;
wire [0:3] mux2_size12_0_sram;
wire [0:3] mux2_size12_0_sram_inv;
wire [0:3] mux2_size12_10_sram;
wire [0:3] mux2_size12_10_sram_inv;
wire [0:3] mux2_size12_11_sram;
wire [0:3] mux2_size12_11_sram_inv;
wire [0:3] mux2_size12_12_sram;
wire [0:3] mux2_size12_12_sram_inv;
wire [0:3] mux2_size12_13_sram;
wire [0:3] mux2_size12_13_sram_inv;
wire [0:3] mux2_size12_14_sram;
wire [0:3] mux2_size12_14_sram_inv;
wire [0:3] mux2_size12_15_sram;
wire [0:3] mux2_size12_15_sram_inv;
wire [0:3] mux2_size12_16_sram;
wire [0:3] mux2_size12_16_sram_inv;
wire [0:3] mux2_size12_17_sram;
wire [0:3] mux2_size12_17_sram_inv;
wire [0:3] mux2_size12_18_sram;
wire [0:3] mux2_size12_18_sram_inv;
wire [0:3] mux2_size12_1_sram;
wire [0:3] mux2_size12_1_sram_inv;
wire [0:3] mux2_size12_2_sram;
wire [0:3] mux2_size12_2_sram_inv;
wire [0:3] mux2_size12_3_sram;
wire [0:3] mux2_size12_3_sram_inv;
wire [0:3] mux2_size12_4_sram;
wire [0:3] mux2_size12_4_sram_inv;
wire [0:3] mux2_size12_5_sram;
wire [0:3] mux2_size12_5_sram_inv;
wire [0:3] mux2_size12_6_sram;
wire [0:3] mux2_size12_6_sram_inv;
wire [0:3] mux2_size12_7_sram;
wire [0:3] mux2_size12_7_sram_inv;
wire [0:3] mux2_size12_8_sram;
wire [0:3] mux2_size12_8_sram_inv;
wire [0:3] mux2_size12_9_sram;
wire [0:3] mux2_size12_9_sram_inv;

// ----- BEGIN Local short connections -----
// ----- Local connection due to Wire 0 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chany_bottom_out[1] = chany_top_in[0];
// ----- Local connection due to Wire 1 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[2] = chany_top_in[1];
// ----- Local connection due to Wire 2 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[3] = chany_top_in[2];
// ----- Local connection due to Wire 4 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[5] = chany_top_in[4];
// ----- Local connection due to Wire 5 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[6] = chany_top_in[5];
// ----- Local connection due to Wire 6 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chany_bottom_out[7] = chany_top_in[6];
// ----- Local connection due to Wire 8 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chany_bottom_out[9] = chany_top_in[8];
// ----- Local connection due to Wire 9 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chany_bottom_out[10] = chany_top_in[9];
// ----- Local connection due to Wire 10 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[11] = chany_top_in[10];
// ----- Local connection due to Wire 12 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[13] = chany_top_in[12];
// ----- Local connection due to Wire 13 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chany_bottom_out[14] = chany_top_in[13];
// ----- Local connection due to Wire 14 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chany_bottom_out[15] = chany_top_in[14];
// ----- Local connection due to Wire 16 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chany_bottom_out[17] = chany_top_in[16];
// ----- Local connection due to Wire 17 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chany_bottom_out[18] = chany_top_in[17];
// ----- Local connection due to Wire 18 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chany_bottom_out[19] = chany_top_in[18];
// ----- Local connection due to Wire 25 -----
// ----- Net source id 0 -----
// ----- Net sink id 3 -----
	assign chanx_left_out[1] = chanx_right_in[0];
// ----- Local connection due to Wire 26 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[2] = chanx_right_in[1];
// ----- Local connection due to Wire 27 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[3] = chanx_right_in[2];
// ----- Local connection due to Wire 29 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[5] = chanx_right_in[4];
// ----- Local connection due to Wire 30 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[6] = chanx_right_in[5];
// ----- Local connection due to Wire 31 -----
// ----- Net source id 0 -----
// ----- Net sink id 3 -----
	assign chanx_left_out[7] = chanx_right_in[6];
// ----- Local connection due to Wire 33 -----
// ----- Net source id 0 -----
// ----- Net sink id 3 -----
	assign chanx_left_out[9] = chanx_right_in[8];
// ----- Local connection due to Wire 34 -----
// ----- Net source id 0 -----
// ----- Net sink id 3 -----
	assign chanx_left_out[10] = chanx_right_in[9];
// ----- Local connection due to Wire 35 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[11] = chanx_right_in[10];
// ----- Local connection due to Wire 37 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[13] = chanx_right_in[12];
// ----- Local connection due to Wire 38 -----
// ----- Net source id 0 -----
// ----- Net sink id 3 -----
	assign chanx_left_out[14] = chanx_right_in[13];
// ----- Local connection due to Wire 39 -----
// ----- Net source id 0 -----
// ----- Net sink id 3 -----
	assign chanx_left_out[15] = chanx_right_in[14];
// ----- Local connection due to Wire 41 -----
// ----- Net source id 0 -----
// ----- Net sink id 3 -----
	assign chanx_left_out[17] = chanx_right_in[16];
// ----- Local connection due to Wire 42 -----
// ----- Net source id 0 -----
// ----- Net sink id 3 -----
	assign chanx_left_out[18] = chanx_right_in[17];
// ----- Local connection due to Wire 43 -----
// ----- Net source id 0 -----
// ----- Net sink id 3 -----
	assign chanx_left_out[19] = chanx_right_in[18];
// ----- Local connection due to Wire 49 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[1] = chany_bottom_in[0];
// ----- Local connection due to Wire 50 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[2] = chany_bottom_in[1];
// ----- Local connection due to Wire 51 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[3] = chany_bottom_in[2];
// ----- Local connection due to Wire 53 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[5] = chany_bottom_in[4];
// ----- Local connection due to Wire 54 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[6] = chany_bottom_in[5];
// ----- Local connection due to Wire 55 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[7] = chany_bottom_in[6];
// ----- Local connection due to Wire 57 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[9] = chany_bottom_in[8];
// ----- Local connection due to Wire 58 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[10] = chany_bottom_in[9];
// ----- Local connection due to Wire 59 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[11] = chany_bottom_in[10];
// ----- Local connection due to Wire 61 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[13] = chany_bottom_in[12];
// ----- Local connection due to Wire 62 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[14] = chany_bottom_in[13];
// ----- Local connection due to Wire 63 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[15] = chany_bottom_in[14];
// ----- Local connection due to Wire 65 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[17] = chany_bottom_in[16];
// ----- Local connection due to Wire 66 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[18] = chany_bottom_in[17];
// ----- Local connection due to Wire 67 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[19] = chany_bottom_in[18];
// ----- Local connection due to Wire 74 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[1] = chanx_left_in[0];
// ----- Local connection due to Wire 75 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[2] = chanx_left_in[1];
// ----- Local connection due to Wire 76 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[3] = chanx_left_in[2];
// ----- Local connection due to Wire 78 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[5] = chanx_left_in[4];
// ----- Local connection due to Wire 79 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[6] = chanx_left_in[5];
// ----- Local connection due to Wire 80 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[7] = chanx_left_in[6];
// ----- Local connection due to Wire 82 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[9] = chanx_left_in[8];
// ----- Local connection due to Wire 83 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[10] = chanx_left_in[9];
// ----- Local connection due to Wire 84 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[11] = chanx_left_in[10];
// ----- Local connection due to Wire 86 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[13] = chanx_left_in[12];
// ----- Local connection due to Wire 87 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[14] = chanx_left_in[13];
// ----- Local connection due to Wire 88 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[15] = chanx_left_in[14];
// ----- Local connection due to Wire 90 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[17] = chanx_left_in[16];
// ----- Local connection due to Wire 91 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[18] = chanx_left_in[17];
// ----- Local connection due to Wire 92 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[19] = chanx_left_in[18];
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	mux2_size12 mux_top_track_0 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_, chanx_right_in[1], chanx_right_in[7:8], chanx_right_in[14], chany_bottom_in[0], chany_bottom_in[6], chany_bottom_in[13], chanx_left_in[0], chanx_left_in[3], chanx_left_in[6], chanx_left_in[13]}),
		.sram(mux2_size12_0_sram[0:3]),
		.sram_inv(mux2_size12_0_sram_inv[0:3]),
		.out(chany_top_out[0]));

	mux2_size12 mux_top_track_8 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_, chanx_right_in[2], chanx_right_in[9], chanx_right_in[11], chanx_right_in[16], chany_bottom_in[1], chany_bottom_in[8], chany_bottom_in[14], chanx_left_in[5], chanx_left_in[12], chanx_left_in[18:19]}),
		.sram(mux2_size12_1_sram[0:3]),
		.sram_inv(mux2_size12_1_sram_inv[0:3]),
		.out(chany_top_out[4]));

	mux2_size12 mux_top_track_16 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_, chanx_right_in[4], chanx_right_in[10], chanx_right_in[15], chanx_right_in[17], chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[16], chanx_left_in[4], chanx_left_in[10], chanx_left_in[15], chanx_left_in[17]}),
		.sram(mux2_size12_2_sram[0:3]),
		.sram_inv(mux2_size12_2_sram_inv[0:3]),
		.out(chany_top_out[8]));

	mux2_size12 mux_top_track_24 (
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_out_6_, chanx_right_in[5], chanx_right_in[12], chanx_right_in[18:19], chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[17], chanx_left_in[2], chanx_left_in[9], chanx_left_in[11], chanx_left_in[16]}),
		.sram(mux2_size12_3_sram[0:3]),
		.sram_inv(mux2_size12_3_sram_inv[0:3]),
		.out(chany_top_out[12]));

	mux2_size12 mux_top_track_32 (
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_out_14_, chanx_right_in[0], chanx_right_in[3], chanx_right_in[6], chanx_right_in[13], chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18], chanx_left_in[1], chanx_left_in[7:8], chanx_left_in[14]}),
		.sram(mux2_size12_4_sram[0:3]),
		.sram_inv(mux2_size12_4_sram_inv[0:3]),
		.out(chany_top_out[16]));

	mux2_size12 mux_right_track_0 (
		.in({chany_top_in[5], chany_top_in[12], chany_top_in[18:19], right_top_grid_bottom_width_0_height_0_subtile_0__pin_out_4_, chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[15], chany_bottom_in[17], chanx_left_in[0], chanx_left_in[6], chanx_left_in[13]}),
		.sram(mux2_size12_5_sram[0:3]),
		.sram_inv(mux2_size12_5_sram_inv[0:3]),
		.out(chanx_right_out[0]));

	mux2_size12 mux_right_track_8 (
		.in({chany_top_in[0], chany_top_in[3], chany_top_in[6], chany_top_in[13], right_top_grid_bottom_width_0_height_0_subtile_0__pin_out_12_, chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[11], chany_bottom_in[16], chanx_left_in[1], chanx_left_in[8], chanx_left_in[14]}),
		.sram(mux2_size12_6_sram[0:3]),
		.sram_inv(mux2_size12_6_sram_inv[0:3]),
		.out(chanx_right_out[4]));

	mux2_size12 mux_right_track_16 (
		.in({chany_top_in[1], chany_top_in[7:8], chany_top_in[14], right_bottom_grid_top_width_0_height_1_subtile_0__pin_out_1_, chany_bottom_in[1], chany_bottom_in[7:8], chany_bottom_in[14], chanx_left_in[2], chanx_left_in[9], chanx_left_in[16]}),
		.sram(mux2_size12_7_sram[0:3]),
		.sram_inv(mux2_size12_7_sram_inv[0:3]),
		.out(chanx_right_out[8]));

	mux2_size12 mux_right_track_24 (
		.in({chany_top_in[2], chany_top_in[9], chany_top_in[11], chany_top_in[16], right_bottom_grid_top_width_0_height_1_subtile_0__pin_out_9_, chany_bottom_in[0], chany_bottom_in[3], chany_bottom_in[6], chany_bottom_in[13], chanx_left_in[4], chanx_left_in[10], chanx_left_in[17]}),
		.sram(mux2_size12_8_sram[0:3]),
		.sram_inv(mux2_size12_8_sram_inv[0:3]),
		.out(chanx_right_out[12]));

	mux2_size12 mux_bottom_track_1 (
		.in({chany_top_in[0], chany_top_in[6], chany_top_in[13], chanx_right_in[4], chanx_right_in[10], chanx_right_in[15], chanx_right_in[17], bottom_right_grid_left_width_0_height_1_subtile_0__pin_out_7_, chanx_left_in[1], chanx_left_in[7:8], chanx_left_in[14]}),
		.sram(mux2_size12_9_sram[0:3]),
		.sram_inv(mux2_size12_9_sram_inv[0:3]),
		.out(chany_bottom_out[0]));

	mux2_size12 mux_bottom_track_9 (
		.in({chany_top_in[1], chany_top_in[8], chany_top_in[14], chanx_right_in[2], chanx_right_in[9], chanx_right_in[11], chanx_right_in[16], bottom_right_grid_left_width_0_height_1_subtile_0__pin_out_15_, chanx_left_in[2], chanx_left_in[9], chanx_left_in[11], chanx_left_in[16]}),
		.sram(mux2_size12_10_sram[0:3]),
		.sram_inv(mux2_size12_10_sram_inv[0:3]),
		.out(chany_bottom_out[4]));

	mux2_size12 mux_bottom_track_17 (
		.in({chany_top_in[2], chany_top_in[9], chany_top_in[16], chanx_right_in[1], chanx_right_in[7:8], chanx_right_in[14], bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_1_, chanx_left_in[4], chanx_left_in[10], chanx_left_in[15], chanx_left_in[17]}),
		.sram(mux2_size12_11_sram[0:3]),
		.sram_inv(mux2_size12_11_sram_inv[0:3]),
		.out(chany_bottom_out[8]));

	mux2_size12 mux_bottom_track_25 (
		.in({chany_top_in[4], chany_top_in[10], chany_top_in[17], chanx_right_in[0], chanx_right_in[3], chanx_right_in[6], chanx_right_in[13], bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_5_, chanx_left_in[5], chanx_left_in[12], chanx_left_in[18:19]}),
		.sram(mux2_size12_12_sram[0:3]),
		.sram_inv(mux2_size12_12_sram_inv[0:3]),
		.out(chany_bottom_out[12]));

	mux2_size12 mux_bottom_track_33 (
		.in({chany_top_in[5], chany_top_in[12], chany_top_in[18], chanx_right_in[5], chanx_right_in[12], chanx_right_in[18:19], bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_9_, chanx_left_in[0], chanx_left_in[3], chanx_left_in[6], chanx_left_in[13]}),
		.sram(mux2_size12_13_sram[0:3]),
		.sram_inv(mux2_size12_13_sram_inv[0:3]),
		.out(chany_bottom_out[16]));

	mux2_size12 mux_left_track_1 (
		.in({chany_top_in[0], chany_top_in[3], chany_top_in[6], chany_top_in[13], chanx_right_in[0], chanx_right_in[6], chanx_right_in[13], chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18:19], left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_}),
		.sram(mux2_size12_14_sram[0:3]),
		.sram_inv(mux2_size12_14_sram_inv[0:3]),
		.out(chanx_left_out[0]));

	mux2_size12 mux_left_track_9 (
		.in({chany_top_in[5], chany_top_in[12], chany_top_in[18:19], chanx_right_in[1], chanx_right_in[8], chanx_right_in[14], chany_bottom_in[0], chany_bottom_in[3], chany_bottom_in[6], chany_bottom_in[13], left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_}),
		.sram(mux2_size12_15_sram[0:3]),
		.sram_inv(mux2_size12_15_sram_inv[0:3]),
		.out(chanx_left_out[4]));

	mux2_size12 mux_left_track_17 (
		.in({chany_top_in[4], chany_top_in[10], chany_top_in[15], chany_top_in[17], chanx_right_in[2], chanx_right_in[9], chanx_right_in[16], chany_bottom_in[1], chany_bottom_in[7:8], chany_bottom_in[14], left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_0_}),
		.sram(mux2_size12_16_sram[0:3]),
		.sram_inv(mux2_size12_16_sram_inv[0:3]),
		.out(chanx_left_out[8]));

	mux2_size12 mux_left_track_25 (
		.in({chany_top_in[2], chany_top_in[9], chany_top_in[11], chany_top_in[16], chanx_right_in[4], chanx_right_in[10], chanx_right_in[17], chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[11], chany_bottom_in[16], left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_4_}),
		.sram(mux2_size12_17_sram[0:3]),
		.sram_inv(mux2_size12_17_sram_inv[0:3]),
		.out(chanx_left_out[12]));

	mux2_size12 mux_left_track_33 (
		.in({chany_top_in[1], chany_top_in[7:8], chany_top_in[14], chanx_right_in[5], chanx_right_in[12], chanx_right_in[18], chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[15], chany_bottom_in[17], left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_8_}),
		.sram(mux2_size12_18_sram[0:3]),
		.sram_inv(mux2_size12_18_sram_inv[0:3]),
		.out(chanx_left_out[16]));

	mux2_size12_mem mem_top_track_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(ccff_head),
		.ccff_tail(mux2_size12_mem_0_ccff_tail),
		.mem_out(mux2_size12_0_sram[0:3]),
		.mem_outb(mux2_size12_0_sram_inv[0:3]));

	mux2_size12_mem mem_top_track_8 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_0_ccff_tail),
		.ccff_tail(mux2_size12_mem_1_ccff_tail),
		.mem_out(mux2_size12_1_sram[0:3]),
		.mem_outb(mux2_size12_1_sram_inv[0:3]));

	mux2_size12_mem mem_top_track_16 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_1_ccff_tail),
		.ccff_tail(mux2_size12_mem_2_ccff_tail),
		.mem_out(mux2_size12_2_sram[0:3]),
		.mem_outb(mux2_size12_2_sram_inv[0:3]));

	mux2_size12_mem mem_top_track_24 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_2_ccff_tail),
		.ccff_tail(mux2_size12_mem_3_ccff_tail),
		.mem_out(mux2_size12_3_sram[0:3]),
		.mem_outb(mux2_size12_3_sram_inv[0:3]));

	mux2_size12_mem mem_top_track_32 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_3_ccff_tail),
		.ccff_tail(mux2_size12_mem_4_ccff_tail),
		.mem_out(mux2_size12_4_sram[0:3]),
		.mem_outb(mux2_size12_4_sram_inv[0:3]));

	mux2_size12_mem mem_right_track_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_4_ccff_tail),
		.ccff_tail(mux2_size12_mem_5_ccff_tail),
		.mem_out(mux2_size12_5_sram[0:3]),
		.mem_outb(mux2_size12_5_sram_inv[0:3]));

	mux2_size12_mem mem_right_track_8 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_5_ccff_tail),
		.ccff_tail(mux2_size12_mem_6_ccff_tail),
		.mem_out(mux2_size12_6_sram[0:3]),
		.mem_outb(mux2_size12_6_sram_inv[0:3]));

	mux2_size12_mem mem_right_track_16 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_6_ccff_tail),
		.ccff_tail(mux2_size12_mem_7_ccff_tail),
		.mem_out(mux2_size12_7_sram[0:3]),
		.mem_outb(mux2_size12_7_sram_inv[0:3]));

	mux2_size12_mem mem_right_track_24 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_7_ccff_tail),
		.ccff_tail(mux2_size12_mem_8_ccff_tail),
		.mem_out(mux2_size12_8_sram[0:3]),
		.mem_outb(mux2_size12_8_sram_inv[0:3]));

	mux2_size12_mem mem_bottom_track_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size11_mem_0_ccff_tail),
		.ccff_tail(mux2_size12_mem_9_ccff_tail),
		.mem_out(mux2_size12_9_sram[0:3]),
		.mem_outb(mux2_size12_9_sram_inv[0:3]));

	mux2_size12_mem mem_bottom_track_9 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_9_ccff_tail),
		.ccff_tail(mux2_size12_mem_10_ccff_tail),
		.mem_out(mux2_size12_10_sram[0:3]),
		.mem_outb(mux2_size12_10_sram_inv[0:3]));

	mux2_size12_mem mem_bottom_track_17 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_10_ccff_tail),
		.ccff_tail(mux2_size12_mem_11_ccff_tail),
		.mem_out(mux2_size12_11_sram[0:3]),
		.mem_outb(mux2_size12_11_sram_inv[0:3]));

	mux2_size12_mem mem_bottom_track_25 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_11_ccff_tail),
		.ccff_tail(mux2_size12_mem_12_ccff_tail),
		.mem_out(mux2_size12_12_sram[0:3]),
		.mem_outb(mux2_size12_12_sram_inv[0:3]));

	mux2_size12_mem mem_bottom_track_33 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_12_ccff_tail),
		.ccff_tail(mux2_size12_mem_13_ccff_tail),
		.mem_out(mux2_size12_13_sram[0:3]),
		.mem_outb(mux2_size12_13_sram_inv[0:3]));

	mux2_size12_mem mem_left_track_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_13_ccff_tail),
		.ccff_tail(mux2_size12_mem_14_ccff_tail),
		.mem_out(mux2_size12_14_sram[0:3]),
		.mem_outb(mux2_size12_14_sram_inv[0:3]));

	mux2_size12_mem mem_left_track_9 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_14_ccff_tail),
		.ccff_tail(mux2_size12_mem_15_ccff_tail),
		.mem_out(mux2_size12_15_sram[0:3]),
		.mem_outb(mux2_size12_15_sram_inv[0:3]));

	mux2_size12_mem mem_left_track_17 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_15_ccff_tail),
		.ccff_tail(mux2_size12_mem_16_ccff_tail),
		.mem_out(mux2_size12_16_sram[0:3]),
		.mem_outb(mux2_size12_16_sram_inv[0:3]));

	mux2_size12_mem mem_left_track_25 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_16_ccff_tail),
		.ccff_tail(mux2_size12_mem_17_ccff_tail),
		.mem_out(mux2_size12_17_sram[0:3]),
		.mem_outb(mux2_size12_17_sram_inv[0:3]));

	mux2_size12_mem mem_left_track_33 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_17_ccff_tail),
		.ccff_tail(ccff_tail),
		.mem_out(mux2_size12_18_sram[0:3]),
		.mem_outb(mux2_size12_18_sram_inv[0:3]));

	mux2_size11 mux_right_track_32 (
		.in({chany_top_in[4], chany_top_in[10], chany_top_in[15], chany_top_in[17], chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18:19], chanx_left_in[5], chanx_left_in[12], chanx_left_in[18]}),
		.sram(mux2_size11_0_sram[0:3]),
		.sram_inv(mux2_size11_0_sram_inv[0:3]),
		.out(chanx_right_out[16]));

	mux2_size11_mem mem_right_track_32 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size12_mem_8_ccff_tail),
		.ccff_tail(mux2_size11_mem_0_ccff_tail),
		.mem_out(mux2_size11_0_sram[0:3]),
		.mem_outb(mux2_size11_0_sram_inv[0:3]));

endmodule
// ----- END Verilog module for sb_1__2_ -----

//----- Default net type -----
// `default_nettype none



