//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for Unique Switch Blocks[1][0]
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for sb_1__0_ -----
module sb_1__0_(chany_top_in,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_,
                top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_,
                top_right_grid_left_width_0_height_0_subtile_0__pin_O_3_,
                top_right_grid_left_width_0_height_0_subtile_0__pin_O_7_,
                chanx_right_in,
                right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_,
                right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_,
                right_bottom_grid_top_width_0_height_0_subtile_0__pin_inpad_0_,
                right_bottom_grid_top_width_0_height_0_subtile_1__pin_inpad_0_,
                right_bottom_grid_top_width_0_height_0_subtile_2__pin_inpad_0_,
                right_bottom_grid_top_width_0_height_0_subtile_3__pin_inpad_0_,
                right_bottom_grid_top_width_0_height_0_subtile_4__pin_inpad_0_,
                right_bottom_grid_top_width_0_height_0_subtile_5__pin_inpad_0_,
                right_bottom_grid_top_width_0_height_0_subtile_6__pin_inpad_0_,
                right_bottom_grid_top_width_0_height_0_subtile_7__pin_inpad_0_,
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
                bl,
                wl,
                chany_top_out,
                chanx_right_out,
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
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_0__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_1__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_2__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_3__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_4__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_5__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_6__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] right_bottom_grid_top_width_0_height_0_subtile_7__pin_inpad_0_;
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
input [0:77] bl;
//----- INPUT PORTS -----
input [0:77] wl;
//----- OUTPUT PORTS -----
output [0:19] chany_top_out;
//----- OUTPUT PORTS -----
output [0:19] chanx_right_out;
//----- OUTPUT PORTS -----
output [0:19] chanx_left_out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----


wire [0:1] mux2_size2_0_sram;
wire [0:1] mux2_size2_0_sram_inv;
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
wire [0:2] mux2_size4_0_sram;
wire [0:2] mux2_size4_0_sram_inv;
wire [0:2] mux2_size5_0_sram;
wire [0:2] mux2_size5_0_sram_inv;
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
// ----- Local connection due to Wire 25 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[1] = chanx_right_in[0];
// ----- Local connection due to Wire 26 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_left_out[2] = chanx_right_in[1];
// ----- Local connection due to Wire 27 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_left_out[3] = chanx_right_in[2];
// ----- Local connection due to Wire 29 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_left_out[5] = chanx_right_in[4];
// ----- Local connection due to Wire 30 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_left_out[6] = chanx_right_in[5];
// ----- Local connection due to Wire 31 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[7] = chanx_right_in[6];
// ----- Local connection due to Wire 33 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[5] = chanx_right_in[8];
// ----- Net sink id 2 -----
	assign chanx_left_out[9] = chanx_right_in[8];
// ----- Local connection due to Wire 34 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[10] = chanx_right_in[9];
// ----- Local connection due to Wire 35 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_left_out[11] = chanx_right_in[10];
// ----- Local connection due to Wire 37 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_left_out[13] = chanx_right_in[12];
// ----- Local connection due to Wire 38 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[14] = chanx_right_in[13];
// ----- Local connection due to Wire 39 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[15] = chanx_right_in[14];
// ----- Local connection due to Wire 41 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[17] = chanx_right_in[16];
// ----- Local connection due to Wire 42 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[18] = chanx_right_in[17];
// ----- Local connection due to Wire 43 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_left_out[19] = chanx_right_in[18];
// ----- Local connection due to Wire 55 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[1] = chanx_left_in[0];
// ----- Local connection due to Wire 56 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[2] = chanx_left_in[1];
// ----- Local connection due to Wire 57 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[3] = chanx_left_in[2];
// ----- Local connection due to Wire 59 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[5] = chanx_left_in[4];
// ----- Local connection due to Wire 60 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[6] = chanx_left_in[5];
// ----- Local connection due to Wire 61 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[15] = chanx_left_in[6];
// ----- Net sink id 2 -----
	assign chanx_right_out[7] = chanx_left_in[6];
// ----- Local connection due to Wire 63 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[9] = chanx_left_in[8];
// ----- Local connection due to Wire 64 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[10] = chanx_left_in[9];
// ----- Local connection due to Wire 65 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[11] = chanx_left_in[10];
// ----- Local connection due to Wire 67 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chanx_right_out[13] = chanx_left_in[12];
// ----- Local connection due to Wire 68 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[14] = chanx_left_in[13];
// ----- Local connection due to Wire 69 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[15] = chanx_left_in[14];
// ----- Local connection due to Wire 71 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[17] = chanx_left_in[16];
// ----- Local connection due to Wire 72 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[18] = chanx_left_in[17];
// ----- Local connection due to Wire 73 -----
// ----- Net source id 0 -----
// ----- Net sink id 2 -----
	assign chanx_right_out[19] = chanx_left_in[18];
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
	assign chanx_left_out[9] = chany_top_out[5];
	assign chanx_right_out[7] = chany_top_out[15];
// ----- END Local output short connections -----

	mux2_size5 mux_top_track_0 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_, chanx_right_in[1], chanx_right_in[7], chanx_left_in[0], chanx_left_in[3]}),
		.sram(mux2_size5_0_sram[0:2]),
		.sram_inv(mux2_size5_0_sram_inv[0:2]),
		.out(chany_top_out[0]));

	mux2_size5_mem mem_top_track_0 (
		.bl(bl[0:2]),
		.wl({wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size5_0_sram[0:2]),
		.mem_outb(mux2_size5_0_sram_inv[0:2]));

	mux2_size3 mux_top_track_2 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_, chanx_right_in[2], chanx_right_in[11]}),
		.sram(mux2_size3_0_sram[0:1]),
		.sram_inv(mux2_size3_0_sram_inv[0:1]),
		.out(chany_top_out[1]));

	mux2_size3 mux_top_track_4 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_, chanx_right_in[4], chanx_right_in[15]}),
		.sram(mux2_size3_1_sram[0:1]),
		.sram_inv(mux2_size3_1_sram_inv[0:1]),
		.out(chany_top_out[2]));

	mux2_size3 mux_top_track_6 (
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_O_3_, chanx_right_in[5], chanx_right_in[19]}),
		.sram(mux2_size3_2_sram[0:1]),
		.sram_inv(mux2_size3_2_sram_inv[0:1]),
		.out(chany_top_out[3]));

	mux2_size3 mux_top_track_20 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_1_, chanx_right_in[14], chanx_left_in[13]}),
		.sram(mux2_size3_3_sram[0:1]),
		.sram_inv(mux2_size3_3_sram_inv[0:1]),
		.out(chany_top_out[10]));

	mux2_size3 mux_top_track_22 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_5_, chanx_right_in[16], chanx_left_in[12]}),
		.sram(mux2_size3_4_sram[0:1]),
		.sram_inv(mux2_size3_4_sram_inv[0:1]),
		.out(chany_top_out[11]));

	mux2_size3 mux_top_track_24 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_O_9_, chanx_right_in[17], chanx_left_in[10]}),
		.sram(mux2_size3_5_sram[0:1]),
		.sram_inv(mux2_size3_5_sram_inv[0:1]),
		.out(chany_top_out[12]));

	mux2_size3 mux_top_track_26 (
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_O_3_, chanx_right_in[18], chanx_left_in[9]}),
		.sram(mux2_size3_6_sram[0:1]),
		.sram_inv(mux2_size3_6_sram_inv[0:1]),
		.out(chany_top_out[13]));

	mux2_size3_mem mem_top_track_2 (
		.bl(bl[3:4]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_0_sram[0:1]),
		.mem_outb(mux2_size3_0_sram_inv[0:1]));

	mux2_size3_mem mem_top_track_4 (
		.bl(bl[5:6]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_1_sram[0:1]),
		.mem_outb(mux2_size3_1_sram_inv[0:1]));

	mux2_size3_mem mem_top_track_6 (
		.bl(bl[7:8]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_2_sram[0:1]),
		.mem_outb(mux2_size3_2_sram_inv[0:1]));

	mux2_size3_mem mem_top_track_20 (
		.bl(bl[19:20]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_3_sram[0:1]),
		.mem_outb(mux2_size3_3_sram_inv[0:1]));

	mux2_size3_mem mem_top_track_22 (
		.bl(bl[21:22]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_4_sram[0:1]),
		.mem_outb(mux2_size3_4_sram_inv[0:1]));

	mux2_size3_mem mem_top_track_24 (
		.bl(bl[23:24]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_5_sram[0:1]),
		.mem_outb(mux2_size3_5_sram_inv[0:1]));

	mux2_size3_mem mem_top_track_26 (
		.bl(bl[25:26]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_6_sram[0:1]),
		.mem_outb(mux2_size3_6_sram_inv[0:1]));

	mux2_size2 mux_top_track_8 (
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_O_7_, chanx_right_in[6]}),
		.sram(mux2_size2_0_sram[0:1]),
		.sram_inv(mux2_size2_0_sram_inv[0:1]),
		.out(chany_top_out[4]));

	mux2_size2 mux_top_track_12 (
		.in({chanx_right_in[9], chanx_left_in[18]}),
		.sram(mux2_size2_1_sram[0:1]),
		.sram_inv(mux2_size2_1_sram_inv[0:1]),
		.out(chany_top_out[6]));

	mux2_size2 mux_top_track_14 (
		.in({chanx_right_in[10], chanx_left_in[17]}),
		.sram(mux2_size2_2_sram[0:1]),
		.sram_inv(mux2_size2_2_sram_inv[0:1]),
		.out(chany_top_out[7]));

	mux2_size2 mux_top_track_16 (
		.in({chanx_right_in[12], chanx_left_in[16]}),
		.sram(mux2_size2_3_sram[0:1]),
		.sram_inv(mux2_size2_3_sram_inv[0:1]),
		.out(chany_top_out[8]));

	mux2_size2 mux_top_track_18 (
		.in({chanx_right_in[13], chanx_left_in[14]}),
		.sram(mux2_size2_4_sram[0:1]),
		.sram_inv(mux2_size2_4_sram_inv[0:1]),
		.out(chany_top_out[9]));

	mux2_size2 mux_top_track_28 (
		.in({top_right_grid_left_width_0_height_0_subtile_0__pin_O_7_, chanx_left_in[8]}),
		.sram(mux2_size2_5_sram[0:1]),
		.sram_inv(mux2_size2_5_sram_inv[0:1]),
		.out(chany_top_out[14]));

	mux2_size2 mux_top_track_32 (
		.in({chanx_left_in[5], chanx_left_in[19]}),
		.sram(mux2_size2_6_sram[0:1]),
		.sram_inv(mux2_size2_6_sram_inv[0:1]),
		.out(chany_top_out[16]));

	mux2_size2 mux_top_track_34 (
		.in({chanx_left_in[4], chanx_left_in[15]}),
		.sram(mux2_size2_7_sram[0:1]),
		.sram_inv(mux2_size2_7_sram_inv[0:1]),
		.out(chany_top_out[17]));

	mux2_size2 mux_top_track_36 (
		.in({chanx_left_in[2], chanx_left_in[11]}),
		.sram(mux2_size2_8_sram[0:1]),
		.sram_inv(mux2_size2_8_sram_inv[0:1]),
		.out(chany_top_out[18]));

	mux2_size2_mem mem_top_track_8 (
		.bl(bl[9:10]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_0_sram[0:1]),
		.mem_outb(mux2_size2_0_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_12 (
		.bl(bl[11:12]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_1_sram[0:1]),
		.mem_outb(mux2_size2_1_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_14 (
		.bl(bl[13:14]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_2_sram[0:1]),
		.mem_outb(mux2_size2_2_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_16 (
		.bl(bl[15:16]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_3_sram[0:1]),
		.mem_outb(mux2_size2_3_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_18 (
		.bl(bl[17:18]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_4_sram[0:1]),
		.mem_outb(mux2_size2_4_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_28 (
		.bl(bl[27:28]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_5_sram[0:1]),
		.mem_outb(mux2_size2_5_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_32 (
		.bl(bl[29:30]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_6_sram[0:1]),
		.mem_outb(mux2_size2_6_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_34 (
		.bl(bl[31:32]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_7_sram[0:1]),
		.mem_outb(mux2_size2_7_sram_inv[0:1]));

	mux2_size2_mem mem_top_track_36 (
		.bl(bl[33:34]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_8_sram[0:1]),
		.mem_outb(mux2_size2_8_sram_inv[0:1]));

	mux2_size4 mux_top_track_38 (
		.in({chanx_right_in[0], chanx_right_in[3], chanx_left_in[1], chanx_left_in[7]}),
		.sram(mux2_size4_0_sram[0:2]),
		.sram_inv(mux2_size4_0_sram_inv[0:2]),
		.out(chany_top_out[19]));

	mux2_size4_mem mem_top_track_38 (
		.bl(bl[35:37]),
		.wl({wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size4_0_sram[0:2]),
		.mem_outb(mux2_size4_0_sram_inv[0:2]));

	mux2_size9 mux_right_track_0 (
		.in({chany_top_in[4], chany_top_in[9], chany_top_in[14], chany_top_in[19], right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_, right_bottom_grid_top_width_0_height_0_subtile_3__pin_inpad_0_, chanx_left_in[0], chanx_left_in[6], chanx_left_in[13]}),
		.sram(mux2_size9_0_sram[0:3]),
		.sram_inv(mux2_size9_0_sram_inv[0:3]),
		.out(chanx_right_out[0]));

	mux2_size9 mux_right_track_8 (
		.in({chany_top_in[0], chany_top_in[5], chany_top_in[10], chany_top_in[15], right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_, right_bottom_grid_top_width_0_height_0_subtile_4__pin_inpad_0_, chanx_left_in[1], chanx_left_in[8], chanx_left_in[14]}),
		.sram(mux2_size9_1_sram[0:3]),
		.sram_inv(mux2_size9_1_sram_inv[0:3]),
		.out(chanx_right_out[4]));

	mux2_size9 mux_right_track_16 (
		.in({chany_top_in[1], chany_top_in[6], chany_top_in[11], chany_top_in[16], right_bottom_grid_top_width_0_height_0_subtile_0__pin_inpad_0_, right_bottom_grid_top_width_0_height_0_subtile_5__pin_inpad_0_, chanx_left_in[2], chanx_left_in[9], chanx_left_in[16]}),
		.sram(mux2_size9_2_sram[0:3]),
		.sram_inv(mux2_size9_2_sram_inv[0:3]),
		.out(chanx_right_out[8]));

	mux2_size9 mux_right_track_24 (
		.in({chany_top_in[2], chany_top_in[7], chany_top_in[12], chany_top_in[17], right_bottom_grid_top_width_0_height_0_subtile_1__pin_inpad_0_, right_bottom_grid_top_width_0_height_0_subtile_6__pin_inpad_0_, chanx_left_in[4], chanx_left_in[10], chanx_left_in[17]}),
		.sram(mux2_size9_3_sram[0:3]),
		.sram_inv(mux2_size9_3_sram_inv[0:3]),
		.out(chanx_right_out[12]));

	mux2_size9 mux_right_track_32 (
		.in({chany_top_in[3], chany_top_in[8], chany_top_in[13], chany_top_in[18], right_bottom_grid_top_width_0_height_0_subtile_2__pin_inpad_0_, right_bottom_grid_top_width_0_height_0_subtile_7__pin_inpad_0_, chanx_left_in[5], chanx_left_in[12], chanx_left_in[18]}),
		.sram(mux2_size9_4_sram[0:3]),
		.sram_inv(mux2_size9_4_sram_inv[0:3]),
		.out(chanx_right_out[16]));

	mux2_size9 mux_left_track_1 (
		.in({chany_top_in[0], chany_top_in[5], chany_top_in[10], chany_top_in[15], chanx_right_in[0], chanx_right_in[6], chanx_right_in[13], left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_, left_bottom_grid_top_width_0_height_0_subtile_3__pin_inpad_0_}),
		.sram(mux2_size9_5_sram[0:3]),
		.sram_inv(mux2_size9_5_sram_inv[0:3]),
		.out(chanx_left_out[0]));

	mux2_size9 mux_left_track_9 (
		.in({chany_top_in[4], chany_top_in[9], chany_top_in[14], chany_top_in[19], chanx_right_in[1], chanx_right_in[8], chanx_right_in[14], left_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_, left_bottom_grid_top_width_0_height_0_subtile_4__pin_inpad_0_}),
		.sram(mux2_size9_6_sram[0:3]),
		.sram_inv(mux2_size9_6_sram_inv[0:3]),
		.out(chanx_left_out[4]));

	mux2_size9 mux_left_track_17 (
		.in({chany_top_in[3], chany_top_in[8], chany_top_in[13], chany_top_in[18], chanx_right_in[2], chanx_right_in[9], chanx_right_in[16], left_bottom_grid_top_width_0_height_0_subtile_0__pin_inpad_0_, left_bottom_grid_top_width_0_height_0_subtile_5__pin_inpad_0_}),
		.sram(mux2_size9_7_sram[0:3]),
		.sram_inv(mux2_size9_7_sram_inv[0:3]),
		.out(chanx_left_out[8]));

	mux2_size9 mux_left_track_25 (
		.in({chany_top_in[2], chany_top_in[7], chany_top_in[12], chany_top_in[17], chanx_right_in[4], chanx_right_in[10], chanx_right_in[17], left_bottom_grid_top_width_0_height_0_subtile_1__pin_inpad_0_, left_bottom_grid_top_width_0_height_0_subtile_6__pin_inpad_0_}),
		.sram(mux2_size9_8_sram[0:3]),
		.sram_inv(mux2_size9_8_sram_inv[0:3]),
		.out(chanx_left_out[12]));

	mux2_size9 mux_left_track_33 (
		.in({chany_top_in[1], chany_top_in[6], chany_top_in[11], chany_top_in[16], chanx_right_in[5], chanx_right_in[12], chanx_right_in[18], left_bottom_grid_top_width_0_height_0_subtile_2__pin_inpad_0_, left_bottom_grid_top_width_0_height_0_subtile_7__pin_inpad_0_}),
		.sram(mux2_size9_9_sram[0:3]),
		.sram_inv(mux2_size9_9_sram_inv[0:3]),
		.out(chanx_left_out[16]));

	mux2_size9_mem mem_right_track_0 (
		.bl(bl[38:41]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_0_sram[0:3]),
		.mem_outb(mux2_size9_0_sram_inv[0:3]));

	mux2_size9_mem mem_right_track_8 (
		.bl(bl[42:45]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_1_sram[0:3]),
		.mem_outb(mux2_size9_1_sram_inv[0:3]));

	mux2_size9_mem mem_right_track_16 (
		.bl(bl[46:49]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_2_sram[0:3]),
		.mem_outb(mux2_size9_2_sram_inv[0:3]));

	mux2_size9_mem mem_right_track_24 (
		.bl(bl[50:53]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_3_sram[0:3]),
		.mem_outb(mux2_size9_3_sram_inv[0:3]));

	mux2_size9_mem mem_right_track_32 (
		.bl(bl[54:57]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_4_sram[0:3]),
		.mem_outb(mux2_size9_4_sram_inv[0:3]));

	mux2_size9_mem mem_left_track_1 (
		.bl(bl[58:61]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_5_sram[0:3]),
		.mem_outb(mux2_size9_5_sram_inv[0:3]));

	mux2_size9_mem mem_left_track_9 (
		.bl(bl[62:65]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_6_sram[0:3]),
		.mem_outb(mux2_size9_6_sram_inv[0:3]));

	mux2_size9_mem mem_left_track_17 (
		.bl(bl[66:69]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_7_sram[0:3]),
		.mem_outb(mux2_size9_7_sram_inv[0:3]));

	mux2_size9_mem mem_left_track_25 (
		.bl(bl[70:73]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_8_sram[0:3]),
		.mem_outb(mux2_size9_8_sram_inv[0:3]));

	mux2_size9_mem mem_left_track_33 (
		.bl(bl[74:77]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_9_sram[0:3]),
		.mem_outb(mux2_size9_9_sram_inv[0:3]));

endmodule
// ----- END Verilog module for sb_1__0_ -----

//----- Default net type -----
// `default_nettype none



