//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for primitive pb_type: lut6
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6 -----
module logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6(lut6_in,
                                                                                 bl,
                                                                                 wl,
                                                                                 lut6_out);
//----- INPUT PORTS -----
input [0:5] lut6_in;
//----- INPUT PORTS -----
input [0:63] bl;
//----- INPUT PORTS -----
input [0:63] wl;
//----- OUTPUT PORTS -----
output [0:0] lut6_out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----


wire [0:63] lut6_0_sram;
wire [0:63] lut6_SRAM_mem_undriven_mem_outb;

// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	lut6 lut6_0_ (
		.in(lut6_in[0:5]),
		.sram(lut6_0_sram[0:63]),
		.out(lut6_out));

	lut6_SRAM_mem lut6_SRAM_mem (
		.bl(bl[0:63]),
		.wl(wl[0:63]),
		.mem_out(lut6_0_sram[0:63]),
		.mem_outb(lut6_SRAM_mem_undriven_mem_outb[0:63]));

endmodule
// ----- END Verilog module for logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6 -----

//----- Default net type -----
// `default_nettype none



