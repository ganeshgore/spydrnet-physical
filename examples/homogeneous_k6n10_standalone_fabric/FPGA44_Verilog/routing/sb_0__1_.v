//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for Unique Switch Blocks[0][1]
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for sb_0__1_ -----
module sb_0__1_(chany_top_in,
                top_left_grid_right_width_0_height_0_subtile_0__pin_inpad_0_,
                top_left_grid_right_width_0_height_0_subtile_1__pin_inpad_0_,
                top_left_grid_right_width_0_height_0_subtile_2__pin_inpad_0_,
                top_left_grid_right_width_0_height_0_subtile_3__pin_inpad_0_,
                top_left_grid_right_width_0_height_0_subtile_4__pin_inpad_0_,
                top_left_grid_right_width_0_height_0_subtile_5__pin_inpad_0_,
                top_left_grid_right_width_0_height_0_subtile_6__pin_inpad_0_,
                top_left_grid_right_width_0_height_0_subtile_7__pin_inpad_0_,
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
                bottom_left_grid_right_width_0_height_0_subtile_0__pin_inpad_0_,
                bottom_left_grid_right_width_0_height_0_subtile_1__pin_inpad_0_,
                bottom_left_grid_right_width_0_height_0_subtile_2__pin_inpad_0_,
                bottom_left_grid_right_width_0_height_0_subtile_3__pin_inpad_0_,
                bottom_left_grid_right_width_0_height_0_subtile_4__pin_inpad_0_,
                bottom_left_grid_right_width_0_height_0_subtile_5__pin_inpad_0_,
                bottom_left_grid_right_width_0_height_0_subtile_6__pin_inpad_0_,
                bottom_left_grid_right_width_0_height_0_subtile_7__pin_inpad_0_,
                bl,
                wl,
                chany_top_out,
                chanx_right_out,
                chany_bottom_out);
//----- INPUT PORTS -----
input [0:19] chany_top_in;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_0__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_1__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_2__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_3__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_4__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_5__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_6__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] top_left_grid_right_width_0_height_0_subtile_7__pin_inpad_0_;
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
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_0__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_1__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_2__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_3__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_4__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_5__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_6__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:0] bottom_left_grid_right_width_0_height_0_subtile_7__pin_inpad_0_;
//----- INPUT PORTS -----
input [0:77] bl;
//----- INPUT PORTS -----
input [0:77] wl;
//----- OUTPUT PORTS -----
output [0:19] chany_top_out;
//----- OUTPUT PORTS -----
output [0:19] chanx_right_out;
//----- OUTPUT PORTS -----
output [0:19] chany_bottom_out;

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
wire [0:1] mux2_size3_8_sram;
wire [0:1] mux2_size3_8_sram_inv;
wire [0:2] mux2_size4_0_sram;
wire [0:2] mux2_size4_0_sram_inv;
wire [0:2] mux2_size4_1_sram;
wire [0:2] mux2_size4_1_sram_inv;
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
// ----- Local connection due to Wire 50 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chanx_right_out[0] = right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_[0];
// ----- Local connection due to Wire 55 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[1] = chany_bottom_in[0];
// ----- Local connection due to Wire 56 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[2] = chany_bottom_in[1];
// ----- Local connection due to Wire 57 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[3] = chany_bottom_in[2];
// ----- Local connection due to Wire 59 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[5] = chany_bottom_in[4];
// ----- Local connection due to Wire 60 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[6] = chany_bottom_in[5];
// ----- Local connection due to Wire 61 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[7] = chany_bottom_in[6];
// ----- Local connection due to Wire 63 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[9] = chany_bottom_in[8];
// ----- Local connection due to Wire 64 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[10] = chany_bottom_in[9];
// ----- Local connection due to Wire 65 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[11] = chany_bottom_in[10];
// ----- Local connection due to Wire 67 -----
// ----- Net source id 0 -----
// ----- Net sink id 0 -----
	assign chany_top_out[13] = chany_bottom_in[12];
// ----- Local connection due to Wire 68 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[14] = chany_bottom_in[13];
// ----- Local connection due to Wire 69 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[15] = chany_bottom_in[14];
// ----- Local connection due to Wire 71 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[17] = chany_bottom_in[16];
// ----- Local connection due to Wire 72 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[18] = chany_bottom_in[17];
// ----- Local connection due to Wire 73 -----
// ----- Net source id 0 -----
// ----- Net sink id 1 -----
	assign chany_top_out[19] = chany_bottom_in[18];
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	mux2_size9 mux_top_track_0 (
		.in({top_left_grid_right_width_0_height_0_subtile_0__pin_inpad_0_, top_left_grid_right_width_0_height_0_subtile_5__pin_inpad_0_, chanx_right_in[1], chanx_right_in[6], chanx_right_in[11], chanx_right_in[16], chany_bottom_in[0], chany_bottom_in[6], chany_bottom_in[13]}),
		.sram(mux2_size9_0_sram[0:3]),
		.sram_inv(mux2_size9_0_sram_inv[0:3]),
		.out(chany_top_out[0]));

	mux2_size9 mux_top_track_8 (
		.in({top_left_grid_right_width_0_height_0_subtile_1__pin_inpad_0_, top_left_grid_right_width_0_height_0_subtile_6__pin_inpad_0_, chanx_right_in[2], chanx_right_in[7], chanx_right_in[12], chanx_right_in[17], chany_bottom_in[1], chany_bottom_in[8], chany_bottom_in[14]}),
		.sram(mux2_size9_1_sram[0:3]),
		.sram_inv(mux2_size9_1_sram_inv[0:3]),
		.out(chany_top_out[4]));

	mux2_size9 mux_top_track_16 (
		.in({top_left_grid_right_width_0_height_0_subtile_2__pin_inpad_0_, top_left_grid_right_width_0_height_0_subtile_7__pin_inpad_0_, chanx_right_in[3], chanx_right_in[8], chanx_right_in[13], chanx_right_in[18], chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[16]}),
		.sram(mux2_size9_2_sram[0:3]),
		.sram_inv(mux2_size9_2_sram_inv[0:3]),
		.out(chany_top_out[8]));

	mux2_size9 mux_top_track_24 (
		.in({top_left_grid_right_width_0_height_0_subtile_3__pin_inpad_0_, top_right_grid_left_width_0_height_0_subtile_0__pin_O_3_, chanx_right_in[4], chanx_right_in[9], chanx_right_in[14], chanx_right_in[19], chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[17]}),
		.sram(mux2_size9_3_sram[0:3]),
		.sram_inv(mux2_size9_3_sram_inv[0:3]),
		.out(chany_top_out[12]));

	mux2_size9 mux_top_track_32 (
		.in({top_left_grid_right_width_0_height_0_subtile_4__pin_inpad_0_, top_right_grid_left_width_0_height_0_subtile_0__pin_O_7_, chanx_right_in[0], chanx_right_in[5], chanx_right_in[10], chanx_right_in[15], chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18]}),
		.sram(mux2_size9_4_sram[0:3]),
		.sram_inv(mux2_size9_4_sram_inv[0:3]),
		.out(chany_top_out[16]));

	mux2_size9 mux_bottom_track_1 (
		.in({chany_top_in[0], chany_top_in[6], chany_top_in[13], chanx_right_in[3], chanx_right_in[8], chanx_right_in[13], chanx_right_in[18], bottom_right_grid_left_width_0_height_0_subtile_0__pin_O_3_, bottom_left_grid_right_width_0_height_0_subtile_3__pin_inpad_0_}),
		.sram(mux2_size9_5_sram[0:3]),
		.sram_inv(mux2_size9_5_sram_inv[0:3]),
		.out(chany_bottom_out[0]));

	mux2_size9 mux_bottom_track_9 (
		.in({chany_top_in[1], chany_top_in[8], chany_top_in[14], chanx_right_in[2], chanx_right_in[7], chanx_right_in[12], chanx_right_in[17], bottom_right_grid_left_width_0_height_0_subtile_0__pin_O_7_, bottom_left_grid_right_width_0_height_0_subtile_4__pin_inpad_0_}),
		.sram(mux2_size9_6_sram[0:3]),
		.sram_inv(mux2_size9_6_sram_inv[0:3]),
		.out(chany_bottom_out[4]));

	mux2_size9 mux_bottom_track_17 (
		.in({chany_top_in[2], chany_top_in[9], chany_top_in[16], chanx_right_in[1], chanx_right_in[6], chanx_right_in[11], chanx_right_in[16], bottom_left_grid_right_width_0_height_0_subtile_0__pin_inpad_0_, bottom_left_grid_right_width_0_height_0_subtile_5__pin_inpad_0_}),
		.sram(mux2_size9_7_sram[0:3]),
		.sram_inv(mux2_size9_7_sram_inv[0:3]),
		.out(chany_bottom_out[8]));

	mux2_size9 mux_bottom_track_25 (
		.in({chany_top_in[4], chany_top_in[10], chany_top_in[17], chanx_right_in[0], chanx_right_in[5], chanx_right_in[10], chanx_right_in[15], bottom_left_grid_right_width_0_height_0_subtile_1__pin_inpad_0_, bottom_left_grid_right_width_0_height_0_subtile_6__pin_inpad_0_}),
		.sram(mux2_size9_8_sram[0:3]),
		.sram_inv(mux2_size9_8_sram_inv[0:3]),
		.out(chany_bottom_out[12]));

	mux2_size9 mux_bottom_track_33 (
		.in({chany_top_in[5], chany_top_in[12], chany_top_in[18], chanx_right_in[4], chanx_right_in[9], chanx_right_in[14], chanx_right_in[19], bottom_left_grid_right_width_0_height_0_subtile_2__pin_inpad_0_, bottom_left_grid_right_width_0_height_0_subtile_7__pin_inpad_0_}),
		.sram(mux2_size9_9_sram[0:3]),
		.sram_inv(mux2_size9_9_sram_inv[0:3]),
		.out(chany_bottom_out[16]));

	mux2_size9_mem mem_top_track_0 (
		.bl(bl[0:3]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_0_sram[0:3]),
		.mem_outb(mux2_size9_0_sram_inv[0:3]));

	mux2_size9_mem mem_top_track_8 (
		.bl(bl[4:7]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_1_sram[0:3]),
		.mem_outb(mux2_size9_1_sram_inv[0:3]));

	mux2_size9_mem mem_top_track_16 (
		.bl(bl[8:11]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_2_sram[0:3]),
		.mem_outb(mux2_size9_2_sram_inv[0:3]));

	mux2_size9_mem mem_top_track_24 (
		.bl(bl[12:15]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_3_sram[0:3]),
		.mem_outb(mux2_size9_3_sram_inv[0:3]));

	mux2_size9_mem mem_top_track_32 (
		.bl(bl[16:19]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_4_sram[0:3]),
		.mem_outb(mux2_size9_4_sram_inv[0:3]));

	mux2_size9_mem mem_bottom_track_1 (
		.bl(bl[58:61]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_5_sram[0:3]),
		.mem_outb(mux2_size9_5_sram_inv[0:3]));

	mux2_size9_mem mem_bottom_track_9 (
		.bl(bl[62:65]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_6_sram[0:3]),
		.mem_outb(mux2_size9_6_sram_inv[0:3]));

	mux2_size9_mem mem_bottom_track_17 (
		.bl(bl[66:69]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_7_sram[0:3]),
		.mem_outb(mux2_size9_7_sram_inv[0:3]));

	mux2_size9_mem mem_bottom_track_25 (
		.bl(bl[70:73]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_8_sram[0:3]),
		.mem_outb(mux2_size9_8_sram_inv[0:3]));

	mux2_size9_mem mem_bottom_track_33 (
		.bl(bl[74:77]),
		.wl({wl[0], wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size9_9_sram[0:3]),
		.mem_outb(mux2_size9_9_sram_inv[0:3]));

	mux2_size3 mux_right_track_2 (
		.in({chany_top_in[0], chany_top_in[3], right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_}),
		.sram(mux2_size3_0_sram[0:1]),
		.sram_inv(mux2_size3_0_sram_inv[0:1]),
		.out(chanx_right_out[1]));

	mux2_size3 mux_right_track_4 (
		.in({chany_top_in[1], chany_top_in[7], right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_0_}),
		.sram(mux2_size3_1_sram[0:1]),
		.sram_inv(mux2_size3_1_sram_inv[0:1]),
		.out(chanx_right_out[2]));

	mux2_size3 mux_right_track_6 (
		.in({chany_top_in[2], chany_top_in[11], right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_4_}),
		.sram(mux2_size3_2_sram[0:1]),
		.sram_inv(mux2_size3_2_sram_inv[0:1]),
		.out(chanx_right_out[3]));

	mux2_size3 mux_right_track_10 (
		.in({chany_top_in[5], chany_top_in[19], chany_bottom_in[17]}),
		.sram(mux2_size3_3_sram[0:1]),
		.sram_inv(mux2_size3_3_sram_inv[0:1]),
		.out(chanx_right_out[5]));

	mux2_size3 mux_right_track_20 (
		.in({chany_top_in[12], right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_2_, chany_bottom_in[10]}),
		.sram(mux2_size3_4_sram[0:1]),
		.sram_inv(mux2_size3_4_sram_inv[0:1]),
		.out(chanx_right_out[10]));

	mux2_size3 mux_right_track_22 (
		.in({chany_top_in[13], right_top_grid_bottom_width_0_height_0_subtile_0__pin_O_6_, chany_bottom_in[9]}),
		.sram(mux2_size3_5_sram[0:1]),
		.sram_inv(mux2_size3_5_sram_inv[0:1]),
		.out(chanx_right_out[11]));

	mux2_size3 mux_right_track_24 (
		.in({chany_top_in[14], right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_0_, chany_bottom_in[8]}),
		.sram(mux2_size3_6_sram[0:1]),
		.sram_inv(mux2_size3_6_sram_inv[0:1]),
		.out(chanx_right_out[12]));

	mux2_size3 mux_right_track_26 (
		.in({chany_top_in[16], right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_4_, chany_bottom_in[6]}),
		.sram(mux2_size3_7_sram[0:1]),
		.sram_inv(mux2_size3_7_sram_inv[0:1]),
		.out(chanx_right_out[13]));

	mux2_size3 mux_right_track_30 (
		.in({chany_top_in[18], chany_bottom_in[4], chany_bottom_in[15]}),
		.sram(mux2_size3_8_sram[0:1]),
		.sram_inv(mux2_size3_8_sram_inv[0:1]),
		.out(chanx_right_out[15]));

	mux2_size3_mem mem_right_track_2 (
		.bl(bl[20:21]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_0_sram[0:1]),
		.mem_outb(mux2_size3_0_sram_inv[0:1]));

	mux2_size3_mem mem_right_track_4 (
		.bl(bl[22:23]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_1_sram[0:1]),
		.mem_outb(mux2_size3_1_sram_inv[0:1]));

	mux2_size3_mem mem_right_track_6 (
		.bl(bl[24:25]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_2_sram[0:1]),
		.mem_outb(mux2_size3_2_sram_inv[0:1]));

	mux2_size3_mem mem_right_track_10 (
		.bl(bl[29:30]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_3_sram[0:1]),
		.mem_outb(mux2_size3_3_sram_inv[0:1]));

	mux2_size3_mem mem_right_track_20 (
		.bl(bl[39:40]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_4_sram[0:1]),
		.mem_outb(mux2_size3_4_sram_inv[0:1]));

	mux2_size3_mem mem_right_track_22 (
		.bl(bl[41:42]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_5_sram[0:1]),
		.mem_outb(mux2_size3_5_sram_inv[0:1]));

	mux2_size3_mem mem_right_track_24 (
		.bl(bl[43:44]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_6_sram[0:1]),
		.mem_outb(mux2_size3_6_sram_inv[0:1]));

	mux2_size3_mem mem_right_track_26 (
		.bl(bl[45:46]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_7_sram[0:1]),
		.mem_outb(mux2_size3_7_sram_inv[0:1]));

	mux2_size3_mem mem_right_track_30 (
		.bl(bl[50:51]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size3_8_sram[0:1]),
		.mem_outb(mux2_size3_8_sram_inv[0:1]));

	mux2_size4 mux_right_track_8 (
		.in({chany_top_in[4], chany_top_in[15], right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_8_, chany_bottom_in[18]}),
		.sram(mux2_size4_0_sram[0:2]),
		.sram_inv(mux2_size4_0_sram_inv[0:2]),
		.out(chanx_right_out[4]));

	mux2_size4 mux_right_track_28 (
		.in({chany_top_in[17], right_bottom_grid_top_width_0_height_0_subtile_0__pin_O_8_, chany_bottom_in[5], chany_bottom_in[19]}),
		.sram(mux2_size4_1_sram[0:2]),
		.sram_inv(mux2_size4_1_sram_inv[0:2]),
		.out(chanx_right_out[14]));

	mux2_size4_mem mem_right_track_8 (
		.bl(bl[26:28]),
		.wl({wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size4_0_sram[0:2]),
		.mem_outb(mux2_size4_0_sram_inv[0:2]));

	mux2_size4_mem mem_right_track_28 (
		.bl(bl[47:49]),
		.wl({wl[0], wl[0], wl[0]}),
		.mem_out(mux2_size4_1_sram[0:2]),
		.mem_outb(mux2_size4_1_sram_inv[0:2]));

	mux2_size2 mux_right_track_12 (
		.in({chany_top_in[6], chany_bottom_in[16]}),
		.sram(mux2_size2_0_sram[0:1]),
		.sram_inv(mux2_size2_0_sram_inv[0:1]),
		.out(chanx_right_out[6]));

	mux2_size2 mux_right_track_14 (
		.in({chany_top_in[8], chany_bottom_in[14]}),
		.sram(mux2_size2_1_sram[0:1]),
		.sram_inv(mux2_size2_1_sram_inv[0:1]),
		.out(chanx_right_out[7]));

	mux2_size2 mux_right_track_16 (
		.in({chany_top_in[9], chany_bottom_in[13]}),
		.sram(mux2_size2_2_sram[0:1]),
		.sram_inv(mux2_size2_2_sram_inv[0:1]),
		.out(chanx_right_out[8]));

	mux2_size2 mux_right_track_18 (
		.in({chany_top_in[10], chany_bottom_in[12]}),
		.sram(mux2_size2_3_sram[0:1]),
		.sram_inv(mux2_size2_3_sram_inv[0:1]),
		.out(chanx_right_out[9]));

	mux2_size2 mux_right_track_32 (
		.in({chany_bottom_in[2], chany_bottom_in[11]}),
		.sram(mux2_size2_4_sram[0:1]),
		.sram_inv(mux2_size2_4_sram_inv[0:1]),
		.out(chanx_right_out[16]));

	mux2_size2 mux_right_track_34 (
		.in({chany_bottom_in[1], chany_bottom_in[7]}),
		.sram(mux2_size2_5_sram[0:1]),
		.sram_inv(mux2_size2_5_sram_inv[0:1]),
		.out(chanx_right_out[17]));

	mux2_size2 mux_right_track_36 (
		.in({chany_bottom_in[0], chany_bottom_in[3]}),
		.sram(mux2_size2_6_sram[0:1]),
		.sram_inv(mux2_size2_6_sram_inv[0:1]),
		.out(chanx_right_out[18]));

	mux2_size2_mem mem_right_track_12 (
		.bl(bl[31:32]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_0_sram[0:1]),
		.mem_outb(mux2_size2_0_sram_inv[0:1]));

	mux2_size2_mem mem_right_track_14 (
		.bl(bl[33:34]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_1_sram[0:1]),
		.mem_outb(mux2_size2_1_sram_inv[0:1]));

	mux2_size2_mem mem_right_track_16 (
		.bl(bl[35:36]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_2_sram[0:1]),
		.mem_outb(mux2_size2_2_sram_inv[0:1]));

	mux2_size2_mem mem_right_track_18 (
		.bl(bl[37:38]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_3_sram[0:1]),
		.mem_outb(mux2_size2_3_sram_inv[0:1]));

	mux2_size2_mem mem_right_track_32 (
		.bl(bl[52:53]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_4_sram[0:1]),
		.mem_outb(mux2_size2_4_sram_inv[0:1]));

	mux2_size2_mem mem_right_track_34 (
		.bl(bl[54:55]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_5_sram[0:1]),
		.mem_outb(mux2_size2_5_sram_inv[0:1]));

	mux2_size2_mem mem_right_track_36 (
		.bl(bl[56:57]),
		.wl({wl[0], wl[0]}),
		.mem_out(mux2_size2_6_sram[0:1]),
		.mem_outb(mux2_size2_6_sram_inv[0:1]));

endmodule
// ----- END Verilog module for sb_0__1_ -----

//----- Default net type -----
// `default_nettype none



