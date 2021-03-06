//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for Unique Switch Blocks[1][1]
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for sb_1__1_ -----
module sb_1__1_(chany_top_in,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_,
                top_right_grid_left_width_0_height_0_subtile_0__pin_O_3_,
                top_right_grid_left_width_0_height_0_subtile_0__pin_O_7_,
                chanx_right_in,
                right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_,
                right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_,
                right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_0_,
                right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_4_,
                right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_8_,
                chany_bottom_in,
                bottom_right_grid_left_width_0_height_0_subtile_0__pin_O_3_,
                bottom_right_grid_left_width_0_height_0_subtile_0__pin_O_7_,
                bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_1_,
                bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_5_,
                bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_9_,
                chanx_left_in,
                left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_,
                left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_,
                left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_0_,
                left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_4_,
                left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_8_,
                bl,
                wl,
                chany_top_out,
                chanx_right_out,
                chany_bottom_out,
                chanx_left_out);
//----- INPUT PORTS -----
input [0:19] chany_top_in;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_0__pin_O_3_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_0__pin_O_7_;
//----- INPUT PORTS -----
input [0:19] chanx_right_in;
//----- INPUT PORTS -----
input [0:0] right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_;
//----- INPUT PORTS -----
input [0:0] right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_0_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_4_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_8_;
//----- INPUT PORTS -----
input [0:19] chany_bottom_in;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_0_subtile_0__pin_O_3_;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_0_subtile_0__pin_O_7_;
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
input [0:79] bl;
//----- INPUT PORTS -----
input [0:79] wl;
//----- OUTPUT PORTS -----
output [0:19] chany_top_out;
//----- OUTPUT PORTS -----
output [0:19] chanx_right_out;
//----- OUTPUT PORTS -----
output [0:19] chany_bottom_out;
//----- OUTPUT PORTS -----
output [0:19] chanx_left_out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----


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
wire [0:3] mux2_size12_19_sram;
wire [0:3] mux2_size12_19_sram_inv;
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
// ----- Local connection due to Wire 50 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[1] = chany_bottom_in[0];
// ----- Local connection due to Wire 51 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[2] = chany_bottom_in[1];
// ----- Local connection due to Wire 52 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[3] = chany_bottom_in[2];
// ----- Local connection due to Wire 54 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[5] = chany_bottom_in[4];
// ----- Local connection due to Wire 55 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[6] = chany_bottom_in[5];
// ----- Local connection due to Wire 56 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[7] = chany_bottom_in[6];
// ----- Local connection due to Wire 58 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[9] = chany_bottom_in[8];
// ----- Local connection due to Wire 59 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[10] = chany_bottom_in[9];
// ----- Local connection due to Wire 60 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[11] = chany_bottom_in[10];
// ----- Local connection due to Wire 62 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[13] = chany_bottom_in[12];
// ----- Local connection due to Wire 63 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[14] = chany_bottom_in[13];
// ----- Local connection due to Wire 64 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[15] = chany_bottom_in[14];
// ----- Local connection due to Wire 66 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[17] = chany_bottom_in[16];
// ----- Local connection due to Wire 67 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[18] = chany_bottom_in[17];
// ----- Local connection due to Wire 68 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[19] = chany_bottom_in[18];
// ----- Local connection due to Wire 75 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[1] = chanx_left_in[0];
// ----- Local connection due to Wire 76 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[2] = chanx_left_in[1];
// ----- Local connection due to Wire 77 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[3] = chanx_left_in[2];
// ----- Local connection due to Wire 79 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[5] = chanx_left_in[4];
// ----- Local connection due to Wire 80 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[6] = chanx_left_in[5];
// ----- Local connection due to Wire 81 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[7] = chanx_left_in[6];
// ----- Local connection due to Wire 83 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[9] = chanx_left_in[8];
// ----- Local connection due to Wire 84 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[10] = chanx_left_in[9];
// ----- Local connection due to Wire 85 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[11] = chanx_left_in[10];
// ----- Local connection due to Wire 87 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[13] = chanx_left_in[12];
// ----- Local connection due to Wire 88 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[14] = chanx_left_in[13];
// ----- Local connection due to Wire 89 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[15] = chanx_left_in[14];
// ----- Local connection due to Wire 91 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[17] = chanx_left_in[16];
// ----- Local connection due to Wire 92 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[18] = chanx_left_in[17];
// ----- Local connection due to Wire 93 -----
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
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_O_3_, chanx_right_in[5], chanx_right_in[12], chanx_right_in[18:19], chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[17], chanx_left_in[2], chanx_left_in[9], chanx_left_in[11], chanx_left_in[16]}),
		.sram(mux2_size12_3_sram[0:3]),
		.sram_inv(mux2_size12_3_sram_inv[0:3]),
		.out(chany_top_out[12]));

	mux2_size12 mux_top_track_32 (
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_O_7_, chanx_right_in[0], chanx_right_in[3], chanx_right_in[6], chanx_right_in[13], chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18], chanx_left_in[1], chanx_left_in[7:8], chanx_left_in[14]}),
		.sram(mux2_size12_4_sram[0:3]),
		.sram_inv(mux2_size12_4_sram_inv[0:3]),
		.out(chany_top_out[16]));

	mux2_size12 mux_right_track_0 (
		.in({chany_top_in[5], chany_top_in[12], chany_top_in[18:19], right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_, chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[15], chany_bottom_in[17], chanx_left_in[0], chanx_left_in[6], chanx_left_in[13]}),
		.sram(mux2_size12_5_sram[0:3]),
		.sram_inv(mux2_size12_5_sram_inv[0:3]),
		.out(chanx_right_out[0]));

	mux2_size12 mux_right_track_8 (
		.in({chany_top_in[0], chany_top_in[3], chany_top_in[6], chany_top_in[13], right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_, chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[11], chany_bottom_in[16], chanx_left_in[1], chanx_left_in[8], chanx_left_in[14]}),
		.sram(mux2_size12_6_sram[0:3]),
		.sram_inv(mux2_size12_6_sram_inv[0:3]),
		.out(chanx_right_out[4]));

	mux2_size12 mux_right_track_16 (
		.in({chany_top_in[1], chany_top_in[7:8], chany_top_in[14], right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_0_, chany_bottom_in[1], chany_bottom_in[7:8], chany_bottom_in[14], chanx_left_in[2], chanx_left_in[9], chanx_left_in[16]}),
		.sram(mux2_size12_7_sram[0:3]),
		.sram_inv(mux2_size12_7_sram_inv[0:3]),
		.out(chanx_right_out[8]));

	mux2_size12 mux_right_track_24 (
		.in({chany_top_in[2], chany_top_in[9], chany_top_in[11], chany_top_in[16], right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_4_, chany_bottom_in[0], chany_bottom_in[3], chany_bottom_in[6], chany_bottom_in[13], chanx_left_in[4], chanx_left_in[10], chanx_left_in[17]}),
		.sram(mux2_size12_8_sram[0:3]),
		.sram_inv(mux2_size12_8_sram_inv[0:3]),
		.out(chanx_right_out[12]));

	mux2_size12 mux_right_track_32 (
		.in({chany_top_in[4], chany_top_in[10], chany_top_in[15], chany_top_in[17], right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_8_, chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18:19], chanx_left_in[5], chanx_left_in[12], chanx_left_in[18]}),
		.sram(mux2_size12_9_sram[0:3]),
		.sram_inv(mux2_size12_9_sram_inv[0:3]),
		.out(chanx_right_out[16]));

	mux2_size12 mux_bottom_track_1 (
		.in({chany_top_in[0], chany_top_in[6], chany_top_in[13], chanx_right_in[4], chanx_right_in[10], chanx_right_in[15], chanx_right_in[17], bottom_right_grid_left_width_0_height_0_subtile_0__pin_O_3_, chanx_left_in[1], chanx_left_in[7:8], chanx_left_in[14]}),
		.sram(mux2_size12_10_sram[0:3]),
		.sram_inv(mux2_size12_10_sram_inv[0:3]),
		.out(chany_bottom_out[0]));

	mux2_size12 mux_bottom_track_9 (
		.in({chany_top_in[1], chany_top_in[8], chany_top_in[14], chanx_right_in[2], chanx_right_in[9], chanx_right_in[11], chanx_right_in[16], bottom_right_grid_left_width_0_height_0_subtile_0__pin_O_7_, chanx_left_in[2], chanx_left_in[9], chanx_left_in[11], chanx_left_in[16]}),
		.sram(mux2_size12_11_sram[0:3]),
		.sram_inv(mux2_size12_11_sram_inv[0:3]),
		.out(chany_bottom_out[4]));

	mux2_size12 mux_bottom_track_17 (
		.in({chany_top_in[2], chany_top_in[9], chany_top_in[16], chanx_right_in[1], chanx_right_in[7:8], chanx_right_in[14], bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_1_, chanx_left_in[4], chanx_left_in[10], chanx_left_in[15], chanx_left_in[17]}),
		.sram(mux2_size12_12_sram[0:3]),
		.sram_inv(mux2_size12_12_sram_inv[0:3]),
		.out(chany_bottom_out[8]));

	mux2_size12 mux_bottom_track_25 (
		.in({chany_top_in[4], chany_top_in[10], chany_top_in[17], chanx_right_in[0], chanx_right_in[3], chanx_right_in[6], chanx_right_in[13], bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_5_, chanx_left_in[5], chanx_left_in[12], chanx_left_in[18:19]}),
		.sram(mux2_size12_13_sram[0:3]),
		.sram_inv(mux2_size12_13_sram_inv[0:3]),
		.out(chany_bottom_out[12]));

	mux2_size12 mux_bottom_track_33 (
		.in({chany_top_in[5], chany_top_in[12], chany_top_in[18], chanx_right_in[5], chanx_right_in[12], chanx_right_in[18:19], bottom_left_grid_right_width_0_height_0_subtile_0__pin_O_9_, chanx_left_in[0], chanx_left_in[3], chanx_left_in[6], chanx_left_in[13]}),
		.sram(mux2_size12_14_sram[0:3]),
		.sram_inv(mux2_size12_14_sram_inv[0:3]),
		.out(chany_bottom_out[16]));

	mux2_size12 mux_left_track_1 (
		.in({chany_top_in[0], chany_top_in[3], chany_top_in[6], chany_top_in[13], chanx_right_in[0], chanx_right_in[6], chanx_right_in[13], chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18:19], left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_}),
		.sram(mux2_size12_15_sram[0:3]),
		.sram_inv(mux2_size12_15_sram_inv[0:3]),
		.out(chanx_left_out[0]));

	mux2_size12 mux_left_track_9 (
		.in({chany_top_in[5], chany_top_in[12], chany_top_in[18:19], chanx_right_in[1], chanx_right_in[8], chanx_right_in[14], chany_bottom_in[0], chany_bottom_in[3], chany_bottom_in[6], chany_bottom_in[13], left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_}),
		.sram(mux2_size12_16_sram[0:3]),
		.sram_inv(mux2_size12_16_sram_inv[0:3]),
		.out(chanx_left_out[4]));

	mux2_size12 mux_left_track_17 (
		.in({chany_top_in[4], chany_top_in[10], chany_top_in[15], chany_top_in[17], chanx_right_in[2], chanx_right_in[9], chanx_right_in[16], chany_bottom_in[1], chany_bottom_in[7:8], chany_bottom_in[14], left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_0_}),
		.sram(mux2_size12_17_sram[0:3]),
		.sram_inv(mux2_size12_17_sram_inv[0:3]),
		.out(chanx_left_out[8]));

	mux2_size12 mux_left_track_25 (
		.in({chany_top_in[2], chany_top_in[9], chany_top_in[11], chany_top_in[16], chanx_right_in[4], chanx_right_in[10], chanx_right_in[17], chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[11], chany_bottom_in[16], left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_4_}),
		.sram(mux2_size12_18_sram[0:3]),
		.sram_inv(mux2_size12_18_sram_inv[0:3]),
		.out(chanx_left_out[12]));

	mux2_size12 mux_left_track_33 (
		.in({chany_top_in[1], chany_top_in[7:8], chany_top_in[14], chanx_right_in[5], chanx_right_in[12], chanx_right_in[18], chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[15], chany_bottom_in[17], left_bottom_grid_top_width_0_height_0_subtile_0__pin_O_8_}),
		.sram(mux2_size12_19_sram[0:3]),
		.sram_inv(mux2_size12_19_sram_inv[0:3]),
		.out(chanx_left_out[16]));

	mux2_size12_mem mem_top_track_0 (
		.bl(bl[0:3]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_0_sram[0:3]),
		.mem_outb(mux2_size12_0_sram_inv[0:3]));

	mux2_size12_mem mem_top_track_8 (
		.bl(bl[4:7]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_1_sram[0:3]),
		.mem_outb(mux2_size12_1_sram_inv[0:3]));

	mux2_size12_mem mem_top_track_16 (
		.bl(bl[8:11]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_2_sram[0:3]),
		.mem_outb(mux2_size12_2_sram_inv[0:3]));

	mux2_size12_mem mem_top_track_24 (
		.bl(bl[12:15]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_3_sram[0:3]),
		.mem_outb(mux2_size12_3_sram_inv[0:3]));

	mux2_size12_mem mem_top_track_32 (
		.bl(bl[16:19]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_4_sram[0:3]),
		.mem_outb(mux2_size12_4_sram_inv[0:3]));

	mux2_size12_mem mem_right_track_0 (
		.bl(bl[20:23]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_5_sram[0:3]),
		.mem_outb(mux2_size12_5_sram_inv[0:3]));

	mux2_size12_mem mem_right_track_8 (
		.bl(bl[24:27]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_6_sram[0:3]),
		.mem_outb(mux2_size12_6_sram_inv[0:3]));

	mux2_size12_mem mem_right_track_16 (
		.bl(bl[28:31]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_7_sram[0:3]),
		.mem_outb(mux2_size12_7_sram_inv[0:3]));

	mux2_size12_mem mem_right_track_24 (
		.bl(bl[32:35]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_8_sram[0:3]),
		.mem_outb(mux2_size12_8_sram_inv[0:3]));

	mux2_size12_mem mem_right_track_32 (
		.bl(bl[36:39]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_9_sram[0:3]),
		.mem_outb(mux2_size12_9_sram_inv[0:3]));

	mux2_size12_mem mem_bottom_track_1 (
		.bl(bl[40:43]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_10_sram[0:3]),
		.mem_outb(mux2_size12_10_sram_inv[0:3]));

	mux2_size12_mem mem_bottom_track_9 (
		.bl(bl[44:47]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_11_sram[0:3]),
		.mem_outb(mux2_size12_11_sram_inv[0:3]));

	mux2_size12_mem mem_bottom_track_17 (
		.bl(bl[48:51]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_12_sram[0:3]),
		.mem_outb(mux2_size12_12_sram_inv[0:3]));

	mux2_size12_mem mem_bottom_track_25 (
		.bl(bl[52:55]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_13_sram[0:3]),
		.mem_outb(mux2_size12_13_sram_inv[0:3]));

	mux2_size12_mem mem_bottom_track_33 (
		.bl(bl[56:59]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_14_sram[0:3]),
		.mem_outb(mux2_size12_14_sram_inv[0:3]));

	mux2_size12_mem mem_left_track_1 (
		.bl(bl[60:63]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_15_sram[0:3]),
		.mem_outb(mux2_size12_15_sram_inv[0:3]));

	mux2_size12_mem mem_left_track_9 (
		.bl(bl[64:67]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_16_sram[0:3]),
		.mem_outb(mux2_size12_16_sram_inv[0:3]));

	mux2_size12_mem mem_left_track_17 (
		.bl(bl[68:71]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_17_sram[0:3]),
		.mem_outb(mux2_size12_17_sram_inv[0:3]));

	mux2_size12_mem mem_left_track_25 (
		.bl(bl[72:75]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_18_sram[0:3]),
		.mem_outb(mux2_size12_18_sram_inv[0:3]));

	mux2_size12_mem mem_left_track_33 (
		.bl(bl[76:79]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size12_19_sram[0:3]),
		.mem_outb(mux2_size12_19_sram_inv[0:3]));

endmodule
// ----- END Verilog module for sb_1__1_ -----

//----- Default net type -----
// `default_nettype none



