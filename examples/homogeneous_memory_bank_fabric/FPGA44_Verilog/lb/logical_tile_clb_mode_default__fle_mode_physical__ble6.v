//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for pb_type: ble6
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

// ----- BEGIN Physical programmable logic block Verilog module: ble6 -----
//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for logical_tile_clb_mode_default__fle_mode_physical__ble6 -----
module logical_tile_clb_mode_default__fle_mode_physical__ble6(reset,
                                                              clk,
                                                              ble6_in,
                                                              ble6_clk,
                                                              bl,
                                                              wl,
                                                              ble6_out);
//----- GLOBAL PORTS -----
input [0:0] reset;
//----- GLOBAL PORTS -----
input [0:0] clk;
//----- INPUT PORTS -----
input [0:5] ble6_in;
//----- INPUT PORTS -----
input [0:0] ble6_clk;
//----- INPUT PORTS -----
input [0:65] bl;
//----- INPUT PORTS -----
input [0:65] wl;
//----- OUTPUT PORTS -----
output [0:0] ble6_out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----


wire [0:1] mux2_size2_0_sram;
wire [0:1] mux2_size2_0_sram_inv;

// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6 logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6_0 (
		.lut6_in({direct_interc_0_out, direct_interc_1_out, direct_interc_2_out, direct_interc_3_out, direct_interc_4_out, direct_interc_5_out}),
		.bl(bl[0:63]),
		.wl(wl[0:63]),
		.lut6_out(logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6_0_lut6_out));

	logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff_0 (
		.reset(reset),
		.clk(clk),
		.ff_D(direct_interc_6_out),
		.ff_Q(logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff_0_ff_Q),
		.ff_clk(direct_interc_7_out));

	mux2_size2 mux_ble6_out_0 (
		.in({logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff_0_ff_Q, logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6_0_lut6_out}),
		.sram(mux2_size2_0_sram[0:1]),
		.sram_inv(mux2_size2_0_sram_inv[0:1]),
		.out(ble6_out));

	mux2_size2_mem mem_ble6_out_0 (
		.bl(bl[64:65]),
		.wl(wl[64:65]),
		.mem_out(mux2_size2_0_sram[0:1]),
		.mem_outb(mux2_size2_0_sram_inv[0:1]));

	direct_interc direct_interc_0_ (
		.in(ble6_in[0]),
		.out(direct_interc_0_out));

	direct_interc direct_interc_1_ (
		.in(ble6_in[1]),
		.out(direct_interc_1_out));

	direct_interc direct_interc_2_ (
		.in(ble6_in[2]),
		.out(direct_interc_2_out));

	direct_interc direct_interc_3_ (
		.in(ble6_in[3]),
		.out(direct_interc_3_out));

	direct_interc direct_interc_4_ (
		.in(ble6_in[4]),
		.out(direct_interc_4_out));

	direct_interc direct_interc_5_ (
		.in(ble6_in[5]),
		.out(direct_interc_5_out));

	direct_interc direct_interc_6_ (
		.in(logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6_0_lut6_out),
		.out(direct_interc_6_out));

	direct_interc direct_interc_7_ (
		.in(ble6_clk),
		.out(direct_interc_7_out));

endmodule
// ----- END Verilog module for logical_tile_clb_mode_default__fle_mode_physical__ble6 -----

//----- Default net type -----
// `default_nettype none



// ----- END Physical programmable logic block Verilog module: ble6 -----
