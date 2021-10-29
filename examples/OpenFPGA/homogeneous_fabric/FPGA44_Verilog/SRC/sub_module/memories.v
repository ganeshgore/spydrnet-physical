//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Memories used in FPGA
//	Author: Xifan TANG
//	Organization: University of Utah
//	Date: Thu Oct 28 18:40:07 2021
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size8_mem -----
module mux2_size8_mem(cfg_done,
                      prog_reset,
                      prog_clk,
                      ccff_head,
                      ccff_tail,
                      mem_out,
                      mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:3] mem_out;
//----- OUTPUT PORTS -----
output [0:3] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(CCDFF_0_Q),
		.CFGQN(mem_outb[0]),
		.CFGQ(mem_out[0]));

	CCDFF CCDFF_1_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_0_Q),
		.Q(CCDFF_1_Q),
		.CFGQN(mem_outb[1]),
		.CFGQ(mem_out[1]));

	CCDFF CCDFF_2_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_1_Q),
		.Q(CCDFF_2_Q),
		.CFGQN(mem_outb[2]),
		.CFGQ(mem_out[2]));

	CCDFF CCDFF_3_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_2_Q),
		.Q(ccff_tail),
		.CFGQN(mem_outb[3]),
		.CFGQ(mem_out[3]));

endmodule
// ----- END Verilog module for mux2_size8_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size2_mem -----
module mux2_size2_mem(cfg_done,
                      prog_reset,
                      prog_clk,
                      ccff_head,
                      ccff_tail,
                      mem_out,
                      mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:1] mem_out;
//----- OUTPUT PORTS -----
output [0:1] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(CCDFF_0_Q),
		.CFGQN(mem_outb[0]),
		.CFGQ(mem_out[0]));

	CCDFF CCDFF_1_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_0_Q),
		.Q(ccff_tail),
		.CFGQN(mem_outb[1]),
		.CFGQ(mem_out[1]));

endmodule
// ----- END Verilog module for mux2_size2_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size9_mem -----
module mux2_size9_mem(cfg_done,
                      prog_reset,
                      prog_clk,
                      ccff_head,
                      ccff_tail,
                      mem_out,
                      mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:3] mem_out;
//----- OUTPUT PORTS -----
output [0:3] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(CCDFF_0_Q),
		.CFGQN(mem_outb[0]),
		.CFGQ(mem_out[0]));

	CCDFF CCDFF_1_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_0_Q),
		.Q(CCDFF_1_Q),
		.CFGQN(mem_outb[1]),
		.CFGQ(mem_out[1]));

	CCDFF CCDFF_2_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_1_Q),
		.Q(CCDFF_2_Q),
		.CFGQN(mem_outb[2]),
		.CFGQ(mem_out[2]));

	CCDFF CCDFF_3_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_2_Q),
		.Q(ccff_tail),
		.CFGQN(mem_outb[3]),
		.CFGQ(mem_out[3]));

endmodule
// ----- END Verilog module for mux2_size9_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size12_mem -----
module mux2_size12_mem(cfg_done,
                       prog_reset,
                       prog_clk,
                       ccff_head,
                       ccff_tail,
                       mem_out,
                       mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:3] mem_out;
//----- OUTPUT PORTS -----
output [0:3] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(CCDFF_0_Q),
		.CFGQN(mem_outb[0]),
		.CFGQ(mem_out[0]));

	CCDFF CCDFF_1_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_0_Q),
		.Q(CCDFF_1_Q),
		.CFGQN(mem_outb[1]),
		.CFGQ(mem_out[1]));

	CCDFF CCDFF_2_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_1_Q),
		.Q(CCDFF_2_Q),
		.CFGQN(mem_outb[2]),
		.CFGQ(mem_out[2]));

	CCDFF CCDFF_3_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_2_Q),
		.Q(ccff_tail),
		.CFGQN(mem_outb[3]),
		.CFGQ(mem_out[3]));

endmodule
// ----- END Verilog module for mux2_size12_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size3_mem -----
module mux2_size3_mem(cfg_done,
                      prog_reset,
                      prog_clk,
                      ccff_head,
                      ccff_tail,
                      mem_out,
                      mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:1] mem_out;
//----- OUTPUT PORTS -----
output [0:1] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(CCDFF_0_Q),
		.CFGQN(mem_outb[0]),
		.CFGQ(mem_out[0]));

	CCDFF CCDFF_1_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_0_Q),
		.Q(ccff_tail),
		.CFGQN(mem_outb[1]),
		.CFGQ(mem_out[1]));

endmodule
// ----- END Verilog module for mux2_size3_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size4_mem -----
module mux2_size4_mem(cfg_done,
                      prog_reset,
                      prog_clk,
                      ccff_head,
                      ccff_tail,
                      mem_out,
                      mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:2] mem_out;
//----- OUTPUT PORTS -----
output [0:2] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(CCDFF_0_Q),
		.CFGQN(mem_outb[0]),
		.CFGQ(mem_out[0]));

	CCDFF CCDFF_1_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_0_Q),
		.Q(CCDFF_1_Q),
		.CFGQN(mem_outb[1]),
		.CFGQ(mem_out[1]));

	CCDFF CCDFF_2_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_1_Q),
		.Q(ccff_tail),
		.CFGQN(mem_outb[2]),
		.CFGQ(mem_out[2]));

endmodule
// ----- END Verilog module for mux2_size4_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size10_mem -----
module mux2_size10_mem(cfg_done,
                       prog_reset,
                       prog_clk,
                       ccff_head,
                       ccff_tail,
                       mem_out,
                       mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:3] mem_out;
//----- OUTPUT PORTS -----
output [0:3] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(CCDFF_0_Q),
		.CFGQN(mem_outb[0]),
		.CFGQ(mem_out[0]));

	CCDFF CCDFF_1_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_0_Q),
		.Q(CCDFF_1_Q),
		.CFGQN(mem_outb[1]),
		.CFGQ(mem_out[1]));

	CCDFF CCDFF_2_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_1_Q),
		.Q(CCDFF_2_Q),
		.CFGQN(mem_outb[2]),
		.CFGQ(mem_out[2]));

	CCDFF CCDFF_3_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_2_Q),
		.Q(ccff_tail),
		.CFGQN(mem_outb[3]),
		.CFGQ(mem_out[3]));

endmodule
// ----- END Verilog module for mux2_size10_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size5_mem -----
module mux2_size5_mem(cfg_done,
                      prog_reset,
                      prog_clk,
                      ccff_head,
                      ccff_tail,
                      mem_out,
                      mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:2] mem_out;
//----- OUTPUT PORTS -----
output [0:2] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(CCDFF_0_Q),
		.CFGQN(mem_outb[0]),
		.CFGQ(mem_out[0]));

	CCDFF CCDFF_1_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_0_Q),
		.Q(CCDFF_1_Q),
		.CFGQN(mem_outb[1]),
		.CFGQ(mem_out[1]));

	CCDFF CCDFF_2_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_1_Q),
		.Q(ccff_tail),
		.CFGQN(mem_outb[2]),
		.CFGQ(mem_out[2]));

endmodule
// ----- END Verilog module for mux2_size5_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size50_mem -----
module mux2_size50_mem(cfg_done,
                       prog_reset,
                       prog_clk,
                       ccff_head,
                       ccff_tail,
                       mem_out,
                       mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:5] mem_out;
//----- OUTPUT PORTS -----
output [0:5] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(CCDFF_0_Q),
		.CFGQN(mem_outb[0]),
		.CFGQ(mem_out[0]));

	CCDFF CCDFF_1_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_0_Q),
		.Q(CCDFF_1_Q),
		.CFGQN(mem_outb[1]),
		.CFGQ(mem_out[1]));

	CCDFF CCDFF_2_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_1_Q),
		.Q(CCDFF_2_Q),
		.CFGQN(mem_outb[2]),
		.CFGQ(mem_out[2]));

	CCDFF CCDFF_3_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_2_Q),
		.Q(CCDFF_3_Q),
		.CFGQN(mem_outb[3]),
		.CFGQ(mem_out[3]));

	CCDFF CCDFF_4_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_3_Q),
		.Q(CCDFF_4_Q),
		.CFGQN(mem_outb[4]),
		.CFGQ(mem_out[4]));

	CCDFF CCDFF_5_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_4_Q),
		.Q(ccff_tail),
		.CFGQN(mem_outb[5]),
		.CFGQ(mem_out[5]));

endmodule
// ----- END Verilog module for mux2_size50_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for lut6_CCDFF_mem -----
module lut6_CCDFF_mem(cfg_done,
                      prog_reset,
                      prog_clk,
                      ccff_head,
                      ccff_tail,
                      mem_out,
                      mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:63] mem_out;
//----- OUTPUT PORTS -----
output [0:63] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(CCDFF_0_Q),
		.CFGQN(mem_outb[0]),
		.CFGQ(mem_out[0]));

	CCDFF CCDFF_1_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_0_Q),
		.Q(CCDFF_1_Q),
		.CFGQN(mem_outb[1]),
		.CFGQ(mem_out[1]));

	CCDFF CCDFF_2_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_1_Q),
		.Q(CCDFF_2_Q),
		.CFGQN(mem_outb[2]),
		.CFGQ(mem_out[2]));

	CCDFF CCDFF_3_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_2_Q),
		.Q(CCDFF_3_Q),
		.CFGQN(mem_outb[3]),
		.CFGQ(mem_out[3]));

	CCDFF CCDFF_4_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_3_Q),
		.Q(CCDFF_4_Q),
		.CFGQN(mem_outb[4]),
		.CFGQ(mem_out[4]));

	CCDFF CCDFF_5_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_4_Q),
		.Q(CCDFF_5_Q),
		.CFGQN(mem_outb[5]),
		.CFGQ(mem_out[5]));

	CCDFF CCDFF_6_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_5_Q),
		.Q(CCDFF_6_Q),
		.CFGQN(mem_outb[6]),
		.CFGQ(mem_out[6]));

	CCDFF CCDFF_7_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_6_Q),
		.Q(CCDFF_7_Q),
		.CFGQN(mem_outb[7]),
		.CFGQ(mem_out[7]));

	CCDFF CCDFF_8_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_7_Q),
		.Q(CCDFF_8_Q),
		.CFGQN(mem_outb[8]),
		.CFGQ(mem_out[8]));

	CCDFF CCDFF_9_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_8_Q),
		.Q(CCDFF_9_Q),
		.CFGQN(mem_outb[9]),
		.CFGQ(mem_out[9]));

	CCDFF CCDFF_10_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_9_Q),
		.Q(CCDFF_10_Q),
		.CFGQN(mem_outb[10]),
		.CFGQ(mem_out[10]));

	CCDFF CCDFF_11_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_10_Q),
		.Q(CCDFF_11_Q),
		.CFGQN(mem_outb[11]),
		.CFGQ(mem_out[11]));

	CCDFF CCDFF_12_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_11_Q),
		.Q(CCDFF_12_Q),
		.CFGQN(mem_outb[12]),
		.CFGQ(mem_out[12]));

	CCDFF CCDFF_13_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_12_Q),
		.Q(CCDFF_13_Q),
		.CFGQN(mem_outb[13]),
		.CFGQ(mem_out[13]));

	CCDFF CCDFF_14_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_13_Q),
		.Q(CCDFF_14_Q),
		.CFGQN(mem_outb[14]),
		.CFGQ(mem_out[14]));

	CCDFF CCDFF_15_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_14_Q),
		.Q(CCDFF_15_Q),
		.CFGQN(mem_outb[15]),
		.CFGQ(mem_out[15]));

	CCDFF CCDFF_16_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_15_Q),
		.Q(CCDFF_16_Q),
		.CFGQN(mem_outb[16]),
		.CFGQ(mem_out[16]));

	CCDFF CCDFF_17_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_16_Q),
		.Q(CCDFF_17_Q),
		.CFGQN(mem_outb[17]),
		.CFGQ(mem_out[17]));

	CCDFF CCDFF_18_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_17_Q),
		.Q(CCDFF_18_Q),
		.CFGQN(mem_outb[18]),
		.CFGQ(mem_out[18]));

	CCDFF CCDFF_19_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_18_Q),
		.Q(CCDFF_19_Q),
		.CFGQN(mem_outb[19]),
		.CFGQ(mem_out[19]));

	CCDFF CCDFF_20_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_19_Q),
		.Q(CCDFF_20_Q),
		.CFGQN(mem_outb[20]),
		.CFGQ(mem_out[20]));

	CCDFF CCDFF_21_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_20_Q),
		.Q(CCDFF_21_Q),
		.CFGQN(mem_outb[21]),
		.CFGQ(mem_out[21]));

	CCDFF CCDFF_22_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_21_Q),
		.Q(CCDFF_22_Q),
		.CFGQN(mem_outb[22]),
		.CFGQ(mem_out[22]));

	CCDFF CCDFF_23_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_22_Q),
		.Q(CCDFF_23_Q),
		.CFGQN(mem_outb[23]),
		.CFGQ(mem_out[23]));

	CCDFF CCDFF_24_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_23_Q),
		.Q(CCDFF_24_Q),
		.CFGQN(mem_outb[24]),
		.CFGQ(mem_out[24]));

	CCDFF CCDFF_25_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_24_Q),
		.Q(CCDFF_25_Q),
		.CFGQN(mem_outb[25]),
		.CFGQ(mem_out[25]));

	CCDFF CCDFF_26_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_25_Q),
		.Q(CCDFF_26_Q),
		.CFGQN(mem_outb[26]),
		.CFGQ(mem_out[26]));

	CCDFF CCDFF_27_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_26_Q),
		.Q(CCDFF_27_Q),
		.CFGQN(mem_outb[27]),
		.CFGQ(mem_out[27]));

	CCDFF CCDFF_28_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_27_Q),
		.Q(CCDFF_28_Q),
		.CFGQN(mem_outb[28]),
		.CFGQ(mem_out[28]));

	CCDFF CCDFF_29_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_28_Q),
		.Q(CCDFF_29_Q),
		.CFGQN(mem_outb[29]),
		.CFGQ(mem_out[29]));

	CCDFF CCDFF_30_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_29_Q),
		.Q(CCDFF_30_Q),
		.CFGQN(mem_outb[30]),
		.CFGQ(mem_out[30]));

	CCDFF CCDFF_31_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_30_Q),
		.Q(CCDFF_31_Q),
		.CFGQN(mem_outb[31]),
		.CFGQ(mem_out[31]));

	CCDFF CCDFF_32_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_31_Q),
		.Q(CCDFF_32_Q),
		.CFGQN(mem_outb[32]),
		.CFGQ(mem_out[32]));

	CCDFF CCDFF_33_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_32_Q),
		.Q(CCDFF_33_Q),
		.CFGQN(mem_outb[33]),
		.CFGQ(mem_out[33]));

	CCDFF CCDFF_34_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_33_Q),
		.Q(CCDFF_34_Q),
		.CFGQN(mem_outb[34]),
		.CFGQ(mem_out[34]));

	CCDFF CCDFF_35_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_34_Q),
		.Q(CCDFF_35_Q),
		.CFGQN(mem_outb[35]),
		.CFGQ(mem_out[35]));

	CCDFF CCDFF_36_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_35_Q),
		.Q(CCDFF_36_Q),
		.CFGQN(mem_outb[36]),
		.CFGQ(mem_out[36]));

	CCDFF CCDFF_37_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_36_Q),
		.Q(CCDFF_37_Q),
		.CFGQN(mem_outb[37]),
		.CFGQ(mem_out[37]));

	CCDFF CCDFF_38_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_37_Q),
		.Q(CCDFF_38_Q),
		.CFGQN(mem_outb[38]),
		.CFGQ(mem_out[38]));

	CCDFF CCDFF_39_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_38_Q),
		.Q(CCDFF_39_Q),
		.CFGQN(mem_outb[39]),
		.CFGQ(mem_out[39]));

	CCDFF CCDFF_40_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_39_Q),
		.Q(CCDFF_40_Q),
		.CFGQN(mem_outb[40]),
		.CFGQ(mem_out[40]));

	CCDFF CCDFF_41_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_40_Q),
		.Q(CCDFF_41_Q),
		.CFGQN(mem_outb[41]),
		.CFGQ(mem_out[41]));

	CCDFF CCDFF_42_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_41_Q),
		.Q(CCDFF_42_Q),
		.CFGQN(mem_outb[42]),
		.CFGQ(mem_out[42]));

	CCDFF CCDFF_43_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_42_Q),
		.Q(CCDFF_43_Q),
		.CFGQN(mem_outb[43]),
		.CFGQ(mem_out[43]));

	CCDFF CCDFF_44_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_43_Q),
		.Q(CCDFF_44_Q),
		.CFGQN(mem_outb[44]),
		.CFGQ(mem_out[44]));

	CCDFF CCDFF_45_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_44_Q),
		.Q(CCDFF_45_Q),
		.CFGQN(mem_outb[45]),
		.CFGQ(mem_out[45]));

	CCDFF CCDFF_46_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_45_Q),
		.Q(CCDFF_46_Q),
		.CFGQN(mem_outb[46]),
		.CFGQ(mem_out[46]));

	CCDFF CCDFF_47_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_46_Q),
		.Q(CCDFF_47_Q),
		.CFGQN(mem_outb[47]),
		.CFGQ(mem_out[47]));

	CCDFF CCDFF_48_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_47_Q),
		.Q(CCDFF_48_Q),
		.CFGQN(mem_outb[48]),
		.CFGQ(mem_out[48]));

	CCDFF CCDFF_49_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_48_Q),
		.Q(CCDFF_49_Q),
		.CFGQN(mem_outb[49]),
		.CFGQ(mem_out[49]));

	CCDFF CCDFF_50_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_49_Q),
		.Q(CCDFF_50_Q),
		.CFGQN(mem_outb[50]),
		.CFGQ(mem_out[50]));

	CCDFF CCDFF_51_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_50_Q),
		.Q(CCDFF_51_Q),
		.CFGQN(mem_outb[51]),
		.CFGQ(mem_out[51]));

	CCDFF CCDFF_52_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_51_Q),
		.Q(CCDFF_52_Q),
		.CFGQN(mem_outb[52]),
		.CFGQ(mem_out[52]));

	CCDFF CCDFF_53_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_52_Q),
		.Q(CCDFF_53_Q),
		.CFGQN(mem_outb[53]),
		.CFGQ(mem_out[53]));

	CCDFF CCDFF_54_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_53_Q),
		.Q(CCDFF_54_Q),
		.CFGQN(mem_outb[54]),
		.CFGQ(mem_out[54]));

	CCDFF CCDFF_55_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_54_Q),
		.Q(CCDFF_55_Q),
		.CFGQN(mem_outb[55]),
		.CFGQ(mem_out[55]));

	CCDFF CCDFF_56_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_55_Q),
		.Q(CCDFF_56_Q),
		.CFGQN(mem_outb[56]),
		.CFGQ(mem_out[56]));

	CCDFF CCDFF_57_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_56_Q),
		.Q(CCDFF_57_Q),
		.CFGQN(mem_outb[57]),
		.CFGQ(mem_out[57]));

	CCDFF CCDFF_58_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_57_Q),
		.Q(CCDFF_58_Q),
		.CFGQN(mem_outb[58]),
		.CFGQ(mem_out[58]));

	CCDFF CCDFF_59_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_58_Q),
		.Q(CCDFF_59_Q),
		.CFGQN(mem_outb[59]),
		.CFGQ(mem_out[59]));

	CCDFF CCDFF_60_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_59_Q),
		.Q(CCDFF_60_Q),
		.CFGQN(mem_outb[60]),
		.CFGQ(mem_out[60]));

	CCDFF CCDFF_61_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_60_Q),
		.Q(CCDFF_61_Q),
		.CFGQN(mem_outb[61]),
		.CFGQ(mem_out[61]));

	CCDFF CCDFF_62_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_61_Q),
		.Q(CCDFF_62_Q),
		.CFGQN(mem_outb[62]),
		.CFGQ(mem_out[62]));

	CCDFF CCDFF_63_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(CCDFF_62_Q),
		.Q(ccff_tail),
		.CFGQN(mem_outb[63]),
		.CFGQ(mem_out[63]));

endmodule
// ----- END Verilog module for lut6_CCDFF_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for GPIO_CCDFF_mem -----
module GPIO_CCDFF_mem(cfg_done,
                      prog_reset,
                      prog_clk,
                      ccff_head,
                      ccff_tail,
                      mem_out,
                      mem_outb);
//----- GLOBAL PORTS -----
input [0:0] cfg_done;
//----- GLOBAL PORTS -----
input [0:0] prog_reset;
//----- GLOBAL PORTS -----
input [0:0] prog_clk;
//----- INPUT PORTS -----
input [0:0] ccff_head;
//----- OUTPUT PORTS -----
output [0:0] ccff_tail;
//----- OUTPUT PORTS -----
output [0:0] mem_out;
//----- OUTPUT PORTS -----
output [0:0] mem_outb;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	CCDFF CCDFF_0_ (
		.CFGE(cfg_done),
		.RESET_B(prog_reset),
		.CLK(prog_clk),
		.D(ccff_head),
		.Q(ccff_tail),
		.CFGQN(mem_outb),
		.CFGQ(mem_out));

endmodule
// ----- END Verilog module for GPIO_CCDFF_mem -----

//----- Default net type -----
// `default_nettype none




