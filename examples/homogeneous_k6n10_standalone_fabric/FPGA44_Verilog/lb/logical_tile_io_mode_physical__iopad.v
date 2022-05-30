//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Verilog modules for primitive pb_type: iopad
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for logical_tile_io_mode_physical__iopad -----
module logical_tile_io_mode_physical__iopad(gfpga_pad_GPIO_PAD,
                                            iopad_outpad,
                                            bl,
                                            wl,
                                            iopad_inpad);
//----- GPIO PORTS -----
inout [0:0] gfpga_pad_GPIO_PAD;
//----- INPUT PORTS -----
input [0:0] iopad_outpad;
//----- INPUT PORTS -----
input [0:0] bl;
//----- INPUT PORTS -----
input [0:0] wl;
//----- OUTPUT PORTS -----
output [0:0] iopad_inpad;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	GPIO GPIO_0_ (
		.PAD(gfpga_pad_GPIO_PAD),
		.outpad(iopad_outpad),
		.DIR(GPIO_0_DIR),
		.inpad(iopad_inpad));

	GPIO_SRAM_mem GPIO_SRAM_mem (
		.bl(bl),
		.wl(wl),
		.mem_out(GPIO_0_DIR),
		.mem_outb(GPIO_SRAM_mem_undriven_mem_outb));

endmodule
// ----- END Verilog module for logical_tile_io_mode_physical__iopad -----

//----- Default net type -----
// `default_nettype none



