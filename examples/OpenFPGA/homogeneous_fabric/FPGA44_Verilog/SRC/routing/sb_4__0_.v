//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for Unique Switch Blocks[4][0]
//	Author: Xifan TANG
//	Organization: University of Utah
//	Date: Thu Oct 28 13:20:02 2021
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
`default_nettype wire

// ----- Verilog module for sb_4__0_ -----
module sb_4__0_(cfg_done,
                prog_reset,
                prog_clk,
                chany_top_in,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_,
                top_right_grid_left_width_0_height_0_subtile_0__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_1__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_2__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_3__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_4__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_5__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_6__pin_inpad_0_,
                top_right_grid_left_width_0_height_0_subtile_7__pin_inpad_0_,
                chanx_left_in,
                left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_,
                left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_,
                left_bottom_grid_top_width_0_height_0_subtile_0__pin_inpad_0_,
                left_bottom_grid_top_width_0_height_0_subtile_1__pin_inpad_0_,
                left_bottom_grid_top_width_0_height_0_subtile_2__pin_inpad_0_,
                left_bottom_grid_top_width_0_height_0_subtile_3__pin_inpad_0_,
                left_bottom_grid_top_width_0_height_0_subtile_4__pin_inpad_0_,
                left_bottom_grid_top_width_0_height_0_subtile_5__pin_inpad_0_,
                left_bottom_grid_top_width_0_height_0_subtile_6__pin_inpad_0_,
                left_bottom_grid_top_width_0_height_0_subtile_7__pin_inpad_0_,
                ccff_head,
                chany_top_out,
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
input [0:19] chanx_left_in;
//----- INPUT PORTS -----
input [0:0] left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_;
//----- INPUT PORTS -----
input [0:0] left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_0__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_1__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_2__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_3__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_4__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_5__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_6__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] left_bottom_grid_top_width_0_height_0_subtile_7__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:19] chany_top_out;
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
wire [0:1] mux2_size2_12_sram;
wire [0:1] mux2_size2_12_sram_inv;
wire [0:1] mux2_size2_13_sram;
wire [0:1] mux2_size2_13_sram_inv;
wire [0:1] mux2_size2_14_sram;
wire [0:1] mux2_size2_14_sram_inv;
wire [0:1] mux2_size2_15_sram;
wire [0:1] mux2_size2_15_sram_inv;
wire [0:1] mux2_size2_16_sram;
wire [0:1] mux2_size2_16_sram_inv;
wire [0:1] mux2_size2_17_sram;
wire [0:1] mux2_size2_17_sram_inv;
wire [0:1] mux2_size2_18_sram;
wire [0:1] mux2_size2_18_sram_inv;
wire [0:1] mux2_size2_19_sram;
wire [0:1] mux2_size2_19_sram_inv;
wire [0:1] mux2_size2_1_sram;
wire [0:1] mux2_size2_1_sram_inv;
wire [0:1] mux2_size2_20_sram;
wire [0:1] mux2_size2_20_sram_inv;
wire [0:1] mux2_size2_21_sram;
wire [0:1] mux2_size2_21_sram_inv;
wire [0:1] mux2_size2_22_sram;
wire [0:1] mux2_size2_22_sram_inv;
wire [0:1] mux2_size2_23_sram;
wire [0:1] mux2_size2_23_sram_inv;
wire [0:1] mux2_size2_24_sram;
wire [0:1] mux2_size2_24_sram_inv;
wire [0:1] mux2_size2_25_sram;
wire [0:1] mux2_size2_25_sram_inv;
wire [0:1] mux2_size2_26_sram;
wire [0:1] mux2_size2_26_sram_inv;
wire [0:1] mux2_size2_27_sram;
wire [0:1] mux2_size2_27_sram_inv;
wire [0:1] mux2_size2_28_sram;
wire [0:1] mux2_size2_28_sram_inv;
wire [0:1] mux2_size2_29_sram;
wire [0:1] mux2_size2_29_sram_inv;
wire [0:1] mux2_size2_2_sram;
wire [0:1] mux2_size2_2_sram_inv;
wire [0:1] mux2_size2_30_sram;
wire [0:1] mux2_size2_30_sram_inv;
wire [0:1] mux2_size2_31_sram;
wire [0:1] mux2_size2_31_sram_inv;
wire [0:1] mux2_size2_32_sram;
wire [0:1] mux2_size2_32_sram_inv;
wire [0:1] mux2_size2_33_sram;
wire [0:1] mux2_size2_33_sram_inv;
wire [0:1] mux2_size2_34_sram;
wire [0:1] mux2_size2_34_sram_inv;
wire [0:1] mux2_size2_35_sram;
wire [0:1] mux2_size2_35_sram_inv;
wire [0:1] mux2_size2_36_sram;
wire [0:1] mux2_size2_36_sram_inv;
wire [0:1] mux2_size2_37_sram;
wire [0:1] mux2_size2_37_sram_inv;
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

// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	mux2_size3 mux_top_track_0 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_, top_right_grid_left_width_0_height_0_subtile_7__pin_inpad_0_, chanx_left_in[0]}),
		.sram(mux2_size3_0_sram[0:1]),
		.sram_inv(mux2_size3_0_sram_inv[0:1]),
		.out(chany_top_out[0]));

	mux2_size3 mux_top_track_20 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_, top_right_grid_left_width_0_height_0_subtile_7__pin_inpad_0_, chanx_left_in[10]}),
		.sram(mux2_size3_1_sram[0:1]),
		.sram_inv(mux2_size3_1_sram_inv[0:1]),
		.out(chany_top_out[10]));

	mux2_size3_mem mem_top_track_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(ccff_head),
		.ccff_tail(mux2_size3_mem_0_ccff_tail),
		.mem_out(mux2_size3_0_sram[0:1]),
		.mem_outb(mux2_size3_0_sram_inv[0:1]));

	mux2_size3_mem mem_top_track_20 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_8_ccff_tail),
		.ccff_tail(mux2_size3_mem_1_ccff_tail),
		.mem_out(mux2_size3_1_sram[0:1]),
		.mem_outb(mux2_size3_1_sram_inv[0:1]));

	mux2_size2 mux_top_track_2 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_, chanx_left_in[19]}),
		.sram(mux2_size2_0_sram[0:1]),
		.sram_inv(mux2_size2_0_sram_inv[0:1]),
		.out(chany_top_out[1]));

	mux2_size2 mux_top_track_4 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_, chanx_left_in[18]}),
		.sram(mux2_size2_1_sram[0:1]),
		.sram_inv(mux2_size2_1_sram_inv[0:1]),
		.out(chany_top_out[2]));

	mux2_size2 mux_top_track_6 (
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_inpad_0_, chanx_left_in[17]}),
		.sram(mux2_size2_2_sram[0:1]),
		.sram_inv(mux2_size2_2_sram_inv[0:1]),
		.out(chany_top_out[3]));

	mux2_size2 mux_top_track_8 (
		.in({top_right_grid_left_width_0_height_0_subtile_1__pin_inpad_0_, chanx_left_in[16]}),
		.sram(mux2_size2_3_sram[0:1]),
		.sram_inv(mux2_size2_3_sram_inv[0:1]),
		.out(chany_top_out[4]));

	mux2_size2 mux_top_track_10 (
		.in({top_right_grid_left_width_0_height_0_subtile_2__pin_inpad_0_, chanx_left_in[15]}),
		.sram(mux2_size2_4_sram[0:1]),
		.sram_inv(mux2_size2_4_sram_inv[0:1]),
		.out(chany_top_out[5]));

	mux2_size2 mux_top_track_12 (
		.in({top_right_grid_left_width_0_height_0_subtile_3__pin_inpad_0_, chanx_left_in[14]}),
		.sram(mux2_size2_5_sram[0:1]),
		.sram_inv(mux2_size2_5_sram_inv[0:1]),
		.out(chany_top_out[6]));

	mux2_size2 mux_top_track_14 (
		.in({top_right_grid_left_width_0_height_0_subtile_4__pin_inpad_0_, chanx_left_in[13]}),
		.sram(mux2_size2_6_sram[0:1]),
		.sram_inv(mux2_size2_6_sram_inv[0:1]),
		.out(chany_top_out[7]));

	mux2_size2 mux_top_track_16 (
		.in({top_right_grid_left_width_0_height_0_subtile_5__pin_inpad_0_, chanx_left_in[12]}),
		.sram(mux2_size2_7_sram[0:1]),
		.sram_inv(mux2_size2_7_sram_inv[0:1]),
		.out(chany_top_out[8]));

	mux2_size2 mux_top_track_18 (
		.in({top_right_grid_left_width_0_height_0_subtile_6__pin_inpad_0_, chanx_left_in[11]}),
		.sram(mux2_size2_8_sram[0:1]),
		.sram_inv(mux2_size2_8_sram_inv[0:1]),
		.out(chany_top_out[9]));

	mux2_size2 mux_top_track_22 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_, chanx_left_in[9]}),
		.sram(mux2_size2_9_sram[0:1]),
		.sram_inv(mux2_size2_9_sram_inv[0:1]),
		.out(chany_top_out[11]));

	mux2_size2 mux_top_track_24 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_, chanx_left_in[8]}),
		.sram(mux2_size2_10_sram[0:1]),
		.sram_inv(mux2_size2_10_sram_inv[0:1]),
		.out(chany_top_out[12]));

	mux2_size2 mux_top_track_26 (
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_inpad_0_, chanx_left_in[7]}),
		.sram(mux2_size2_11_sram[0:1]),
		.sram_inv(mux2_size2_11_sram_inv[0:1]),
		.out(chany_top_out[13]));

	mux2_size2 mux_top_track_28 (
		.in({top_right_grid_left_width_0_height_0_subtile_1__pin_inpad_0_, chanx_left_in[6]}),
		.sram(mux2_size2_12_sram[0:1]),
		.sram_inv(mux2_size2_12_sram_inv[0:1]),
		.out(chany_top_out[14]));

	mux2_size2 mux_top_track_30 (
		.in({top_right_grid_left_width_0_height_0_subtile_2__pin_inpad_0_, chanx_left_in[5]}),
		.sram(mux2_size2_13_sram[0:1]),
		.sram_inv(mux2_size2_13_sram_inv[0:1]),
		.out(chany_top_out[15]));

	mux2_size2 mux_top_track_32 (
		.in({top_right_grid_left_width_0_height_0_subtile_3__pin_inpad_0_, chanx_left_in[4]}),
		.sram(mux2_size2_14_sram[0:1]),
		.sram_inv(mux2_size2_14_sram_inv[0:1]),
		.out(chany_top_out[16]));

	mux2_size2 mux_top_track_34 (
		.in({top_right_grid_left_width_0_height_0_subtile_4__pin_inpad_0_, chanx_left_in[3]}),
		.sram(mux2_size2_15_sram[0:1]),
		.sram_inv(mux2_size2_15_sram_inv[0:1]),
		.out(chany_top_out[17]));

	mux2_size2 mux_top_track_36 (
		.in({top_right_grid_left_width_0_height_0_subtile_5__pin_inpad_0_, chanx_left_in[2]}),
		.sram(mux2_size2_16_sram[0:1]),
		.sram_inv(mux2_size2_16_sram_inv[0:1]),
		.out(chany_top_out[18]));

	mux2_size2 mux_top_track_38 (
		.in({top_right_grid_left_width_0_height_0_subtile_6__pin_inpad_0_, chanx_left_in[1]}),
		.sram(mux2_size2_17_sram[0:1]),
		.sram_inv(mux2_size2_17_sram_inv[0:1]),
		.out(chany_top_out[19]));

	mux2_size2 mux_left_track_1 (
		.in({chany_top_in[0], left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_}),
		.sram(mux2_size2_18_sram[0:1]),
		.sram_inv(mux2_size2_18_sram_inv[0:1]),
		.out(chanx_left_out[0]));

	mux2_size2 mux_left_track_3 (
		.in({chany_top_in[19], left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_}),
		.sram(mux2_size2_19_sram[0:1]),
		.sram_inv(mux2_size2_19_sram_inv[0:1]),
		.out(chanx_left_out[1]));

	mux2_size2 mux_left_track_5 (
		.in({chany_top_in[18], left_bottom_grid_top_width_0_height_0_subtile_0__pin_inpad_0_}),
		.sram(mux2_size2_20_sram[0:1]),
		.sram_inv(mux2_size2_20_sram_inv[0:1]),
		.out(chanx_left_out[2]));

	mux2_size2 mux_left_track_7 (
		.in({chany_top_in[17], left_bottom_grid_top_width_0_height_0_subtile_1__pin_inpad_0_}),
		.sram(mux2_size2_21_sram[0:1]),
		.sram_inv(mux2_size2_21_sram_inv[0:1]),
		.out(chanx_left_out[3]));

	mux2_size2 mux_left_track_9 (
		.in({chany_top_in[16], left_bottom_grid_top_width_0_height_0_subtile_2__pin_inpad_0_}),
		.sram(mux2_size2_22_sram[0:1]),
		.sram_inv(mux2_size2_22_sram_inv[0:1]),
		.out(chanx_left_out[4]));

	mux2_size2 mux_left_track_11 (
		.in({chany_top_in[15], left_bottom_grid_top_width_0_height_0_subtile_3__pin_inpad_0_}),
		.sram(mux2_size2_23_sram[0:1]),
		.sram_inv(mux2_size2_23_sram_inv[0:1]),
		.out(chanx_left_out[5]));

	mux2_size2 mux_left_track_13 (
		.in({chany_top_in[14], left_bottom_grid_top_width_0_height_0_subtile_4__pin_inpad_0_}),
		.sram(mux2_size2_24_sram[0:1]),
		.sram_inv(mux2_size2_24_sram_inv[0:1]),
		.out(chanx_left_out[6]));

	mux2_size2 mux_left_track_15 (
		.in({chany_top_in[13], left_bottom_grid_top_width_0_height_0_subtile_5__pin_inpad_0_}),
		.sram(mux2_size2_25_sram[0:1]),
		.sram_inv(mux2_size2_25_sram_inv[0:1]),
		.out(chanx_left_out[7]));

	mux2_size2 mux_left_track_17 (
		.in({chany_top_in[12], left_bottom_grid_top_width_0_height_0_subtile_6__pin_inpad_0_}),
		.sram(mux2_size2_26_sram[0:1]),
		.sram_inv(mux2_size2_26_sram_inv[0:1]),
		.out(chanx_left_out[8]));

	mux2_size2 mux_left_track_19 (
		.in({chany_top_in[11], left_bottom_grid_top_width_0_height_0_subtile_7__pin_inpad_0_}),
		.sram(mux2_size2_27_sram[0:1]),
		.sram_inv(mux2_size2_27_sram_inv[0:1]),
		.out(chanx_left_out[9]));

	mux2_size2 mux_left_track_21 (
		.in({chany_top_in[10], left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_}),
		.sram(mux2_size2_28_sram[0:1]),
		.sram_inv(mux2_size2_28_sram_inv[0:1]),
		.out(chanx_left_out[10]));

	mux2_size2 mux_left_track_23 (
		.in({chany_top_in[9], left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_}),
		.sram(mux2_size2_29_sram[0:1]),
		.sram_inv(mux2_size2_29_sram_inv[0:1]),
		.out(chanx_left_out[11]));

	mux2_size2 mux_left_track_25 (
		.in({chany_top_in[8], left_bottom_grid_top_width_0_height_0_subtile_0__pin_inpad_0_}),
		.sram(mux2_size2_30_sram[0:1]),
		.sram_inv(mux2_size2_30_sram_inv[0:1]),
		.out(chanx_left_out[12]));

	mux2_size2 mux_left_track_27 (
		.in({chany_top_in[7], left_bottom_grid_top_width_0_height_0_subtile_1__pin_inpad_0_}),
		.sram(mux2_size2_31_sram[0:1]),
		.sram_inv(mux2_size2_31_sram_inv[0:1]),
		.out(chanx_left_out[13]));

	mux2_size2 mux_left_track_29 (
		.in({chany_top_in[6], left_bottom_grid_top_width_0_height_0_subtile_2__pin_inpad_0_}),
		.sram(mux2_size2_32_sram[0:1]),
		.sram_inv(mux2_size2_32_sram_inv[0:1]),
		.out(chanx_left_out[14]));

	mux2_size2 mux_left_track_31 (
		.in({chany_top_in[5], left_bottom_grid_top_width_0_height_0_subtile_3__pin_inpad_0_}),
		.sram(mux2_size2_33_sram[0:1]),
		.sram_inv(mux2_size2_33_sram_inv[0:1]),
		.out(chanx_left_out[15]));

	mux2_size2 mux_left_track_33 (
		.in({chany_top_in[4], left_bottom_grid_top_width_0_height_0_subtile_4__pin_inpad_0_}),
		.sram(mux2_size2_34_sram[0:1]),
		.sram_inv(mux2_size2_34_sram_inv[0:1]),
		.out(chanx_left_out[16]));

	mux2_size2 mux_left_track_35 (
		.in({chany_top_in[3], left_bottom_grid_top_width_0_height_0_subtile_5__pin_inpad_0_}),
		.sram(mux2_size2_35_sram[0:1]),
		.sram_inv(mux2_size2_35_sram_inv[0:1]),
		.out(chanx_left_out[17]));

	mux2_size2 mux_left_track_37 (
		.in({chany_top_in[2], left_bottom_grid_top_width_0_height_0_subtile_6__pin_inpad_0_}),
		.sram(mux2_size2_36_sram[0:1]),
		.sram_inv(mux2_size2_36_sram_inv[0:1]),
		.out(chanx_left_out[18]));

	mux2_size2 mux_left_track_39 (
		.in({chany_top_in[1], left_bottom_grid_top_width_0_height_0_subtile_7__pin_inpad_0_}),
		.sram(mux2_size2_37_sram[0:1]),
		.sram_inv(mux2_size2_37_sram_inv[0:1]),
		.out(chanx_left_out[19]));

	mux2_size2_mem mem_top_track_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size3_mem_0_ccff_tail),
		.ccff_tail(mux2_size2_mem_0_ccff_tail),
		.mem_out(mux2_size2_0_sram[0:1]),
		.mem_outb(mux2_size2_0_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_0_ccff_tail),
		.ccff_tail(mux2_size2_mem_1_ccff_tail),
		.mem_out(mux2_size2_1_sram[0:1]),
		.mem_outb(mux2_size2_1_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_6 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_1_ccff_tail),
		.ccff_tail(mux2_size2_mem_2_ccff_tail),
		.mem_out(mux2_size2_2_sram[0:1]),
		.mem_outb(mux2_size2_2_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_8 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_2_ccff_tail),
		.ccff_tail(mux2_size2_mem_3_ccff_tail),
		.mem_out(mux2_size2_3_sram[0:1]),
		.mem_outb(mux2_size2_3_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_10 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_3_ccff_tail),
		.ccff_tail(mux2_size2_mem_4_ccff_tail),
		.mem_out(mux2_size2_4_sram[0:1]),
		.mem_outb(mux2_size2_4_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_12 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_4_ccff_tail),
		.ccff_tail(mux2_size2_mem_5_ccff_tail),
		.mem_out(mux2_size2_5_sram[0:1]),
		.mem_outb(mux2_size2_5_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_14 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_5_ccff_tail),
		.ccff_tail(mux2_size2_mem_6_ccff_tail),
		.mem_out(mux2_size2_6_sram[0:1]),
		.mem_outb(mux2_size2_6_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_16 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_6_ccff_tail),
		.ccff_tail(mux2_size2_mem_7_ccff_tail),
		.mem_out(mux2_size2_7_sram[0:1]),
		.mem_outb(mux2_size2_7_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_18 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_7_ccff_tail),
		.ccff_tail(mux2_size2_mem_8_ccff_tail),
		.mem_out(mux2_size2_8_sram[0:1]),
		.mem_outb(mux2_size2_8_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_22 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size3_mem_1_ccff_tail),
		.ccff_tail(mux2_size2_mem_9_ccff_tail),
		.mem_out(mux2_size2_9_sram[0:1]),
		.mem_outb(mux2_size2_9_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_24 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_9_ccff_tail),
		.ccff_tail(mux2_size2_mem_10_ccff_tail),
		.mem_out(mux2_size2_10_sram[0:1]),
		.mem_outb(mux2_size2_10_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_26 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_10_ccff_tail),
		.ccff_tail(mux2_size2_mem_11_ccff_tail),
		.mem_out(mux2_size2_11_sram[0:1]),
		.mem_outb(mux2_size2_11_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_28 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_11_ccff_tail),
		.ccff_tail(mux2_size2_mem_12_ccff_tail),
		.mem_out(mux2_size2_12_sram[0:1]),
		.mem_outb(mux2_size2_12_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_30 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_12_ccff_tail),
		.ccff_tail(mux2_size2_mem_13_ccff_tail),
		.mem_out(mux2_size2_13_sram[0:1]),
		.mem_outb(mux2_size2_13_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_32 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_13_ccff_tail),
		.ccff_tail(mux2_size2_mem_14_ccff_tail),
		.mem_out(mux2_size2_14_sram[0:1]),
		.mem_outb(mux2_size2_14_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_34 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_14_ccff_tail),
		.ccff_tail(mux2_size2_mem_15_ccff_tail),
		.mem_out(mux2_size2_15_sram[0:1]),
		.mem_outb(mux2_size2_15_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_36 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_15_ccff_tail),
		.ccff_tail(mux2_size2_mem_16_ccff_tail),
		.mem_out(mux2_size2_16_sram[0:1]),
		.mem_outb(mux2_size2_16_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_38 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_16_ccff_tail),
		.ccff_tail(mux2_size2_mem_17_ccff_tail),
		.mem_out(mux2_size2_17_sram[0:1]),
		.mem_outb(mux2_size2_17_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_17_ccff_tail),
		.ccff_tail(mux2_size2_mem_18_ccff_tail),
		.mem_out(mux2_size2_18_sram[0:1]),
		.mem_outb(mux2_size2_18_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_18_ccff_tail),
		.ccff_tail(mux2_size2_mem_19_ccff_tail),
		.mem_out(mux2_size2_19_sram[0:1]),
		.mem_outb(mux2_size2_19_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_19_ccff_tail),
		.ccff_tail(mux2_size2_mem_20_ccff_tail),
		.mem_out(mux2_size2_20_sram[0:1]),
		.mem_outb(mux2_size2_20_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_7 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_20_ccff_tail),
		.ccff_tail(mux2_size2_mem_21_ccff_tail),
		.mem_out(mux2_size2_21_sram[0:1]),
		.mem_outb(mux2_size2_21_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_9 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_21_ccff_tail),
		.ccff_tail(mux2_size2_mem_22_ccff_tail),
		.mem_out(mux2_size2_22_sram[0:1]),
		.mem_outb(mux2_size2_22_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_11 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_22_ccff_tail),
		.ccff_tail(mux2_size2_mem_23_ccff_tail),
		.mem_out(mux2_size2_23_sram[0:1]),
		.mem_outb(mux2_size2_23_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_13 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_23_ccff_tail),
		.ccff_tail(mux2_size2_mem_24_ccff_tail),
		.mem_out(mux2_size2_24_sram[0:1]),
		.mem_outb(mux2_size2_24_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_15 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_24_ccff_tail),
		.ccff_tail(mux2_size2_mem_25_ccff_tail),
		.mem_out(mux2_size2_25_sram[0:1]),
		.mem_outb(mux2_size2_25_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_17 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_25_ccff_tail),
		.ccff_tail(mux2_size2_mem_26_ccff_tail),
		.mem_out(mux2_size2_26_sram[0:1]),
		.mem_outb(mux2_size2_26_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_19 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_26_ccff_tail),
		.ccff_tail(mux2_size2_mem_27_ccff_tail),
		.mem_out(mux2_size2_27_sram[0:1]),
		.mem_outb(mux2_size2_27_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_21 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_27_ccff_tail),
		.ccff_tail(mux2_size2_mem_28_ccff_tail),
		.mem_out(mux2_size2_28_sram[0:1]),
		.mem_outb(mux2_size2_28_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_23 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_28_ccff_tail),
		.ccff_tail(mux2_size2_mem_29_ccff_tail),
		.mem_out(mux2_size2_29_sram[0:1]),
		.mem_outb(mux2_size2_29_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_25 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_29_ccff_tail),
		.ccff_tail(mux2_size2_mem_30_ccff_tail),
		.mem_out(mux2_size2_30_sram[0:1]),
		.mem_outb(mux2_size2_30_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_27 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_30_ccff_tail),
		.ccff_tail(mux2_size2_mem_31_ccff_tail),
		.mem_out(mux2_size2_31_sram[0:1]),
		.mem_outb(mux2_size2_31_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_29 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_31_ccff_tail),
		.ccff_tail(mux2_size2_mem_32_ccff_tail),
		.mem_out(mux2_size2_32_sram[0:1]),
		.mem_outb(mux2_size2_32_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_31 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_32_ccff_tail),
		.ccff_tail(mux2_size2_mem_33_ccff_tail),
		.mem_out(mux2_size2_33_sram[0:1]),
		.mem_outb(mux2_size2_33_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_33 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_33_ccff_tail),
		.ccff_tail(mux2_size2_mem_34_ccff_tail),
		.mem_out(mux2_size2_34_sram[0:1]),
		.mem_outb(mux2_size2_34_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_35 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_34_ccff_tail),
		.ccff_tail(mux2_size2_mem_35_ccff_tail),
		.mem_out(mux2_size2_35_sram[0:1]),
		.mem_outb(mux2_size2_35_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_37 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_35_ccff_tail),
		.ccff_tail(mux2_size2_mem_36_ccff_tail),
		.mem_out(mux2_size2_36_sram[0:1]),
		.mem_outb(mux2_size2_36_sram_inv[0:1]));

	mux2_size2_mem mem_left_track_39 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size2_mem_36_ccff_tail),
		.ccff_tail(ccff_tail),
		.mem_out(mux2_size2_37_sram[0:1]),
		.mem_outb(mux2_size2_37_sram_inv[0:1]));

endmodule
// ----- END Verilog module for sb_4__0_ -----

//----- Default net type -----
`default_nettype none



