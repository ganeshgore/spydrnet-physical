//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for pb_type: clb
//	Author: Xifan TANG
//	Organization: University of Utah
//	Date: Thu Oct 28 13:17:18 2021
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

// ----- BEGIN Physical programmable logic block Verilog module: clb -----
//----- Default net type -----
`default_nettype wire

// ----- Verilog module for logical_tile_clb_mode_clb_ -----
module logical_tile_clb_mode_clb_(cfg_done,
                                  prog_reset,
                                  prog_clk,
                                  reset,
                                  clk,
                                  clb_I,
                                  clb_clk,
                                  ccff_head,
                                  clb_O,
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
input [0:39] clb_I;
//----- INPUT PORTS -----
input [0:0] clb_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:9] clb_O;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;

//----- BEGIN Registered ports -----
//----- END Registered ports -----


wire [0:5] mux2_size50_0_sram;
wire [0:5] mux2_size50_0_sram_inv;
wire [0:5] mux2_size50_10_sram;
wire [0:5] mux2_size50_10_sram_inv;
wire [0:5] mux2_size50_11_sram;
wire [0:5] mux2_size50_11_sram_inv;
wire [0:5] mux2_size50_12_sram;
wire [0:5] mux2_size50_12_sram_inv;
wire [0:5] mux2_size50_13_sram;
wire [0:5] mux2_size50_13_sram_inv;
wire [0:5] mux2_size50_14_sram;
wire [0:5] mux2_size50_14_sram_inv;
wire [0:5] mux2_size50_15_sram;
wire [0:5] mux2_size50_15_sram_inv;
wire [0:5] mux2_size50_16_sram;
wire [0:5] mux2_size50_16_sram_inv;
wire [0:5] mux2_size50_17_sram;
wire [0:5] mux2_size50_17_sram_inv;
wire [0:5] mux2_size50_18_sram;
wire [0:5] mux2_size50_18_sram_inv;
wire [0:5] mux2_size50_19_sram;
wire [0:5] mux2_size50_19_sram_inv;
wire [0:5] mux2_size50_1_sram;
wire [0:5] mux2_size50_1_sram_inv;
wire [0:5] mux2_size50_20_sram;
wire [0:5] mux2_size50_20_sram_inv;
wire [0:5] mux2_size50_21_sram;
wire [0:5] mux2_size50_21_sram_inv;
wire [0:5] mux2_size50_22_sram;
wire [0:5] mux2_size50_22_sram_inv;
wire [0:5] mux2_size50_23_sram;
wire [0:5] mux2_size50_23_sram_inv;
wire [0:5] mux2_size50_24_sram;
wire [0:5] mux2_size50_24_sram_inv;
wire [0:5] mux2_size50_25_sram;
wire [0:5] mux2_size50_25_sram_inv;
wire [0:5] mux2_size50_26_sram;
wire [0:5] mux2_size50_26_sram_inv;
wire [0:5] mux2_size50_27_sram;
wire [0:5] mux2_size50_27_sram_inv;
wire [0:5] mux2_size50_28_sram;
wire [0:5] mux2_size50_28_sram_inv;
wire [0:5] mux2_size50_29_sram;
wire [0:5] mux2_size50_29_sram_inv;
wire [0:5] mux2_size50_2_sram;
wire [0:5] mux2_size50_2_sram_inv;
wire [0:5] mux2_size50_30_sram;
wire [0:5] mux2_size50_30_sram_inv;
wire [0:5] mux2_size50_31_sram;
wire [0:5] mux2_size50_31_sram_inv;
wire [0:5] mux2_size50_32_sram;
wire [0:5] mux2_size50_32_sram_inv;
wire [0:5] mux2_size50_33_sram;
wire [0:5] mux2_size50_33_sram_inv;
wire [0:5] mux2_size50_34_sram;
wire [0:5] mux2_size50_34_sram_inv;
wire [0:5] mux2_size50_35_sram;
wire [0:5] mux2_size50_35_sram_inv;
wire [0:5] mux2_size50_36_sram;
wire [0:5] mux2_size50_36_sram_inv;
wire [0:5] mux2_size50_37_sram;
wire [0:5] mux2_size50_37_sram_inv;
wire [0:5] mux2_size50_38_sram;
wire [0:5] mux2_size50_38_sram_inv;
wire [0:5] mux2_size50_39_sram;
wire [0:5] mux2_size50_39_sram_inv;
wire [0:5] mux2_size50_3_sram;
wire [0:5] mux2_size50_3_sram_inv;
wire [0:5] mux2_size50_40_sram;
wire [0:5] mux2_size50_40_sram_inv;
wire [0:5] mux2_size50_41_sram;
wire [0:5] mux2_size50_41_sram_inv;
wire [0:5] mux2_size50_42_sram;
wire [0:5] mux2_size50_42_sram_inv;
wire [0:5] mux2_size50_43_sram;
wire [0:5] mux2_size50_43_sram_inv;
wire [0:5] mux2_size50_44_sram;
wire [0:5] mux2_size50_44_sram_inv;
wire [0:5] mux2_size50_45_sram;
wire [0:5] mux2_size50_45_sram_inv;
wire [0:5] mux2_size50_46_sram;
wire [0:5] mux2_size50_46_sram_inv;
wire [0:5] mux2_size50_47_sram;
wire [0:5] mux2_size50_47_sram_inv;
wire [0:5] mux2_size50_48_sram;
wire [0:5] mux2_size50_48_sram_inv;
wire [0:5] mux2_size50_49_sram;
wire [0:5] mux2_size50_49_sram_inv;
wire [0:5] mux2_size50_4_sram;
wire [0:5] mux2_size50_4_sram_inv;
wire [0:5] mux2_size50_50_sram;
wire [0:5] mux2_size50_50_sram_inv;
wire [0:5] mux2_size50_51_sram;
wire [0:5] mux2_size50_51_sram_inv;
wire [0:5] mux2_size50_52_sram;
wire [0:5] mux2_size50_52_sram_inv;
wire [0:5] mux2_size50_53_sram;
wire [0:5] mux2_size50_53_sram_inv;
wire [0:5] mux2_size50_54_sram;
wire [0:5] mux2_size50_54_sram_inv;
wire [0:5] mux2_size50_55_sram;
wire [0:5] mux2_size50_55_sram_inv;
wire [0:5] mux2_size50_56_sram;
wire [0:5] mux2_size50_56_sram_inv;
wire [0:5] mux2_size50_57_sram;
wire [0:5] mux2_size50_57_sram_inv;
wire [0:5] mux2_size50_58_sram;
wire [0:5] mux2_size50_58_sram_inv;
wire [0:5] mux2_size50_59_sram;
wire [0:5] mux2_size50_59_sram_inv;
wire [0:5] mux2_size50_5_sram;
wire [0:5] mux2_size50_5_sram_inv;
wire [0:5] mux2_size50_6_sram;
wire [0:5] mux2_size50_6_sram_inv;
wire [0:5] mux2_size50_7_sram;
wire [0:5] mux2_size50_7_sram_inv;
wire [0:5] mux2_size50_8_sram;
wire [0:5] mux2_size50_8_sram_inv;
wire [0:5] mux2_size50_9_sram;
wire [0:5] mux2_size50_9_sram_inv;

// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.fle_in({mux2_size50_0_out, mux2_size50_1_out, mux2_size50_2_out, mux2_size50_3_out, mux2_size50_4_out, mux2_size50_5_out}),
		.fle_clk(direct_interc_10_out),
		.ccff_head(ccff_head),
		.fle_out(logical_tile_clb_mode_default__fle_0_fle_out),
		.ccff_tail(logical_tile_clb_mode_default__fle_0_ccff_tail));

	logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.fle_in({mux2_size50_6_out, mux2_size50_7_out, mux2_size50_8_out, mux2_size50_9_out, mux2_size50_10_out, mux2_size50_11_out}),
		.fle_clk(direct_interc_11_out),
		.ccff_head(logical_tile_clb_mode_default__fle_0_ccff_tail),
		.fle_out(logical_tile_clb_mode_default__fle_1_fle_out),
		.ccff_tail(logical_tile_clb_mode_default__fle_1_ccff_tail));

	logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.fle_in({mux2_size50_12_out, mux2_size50_13_out, mux2_size50_14_out, mux2_size50_15_out, mux2_size50_16_out, mux2_size50_17_out}),
		.fle_clk(direct_interc_12_out),
		.ccff_head(logical_tile_clb_mode_default__fle_1_ccff_tail),
		.fle_out(logical_tile_clb_mode_default__fle_2_fle_out),
		.ccff_tail(logical_tile_clb_mode_default__fle_2_ccff_tail));

	logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.fle_in({mux2_size50_18_out, mux2_size50_19_out, mux2_size50_20_out, mux2_size50_21_out, mux2_size50_22_out, mux2_size50_23_out}),
		.fle_clk(direct_interc_13_out),
		.ccff_head(logical_tile_clb_mode_default__fle_2_ccff_tail),
		.fle_out(logical_tile_clb_mode_default__fle_3_fle_out),
		.ccff_tail(logical_tile_clb_mode_default__fle_3_ccff_tail));

	logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.fle_in({mux2_size50_24_out, mux2_size50_25_out, mux2_size50_26_out, mux2_size50_27_out, mux2_size50_28_out, mux2_size50_29_out}),
		.fle_clk(direct_interc_14_out),
		.ccff_head(logical_tile_clb_mode_default__fle_3_ccff_tail),
		.fle_out(logical_tile_clb_mode_default__fle_4_fle_out),
		.ccff_tail(logical_tile_clb_mode_default__fle_4_ccff_tail));

	logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.fle_in({mux2_size50_30_out, mux2_size50_31_out, mux2_size50_32_out, mux2_size50_33_out, mux2_size50_34_out, mux2_size50_35_out}),
		.fle_clk(direct_interc_15_out),
		.ccff_head(logical_tile_clb_mode_default__fle_4_ccff_tail),
		.fle_out(logical_tile_clb_mode_default__fle_5_fle_out),
		.ccff_tail(logical_tile_clb_mode_default__fle_5_ccff_tail));

	logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_6 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.fle_in({mux2_size50_36_out, mux2_size50_37_out, mux2_size50_38_out, mux2_size50_39_out, mux2_size50_40_out, mux2_size50_41_out}),
		.fle_clk(direct_interc_16_out),
		.ccff_head(logical_tile_clb_mode_default__fle_5_ccff_tail),
		.fle_out(logical_tile_clb_mode_default__fle_6_fle_out),
		.ccff_tail(logical_tile_clb_mode_default__fle_6_ccff_tail));

	logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_7 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.fle_in({mux2_size50_42_out, mux2_size50_43_out, mux2_size50_44_out, mux2_size50_45_out, mux2_size50_46_out, mux2_size50_47_out}),
		.fle_clk(direct_interc_17_out),
		.ccff_head(logical_tile_clb_mode_default__fle_6_ccff_tail),
		.fle_out(logical_tile_clb_mode_default__fle_7_fle_out),
		.ccff_tail(logical_tile_clb_mode_default__fle_7_ccff_tail));

	logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_8 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.fle_in({mux2_size50_48_out, mux2_size50_49_out, mux2_size50_50_out, mux2_size50_51_out, mux2_size50_52_out, mux2_size50_53_out}),
		.fle_clk(direct_interc_18_out),
		.ccff_head(logical_tile_clb_mode_default__fle_7_ccff_tail),
		.fle_out(logical_tile_clb_mode_default__fle_8_fle_out),
		.ccff_tail(logical_tile_clb_mode_default__fle_8_ccff_tail));

	logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_9 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.fle_in({mux2_size50_54_out, mux2_size50_55_out, mux2_size50_56_out, mux2_size50_57_out, mux2_size50_58_out, mux2_size50_59_out}),
		.fle_clk(direct_interc_19_out),
		.ccff_head(logical_tile_clb_mode_default__fle_8_ccff_tail),
		.fle_out(logical_tile_clb_mode_default__fle_9_fle_out),
		.ccff_tail(logical_tile_clb_mode_default__fle_9_ccff_tail));

	direct_interc direct_interc_0_ (
		.in(logical_tile_clb_mode_default__fle_0_fle_out),
		.out(clb_O[0]));

	direct_interc direct_interc_1_ (
		.in(logical_tile_clb_mode_default__fle_1_fle_out),
		.out(clb_O[1]));

	direct_interc direct_interc_2_ (
		.in(logical_tile_clb_mode_default__fle_2_fle_out),
		.out(clb_O[2]));

	direct_interc direct_interc_3_ (
		.in(logical_tile_clb_mode_default__fle_3_fle_out),
		.out(clb_O[3]));

	direct_interc direct_interc_4_ (
		.in(logical_tile_clb_mode_default__fle_4_fle_out),
		.out(clb_O[4]));

	direct_interc direct_interc_5_ (
		.in(logical_tile_clb_mode_default__fle_5_fle_out),
		.out(clb_O[5]));

	direct_interc direct_interc_6_ (
		.in(logical_tile_clb_mode_default__fle_6_fle_out),
		.out(clb_O[6]));

	direct_interc direct_interc_7_ (
		.in(logical_tile_clb_mode_default__fle_7_fle_out),
		.out(clb_O[7]));

	direct_interc direct_interc_8_ (
		.in(logical_tile_clb_mode_default__fle_8_fle_out),
		.out(clb_O[8]));

	direct_interc direct_interc_9_ (
		.in(logical_tile_clb_mode_default__fle_9_fle_out),
		.out(clb_O[9]));

	direct_interc direct_interc_10_ (
		.in(clb_clk),
		.out(direct_interc_10_out));

	direct_interc direct_interc_11_ (
		.in(clb_clk),
		.out(direct_interc_11_out));

	direct_interc direct_interc_12_ (
		.in(clb_clk),
		.out(direct_interc_12_out));

	direct_interc direct_interc_13_ (
		.in(clb_clk),
		.out(direct_interc_13_out));

	direct_interc direct_interc_14_ (
		.in(clb_clk),
		.out(direct_interc_14_out));

	direct_interc direct_interc_15_ (
		.in(clb_clk),
		.out(direct_interc_15_out));

	direct_interc direct_interc_16_ (
		.in(clb_clk),
		.out(direct_interc_16_out));

	direct_interc direct_interc_17_ (
		.in(clb_clk),
		.out(direct_interc_17_out));

	direct_interc direct_interc_18_ (
		.in(clb_clk),
		.out(direct_interc_18_out));

	direct_interc direct_interc_19_ (
		.in(clb_clk),
		.out(direct_interc_19_out));

	mux2_size50 mux_fle_0_in_0 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_0_sram[0:5]),
		.sram_inv(mux2_size50_0_sram_inv[0:5]),
		.out(mux2_size50_0_out));

	mux2_size50 mux_fle_0_in_1 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_1_sram[0:5]),
		.sram_inv(mux2_size50_1_sram_inv[0:5]),
		.out(mux2_size50_1_out));

	mux2_size50 mux_fle_0_in_2 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_2_sram[0:5]),
		.sram_inv(mux2_size50_2_sram_inv[0:5]),
		.out(mux2_size50_2_out));

	mux2_size50 mux_fle_0_in_3 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_3_sram[0:5]),
		.sram_inv(mux2_size50_3_sram_inv[0:5]),
		.out(mux2_size50_3_out));

	mux2_size50 mux_fle_0_in_4 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_4_sram[0:5]),
		.sram_inv(mux2_size50_4_sram_inv[0:5]),
		.out(mux2_size50_4_out));

	mux2_size50 mux_fle_0_in_5 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_5_sram[0:5]),
		.sram_inv(mux2_size50_5_sram_inv[0:5]),
		.out(mux2_size50_5_out));

	mux2_size50 mux_fle_1_in_0 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_6_sram[0:5]),
		.sram_inv(mux2_size50_6_sram_inv[0:5]),
		.out(mux2_size50_6_out));

	mux2_size50 mux_fle_1_in_1 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_7_sram[0:5]),
		.sram_inv(mux2_size50_7_sram_inv[0:5]),
		.out(mux2_size50_7_out));

	mux2_size50 mux_fle_1_in_2 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_8_sram[0:5]),
		.sram_inv(mux2_size50_8_sram_inv[0:5]),
		.out(mux2_size50_8_out));

	mux2_size50 mux_fle_1_in_3 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_9_sram[0:5]),
		.sram_inv(mux2_size50_9_sram_inv[0:5]),
		.out(mux2_size50_9_out));

	mux2_size50 mux_fle_1_in_4 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_10_sram[0:5]),
		.sram_inv(mux2_size50_10_sram_inv[0:5]),
		.out(mux2_size50_10_out));

	mux2_size50 mux_fle_1_in_5 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_11_sram[0:5]),
		.sram_inv(mux2_size50_11_sram_inv[0:5]),
		.out(mux2_size50_11_out));

	mux2_size50 mux_fle_2_in_0 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_12_sram[0:5]),
		.sram_inv(mux2_size50_12_sram_inv[0:5]),
		.out(mux2_size50_12_out));

	mux2_size50 mux_fle_2_in_1 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_13_sram[0:5]),
		.sram_inv(mux2_size50_13_sram_inv[0:5]),
		.out(mux2_size50_13_out));

	mux2_size50 mux_fle_2_in_2 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_14_sram[0:5]),
		.sram_inv(mux2_size50_14_sram_inv[0:5]),
		.out(mux2_size50_14_out));

	mux2_size50 mux_fle_2_in_3 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_15_sram[0:5]),
		.sram_inv(mux2_size50_15_sram_inv[0:5]),
		.out(mux2_size50_15_out));

	mux2_size50 mux_fle_2_in_4 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_16_sram[0:5]),
		.sram_inv(mux2_size50_16_sram_inv[0:5]),
		.out(mux2_size50_16_out));

	mux2_size50 mux_fle_2_in_5 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_17_sram[0:5]),
		.sram_inv(mux2_size50_17_sram_inv[0:5]),
		.out(mux2_size50_17_out));

	mux2_size50 mux_fle_3_in_0 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_18_sram[0:5]),
		.sram_inv(mux2_size50_18_sram_inv[0:5]),
		.out(mux2_size50_18_out));

	mux2_size50 mux_fle_3_in_1 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_19_sram[0:5]),
		.sram_inv(mux2_size50_19_sram_inv[0:5]),
		.out(mux2_size50_19_out));

	mux2_size50 mux_fle_3_in_2 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_20_sram[0:5]),
		.sram_inv(mux2_size50_20_sram_inv[0:5]),
		.out(mux2_size50_20_out));

	mux2_size50 mux_fle_3_in_3 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_21_sram[0:5]),
		.sram_inv(mux2_size50_21_sram_inv[0:5]),
		.out(mux2_size50_21_out));

	mux2_size50 mux_fle_3_in_4 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_22_sram[0:5]),
		.sram_inv(mux2_size50_22_sram_inv[0:5]),
		.out(mux2_size50_22_out));

	mux2_size50 mux_fle_3_in_5 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_23_sram[0:5]),
		.sram_inv(mux2_size50_23_sram_inv[0:5]),
		.out(mux2_size50_23_out));

	mux2_size50 mux_fle_4_in_0 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_24_sram[0:5]),
		.sram_inv(mux2_size50_24_sram_inv[0:5]),
		.out(mux2_size50_24_out));

	mux2_size50 mux_fle_4_in_1 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_25_sram[0:5]),
		.sram_inv(mux2_size50_25_sram_inv[0:5]),
		.out(mux2_size50_25_out));

	mux2_size50 mux_fle_4_in_2 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_26_sram[0:5]),
		.sram_inv(mux2_size50_26_sram_inv[0:5]),
		.out(mux2_size50_26_out));

	mux2_size50 mux_fle_4_in_3 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_27_sram[0:5]),
		.sram_inv(mux2_size50_27_sram_inv[0:5]),
		.out(mux2_size50_27_out));

	mux2_size50 mux_fle_4_in_4 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_28_sram[0:5]),
		.sram_inv(mux2_size50_28_sram_inv[0:5]),
		.out(mux2_size50_28_out));

	mux2_size50 mux_fle_4_in_5 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_29_sram[0:5]),
		.sram_inv(mux2_size50_29_sram_inv[0:5]),
		.out(mux2_size50_29_out));

	mux2_size50 mux_fle_5_in_0 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_30_sram[0:5]),
		.sram_inv(mux2_size50_30_sram_inv[0:5]),
		.out(mux2_size50_30_out));

	mux2_size50 mux_fle_5_in_1 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_31_sram[0:5]),
		.sram_inv(mux2_size50_31_sram_inv[0:5]),
		.out(mux2_size50_31_out));

	mux2_size50 mux_fle_5_in_2 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_32_sram[0:5]),
		.sram_inv(mux2_size50_32_sram_inv[0:5]),
		.out(mux2_size50_32_out));

	mux2_size50 mux_fle_5_in_3 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_33_sram[0:5]),
		.sram_inv(mux2_size50_33_sram_inv[0:5]),
		.out(mux2_size50_33_out));

	mux2_size50 mux_fle_5_in_4 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_34_sram[0:5]),
		.sram_inv(mux2_size50_34_sram_inv[0:5]),
		.out(mux2_size50_34_out));

	mux2_size50 mux_fle_5_in_5 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_35_sram[0:5]),
		.sram_inv(mux2_size50_35_sram_inv[0:5]),
		.out(mux2_size50_35_out));

	mux2_size50 mux_fle_6_in_0 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_36_sram[0:5]),
		.sram_inv(mux2_size50_36_sram_inv[0:5]),
		.out(mux2_size50_36_out));

	mux2_size50 mux_fle_6_in_1 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_37_sram[0:5]),
		.sram_inv(mux2_size50_37_sram_inv[0:5]),
		.out(mux2_size50_37_out));

	mux2_size50 mux_fle_6_in_2 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_38_sram[0:5]),
		.sram_inv(mux2_size50_38_sram_inv[0:5]),
		.out(mux2_size50_38_out));

	mux2_size50 mux_fle_6_in_3 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_39_sram[0:5]),
		.sram_inv(mux2_size50_39_sram_inv[0:5]),
		.out(mux2_size50_39_out));

	mux2_size50 mux_fle_6_in_4 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_40_sram[0:5]),
		.sram_inv(mux2_size50_40_sram_inv[0:5]),
		.out(mux2_size50_40_out));

	mux2_size50 mux_fle_6_in_5 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_41_sram[0:5]),
		.sram_inv(mux2_size50_41_sram_inv[0:5]),
		.out(mux2_size50_41_out));

	mux2_size50 mux_fle_7_in_0 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_42_sram[0:5]),
		.sram_inv(mux2_size50_42_sram_inv[0:5]),
		.out(mux2_size50_42_out));

	mux2_size50 mux_fle_7_in_1 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_43_sram[0:5]),
		.sram_inv(mux2_size50_43_sram_inv[0:5]),
		.out(mux2_size50_43_out));

	mux2_size50 mux_fle_7_in_2 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_44_sram[0:5]),
		.sram_inv(mux2_size50_44_sram_inv[0:5]),
		.out(mux2_size50_44_out));

	mux2_size50 mux_fle_7_in_3 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_45_sram[0:5]),
		.sram_inv(mux2_size50_45_sram_inv[0:5]),
		.out(mux2_size50_45_out));

	mux2_size50 mux_fle_7_in_4 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_46_sram[0:5]),
		.sram_inv(mux2_size50_46_sram_inv[0:5]),
		.out(mux2_size50_46_out));

	mux2_size50 mux_fle_7_in_5 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_47_sram[0:5]),
		.sram_inv(mux2_size50_47_sram_inv[0:5]),
		.out(mux2_size50_47_out));

	mux2_size50 mux_fle_8_in_0 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_48_sram[0:5]),
		.sram_inv(mux2_size50_48_sram_inv[0:5]),
		.out(mux2_size50_48_out));

	mux2_size50 mux_fle_8_in_1 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_49_sram[0:5]),
		.sram_inv(mux2_size50_49_sram_inv[0:5]),
		.out(mux2_size50_49_out));

	mux2_size50 mux_fle_8_in_2 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_50_sram[0:5]),
		.sram_inv(mux2_size50_50_sram_inv[0:5]),
		.out(mux2_size50_50_out));

	mux2_size50 mux_fle_8_in_3 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_51_sram[0:5]),
		.sram_inv(mux2_size50_51_sram_inv[0:5]),
		.out(mux2_size50_51_out));

	mux2_size50 mux_fle_8_in_4 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_52_sram[0:5]),
		.sram_inv(mux2_size50_52_sram_inv[0:5]),
		.out(mux2_size50_52_out));

	mux2_size50 mux_fle_8_in_5 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_53_sram[0:5]),
		.sram_inv(mux2_size50_53_sram_inv[0:5]),
		.out(mux2_size50_53_out));

	mux2_size50 mux_fle_9_in_0 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_54_sram[0:5]),
		.sram_inv(mux2_size50_54_sram_inv[0:5]),
		.out(mux2_size50_54_out));

	mux2_size50 mux_fle_9_in_1 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_55_sram[0:5]),
		.sram_inv(mux2_size50_55_sram_inv[0:5]),
		.out(mux2_size50_55_out));

	mux2_size50 mux_fle_9_in_2 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_56_sram[0:5]),
		.sram_inv(mux2_size50_56_sram_inv[0:5]),
		.out(mux2_size50_56_out));

	mux2_size50 mux_fle_9_in_3 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_57_sram[0:5]),
		.sram_inv(mux2_size50_57_sram_inv[0:5]),
		.out(mux2_size50_57_out));

	mux2_size50 mux_fle_9_in_4 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_58_sram[0:5]),
		.sram_inv(mux2_size50_58_sram_inv[0:5]),
		.out(mux2_size50_58_out));

	mux2_size50 mux_fle_9_in_5 (
		.in({clb_I[0:39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
		.sram(mux2_size50_59_sram[0:5]),
		.sram_inv(mux2_size50_59_sram_inv[0:5]),
		.out(mux2_size50_59_out));

	mux2_size50_mem mem_fle_0_in_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(logical_tile_clb_mode_default__fle_9_ccff_tail),
		.ccff_tail(mux2_size50_mem_0_ccff_tail),
		.mem_out(mux2_size50_0_sram[0:5]),
		.mem_outb(mux2_size50_0_sram_inv[0:5]));

	mux2_size50_mem mem_fle_0_in_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_0_ccff_tail),
		.ccff_tail(mux2_size50_mem_1_ccff_tail),
		.mem_out(mux2_size50_1_sram[0:5]),
		.mem_outb(mux2_size50_1_sram_inv[0:5]));

	mux2_size50_mem mem_fle_0_in_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_1_ccff_tail),
		.ccff_tail(mux2_size50_mem_2_ccff_tail),
		.mem_out(mux2_size50_2_sram[0:5]),
		.mem_outb(mux2_size50_2_sram_inv[0:5]));

	mux2_size50_mem mem_fle_0_in_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_2_ccff_tail),
		.ccff_tail(mux2_size50_mem_3_ccff_tail),
		.mem_out(mux2_size50_3_sram[0:5]),
		.mem_outb(mux2_size50_3_sram_inv[0:5]));

	mux2_size50_mem mem_fle_0_in_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_3_ccff_tail),
		.ccff_tail(mux2_size50_mem_4_ccff_tail),
		.mem_out(mux2_size50_4_sram[0:5]),
		.mem_outb(mux2_size50_4_sram_inv[0:5]));

	mux2_size50_mem mem_fle_0_in_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_4_ccff_tail),
		.ccff_tail(mux2_size50_mem_5_ccff_tail),
		.mem_out(mux2_size50_5_sram[0:5]),
		.mem_outb(mux2_size50_5_sram_inv[0:5]));

	mux2_size50_mem mem_fle_1_in_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_5_ccff_tail),
		.ccff_tail(mux2_size50_mem_6_ccff_tail),
		.mem_out(mux2_size50_6_sram[0:5]),
		.mem_outb(mux2_size50_6_sram_inv[0:5]));

	mux2_size50_mem mem_fle_1_in_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_6_ccff_tail),
		.ccff_tail(mux2_size50_mem_7_ccff_tail),
		.mem_out(mux2_size50_7_sram[0:5]),
		.mem_outb(mux2_size50_7_sram_inv[0:5]));

	mux2_size50_mem mem_fle_1_in_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_7_ccff_tail),
		.ccff_tail(mux2_size50_mem_8_ccff_tail),
		.mem_out(mux2_size50_8_sram[0:5]),
		.mem_outb(mux2_size50_8_sram_inv[0:5]));

	mux2_size50_mem mem_fle_1_in_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_8_ccff_tail),
		.ccff_tail(mux2_size50_mem_9_ccff_tail),
		.mem_out(mux2_size50_9_sram[0:5]),
		.mem_outb(mux2_size50_9_sram_inv[0:5]));

	mux2_size50_mem mem_fle_1_in_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_9_ccff_tail),
		.ccff_tail(mux2_size50_mem_10_ccff_tail),
		.mem_out(mux2_size50_10_sram[0:5]),
		.mem_outb(mux2_size50_10_sram_inv[0:5]));

	mux2_size50_mem mem_fle_1_in_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_10_ccff_tail),
		.ccff_tail(mux2_size50_mem_11_ccff_tail),
		.mem_out(mux2_size50_11_sram[0:5]),
		.mem_outb(mux2_size50_11_sram_inv[0:5]));

	mux2_size50_mem mem_fle_2_in_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_11_ccff_tail),
		.ccff_tail(mux2_size50_mem_12_ccff_tail),
		.mem_out(mux2_size50_12_sram[0:5]),
		.mem_outb(mux2_size50_12_sram_inv[0:5]));

	mux2_size50_mem mem_fle_2_in_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_12_ccff_tail),
		.ccff_tail(mux2_size50_mem_13_ccff_tail),
		.mem_out(mux2_size50_13_sram[0:5]),
		.mem_outb(mux2_size50_13_sram_inv[0:5]));

	mux2_size50_mem mem_fle_2_in_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_13_ccff_tail),
		.ccff_tail(mux2_size50_mem_14_ccff_tail),
		.mem_out(mux2_size50_14_sram[0:5]),
		.mem_outb(mux2_size50_14_sram_inv[0:5]));

	mux2_size50_mem mem_fle_2_in_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_14_ccff_tail),
		.ccff_tail(mux2_size50_mem_15_ccff_tail),
		.mem_out(mux2_size50_15_sram[0:5]),
		.mem_outb(mux2_size50_15_sram_inv[0:5]));

	mux2_size50_mem mem_fle_2_in_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_15_ccff_tail),
		.ccff_tail(mux2_size50_mem_16_ccff_tail),
		.mem_out(mux2_size50_16_sram[0:5]),
		.mem_outb(mux2_size50_16_sram_inv[0:5]));

	mux2_size50_mem mem_fle_2_in_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_16_ccff_tail),
		.ccff_tail(mux2_size50_mem_17_ccff_tail),
		.mem_out(mux2_size50_17_sram[0:5]),
		.mem_outb(mux2_size50_17_sram_inv[0:5]));

	mux2_size50_mem mem_fle_3_in_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_17_ccff_tail),
		.ccff_tail(mux2_size50_mem_18_ccff_tail),
		.mem_out(mux2_size50_18_sram[0:5]),
		.mem_outb(mux2_size50_18_sram_inv[0:5]));

	mux2_size50_mem mem_fle_3_in_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_18_ccff_tail),
		.ccff_tail(mux2_size50_mem_19_ccff_tail),
		.mem_out(mux2_size50_19_sram[0:5]),
		.mem_outb(mux2_size50_19_sram_inv[0:5]));

	mux2_size50_mem mem_fle_3_in_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_19_ccff_tail),
		.ccff_tail(mux2_size50_mem_20_ccff_tail),
		.mem_out(mux2_size50_20_sram[0:5]),
		.mem_outb(mux2_size50_20_sram_inv[0:5]));

	mux2_size50_mem mem_fle_3_in_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_20_ccff_tail),
		.ccff_tail(mux2_size50_mem_21_ccff_tail),
		.mem_out(mux2_size50_21_sram[0:5]),
		.mem_outb(mux2_size50_21_sram_inv[0:5]));

	mux2_size50_mem mem_fle_3_in_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_21_ccff_tail),
		.ccff_tail(mux2_size50_mem_22_ccff_tail),
		.mem_out(mux2_size50_22_sram[0:5]),
		.mem_outb(mux2_size50_22_sram_inv[0:5]));

	mux2_size50_mem mem_fle_3_in_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_22_ccff_tail),
		.ccff_tail(mux2_size50_mem_23_ccff_tail),
		.mem_out(mux2_size50_23_sram[0:5]),
		.mem_outb(mux2_size50_23_sram_inv[0:5]));

	mux2_size50_mem mem_fle_4_in_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_23_ccff_tail),
		.ccff_tail(mux2_size50_mem_24_ccff_tail),
		.mem_out(mux2_size50_24_sram[0:5]),
		.mem_outb(mux2_size50_24_sram_inv[0:5]));

	mux2_size50_mem mem_fle_4_in_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_24_ccff_tail),
		.ccff_tail(mux2_size50_mem_25_ccff_tail),
		.mem_out(mux2_size50_25_sram[0:5]),
		.mem_outb(mux2_size50_25_sram_inv[0:5]));

	mux2_size50_mem mem_fle_4_in_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_25_ccff_tail),
		.ccff_tail(mux2_size50_mem_26_ccff_tail),
		.mem_out(mux2_size50_26_sram[0:5]),
		.mem_outb(mux2_size50_26_sram_inv[0:5]));

	mux2_size50_mem mem_fle_4_in_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_26_ccff_tail),
		.ccff_tail(mux2_size50_mem_27_ccff_tail),
		.mem_out(mux2_size50_27_sram[0:5]),
		.mem_outb(mux2_size50_27_sram_inv[0:5]));

	mux2_size50_mem mem_fle_4_in_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_27_ccff_tail),
		.ccff_tail(mux2_size50_mem_28_ccff_tail),
		.mem_out(mux2_size50_28_sram[0:5]),
		.mem_outb(mux2_size50_28_sram_inv[0:5]));

	mux2_size50_mem mem_fle_4_in_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_28_ccff_tail),
		.ccff_tail(mux2_size50_mem_29_ccff_tail),
		.mem_out(mux2_size50_29_sram[0:5]),
		.mem_outb(mux2_size50_29_sram_inv[0:5]));

	mux2_size50_mem mem_fle_5_in_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_29_ccff_tail),
		.ccff_tail(mux2_size50_mem_30_ccff_tail),
		.mem_out(mux2_size50_30_sram[0:5]),
		.mem_outb(mux2_size50_30_sram_inv[0:5]));

	mux2_size50_mem mem_fle_5_in_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_30_ccff_tail),
		.ccff_tail(mux2_size50_mem_31_ccff_tail),
		.mem_out(mux2_size50_31_sram[0:5]),
		.mem_outb(mux2_size50_31_sram_inv[0:5]));

	mux2_size50_mem mem_fle_5_in_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_31_ccff_tail),
		.ccff_tail(mux2_size50_mem_32_ccff_tail),
		.mem_out(mux2_size50_32_sram[0:5]),
		.mem_outb(mux2_size50_32_sram_inv[0:5]));

	mux2_size50_mem mem_fle_5_in_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_32_ccff_tail),
		.ccff_tail(mux2_size50_mem_33_ccff_tail),
		.mem_out(mux2_size50_33_sram[0:5]),
		.mem_outb(mux2_size50_33_sram_inv[0:5]));

	mux2_size50_mem mem_fle_5_in_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_33_ccff_tail),
		.ccff_tail(mux2_size50_mem_34_ccff_tail),
		.mem_out(mux2_size50_34_sram[0:5]),
		.mem_outb(mux2_size50_34_sram_inv[0:5]));

	mux2_size50_mem mem_fle_5_in_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_34_ccff_tail),
		.ccff_tail(mux2_size50_mem_35_ccff_tail),
		.mem_out(mux2_size50_35_sram[0:5]),
		.mem_outb(mux2_size50_35_sram_inv[0:5]));

	mux2_size50_mem mem_fle_6_in_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_35_ccff_tail),
		.ccff_tail(mux2_size50_mem_36_ccff_tail),
		.mem_out(mux2_size50_36_sram[0:5]),
		.mem_outb(mux2_size50_36_sram_inv[0:5]));

	mux2_size50_mem mem_fle_6_in_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_36_ccff_tail),
		.ccff_tail(mux2_size50_mem_37_ccff_tail),
		.mem_out(mux2_size50_37_sram[0:5]),
		.mem_outb(mux2_size50_37_sram_inv[0:5]));

	mux2_size50_mem mem_fle_6_in_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_37_ccff_tail),
		.ccff_tail(mux2_size50_mem_38_ccff_tail),
		.mem_out(mux2_size50_38_sram[0:5]),
		.mem_outb(mux2_size50_38_sram_inv[0:5]));

	mux2_size50_mem mem_fle_6_in_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_38_ccff_tail),
		.ccff_tail(mux2_size50_mem_39_ccff_tail),
		.mem_out(mux2_size50_39_sram[0:5]),
		.mem_outb(mux2_size50_39_sram_inv[0:5]));

	mux2_size50_mem mem_fle_6_in_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_39_ccff_tail),
		.ccff_tail(mux2_size50_mem_40_ccff_tail),
		.mem_out(mux2_size50_40_sram[0:5]),
		.mem_outb(mux2_size50_40_sram_inv[0:5]));

	mux2_size50_mem mem_fle_6_in_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_40_ccff_tail),
		.ccff_tail(mux2_size50_mem_41_ccff_tail),
		.mem_out(mux2_size50_41_sram[0:5]),
		.mem_outb(mux2_size50_41_sram_inv[0:5]));

	mux2_size50_mem mem_fle_7_in_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_41_ccff_tail),
		.ccff_tail(mux2_size50_mem_42_ccff_tail),
		.mem_out(mux2_size50_42_sram[0:5]),
		.mem_outb(mux2_size50_42_sram_inv[0:5]));

	mux2_size50_mem mem_fle_7_in_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_42_ccff_tail),
		.ccff_tail(mux2_size50_mem_43_ccff_tail),
		.mem_out(mux2_size50_43_sram[0:5]),
		.mem_outb(mux2_size50_43_sram_inv[0:5]));

	mux2_size50_mem mem_fle_7_in_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_43_ccff_tail),
		.ccff_tail(mux2_size50_mem_44_ccff_tail),
		.mem_out(mux2_size50_44_sram[0:5]),
		.mem_outb(mux2_size50_44_sram_inv[0:5]));

	mux2_size50_mem mem_fle_7_in_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_44_ccff_tail),
		.ccff_tail(mux2_size50_mem_45_ccff_tail),
		.mem_out(mux2_size50_45_sram[0:5]),
		.mem_outb(mux2_size50_45_sram_inv[0:5]));

	mux2_size50_mem mem_fle_7_in_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_45_ccff_tail),
		.ccff_tail(mux2_size50_mem_46_ccff_tail),
		.mem_out(mux2_size50_46_sram[0:5]),
		.mem_outb(mux2_size50_46_sram_inv[0:5]));

	mux2_size50_mem mem_fle_7_in_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_46_ccff_tail),
		.ccff_tail(mux2_size50_mem_47_ccff_tail),
		.mem_out(mux2_size50_47_sram[0:5]),
		.mem_outb(mux2_size50_47_sram_inv[0:5]));

	mux2_size50_mem mem_fle_8_in_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_47_ccff_tail),
		.ccff_tail(mux2_size50_mem_48_ccff_tail),
		.mem_out(mux2_size50_48_sram[0:5]),
		.mem_outb(mux2_size50_48_sram_inv[0:5]));

	mux2_size50_mem mem_fle_8_in_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_48_ccff_tail),
		.ccff_tail(mux2_size50_mem_49_ccff_tail),
		.mem_out(mux2_size50_49_sram[0:5]),
		.mem_outb(mux2_size50_49_sram_inv[0:5]));

	mux2_size50_mem mem_fle_8_in_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_49_ccff_tail),
		.ccff_tail(mux2_size50_mem_50_ccff_tail),
		.mem_out(mux2_size50_50_sram[0:5]),
		.mem_outb(mux2_size50_50_sram_inv[0:5]));

	mux2_size50_mem mem_fle_8_in_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_50_ccff_tail),
		.ccff_tail(mux2_size50_mem_51_ccff_tail),
		.mem_out(mux2_size50_51_sram[0:5]),
		.mem_outb(mux2_size50_51_sram_inv[0:5]));

	mux2_size50_mem mem_fle_8_in_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_51_ccff_tail),
		.ccff_tail(mux2_size50_mem_52_ccff_tail),
		.mem_out(mux2_size50_52_sram[0:5]),
		.mem_outb(mux2_size50_52_sram_inv[0:5]));

	mux2_size50_mem mem_fle_8_in_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_52_ccff_tail),
		.ccff_tail(mux2_size50_mem_53_ccff_tail),
		.mem_out(mux2_size50_53_sram[0:5]),
		.mem_outb(mux2_size50_53_sram_inv[0:5]));

	mux2_size50_mem mem_fle_9_in_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_53_ccff_tail),
		.ccff_tail(mux2_size50_mem_54_ccff_tail),
		.mem_out(mux2_size50_54_sram[0:5]),
		.mem_outb(mux2_size50_54_sram_inv[0:5]));

	mux2_size50_mem mem_fle_9_in_1 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_54_ccff_tail),
		.ccff_tail(mux2_size50_mem_55_ccff_tail),
		.mem_out(mux2_size50_55_sram[0:5]),
		.mem_outb(mux2_size50_55_sram_inv[0:5]));

	mux2_size50_mem mem_fle_9_in_2 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_55_ccff_tail),
		.ccff_tail(mux2_size50_mem_56_ccff_tail),
		.mem_out(mux2_size50_56_sram[0:5]),
		.mem_outb(mux2_size50_56_sram_inv[0:5]));

	mux2_size50_mem mem_fle_9_in_3 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_56_ccff_tail),
		.ccff_tail(mux2_size50_mem_57_ccff_tail),
		.mem_out(mux2_size50_57_sram[0:5]),
		.mem_outb(mux2_size50_57_sram_inv[0:5]));

	mux2_size50_mem mem_fle_9_in_4 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_57_ccff_tail),
		.ccff_tail(mux2_size50_mem_58_ccff_tail),
		.mem_out(mux2_size50_58_sram[0:5]),
		.mem_outb(mux2_size50_58_sram_inv[0:5]));

	mux2_size50_mem mem_fle_9_in_5 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.ccff_head(mux2_size50_mem_58_ccff_tail),
		.ccff_tail(ccff_tail),
		.mem_out(mux2_size50_59_sram[0:5]),
		.mem_outb(mux2_size50_59_sram_inv[0:5]));

endmodule
// ----- END Verilog module for logical_tile_clb_mode_clb_ -----

//----- Default net type -----
`default_nettype none



// ----- END Physical programmable logic block Verilog module: clb -----
