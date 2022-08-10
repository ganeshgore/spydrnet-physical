//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for Unique Switch Blocks[8][2]
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for sb_8__2_ -----
module sb_8__2_(cfg_done,
                prog_reset,
                prog_clk,
                chany_top_in,
                top_left_grid_right_width_0_height_0_subtile_0__pin_out_2_,
                top_left_grid_right_width_0_height_0_subtile_0__pin_out_10_,
                top_right_grid_left_width_0_height_0_subtile_0__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_1__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_2__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_3__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_4__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_5__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_6__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_7__pin_inpad_0_,
                chany_bottom_in,
                bottom_right_grid_left_width_0_height_0_subtile_0__pin_inpad_0_,
                bottom_right_grid_left_width_0_height_0_subtile_1__pin_inpad_0_,
                bottom_right_grid_left_width_0_height_0_subtile_2__pin_inpad_0_,
                bottom_right_grid_left_width_0_height_0_subtile_3__pin_inpad_0_,
                bottom_right_grid_left_width_0_height_0_subtile_4__pin_inpad_0_,
                bottom_right_grid_left_width_0_height_0_subtile_5__pin_inpad_0_,
                bottom_right_grid_left_width_0_height_0_subtile_6__pin_inpad_0_,
                bottom_right_grid_left_width_0_height_0_subtile_7__pin_inpad_0_,
                bottom_left_grid_right_width_0_height_1_subtile_0__pin_out_3_,
                bottom_left_grid_right_width_0_height_1_subtile_0__pin_out_11_,
                chanx_left_in,
                left_top_grid_bottom_width_0_height_0_subtile_0__pin_out_4_,
                left_top_grid_bottom_width_0_height_0_subtile_0__pin_out_12_,
                left_bottom_grid_top_width_0_height_1_subtile_0__pin_out_1_,
                left_bottom_grid_top_width_0_height_1_subtile_0__pin_out_9_,
                ccff_head,
                chany_top_out,
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
input [0:0] top_left_grid_right_width_0_height_0_subtile_0__pin_out_2_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_0__pin_out_10_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_0__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_1__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_2__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_3__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_4__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_5__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_6__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_right_grid_left_width_0_height_0_subtile_7__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:19] chany_bottom_in;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_0_subtile_0__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_0_subtile_1__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_0_subtile_2__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_0_subtile_3__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_0_subtile_4__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_0_subtile_5__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_0_subtile_6__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_right_grid_left_width_0_height_0_subtile_7__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_1_subtile_0__pin_out_3_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_1_subtile_0__pin_out_11_;
//----- INPUT PORTS -----
input [0:19] chanx_left_in;
//----- INPUT PORTS -----
input [0:0] left_top_grid_bottom_width_0_height_0_subtile_0__pin_out_4_;
//----- INPUT PORTS -----
input [0:0] left_top_grid_bottom_width_0_height_0_subtile_0__pin_out_12_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_1_subtile_0__pin_out_1_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_1_subtile_0__pin_out_9_;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:19] chany_top_out;
//----- OUTPUT PORTS -----
output [0:19] chany_bottom_out;
//----- OUTPUT PORTS -----
output [0:19] chanx_left_out;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;

//----- BEGIN Registered ports -----
//----- END Registered ports -----


wire [0:1] mux2_size2_0_sram;
wire [0:1] mux2_size2_0_sram_inv;
wire [0:1] mux2_size2_10_sram;
wire [0:1] mux2_size2_10_sram_inv;
wire [0:1] mux2_size2_11_sram;
wire [0:1] mux2_size2_11_sram_inv;
wire [0:1] mux2_size2_1_sram;
wire [0:1] mux2_size2_1_sram_inv;
wire [0:1] mux2_size2_2_sram;
wire [0:1] mux2_size2_2_sram_inv;
wire [0:1] mux2_size2_3_sram;
wire [0:1] mux2_size2_3_sram_inv;
wire [0:1] mux2_size2_4_sram;
wire [0:1] mux2_size2_4_sram_inv;
wire [0:1] mux2_size2_5_sram;
wire [0:1] mux2_size2_5_sram_inv;
wire [0:1] mux2_size2_6_sram;
wire [0:1] mux2_size2_6_sram_inv;
wire [0:1] mux2_size2_7_sram;
wire [0:1] mux2_size2_7_sram_inv;
wire [0:1] mux2_size2_8_sram;
wire [0:1] mux2_size2_8_sram_inv;
wire [0:1] mux2_size2_9_sram;
wire [0:1] mux2_size2_9_sram_inv;
wire [0:1] mux2_size3_0_sram;
wire [0:1] mux2_size3_0_sram_inv;
wire [0:1] mux2_size3_1_sram;
wire [0:1] mux2_size3_1_sram_inv;
wire [0:1] mux2_size3_2_sram;
wire [0:1] mux2_size3_2_sram_inv;
wire [0:1] mux2_size3_3_sram;
wire [0:1] mux2_size3_3_sram_inv;
wire [0:1] mux2_size3_4_sram;
wire [0:1] mux2_size3_4_sram_inv;
wire [0:1] mux2_size3_5_sram;
wire [0:1] mux2_size3_5_sram_inv;
wire [0:1] mux2_size3_6_sram;
wire [0:1] mux2_size3_6_sram_inv;
wire [0:1] mux2_size3_7_sram;
wire [0:1] mux2_size3_7_sram_inv;
wire [0:3] mux2_size9_0_sram;
wire [0:3] mux2_size9_0_sram_inv;
wire [0:3] mux2_size9_1_sram;
wire [0:3] mux2_size9_1_sram_inv;
wire [0:3] mux2_size9_2_sram;
wire [0:3] mux2_size9_2_sram_inv;
wire [0:3] mux2_size9_3_sram;
wire [0:3] mux2_size9_3_sram_inv;
wire [0:3] mux2_size9_4_sram;
wire [0:3] mux2_size9_4_sram_inv;
wire [0:3] mux2_size9_5_sram;
wire [0:3] mux2_size9_5_sram_inv;
wire [0:3] mux2_size9_6_sram;
wire [0:3] mux2_size9_6_sram_inv;
wire [0:3] mux2_size9_7_sram;
wire [0:3] mux2_size9_7_sram_inv;
wire [0:3] mux2_size9_8_sram;
wire [0:3] mux2_size9_8_sram_inv;
wire [0:3] mux2_size9_9_sram;
wire [0:3] mux2_size9_9_sram_inv;

// ----- BEGIN Local short connections -----
// ----- Local connection due to Wire 0 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[1] = chany_top_in[0];
// ----- Local connection due to Wire 1 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[2] = chany_top_in[1];
// ----- Local connection due to Wire 2 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[3] = chany_top_in[2];
// ----- Local connection due to Wire 4 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[5] = chany_top_in[4];
// ----- Local connection due to Wire 5 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[6] = chany_top_in[5];
// ----- Local connection due to Wire 6 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[7] = chany_top_in[6];
// ----- Local connection due to Wire 8 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[9] = chany_top_in[8];
// ----- Local connection due to Wire 9 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[10] = chany_top_in[9];
// ----- Local connection due to Wire 10 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[11] = chany_top_in[10];
// ----- Local connection due to Wire 12 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_bottom_out[13] = chany_top_in[12];
// ----- Local connection due to Wire 13 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[14] = chany_top_in[13];
// ----- Local connection due to Wire 14 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[15] = chany_top_in[14];
// ----- Local connection due to Wire 16 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[17] = chany_top_in[16];
// ----- Local connection due to Wire 17 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[18] = chany_top_in[17];
// ----- Local connection due to Wire 18 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_bottom_out[19] = chany_top_in[18];
// ----- Local connection due to Wire 30 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[1] = chany_bottom_in[0];
// ----- Local connection due to Wire 31 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[2] = chany_bottom_in[1];
// ----- Local connection due to Wire 32 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[3] = chany_bottom_in[2];
// ----- Local connection due to Wire 34 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[5] = chany_bottom_in[4];
// ----- Local connection due to Wire 35 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[6] = chany_bottom_in[5];
// ----- Local connection due to Wire 36 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[7] = chany_bottom_in[6];
// ----- Local connection due to Wire 38 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[9] = chany_bottom_in[8];
// ----- Local connection due to Wire 39 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[10] = chany_bottom_in[9];
// ----- Local connection due to Wire 40 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[11] = chany_bottom_in[10];
// ----- Local connection due to Wire 42 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[13] = chany_bottom_in[12];
// ----- Local connection due to Wire 43 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[14] = chany_bottom_in[13];
// ----- Local connection due to Wire 44 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[15] = chany_bottom_in[14];
// ----- Local connection due to Wire 46 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[17] = chany_bottom_in[16];
// ----- Local connection due to Wire 47 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[18] = chany_bottom_in[17];
// ----- Local connection due to Wire 48 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[19] = chany_bottom_in[18];
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	mux2_size9 mux_top_track_0 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_out_2_, top_right_grid_left_width_0_height_0_subtile_3__pin_inpad_0_, chany_bottom_in[0], chany_bottom_in[6], chany_bottom_in[13], chanx_left_in[0], chanx_left_in[5], chanx_left_in[10], chanx_left_in[15]}),
		.sram(mux2_size9_0_sram[0:3]),
		.sram_inv(mux2_size9_0_sram_inv[0:3]),
		.out(chany_top_out[0]));

	mux2_size9 mux_top_track_8 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_out_10_, top_right_grid_left_width_0_height_0_subtile_4__pin_inpad_0_, chany_bottom_in[1], chany_bottom_in[8], chany_bottom_in[14], chanx_left_in[4], chanx_left_in[9], chanx_left_in[14], chanx_left_in[19]}),
		.sram(mux2_size9_1_sram[0:3]),
		.sram_inv(mux2_size9_1_sram_inv[0:3]),
		.out(chany_top_out[4]));

	mux2_size9 mux_top_track_16 (
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_inpad_0_, top_right_grid_left_width_0_height_0_subtile_5__pin_inpad_0_, chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[16], chanx_left_in[3], chanx_left_in[8], chanx_left_in[13], chanx_left_in[18]}),
		.sram(mux2_size9_2_sram[0:3]),
		.sram_inv(mux2_size9_2_sram_inv[0:3]),
		.out(chany_top_out[8]));

	mux2_size9 mux_top_track_24 (
		.in({top_right_grid_left_width_0_height_0_subtile_1__pin_inpad_0_, top_right_grid_left_width_0_height_0_subtile_6__pin_inpad_0_, chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[17], chanx_left_in[2], chanx_left_in[7], chanx_left_in[12], chanx_left_in[17]}),
		.sram(mux2_size9_3_sram[0:3]),
		.sram_inv(mux2_size9_3_sram_inv[0:3]),
		.out(chany_top_out[12]));

	mux2_size9 mux_top_track_32 (
		.in({top_right_grid_left_width_0_height_0_subtile_2__pin_inpad_0_, top_right_grid_left_width_0_height_0_subtile_7__pin_inpad_0_, chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18], chanx_left_in[1], chanx_left_in[6], chanx_left_in[11], chanx_left_in[16]}),
		.sram(mux2_size9_4_sram[0:3]),
		.sram_inv(mux2_size9_4_sram_inv[0:3]),
		.out(chany_top_out[16]));

	mux2_size9 mux_bottom_track_1 (
		.in({chany_top_in[0], chany_top_in[6], chany_top_in[13], bottom_right_grid_left_width_0_height_0_subtile_0__pin_inpad_0_, bottom_right_grid_left_width_0_height_0_subtile_5__pin_inpad_0_, chanx_left_in[1], chanx_left_in[6], chanx_left_in[11], chanx_left_in[16]}),
		.sram(mux2_size9_5_sram[0:3]),
		.sram_inv(mux2_size9_5_sram_inv[0:3]),
		.out(chany_bottom_out[0]));

	mux2_size9 mux_bottom_track_9 (
		.in({chany_top_in[1], chany_top_in[8], chany_top_in[14], bottom_right_grid_left_width_0_height_0_subtile_1__pin_inpad_0_, bottom_right_grid_left_width_0_height_0_subtile_6__pin_inpad_0_, chanx_left_in[2], chanx_left_in[7], chanx_left_in[12], chanx_left_in[17]}),
		.sram(mux2_size9_6_sram[0:3]),
		.sram_inv(mux2_size9_6_sram_inv[0:3]),
		.out(chany_bottom_out[4]));

	mux2_size9 mux_bottom_track_17 (
		.in({chany_top_in[2], chany_top_in[9], chany_top_in[16], bottom_right_grid_left_width_0_height_0_subtile_2__pin_inpad_0_, bottom_right_grid_left_width_0_height_0_subtile_7__pin_inpad_0_, chanx_left_in[3], chanx_left_in[8], chanx_left_in[13], chanx_left_in[18]}),
		.sram(mux2_size9_7_sram[0:3]),
		.sram_inv(mux2_size9_7_sram_inv[0:3]),
		.out(chany_bottom_out[8]));

	mux2_size9 mux_bottom_track_25 (
		.in({chany_top_in[4], chany_top_in[10], chany_top_in[17], bottom_right_grid_left_width_0_height_0_subtile_3__pin_inpad_0_, bottom_left_grid_right_width_0_height_1_subtile_0__pin_out_3_, chanx_left_in[4], chanx_left_in[9], chanx_left_in[14], chanx_left_in[19]}),
		.sram(mux2_size9_8_sram[0:3]),
		.sram_inv(mux2_size9_8_sram_inv[0:3]),
		.out(chany_bottom_out[12]));

	mux2_size9 mux_bottom_track_33 (
		.in({chany_top_in[5], chany_top_in[12], chany_top_in[18], bottom_right_grid_left_width_0_height_0_subtile_4__pin_inpad_0_, bottom_left_grid_right_width_0_height_1_subtile_0__pin_out_11_, chanx_left_in[0], chanx_left_in[5], chanx_left_in[10], chanx_left_in[15]}),
		.sram(mux2_size9_9_sram[0:3]),
		.sram_inv(mux2_size9_9_sram_inv[0:3]),
		.out(chany_bottom_out[16]));

	mux2_size9_mem mem_top_track_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(ccff_head),
		.ccff_tail(mux2_size9_mem_0_ccff_tail),
		.mem_out(mux2_size9_0_sram[0:3]),
		.mem_outb(mux2_size9_0_sram_inv[0:3]));

	mux2_size9_mem mem_top_track_8 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size9_mem_0_ccff_tail),
		.ccff_tail(mux2_size9_mem_1_ccff_tail),
		.mem_out(mux2_size9_1_sram[0:3]),
		.mem_outb(mux2_size9_1_sram_inv[0:3]));

	mux2_size9_mem mem_top_track_16 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size9_mem_1_ccff_tail),
		.ccff_tail(mux2_size9_mem_2_ccff_tail),
		.mem_out(mux2_size9_2_sram[0:3]),
		.mem_outb(mux2_size9_2_sram_inv[0:3]));

	mux2_size9_mem mem_top_track_24 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size9_mem_2_ccff_tail),
		.ccff_tail(mux2_size9_mem_3_ccff_tail),
		.mem_out(mux2_size9_3_sram[0:3]),
		.mem_outb(mux2_size9_3_sram_inv[0:3]));

	mux2_size9_mem mem_top_track_32 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size9_mem_3_ccff_tail),
		.ccff_tail(mux2_size9_mem_4_ccff_tail),
		.mem_out(mux2_size9_4_sram[0:3]),
		.mem_outb(mux2_size9_4_sram_inv[0:3]));

	mux2_size9_mem mem_bottom_track_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size9_mem_4_ccff_tail),
		.ccff_tail(mux2_size9_mem_5_ccff_tail),
		.mem_out(mux2_size9_5_sram[0:3]),
		.mem_outb(mux2_size9_5_sram_inv[0:3]));

	mux2_size9_mem mem_bottom_track_9 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size9_mem_5_ccff_tail),
		.ccff_tail(mux2_size9_mem_6_ccff_tail),
		.mem_out(mux2_size9_6_sram[0:3]),
		.mem_outb(mux2_size9_6_sram_inv[0:3]));

	mux2_size9_mem mem_bottom_track_17 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size9_mem_6_ccff_tail),
		.ccff_tail(mux2_size9_mem_7_ccff_tail),
		.mem_out(mux2_size9_7_sram[0:3]),
		.mem_outb(mux2_size9_7_sram_inv[0:3]));

	mux2_size9_mem mem_bottom_track_25 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size9_mem_7_ccff_tail),
		.ccff_tail(mux2_size9_mem_8_ccff_tail),
		.mem_out(mux2_size9_8_sram[0:3]),
		.mem_outb(mux2_size9_8_sram_inv[0:3]));

	mux2_size9_mem mem_bottom_track_33 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size9_mem_8_ccff_tail),
		.ccff_tail(mux2_size9_mem_9_ccff_tail),
		.mem_out(mux2_size9_9_sram[0:3]),
		.mem_outb(mux2_size9_9_sram_inv[0:3]));

	mux2_size3 mux_left_track_1 (
		.in({chany_top_in[0], chany_top_in[3], left_top_grid_bottom_width_0_height_0_subtile_0__pin_out_4_}),
		.sram(mux2_size3_0_sram[0:1]),
		.sram_inv(mux2_size3_0_sram_inv[0:1]),
		.out(chanx_left_out[0]));

	mux2_size3 mux_left_track_3 (
		.in({chany_bottom_in[0], chany_bottom_in[3], left_top_grid_bottom_width_0_height_0_subtile_0__pin_out_12_}),
		.sram(mux2_size3_1_sram[0:1]),
		.sram_inv(mux2_size3_1_sram_inv[0:1]),
		.out(chanx_left_out[1]));

	mux2_size3 mux_left_track_5 (
		.in({chany_bottom_in[1], chany_bottom_in[7], left_bottom_grid_top_width_0_height_1_subtile_0__pin_out_1_}),
		.sram(mux2_size3_2_sram[0:1]),
		.sram_inv(mux2_size3_2_sram_inv[0:1]),
		.out(chanx_left_out[2]));

	mux2_size3 mux_left_track_7 (
		.in({chany_bottom_in[2], chany_bottom_in[11], left_bottom_grid_top_width_0_height_1_subtile_0__pin_out_9_}),
		.sram(mux2_size3_3_sram[0:1]),
		.sram_inv(mux2_size3_3_sram_inv[0:1]),
		.out(chanx_left_out[3]));

	mux2_size3 mux_left_track_21 (
		.in({chany_top_in[13], chany_bottom_in[12], left_top_grid_bottom_width_0_height_0_subtile_0__pin_out_4_}),
		.sram(mux2_size3_4_sram[0:1]),
		.sram_inv(mux2_size3_4_sram_inv[0:1]),
		.out(chanx_left_out[10]));

	mux2_size3 mux_left_track_23 (
		.in({chany_top_in[12], chany_bottom_in[13], left_top_grid_bottom_width_0_height_0_subtile_0__pin_out_12_}),
		.sram(mux2_size3_5_sram[0:1]),
		.sram_inv(mux2_size3_5_sram_inv[0:1]),
		.out(chanx_left_out[11]));

	mux2_size3 mux_left_track_25 (
		.in({chany_top_in[10], chany_bottom_in[14], left_bottom_grid_top_width_0_height_1_subtile_0__pin_out_1_}),
		.sram(mux2_size3_6_sram[0:1]),
		.sram_inv(mux2_size3_6_sram_inv[0:1]),
		.out(chanx_left_out[12]));

	mux2_size3 mux_left_track_27 (
		.in({chany_top_in[9], chany_bottom_in[16], left_bottom_grid_top_width_0_height_1_subtile_0__pin_out_9_}),
		.sram(mux2_size3_7_sram[0:1]),
		.sram_inv(mux2_size3_7_sram_inv[0:1]),
		.out(chanx_left_out[13]));

	mux2_size3_mem mem_left_track_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size9_mem_9_ccff_tail),
		.ccff_tail(mux2_size3_mem_0_ccff_tail),
		.mem_out(mux2_size3_0_sram[0:1]),
		.mem_outb(mux2_size3_0_sram_inv[0:1]));

	mux2_size3_mem mem_left_track_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size3_mem_0_ccff_tail),
		.ccff_tail(mux2_size3_mem_1_ccff_tail),
		.mem_out(mux2_size3_1_sram[0:1]),
		.mem_outb(mux2_size3_1_sram_inv[0:1]));

	mux2_size3_mem mem_left_track_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size3_mem_1_ccff_tail),
		.ccff_tail(mux2_size3_mem_2_ccff_tail),
		.mem_out(mux2_size3_2_sram[0:1]),
		.mem_outb(mux2_size3_2_sram_inv[0:1]));

	mux2_size3_mem mem_left_track_7 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size3_mem_2_ccff_tail),
		.ccff_tail(mux2_size3_mem_3_ccff_tail),
		.mem_out(mux2_size3_3_sram[0:1]),
		.mem_outb(mux2_size3_3_sram_inv[0:1]));

	mux2_size3_mem mem_left_track_21 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_5_ccff_tail),
		.ccff_tail(mux2_size3_mem_4_ccff_tail),
		.mem_out(mux2_size3_4_sram[0:1]),
		.mem_outb(mux2_size3_4_sram_inv[0:1]));

	mux2_size3_mem mem_left_track_23 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size3_mem_4_ccff_tail),
		.ccff_tail(mux2_size3_mem_5_ccff_tail),
		.mem_out(mux2_size3_5_sram[0:1]),
		.mem_outb(mux2_size3_5_sram_inv[0:1]));

	mux2_size3_mem mem_left_track_25 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size3_mem_5_ccff_tail),
		.ccff_tail(mux2_size3_mem_6_ccff_tail),
		.mem_out(mux2_size3_6_sram[0:1]),
		.mem_outb(mux2_size3_6_sram_inv[0:1]));

	mux2_size3_mem mem_left_track_27 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size3_mem_6_ccff_tail),
		.ccff_tail(mux2_size3_mem_7_ccff_tail),
		.mem_out(mux2_size3_7_sram[0:1]),
		.mem_outb(mux2_size3_7_sram_inv[0:1]));

	mux2_size2 mux_left_track_9 (
		.in({chany_bottom_in[4], chany_bottom_in[15]}),
		.sram(mux2_size2_0_sram[0:1]),
		.sram_inv(mux2_size2_0_sram_inv[0:1]),
		.out(chanx_left_out[4]));

	mux2_size2 mux_left_track_11 (
		.in({chany_bottom_in[5], chany_bottom_in[19]}),
		.sram(mux2_size2_1_sram[0:1]),
		.sram_inv(mux2_size2_1_sram_inv[0:1]),
		.out(chanx_left_out[5]));

	mux2_size2 mux_left_track_13 (
		.in({chany_top_in[18], chany_bottom_in[6]}),
		.sram(mux2_size2_2_sram[0:1]),
		.sram_inv(mux2_size2_2_sram_inv[0:1]),
		.out(chanx_left_out[6]));

	mux2_size2 mux_left_track_15 (
		.in({chany_top_in[17], chany_bottom_in[8]}),
		.sram(mux2_size2_3_sram[0:1]),
		.sram_inv(mux2_size2_3_sram_inv[0:1]),
		.out(chanx_left_out[7]));

	mux2_size2 mux_left_track_17 (
		.in({chany_top_in[16], chany_bottom_in[9]}),
		.sram(mux2_size2_4_sram[0:1]),
		.sram_inv(mux2_size2_4_sram_inv[0:1]),
		.out(chanx_left_out[8]));

	mux2_size2 mux_left_track_19 (
		.in({chany_top_in[14], chany_bottom_in[10]}),
		.sram(mux2_size2_5_sram[0:1]),
		.sram_inv(mux2_size2_5_sram_inv[0:1]),
		.out(chanx_left_out[9]));

	mux2_size2 mux_left_track_29 (
		.in({chany_top_in[8], chany_bottom_in[17]}),
		.sram(mux2_size2_6_sram[0:1]),
		.sram_inv(mux2_size2_6_sram_inv[0:1]),
		.out(chanx_left_out[14]));

	mux2_size2 mux_left_track_31 (
		.in({chany_top_in[6], chany_bottom_in[18]}),
		.sram(mux2_size2_7_sram[0:1]),
		.sram_inv(mux2_size2_7_sram_inv[0:1]),
		.out(chanx_left_out[15]));

	mux2_size2 mux_left_track_33 (
		.in({chany_top_in[5], chany_top_in[19]}),
		.sram(mux2_size2_8_sram[0:1]),
		.sram_inv(mux2_size2_8_sram_inv[0:1]),
		.out(chanx_left_out[16]));

	mux2_size2 mux_left_track_35 (
		.in({chany_top_in[4], chany_top_in[15]}),
		.sram(mux2_size2_9_sram[0:1]),
		.sram_inv(mux2_size2_9_sram_inv[0:1]),
		.out(chanx_left_out[17]));

	mux2_size2 mux_left_track_37 (
		.in({chany_top_in[2], chany_top_in[11]}),
		.sram(mux2_size2_10_sram[0:1]),
		.sram_inv(mux2_size2_10_sram_inv[0:1]),
		.out(chanx_left_out[18]));

	mux2_size2 mux_left_track_39 (
		.in({chany_top_in[1], chany_top_in[7]}),
		.sram(mux2_size2_11_sram[0:1]),
		.sram_inv(mux2_size2_11_sram_inv[0:1]),
		.out(chanx_left_out[19]));

	mux2_size2_mem mem_left_track_9 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size3_mem_3_ccff_tail),
		.ccff_tail(mux2_size2_mem_0_ccff_tail),
		.mem_out(mux2_size2_0_sram[0:1]),
		.mem_outb(mux2_size2_0_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_11 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_0_ccff_tail),
		.ccff_tail(mux2_size2_mem_1_ccff_tail),
		.mem_out(mux2_size2_1_sram[0:1]),
		.mem_outb(mux2_size2_1_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_13 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_1_ccff_tail),
		.ccff_tail(mux2_size2_mem_2_ccff_tail),
		.mem_out(mux2_size2_2_sram[0:1]),
		.mem_outb(mux2_size2_2_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_15 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_2_ccff_tail),
		.ccff_tail(mux2_size2_mem_3_ccff_tail),
		.mem_out(mux2_size2_3_sram[0:1]),
		.mem_outb(mux2_size2_3_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_17 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_3_ccff_tail),
		.ccff_tail(mux2_size2_mem_4_ccff_tail),
		.mem_out(mux2_size2_4_sram[0:1]),
		.mem_outb(mux2_size2_4_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_19 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_4_ccff_tail),
		.ccff_tail(mux2_size2_mem_5_ccff_tail),
		.mem_out(mux2_size2_5_sram[0:1]),
		.mem_outb(mux2_size2_5_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_29 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size3_mem_7_ccff_tail),
		.ccff_tail(mux2_size2_mem_6_ccff_tail),
		.mem_out(mux2_size2_6_sram[0:1]),
		.mem_outb(mux2_size2_6_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_31 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_6_ccff_tail),
		.ccff_tail(mux2_size2_mem_7_ccff_tail),
		.mem_out(mux2_size2_7_sram[0:1]),
		.mem_outb(mux2_size2_7_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_33 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_7_ccff_tail),
		.ccff_tail(mux2_size2_mem_8_ccff_tail),
		.mem_out(mux2_size2_8_sram[0:1]),
		.mem_outb(mux2_size2_8_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_35 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_8_ccff_tail),
		.ccff_tail(mux2_size2_mem_9_ccff_tail),
		.mem_out(mux2_size2_9_sram[0:1]),
		.mem_outb(mux2_size2_9_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_37 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_9_ccff_tail),
		.ccff_tail(mux2_size2_mem_10_ccff_tail),
		.mem_out(mux2_size2_10_sram[0:1]),
		.mem_outb(mux2_size2_10_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_39 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_10_ccff_tail),
		.ccff_tail(ccff_tail),
		.mem_out(mux2_size2_11_sram[0:1]),
		.mem_outb(mux2_size2_11_sram_inv[0:1]));

endmodule
// ----- END Verilog module for sb_8__2_ -----

//----- Default net type -----
// `default_nettype none



