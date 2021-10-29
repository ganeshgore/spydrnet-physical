//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Multiplexers
//	Author: Xifan TANG
//	Organization: University of Utah
//	Date: Thu Oct 28 18:40:07 2021
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size8 -----
module mux2_size8(in,
                  sram,
                  sram_inv,
                  out);
//----- INPUT PORTS -----
input [0:7] in;
//----- INPUT PORTS -----
input [0:3] sram;
//----- INPUT PORTS -----
input [0:3] sram_inv;
//----- OUTPUT PORTS -----
output [0:0] out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	const1 const1_0_ (
		.const1(const1_0_const1));

	BUF_X1 BUF_X1_0_ (
		.A(MUX2_X1_7_Y),
		.Y(out));

	MUX2_X1 mux_l1_in_0_ (
		.A0(in[0]),
		.A1(in[1]),
		.S(sram[0]),
		.Y(MUX2_X1_0_Y));

	MUX2_X1 mux_l2_in_0_ (
		.A0(MUX2_X1_0_Y),
		.A1(in[2]),
		.S(sram[1]),
		.Y(MUX2_X1_1_Y));

	MUX2_X1 mux_l2_in_1_ (
		.A0(in[3]),
		.A1(in[4]),
		.S(sram[1]),
		.Y(MUX2_X1_2_Y));

	MUX2_X1 mux_l2_in_2_ (
		.A0(in[5]),
		.A1(in[6]),
		.S(sram[1]),
		.Y(MUX2_X1_3_Y));

	MUX2_X1 mux_l2_in_3_ (
		.A0(in[7]),
		.A1(const1_0_const1),
		.S(sram[1]),
		.Y(MUX2_X1_4_Y));

	MUX2_X1 mux_l3_in_0_ (
		.A0(MUX2_X1_1_Y),
		.A1(MUX2_X1_2_Y),
		.S(sram[2]),
		.Y(MUX2_X1_5_Y));

	MUX2_X1 mux_l3_in_1_ (
		.A0(MUX2_X1_3_Y),
		.A1(MUX2_X1_4_Y),
		.S(sram[2]),
		.Y(MUX2_X1_6_Y));

	MUX2_X1 mux_l4_in_0_ (
		.A0(MUX2_X1_5_Y),
		.A1(MUX2_X1_6_Y),
		.S(sram[3]),
		.Y(MUX2_X1_7_Y));

endmodule
// ----- END Verilog module for mux2_size8 -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size2 -----
module mux2_size2(in,
                  sram,
                  sram_inv,
                  out);
//----- INPUT PORTS -----
input [0:1] in;
//----- INPUT PORTS -----
input [0:1] sram;
//----- INPUT PORTS -----
input [0:1] sram_inv;
//----- OUTPUT PORTS -----
output [0:0] out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	const1 const1_0_ (
		.const1(const1_0_const1));

	BUF_X1 BUF_X1_0_ (
		.A(MUX2_X1_1_Y),
		.Y(out));

	MUX2_X1 mux_l1_in_0_ (
		.A0(in[0]),
		.A1(in[1]),
		.S(sram[0]),
		.Y(MUX2_X1_0_Y));

	MUX2_X1 mux_l2_in_0_ (
		.A0(MUX2_X1_0_Y),
		.A1(const1_0_const1),
		.S(sram[1]),
		.Y(MUX2_X1_1_Y));

endmodule
// ----- END Verilog module for mux2_size2 -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size9 -----
module mux2_size9(in,
                  sram,
                  sram_inv,
                  out);
//----- INPUT PORTS -----
input [0:8] in;
//----- INPUT PORTS -----
input [0:3] sram;
//----- INPUT PORTS -----
input [0:3] sram_inv;
//----- OUTPUT PORTS -----
output [0:0] out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	const1 const1_0_ (
		.const1(const1_0_const1));

	BUF_X1 BUF_X1_0_ (
		.A(MUX2_X1_8_Y),
		.Y(out));

	MUX2_X1 mux_l1_in_0_ (
		.A0(in[0]),
		.A1(in[1]),
		.S(sram[0]),
		.Y(MUX2_X1_0_Y));

	MUX2_X1 mux_l1_in_1_ (
		.A0(in[2]),
		.A1(in[3]),
		.S(sram[0]),
		.Y(MUX2_X1_1_Y));

	MUX2_X1 mux_l2_in_0_ (
		.A0(MUX2_X1_0_Y),
		.A1(MUX2_X1_1_Y),
		.S(sram[1]),
		.Y(MUX2_X1_2_Y));

	MUX2_X1 mux_l2_in_1_ (
		.A0(in[4]),
		.A1(in[5]),
		.S(sram[1]),
		.Y(MUX2_X1_3_Y));

	MUX2_X1 mux_l2_in_2_ (
		.A0(in[6]),
		.A1(in[7]),
		.S(sram[1]),
		.Y(MUX2_X1_4_Y));

	MUX2_X1 mux_l2_in_3_ (
		.A0(in[8]),
		.A1(const1_0_const1),
		.S(sram[1]),
		.Y(MUX2_X1_5_Y));

	MUX2_X1 mux_l3_in_0_ (
		.A0(MUX2_X1_2_Y),
		.A1(MUX2_X1_3_Y),
		.S(sram[2]),
		.Y(MUX2_X1_6_Y));

	MUX2_X1 mux_l3_in_1_ (
		.A0(MUX2_X1_4_Y),
		.A1(MUX2_X1_5_Y),
		.S(sram[2]),
		.Y(MUX2_X1_7_Y));

	MUX2_X1 mux_l4_in_0_ (
		.A0(MUX2_X1_6_Y),
		.A1(MUX2_X1_7_Y),
		.S(sram[3]),
		.Y(MUX2_X1_8_Y));

endmodule
// ----- END Verilog module for mux2_size9 -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size12 -----
module mux2_size12(in,
                   sram,
                   sram_inv,
                   out);
//----- INPUT PORTS -----
input [0:11] in;
//----- INPUT PORTS -----
input [0:3] sram;
//----- INPUT PORTS -----
input [0:3] sram_inv;
//----- OUTPUT PORTS -----
output [0:0] out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	const1 const1_0_ (
		.const1(const1_0_const1));

	BUF_X1 BUF_X1_0_ (
		.A(MUX2_X1_11_Y),
		.Y(out));

	MUX2_X1 mux_l1_in_0_ (
		.A0(in[0]),
		.A1(in[1]),
		.S(sram[0]),
		.Y(MUX2_X1_0_Y));

	MUX2_X1 mux_l1_in_1_ (
		.A0(in[2]),
		.A1(in[3]),
		.S(sram[0]),
		.Y(MUX2_X1_1_Y));

	MUX2_X1 mux_l1_in_2_ (
		.A0(in[4]),
		.A1(in[5]),
		.S(sram[0]),
		.Y(MUX2_X1_2_Y));

	MUX2_X1 mux_l1_in_3_ (
		.A0(in[6]),
		.A1(in[7]),
		.S(sram[0]),
		.Y(MUX2_X1_3_Y));

	MUX2_X1 mux_l1_in_4_ (
		.A0(in[8]),
		.A1(in[9]),
		.S(sram[0]),
		.Y(MUX2_X1_4_Y));

	MUX2_X1 mux_l2_in_0_ (
		.A0(MUX2_X1_0_Y),
		.A1(MUX2_X1_1_Y),
		.S(sram[1]),
		.Y(MUX2_X1_5_Y));

	MUX2_X1 mux_l2_in_1_ (
		.A0(MUX2_X1_2_Y),
		.A1(MUX2_X1_3_Y),
		.S(sram[1]),
		.Y(MUX2_X1_6_Y));

	MUX2_X1 mux_l2_in_2_ (
		.A0(MUX2_X1_4_Y),
		.A1(in[10]),
		.S(sram[1]),
		.Y(MUX2_X1_7_Y));

	MUX2_X1 mux_l2_in_3_ (
		.A0(in[11]),
		.A1(const1_0_const1),
		.S(sram[1]),
		.Y(MUX2_X1_8_Y));

	MUX2_X1 mux_l3_in_0_ (
		.A0(MUX2_X1_5_Y),
		.A1(MUX2_X1_6_Y),
		.S(sram[2]),
		.Y(MUX2_X1_9_Y));

	MUX2_X1 mux_l3_in_1_ (
		.A0(MUX2_X1_7_Y),
		.A1(MUX2_X1_8_Y),
		.S(sram[2]),
		.Y(MUX2_X1_10_Y));

	MUX2_X1 mux_l4_in_0_ (
		.A0(MUX2_X1_9_Y),
		.A1(MUX2_X1_10_Y),
		.S(sram[3]),
		.Y(MUX2_X1_11_Y));

endmodule
// ----- END Verilog module for mux2_size12 -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size3 -----
module mux2_size3(in,
                  sram,
                  sram_inv,
                  out);
//----- INPUT PORTS -----
input [0:2] in;
//----- INPUT PORTS -----
input [0:1] sram;
//----- INPUT PORTS -----
input [0:1] sram_inv;
//----- OUTPUT PORTS -----
output [0:0] out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	const1 const1_0_ (
		.const1(const1_0_const1));

	BUF_X1 BUF_X1_0_ (
		.A(MUX2_X1_2_Y),
		.Y(out));

	MUX2_X1 mux_l1_in_0_ (
		.A0(in[0]),
		.A1(in[1]),
		.S(sram[0]),
		.Y(MUX2_X1_0_Y));

	MUX2_X1 mux_l1_in_1_ (
		.A0(in[2]),
		.A1(const1_0_const1),
		.S(sram[0]),
		.Y(MUX2_X1_1_Y));

	MUX2_X1 mux_l2_in_0_ (
		.A0(MUX2_X1_0_Y),
		.A1(MUX2_X1_1_Y),
		.S(sram[1]),
		.Y(MUX2_X1_2_Y));

endmodule
// ----- END Verilog module for mux2_size3 -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size4 -----
module mux2_size4(in,
                  sram,
                  sram_inv,
                  out);
//----- INPUT PORTS -----
input [0:3] in;
//----- INPUT PORTS -----
input [0:2] sram;
//----- INPUT PORTS -----
input [0:2] sram_inv;
//----- OUTPUT PORTS -----
output [0:0] out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	const1 const1_0_ (
		.const1(const1_0_const1));

	BUF_X1 BUF_X1_0_ (
		.A(MUX2_X1_3_Y),
		.Y(out));

	MUX2_X1 mux_l1_in_0_ (
		.A0(in[0]),
		.A1(in[1]),
		.S(sram[0]),
		.Y(MUX2_X1_0_Y));

	MUX2_X1 mux_l2_in_0_ (
		.A0(MUX2_X1_0_Y),
		.A1(in[2]),
		.S(sram[1]),
		.Y(MUX2_X1_1_Y));

	MUX2_X1 mux_l2_in_1_ (
		.A0(in[3]),
		.A1(const1_0_const1),
		.S(sram[1]),
		.Y(MUX2_X1_2_Y));

	MUX2_X1 mux_l3_in_0_ (
		.A0(MUX2_X1_1_Y),
		.A1(MUX2_X1_2_Y),
		.S(sram[2]),
		.Y(MUX2_X1_3_Y));

endmodule
// ----- END Verilog module for mux2_size4 -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size10 -----
module mux2_size10(in,
                   sram,
                   sram_inv,
                   out);
//----- INPUT PORTS -----
input [0:9] in;
//----- INPUT PORTS -----
input [0:3] sram;
//----- INPUT PORTS -----
input [0:3] sram_inv;
//----- OUTPUT PORTS -----
output [0:0] out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	const1 const1_0_ (
		.const1(const1_0_const1));

	BUF_X1 BUF_X1_0_ (
		.A(MUX2_X1_9_Y),
		.Y(out));

	MUX2_X1 mux_l1_in_0_ (
		.A0(in[0]),
		.A1(in[1]),
		.S(sram[0]),
		.Y(MUX2_X1_0_Y));

	MUX2_X1 mux_l1_in_1_ (
		.A0(in[2]),
		.A1(in[3]),
		.S(sram[0]),
		.Y(MUX2_X1_1_Y));

	MUX2_X1 mux_l1_in_2_ (
		.A0(in[4]),
		.A1(in[5]),
		.S(sram[0]),
		.Y(MUX2_X1_2_Y));

	MUX2_X1 mux_l2_in_0_ (
		.A0(MUX2_X1_0_Y),
		.A1(MUX2_X1_1_Y),
		.S(sram[1]),
		.Y(MUX2_X1_3_Y));

	MUX2_X1 mux_l2_in_1_ (
		.A0(MUX2_X1_2_Y),
		.A1(in[6]),
		.S(sram[1]),
		.Y(MUX2_X1_4_Y));

	MUX2_X1 mux_l2_in_2_ (
		.A0(in[7]),
		.A1(in[8]),
		.S(sram[1]),
		.Y(MUX2_X1_5_Y));

	MUX2_X1 mux_l2_in_3_ (
		.A0(in[9]),
		.A1(const1_0_const1),
		.S(sram[1]),
		.Y(MUX2_X1_6_Y));

	MUX2_X1 mux_l3_in_0_ (
		.A0(MUX2_X1_3_Y),
		.A1(MUX2_X1_4_Y),
		.S(sram[2]),
		.Y(MUX2_X1_7_Y));

	MUX2_X1 mux_l3_in_1_ (
		.A0(MUX2_X1_5_Y),
		.A1(MUX2_X1_6_Y),
		.S(sram[2]),
		.Y(MUX2_X1_8_Y));

	MUX2_X1 mux_l4_in_0_ (
		.A0(MUX2_X1_7_Y),
		.A1(MUX2_X1_8_Y),
		.S(sram[3]),
		.Y(MUX2_X1_9_Y));

endmodule
// ----- END Verilog module for mux2_size10 -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size5 -----
module mux2_size5(in,
                  sram,
                  sram_inv,
                  out);
//----- INPUT PORTS -----
input [0:4] in;
//----- INPUT PORTS -----
input [0:2] sram;
//----- INPUT PORTS -----
input [0:2] sram_inv;
//----- OUTPUT PORTS -----
output [0:0] out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	const1 const1_0_ (
		.const1(const1_0_const1));

	BUF_X1 BUF_X1_0_ (
		.A(MUX2_X1_4_Y),
		.Y(out));

	MUX2_X1 mux_l1_in_0_ (
		.A0(in[0]),
		.A1(in[1]),
		.S(sram[0]),
		.Y(MUX2_X1_0_Y));

	MUX2_X1 mux_l1_in_1_ (
		.A0(in[2]),
		.A1(in[3]),
		.S(sram[0]),
		.Y(MUX2_X1_1_Y));

	MUX2_X1 mux_l2_in_0_ (
		.A0(MUX2_X1_0_Y),
		.A1(MUX2_X1_1_Y),
		.S(sram[1]),
		.Y(MUX2_X1_2_Y));

	MUX2_X1 mux_l2_in_1_ (
		.A0(in[4]),
		.A1(const1_0_const1),
		.S(sram[1]),
		.Y(MUX2_X1_3_Y));

	MUX2_X1 mux_l3_in_0_ (
		.A0(MUX2_X1_2_Y),
		.A1(MUX2_X1_3_Y),
		.S(sram[2]),
		.Y(MUX2_X1_4_Y));

endmodule
// ----- END Verilog module for mux2_size5 -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size50 -----
module mux2_size50(in,
                   sram,
                   sram_inv,
                   out);
//----- INPUT PORTS -----
input [0:49] in;
//----- INPUT PORTS -----
input [0:5] sram;
//----- INPUT PORTS -----
input [0:5] sram_inv;
//----- OUTPUT PORTS -----
output [0:0] out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	const1 const1_0_ (
		.const1(const1_0_const1));

	BUF_X1 BUF_X1_0_ (
		.A(MUX2_X1_49_Y),
		.Y(out));

	MUX2_X1 mux_l1_in_0_ (
		.A0(in[0]),
		.A1(in[1]),
		.S(sram[0]),
		.Y(MUX2_X1_0_Y));

	MUX2_X1 mux_l1_in_1_ (
		.A0(in[2]),
		.A1(in[3]),
		.S(sram[0]),
		.Y(MUX2_X1_1_Y));

	MUX2_X1 mux_l1_in_2_ (
		.A0(in[4]),
		.A1(in[5]),
		.S(sram[0]),
		.Y(MUX2_X1_2_Y));

	MUX2_X1 mux_l1_in_3_ (
		.A0(in[6]),
		.A1(in[7]),
		.S(sram[0]),
		.Y(MUX2_X1_3_Y));

	MUX2_X1 mux_l1_in_4_ (
		.A0(in[8]),
		.A1(in[9]),
		.S(sram[0]),
		.Y(MUX2_X1_4_Y));

	MUX2_X1 mux_l1_in_5_ (
		.A0(in[10]),
		.A1(in[11]),
		.S(sram[0]),
		.Y(MUX2_X1_5_Y));

	MUX2_X1 mux_l1_in_6_ (
		.A0(in[12]),
		.A1(in[13]),
		.S(sram[0]),
		.Y(MUX2_X1_6_Y));

	MUX2_X1 mux_l1_in_7_ (
		.A0(in[14]),
		.A1(in[15]),
		.S(sram[0]),
		.Y(MUX2_X1_7_Y));

	MUX2_X1 mux_l1_in_8_ (
		.A0(in[16]),
		.A1(in[17]),
		.S(sram[0]),
		.Y(MUX2_X1_8_Y));

	MUX2_X1 mux_l1_in_9_ (
		.A0(in[18]),
		.A1(in[19]),
		.S(sram[0]),
		.Y(MUX2_X1_9_Y));

	MUX2_X1 mux_l1_in_10_ (
		.A0(in[20]),
		.A1(in[21]),
		.S(sram[0]),
		.Y(MUX2_X1_10_Y));

	MUX2_X1 mux_l1_in_11_ (
		.A0(in[22]),
		.A1(in[23]),
		.S(sram[0]),
		.Y(MUX2_X1_11_Y));

	MUX2_X1 mux_l1_in_12_ (
		.A0(in[24]),
		.A1(in[25]),
		.S(sram[0]),
		.Y(MUX2_X1_12_Y));

	MUX2_X1 mux_l1_in_13_ (
		.A0(in[26]),
		.A1(in[27]),
		.S(sram[0]),
		.Y(MUX2_X1_13_Y));

	MUX2_X1 mux_l1_in_14_ (
		.A0(in[28]),
		.A1(in[29]),
		.S(sram[0]),
		.Y(MUX2_X1_14_Y));

	MUX2_X1 mux_l1_in_15_ (
		.A0(in[30]),
		.A1(in[31]),
		.S(sram[0]),
		.Y(MUX2_X1_15_Y));

	MUX2_X1 mux_l1_in_16_ (
		.A0(in[32]),
		.A1(in[33]),
		.S(sram[0]),
		.Y(MUX2_X1_16_Y));

	MUX2_X1 mux_l1_in_17_ (
		.A0(in[34]),
		.A1(in[35]),
		.S(sram[0]),
		.Y(MUX2_X1_17_Y));

	MUX2_X1 mux_l1_in_18_ (
		.A0(in[36]),
		.A1(in[37]),
		.S(sram[0]),
		.Y(MUX2_X1_18_Y));

	MUX2_X1 mux_l2_in_0_ (
		.A0(MUX2_X1_0_Y),
		.A1(MUX2_X1_1_Y),
		.S(sram[1]),
		.Y(MUX2_X1_19_Y));

	MUX2_X1 mux_l2_in_1_ (
		.A0(MUX2_X1_2_Y),
		.A1(MUX2_X1_3_Y),
		.S(sram[1]),
		.Y(MUX2_X1_20_Y));

	MUX2_X1 mux_l2_in_2_ (
		.A0(MUX2_X1_4_Y),
		.A1(MUX2_X1_5_Y),
		.S(sram[1]),
		.Y(MUX2_X1_21_Y));

	MUX2_X1 mux_l2_in_3_ (
		.A0(MUX2_X1_6_Y),
		.A1(MUX2_X1_7_Y),
		.S(sram[1]),
		.Y(MUX2_X1_22_Y));

	MUX2_X1 mux_l2_in_4_ (
		.A0(MUX2_X1_8_Y),
		.A1(MUX2_X1_9_Y),
		.S(sram[1]),
		.Y(MUX2_X1_23_Y));

	MUX2_X1 mux_l2_in_5_ (
		.A0(MUX2_X1_10_Y),
		.A1(MUX2_X1_11_Y),
		.S(sram[1]),
		.Y(MUX2_X1_24_Y));

	MUX2_X1 mux_l2_in_6_ (
		.A0(MUX2_X1_12_Y),
		.A1(MUX2_X1_13_Y),
		.S(sram[1]),
		.Y(MUX2_X1_25_Y));

	MUX2_X1 mux_l2_in_7_ (
		.A0(MUX2_X1_14_Y),
		.A1(MUX2_X1_15_Y),
		.S(sram[1]),
		.Y(MUX2_X1_26_Y));

	MUX2_X1 mux_l2_in_8_ (
		.A0(MUX2_X1_16_Y),
		.A1(MUX2_X1_17_Y),
		.S(sram[1]),
		.Y(MUX2_X1_27_Y));

	MUX2_X1 mux_l2_in_9_ (
		.A0(MUX2_X1_18_Y),
		.A1(in[38]),
		.S(sram[1]),
		.Y(MUX2_X1_28_Y));

	MUX2_X1 mux_l2_in_10_ (
		.A0(in[39]),
		.A1(in[40]),
		.S(sram[1]),
		.Y(MUX2_X1_29_Y));

	MUX2_X1 mux_l2_in_11_ (
		.A0(in[41]),
		.A1(in[42]),
		.S(sram[1]),
		.Y(MUX2_X1_30_Y));

	MUX2_X1 mux_l2_in_12_ (
		.A0(in[43]),
		.A1(in[44]),
		.S(sram[1]),
		.Y(MUX2_X1_31_Y));

	MUX2_X1 mux_l2_in_13_ (
		.A0(in[45]),
		.A1(in[46]),
		.S(sram[1]),
		.Y(MUX2_X1_32_Y));

	MUX2_X1 mux_l2_in_14_ (
		.A0(in[47]),
		.A1(in[48]),
		.S(sram[1]),
		.Y(MUX2_X1_33_Y));

	MUX2_X1 mux_l2_in_15_ (
		.A0(in[49]),
		.A1(const1_0_const1),
		.S(sram[1]),
		.Y(MUX2_X1_34_Y));

	MUX2_X1 mux_l3_in_0_ (
		.A0(MUX2_X1_19_Y),
		.A1(MUX2_X1_20_Y),
		.S(sram[2]),
		.Y(MUX2_X1_35_Y));

	MUX2_X1 mux_l3_in_1_ (
		.A0(MUX2_X1_21_Y),
		.A1(MUX2_X1_22_Y),
		.S(sram[2]),
		.Y(MUX2_X1_36_Y));

	MUX2_X1 mux_l3_in_2_ (
		.A0(MUX2_X1_23_Y),
		.A1(MUX2_X1_24_Y),
		.S(sram[2]),
		.Y(MUX2_X1_37_Y));

	MUX2_X1 mux_l3_in_3_ (
		.A0(MUX2_X1_25_Y),
		.A1(MUX2_X1_26_Y),
		.S(sram[2]),
		.Y(MUX2_X1_38_Y));

	MUX2_X1 mux_l3_in_4_ (
		.A0(MUX2_X1_27_Y),
		.A1(MUX2_X1_28_Y),
		.S(sram[2]),
		.Y(MUX2_X1_39_Y));

	MUX2_X1 mux_l3_in_5_ (
		.A0(MUX2_X1_29_Y),
		.A1(MUX2_X1_30_Y),
		.S(sram[2]),
		.Y(MUX2_X1_40_Y));

	MUX2_X1 mux_l3_in_6_ (
		.A0(MUX2_X1_31_Y),
		.A1(MUX2_X1_32_Y),
		.S(sram[2]),
		.Y(MUX2_X1_41_Y));

	MUX2_X1 mux_l3_in_7_ (
		.A0(MUX2_X1_33_Y),
		.A1(MUX2_X1_34_Y),
		.S(sram[2]),
		.Y(MUX2_X1_42_Y));

	MUX2_X1 mux_l4_in_0_ (
		.A0(MUX2_X1_35_Y),
		.A1(MUX2_X1_36_Y),
		.S(sram[3]),
		.Y(MUX2_X1_43_Y));

	MUX2_X1 mux_l4_in_1_ (
		.A0(MUX2_X1_37_Y),
		.A1(MUX2_X1_38_Y),
		.S(sram[3]),
		.Y(MUX2_X1_44_Y));

	MUX2_X1 mux_l4_in_2_ (
		.A0(MUX2_X1_39_Y),
		.A1(MUX2_X1_40_Y),
		.S(sram[3]),
		.Y(MUX2_X1_45_Y));

	MUX2_X1 mux_l4_in_3_ (
		.A0(MUX2_X1_41_Y),
		.A1(MUX2_X1_42_Y),
		.S(sram[3]),
		.Y(MUX2_X1_46_Y));

	MUX2_X1 mux_l5_in_0_ (
		.A0(MUX2_X1_43_Y),
		.A1(MUX2_X1_44_Y),
		.S(sram[4]),
		.Y(MUX2_X1_47_Y));

	MUX2_X1 mux_l5_in_1_ (
		.A0(MUX2_X1_45_Y),
		.A1(MUX2_X1_46_Y),
		.S(sram[4]),
		.Y(MUX2_X1_48_Y));

	MUX2_X1 mux_l6_in_0_ (
		.A0(MUX2_X1_47_Y),
		.A1(MUX2_X1_48_Y),
		.S(sram[5]),
		.Y(MUX2_X1_49_Y));

endmodule
// ----- END Verilog module for mux2_size50 -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for lut6_mux -----
module lut6_mux(in,
                sram,
                sram_inv,
                out);
//----- INPUT PORTS -----
input [0:63] in;
//----- INPUT PORTS -----
input [0:5] sram;
//----- INPUT PORTS -----
input [0:5] sram_inv;
//----- OUTPUT PORTS -----
output [0:0] out;

//----- BEGIN Registered ports -----
//----- END Registered ports -----



// ----- BEGIN Local short connections -----
// ----- END Local short connections -----
// ----- BEGIN Local output short connections -----
// ----- END Local output short connections -----

	MUX2_X1 mux_l1_in_0_ (
		.A0(in[0]),
		.A1(in[1]),
		.S(sram[0]),
		.Y(MUX2_X1_0_Y));

	MUX2_X1 mux_l1_in_1_ (
		.A0(in[2]),
		.A1(in[3]),
		.S(sram[0]),
		.Y(MUX2_X1_1_Y));

	MUX2_X1 mux_l1_in_2_ (
		.A0(in[4]),
		.A1(in[5]),
		.S(sram[0]),
		.Y(MUX2_X1_2_Y));

	MUX2_X1 mux_l1_in_3_ (
		.A0(in[6]),
		.A1(in[7]),
		.S(sram[0]),
		.Y(MUX2_X1_3_Y));

	MUX2_X1 mux_l1_in_4_ (
		.A0(in[8]),
		.A1(in[9]),
		.S(sram[0]),
		.Y(MUX2_X1_4_Y));

	MUX2_X1 mux_l1_in_5_ (
		.A0(in[10]),
		.A1(in[11]),
		.S(sram[0]),
		.Y(MUX2_X1_5_Y));

	MUX2_X1 mux_l1_in_6_ (
		.A0(in[12]),
		.A1(in[13]),
		.S(sram[0]),
		.Y(MUX2_X1_6_Y));

	MUX2_X1 mux_l1_in_7_ (
		.A0(in[14]),
		.A1(in[15]),
		.S(sram[0]),
		.Y(MUX2_X1_7_Y));

	MUX2_X1 mux_l1_in_8_ (
		.A0(in[16]),
		.A1(in[17]),
		.S(sram[0]),
		.Y(MUX2_X1_8_Y));

	MUX2_X1 mux_l1_in_9_ (
		.A0(in[18]),
		.A1(in[19]),
		.S(sram[0]),
		.Y(MUX2_X1_9_Y));

	MUX2_X1 mux_l1_in_10_ (
		.A0(in[20]),
		.A1(in[21]),
		.S(sram[0]),
		.Y(MUX2_X1_10_Y));

	MUX2_X1 mux_l1_in_11_ (
		.A0(in[22]),
		.A1(in[23]),
		.S(sram[0]),
		.Y(MUX2_X1_11_Y));

	MUX2_X1 mux_l1_in_12_ (
		.A0(in[24]),
		.A1(in[25]),
		.S(sram[0]),
		.Y(MUX2_X1_12_Y));

	MUX2_X1 mux_l1_in_13_ (
		.A0(in[26]),
		.A1(in[27]),
		.S(sram[0]),
		.Y(MUX2_X1_13_Y));

	MUX2_X1 mux_l1_in_14_ (
		.A0(in[28]),
		.A1(in[29]),
		.S(sram[0]),
		.Y(MUX2_X1_14_Y));

	MUX2_X1 mux_l1_in_15_ (
		.A0(in[30]),
		.A1(in[31]),
		.S(sram[0]),
		.Y(MUX2_X1_15_Y));

	MUX2_X1 mux_l1_in_16_ (
		.A0(in[32]),
		.A1(in[33]),
		.S(sram[0]),
		.Y(MUX2_X1_16_Y));

	MUX2_X1 mux_l1_in_17_ (
		.A0(in[34]),
		.A1(in[35]),
		.S(sram[0]),
		.Y(MUX2_X1_17_Y));

	MUX2_X1 mux_l1_in_18_ (
		.A0(in[36]),
		.A1(in[37]),
		.S(sram[0]),
		.Y(MUX2_X1_18_Y));

	MUX2_X1 mux_l1_in_19_ (
		.A0(in[38]),
		.A1(in[39]),
		.S(sram[0]),
		.Y(MUX2_X1_19_Y));

	MUX2_X1 mux_l1_in_20_ (
		.A0(in[40]),
		.A1(in[41]),
		.S(sram[0]),
		.Y(MUX2_X1_20_Y));

	MUX2_X1 mux_l1_in_21_ (
		.A0(in[42]),
		.A1(in[43]),
		.S(sram[0]),
		.Y(MUX2_X1_21_Y));

	MUX2_X1 mux_l1_in_22_ (
		.A0(in[44]),
		.A1(in[45]),
		.S(sram[0]),
		.Y(MUX2_X1_22_Y));

	MUX2_X1 mux_l1_in_23_ (
		.A0(in[46]),
		.A1(in[47]),
		.S(sram[0]),
		.Y(MUX2_X1_23_Y));

	MUX2_X1 mux_l1_in_24_ (
		.A0(in[48]),
		.A1(in[49]),
		.S(sram[0]),
		.Y(MUX2_X1_24_Y));

	MUX2_X1 mux_l1_in_25_ (
		.A0(in[50]),
		.A1(in[51]),
		.S(sram[0]),
		.Y(MUX2_X1_25_Y));

	MUX2_X1 mux_l1_in_26_ (
		.A0(in[52]),
		.A1(in[53]),
		.S(sram[0]),
		.Y(MUX2_X1_26_Y));

	MUX2_X1 mux_l1_in_27_ (
		.A0(in[54]),
		.A1(in[55]),
		.S(sram[0]),
		.Y(MUX2_X1_27_Y));

	MUX2_X1 mux_l1_in_28_ (
		.A0(in[56]),
		.A1(in[57]),
		.S(sram[0]),
		.Y(MUX2_X1_28_Y));

	MUX2_X1 mux_l1_in_29_ (
		.A0(in[58]),
		.A1(in[59]),
		.S(sram[0]),
		.Y(MUX2_X1_29_Y));

	MUX2_X1 mux_l1_in_30_ (
		.A0(in[60]),
		.A1(in[61]),
		.S(sram[0]),
		.Y(MUX2_X1_30_Y));

	MUX2_X1 mux_l1_in_31_ (
		.A0(in[62]),
		.A1(in[63]),
		.S(sram[0]),
		.Y(MUX2_X1_31_Y));

	MUX2_X1 mux_l2_in_0_ (
		.A0(MUX2_X1_0_Y),
		.A1(MUX2_X1_1_Y),
		.S(sram[1]),
		.Y(MUX2_X1_32_Y));

	MUX2_X1 mux_l2_in_1_ (
		.A0(MUX2_X1_2_Y),
		.A1(MUX2_X1_3_Y),
		.S(sram[1]),
		.Y(MUX2_X1_33_Y));

	MUX2_X1 mux_l2_in_2_ (
		.A0(MUX2_X1_4_Y),
		.A1(MUX2_X1_5_Y),
		.S(sram[1]),
		.Y(MUX2_X1_34_Y));

	MUX2_X1 mux_l2_in_3_ (
		.A0(MUX2_X1_6_Y),
		.A1(MUX2_X1_7_Y),
		.S(sram[1]),
		.Y(MUX2_X1_35_Y));

	MUX2_X1 mux_l2_in_4_ (
		.A0(MUX2_X1_8_Y),
		.A1(MUX2_X1_9_Y),
		.S(sram[1]),
		.Y(MUX2_X1_36_Y));

	MUX2_X1 mux_l2_in_5_ (
		.A0(MUX2_X1_10_Y),
		.A1(MUX2_X1_11_Y),
		.S(sram[1]),
		.Y(MUX2_X1_37_Y));

	MUX2_X1 mux_l2_in_6_ (
		.A0(MUX2_X1_12_Y),
		.A1(MUX2_X1_13_Y),
		.S(sram[1]),
		.Y(MUX2_X1_38_Y));

	MUX2_X1 mux_l2_in_7_ (
		.A0(MUX2_X1_14_Y),
		.A1(MUX2_X1_15_Y),
		.S(sram[1]),
		.Y(MUX2_X1_39_Y));

	MUX2_X1 mux_l2_in_8_ (
		.A0(MUX2_X1_16_Y),
		.A1(MUX2_X1_17_Y),
		.S(sram[1]),
		.Y(MUX2_X1_40_Y));

	MUX2_X1 mux_l2_in_9_ (
		.A0(MUX2_X1_18_Y),
		.A1(MUX2_X1_19_Y),
		.S(sram[1]),
		.Y(MUX2_X1_41_Y));

	MUX2_X1 mux_l2_in_10_ (
		.A0(MUX2_X1_20_Y),
		.A1(MUX2_X1_21_Y),
		.S(sram[1]),
		.Y(MUX2_X1_42_Y));

	MUX2_X1 mux_l2_in_11_ (
		.A0(MUX2_X1_22_Y),
		.A1(MUX2_X1_23_Y),
		.S(sram[1]),
		.Y(MUX2_X1_43_Y));

	MUX2_X1 mux_l2_in_12_ (
		.A0(MUX2_X1_24_Y),
		.A1(MUX2_X1_25_Y),
		.S(sram[1]),
		.Y(MUX2_X1_44_Y));

	MUX2_X1 mux_l2_in_13_ (
		.A0(MUX2_X1_26_Y),
		.A1(MUX2_X1_27_Y),
		.S(sram[1]),
		.Y(MUX2_X1_45_Y));

	MUX2_X1 mux_l2_in_14_ (
		.A0(MUX2_X1_28_Y),
		.A1(MUX2_X1_29_Y),
		.S(sram[1]),
		.Y(MUX2_X1_46_Y));

	MUX2_X1 mux_l2_in_15_ (
		.A0(MUX2_X1_30_Y),
		.A1(MUX2_X1_31_Y),
		.S(sram[1]),
		.Y(MUX2_X1_47_Y));

	MUX2_X1 mux_l3_in_0_ (
		.A0(MUX2_X1_32_Y),
		.A1(MUX2_X1_33_Y),
		.S(sram[2]),
		.Y(MUX2_X1_48_Y));

	MUX2_X1 mux_l3_in_1_ (
		.A0(MUX2_X1_34_Y),
		.A1(MUX2_X1_35_Y),
		.S(sram[2]),
		.Y(MUX2_X1_49_Y));

	MUX2_X1 mux_l3_in_2_ (
		.A0(MUX2_X1_36_Y),
		.A1(MUX2_X1_37_Y),
		.S(sram[2]),
		.Y(MUX2_X1_50_Y));

	MUX2_X1 mux_l3_in_3_ (
		.A0(MUX2_X1_38_Y),
		.A1(MUX2_X1_39_Y),
		.S(sram[2]),
		.Y(MUX2_X1_51_Y));

	MUX2_X1 mux_l3_in_4_ (
		.A0(MUX2_X1_40_Y),
		.A1(MUX2_X1_41_Y),
		.S(sram[2]),
		.Y(MUX2_X1_52_Y));

	MUX2_X1 mux_l3_in_5_ (
		.A0(MUX2_X1_42_Y),
		.A1(MUX2_X1_43_Y),
		.S(sram[2]),
		.Y(MUX2_X1_53_Y));

	MUX2_X1 mux_l3_in_6_ (
		.A0(MUX2_X1_44_Y),
		.A1(MUX2_X1_45_Y),
		.S(sram[2]),
		.Y(MUX2_X1_54_Y));

	MUX2_X1 mux_l3_in_7_ (
		.A0(MUX2_X1_46_Y),
		.A1(MUX2_X1_47_Y),
		.S(sram[2]),
		.Y(MUX2_X1_55_Y));

	MUX2_X1 mux_l4_in_0_ (
		.A0(MUX2_X1_48_Y),
		.A1(MUX2_X1_49_Y),
		.S(sram[3]),
		.Y(MUX2_X1_56_Y));

	MUX2_X1 mux_l4_in_1_ (
		.A0(MUX2_X1_50_Y),
		.A1(MUX2_X1_51_Y),
		.S(sram[3]),
		.Y(MUX2_X1_57_Y));

	MUX2_X1 mux_l4_in_2_ (
		.A0(MUX2_X1_52_Y),
		.A1(MUX2_X1_53_Y),
		.S(sram[3]),
		.Y(MUX2_X1_58_Y));

	MUX2_X1 mux_l4_in_3_ (
		.A0(MUX2_X1_54_Y),
		.A1(MUX2_X1_55_Y),
		.S(sram[3]),
		.Y(MUX2_X1_59_Y));

	MUX2_X1 mux_l5_in_0_ (
		.A0(MUX2_X1_56_Y),
		.A1(MUX2_X1_57_Y),
		.S(sram[4]),
		.Y(MUX2_X1_60_Y));

	MUX2_X1 mux_l5_in_1_ (
		.A0(MUX2_X1_58_Y),
		.A1(MUX2_X1_59_Y),
		.S(sram[4]),
		.Y(MUX2_X1_61_Y));

	MUX2_X1 mux_l6_in_0_ (
		.A0(MUX2_X1_60_Y),
		.A1(MUX2_X1_61_Y),
		.S(sram[5]),
		.Y(out));

endmodule
// ----- END Verilog module for lut6_mux -----

//----- Default net type -----
// `default_nettype none




