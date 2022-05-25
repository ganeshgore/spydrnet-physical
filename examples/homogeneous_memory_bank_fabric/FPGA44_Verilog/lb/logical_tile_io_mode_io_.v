//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for pb_type: io
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

// ----- BEGIN Physical programmable logic block Verilog module: io -----
//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for logical_tile_io_mode_io_ -----
module logical_tile_io_mode_io_(gfpga_pad_GPIO_PAD,
                                io_outpad,
                                bl,
                                wl,
                                io_inpad);
//----- GPIO PORTS -----
inout [0:0] gfpga_pad_GPIO_PAD;
//----- INPUT PORTS -----
input [0:0] io_outpad;
//----- INPUT PORTS -----
input [0:0] bl;
//----- INPUT PORTS -----
input [0:0] wl;
//----- OUTPUT PORTS -----
output [0:0] io_inpad;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	logical_tile_io_mode_physical__iopad logical_tile_io_mode_physical__iopad_0 (
		.gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD),
		.iopad_outpad(direct_interc_1_out),
		.bl(bl),
		.wl(wl),
		.iopad_inpad(logical_tile_io_mode_physical__iopad_0_iopad_inpad));

	direct_interc direct_interc_0_ (
		.in(logical_tile_io_mode_physical__iopad_0_iopad_inpad),
		.out(io_inpad));

	direct_interc direct_interc_1_ (
		.in(io_outpad),
		.out(direct_interc_1_out));

endmodule
// ----- END Verilog module for logical_tile_io_mode_io_ -----

//----- Default net type -----
// `default_nettype none



// ----- END Physical programmable logic block Verilog module: io -----
