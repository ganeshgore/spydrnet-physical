//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for pb_type: fle
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

// ----- BEGIN Physical programmable logic block Verilog module: fle -----
//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for logical_tile_clb_mode_default__fle -----
module logical_tile_clb_mode_default__fle(cfg_done,
                                          prog_reset,
                                          prog_clk,
                                          reset,
                                          clk,
                                          fle_in,
                                          fle_clk,
                                          ccff_head,
                                          fle_out,
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
input [0:5] fle_in;
//----- INPUT PORTS -----
input [0:0] fle_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] fle_out;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	logical_tile_clb_mode_default__fle_mode_physical__ble6 logical_tile_clb_mode_default__fle_mode_physical__ble6_0 (
		.cfg_done(cfg_done),
		.prog_reset(prog_reset),
		.prog_clk(prog_clk),
		.reset(reset),
		.clk(clk),
		.ble6_in({direct_interc_1_out, direct_interc_2_out, direct_interc_3_out, direct_interc_4_out, direct_interc_5_out, direct_interc_6_out}),
		.ble6_clk(direct_interc_7_out),
		.ccff_head(ccff_head),
		.ble6_out(logical_tile_clb_mode_default__fle_mode_physical__ble6_0_ble6_out),
		.ccff_tail(ccff_tail));

	direct_interc direct_interc_0_ (
		.in(logical_tile_clb_mode_default__fle_mode_physical__ble6_0_ble6_out),
		.out(fle_out));

	direct_interc direct_interc_1_ (
		.in(fle_in[0]),
		.out(direct_interc_1_out));

	direct_interc direct_interc_2_ (
		.in(fle_in[1]),
		.out(direct_interc_2_out));

	direct_interc direct_interc_3_ (
		.in(fle_in[2]),
		.out(direct_interc_3_out));

	direct_interc direct_interc_4_ (
		.in(fle_in[3]),
		.out(direct_interc_4_out));

	direct_interc direct_interc_5_ (
		.in(fle_in[4]),
		.out(direct_interc_5_out));

	direct_interc direct_interc_6_ (
		.in(fle_in[5]),
		.out(direct_interc_6_out));

	direct_interc direct_interc_7_ (
		.in(fle_clk),
		.out(direct_interc_7_out));

endmodule
// ----- END Verilog module for logical_tile_clb_mode_default__fle -----

//----- Default net type -----
// `default_nettype none



// ----- END Physical programmable logic block Verilog module: fle -----
