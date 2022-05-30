//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Memories used in FPGA
//	Organization: University of Utah
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size8_mem -----
module mux2_size8_mem(bl,
                      wl,
                      mem_out,
                      mem_outb);
//----- INPUT PORTS -----
input [0:3] bl;
//----- INPUT PORTS -----
input [0:3] wl;
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

	SRAM SRAM_0_ (
		.D(bl[0]),
		.WE(wl[0]),
		.Q(mem_out[0]),
		.QN(mem_outb[0]));

	SRAM SRAM_1_ (
		.D(bl[1]),
		.WE(wl[1]),
		.Q(mem_out[1]),
		.QN(mem_outb[1]));

	SRAM SRAM_2_ (
		.D(bl[2]),
		.WE(wl[2]),
		.Q(mem_out[2]),
		.QN(mem_outb[2]));

	SRAM SRAM_3_ (
		.D(bl[3]),
		.WE(wl[3]),
		.Q(mem_out[3]),
		.QN(mem_outb[3]));

endmodule
// ----- END Verilog module for mux2_size8_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size2_mem -----
module mux2_size2_mem(bl,
                      wl,
                      mem_out,
                      mem_outb);
//----- INPUT PORTS -----
input [0:1] bl;
//----- INPUT PORTS -----
input [0:1] wl;
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

	SRAM SRAM_0_ (
		.D(bl[0]),
		.WE(wl[0]),
		.Q(mem_out[0]),
		.QN(mem_outb[0]));

	SRAM SRAM_1_ (
		.D(bl[1]),
		.WE(wl[1]),
		.Q(mem_out[1]),
		.QN(mem_outb[1]));

endmodule
// ----- END Verilog module for mux2_size2_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size9_mem -----
module mux2_size9_mem(bl,
                      wl,
                      mem_out,
                      mem_outb);
//----- INPUT PORTS -----
input [0:3] bl;
//----- INPUT PORTS -----
input [0:3] wl;
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

	SRAM SRAM_0_ (
		.D(bl[0]),
		.WE(wl[0]),
		.Q(mem_out[0]),
		.QN(mem_outb[0]));

	SRAM SRAM_1_ (
		.D(bl[1]),
		.WE(wl[1]),
		.Q(mem_out[1]),
		.QN(mem_outb[1]));

	SRAM SRAM_2_ (
		.D(bl[2]),
		.WE(wl[2]),
		.Q(mem_out[2]),
		.QN(mem_outb[2]));

	SRAM SRAM_3_ (
		.D(bl[3]),
		.WE(wl[3]),
		.Q(mem_out[3]),
		.QN(mem_outb[3]));

endmodule
// ----- END Verilog module for mux2_size9_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size12_mem -----
module mux2_size12_mem(bl,
                       wl,
                       mem_out,
                       mem_outb);
//----- INPUT PORTS -----
input [0:3] bl;
//----- INPUT PORTS -----
input [0:3] wl;
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

	SRAM SRAM_0_ (
		.D(bl[0]),
		.WE(wl[0]),
		.Q(mem_out[0]),
		.QN(mem_outb[0]));

	SRAM SRAM_1_ (
		.D(bl[1]),
		.WE(wl[1]),
		.Q(mem_out[1]),
		.QN(mem_outb[1]));

	SRAM SRAM_2_ (
		.D(bl[2]),
		.WE(wl[2]),
		.Q(mem_out[2]),
		.QN(mem_outb[2]));

	SRAM SRAM_3_ (
		.D(bl[3]),
		.WE(wl[3]),
		.Q(mem_out[3]),
		.QN(mem_outb[3]));

endmodule
// ----- END Verilog module for mux2_size12_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size3_mem -----
module mux2_size3_mem(bl,
                      wl,
                      mem_out,
                      mem_outb);
//----- INPUT PORTS -----
input [0:1] bl;
//----- INPUT PORTS -----
input [0:1] wl;
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

	SRAM SRAM_0_ (
		.D(bl[0]),
		.WE(wl[0]),
		.Q(mem_out[0]),
		.QN(mem_outb[0]));

	SRAM SRAM_1_ (
		.D(bl[1]),
		.WE(wl[1]),
		.Q(mem_out[1]),
		.QN(mem_outb[1]));

endmodule
// ----- END Verilog module for mux2_size3_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size4_mem -----
module mux2_size4_mem(bl,
                      wl,
                      mem_out,
                      mem_outb);
//----- INPUT PORTS -----
input [0:2] bl;
//----- INPUT PORTS -----
input [0:2] wl;
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

	SRAM SRAM_0_ (
		.D(bl[0]),
		.WE(wl[0]),
		.Q(mem_out[0]),
		.QN(mem_outb[0]));

	SRAM SRAM_1_ (
		.D(bl[1]),
		.WE(wl[1]),
		.Q(mem_out[1]),
		.QN(mem_outb[1]));

	SRAM SRAM_2_ (
		.D(bl[2]),
		.WE(wl[2]),
		.Q(mem_out[2]),
		.QN(mem_outb[2]));

endmodule
// ----- END Verilog module for mux2_size4_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size10_mem -----
module mux2_size10_mem(bl,
                       wl,
                       mem_out,
                       mem_outb);
//----- INPUT PORTS -----
input [0:3] bl;
//----- INPUT PORTS -----
input [0:3] wl;
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

	SRAM SRAM_0_ (
		.D(bl[0]),
		.WE(wl[0]),
		.Q(mem_out[0]),
		.QN(mem_outb[0]));

	SRAM SRAM_1_ (
		.D(bl[1]),
		.WE(wl[1]),
		.Q(mem_out[1]),
		.QN(mem_outb[1]));

	SRAM SRAM_2_ (
		.D(bl[2]),
		.WE(wl[2]),
		.Q(mem_out[2]),
		.QN(mem_outb[2]));

	SRAM SRAM_3_ (
		.D(bl[3]),
		.WE(wl[3]),
		.Q(mem_out[3]),
		.QN(mem_outb[3]));

endmodule
// ----- END Verilog module for mux2_size10_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size5_mem -----
module mux2_size5_mem(bl,
                      wl,
                      mem_out,
                      mem_outb);
//----- INPUT PORTS -----
input [0:2] bl;
//----- INPUT PORTS -----
input [0:2] wl;
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

	SRAM SRAM_0_ (
		.D(bl[0]),
		.WE(wl[0]),
		.Q(mem_out[0]),
		.QN(mem_outb[0]));

	SRAM SRAM_1_ (
		.D(bl[1]),
		.WE(wl[1]),
		.Q(mem_out[1]),
		.QN(mem_outb[1]));

	SRAM SRAM_2_ (
		.D(bl[2]),
		.WE(wl[2]),
		.Q(mem_out[2]),
		.QN(mem_outb[2]));

endmodule
// ----- END Verilog module for mux2_size5_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for mux2_size50_mem -----
module mux2_size50_mem(bl,
                       wl,
                       mem_out,
                       mem_outb);
//----- INPUT PORTS -----
input [0:5] bl;
//----- INPUT PORTS -----
input [0:5] wl;
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

	SRAM SRAM_0_ (
		.D(bl[0]),
		.WE(wl[0]),
		.Q(mem_out[0]),
		.QN(mem_outb[0]));

	SRAM SRAM_1_ (
		.D(bl[1]),
		.WE(wl[1]),
		.Q(mem_out[1]),
		.QN(mem_outb[1]));

	SRAM SRAM_2_ (
		.D(bl[2]),
		.WE(wl[2]),
		.Q(mem_out[2]),
		.QN(mem_outb[2]));

	SRAM SRAM_3_ (
		.D(bl[3]),
		.WE(wl[3]),
		.Q(mem_out[3]),
		.QN(mem_outb[3]));

	SRAM SRAM_4_ (
		.D(bl[4]),
		.WE(wl[4]),
		.Q(mem_out[4]),
		.QN(mem_outb[4]));

	SRAM SRAM_5_ (
		.D(bl[5]),
		.WE(wl[5]),
		.Q(mem_out[5]),
		.QN(mem_outb[5]));

endmodule
// ----- END Verilog module for mux2_size50_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for lut6_SRAM_mem -----
module lut6_SRAM_mem(bl,
                     wl,
                     mem_out,
                     mem_outb);
//----- INPUT PORTS -----
input [0:63] bl;
//----- INPUT PORTS -----
input [0:63] wl;
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

	SRAM SRAM_0_ (
		.D(bl[0]),
		.WE(wl[0]),
		.Q(mem_out[0]),
		.QN(mem_outb[0]));

	SRAM SRAM_1_ (
		.D(bl[1]),
		.WE(wl[1]),
		.Q(mem_out[1]),
		.QN(mem_outb[1]));

	SRAM SRAM_2_ (
		.D(bl[2]),
		.WE(wl[2]),
		.Q(mem_out[2]),
		.QN(mem_outb[2]));

	SRAM SRAM_3_ (
		.D(bl[3]),
		.WE(wl[3]),
		.Q(mem_out[3]),
		.QN(mem_outb[3]));

	SRAM SRAM_4_ (
		.D(bl[4]),
		.WE(wl[4]),
		.Q(mem_out[4]),
		.QN(mem_outb[4]));

	SRAM SRAM_5_ (
		.D(bl[5]),
		.WE(wl[5]),
		.Q(mem_out[5]),
		.QN(mem_outb[5]));

	SRAM SRAM_6_ (
		.D(bl[6]),
		.WE(wl[6]),
		.Q(mem_out[6]),
		.QN(mem_outb[6]));

	SRAM SRAM_7_ (
		.D(bl[7]),
		.WE(wl[7]),
		.Q(mem_out[7]),
		.QN(mem_outb[7]));

	SRAM SRAM_8_ (
		.D(bl[8]),
		.WE(wl[8]),
		.Q(mem_out[8]),
		.QN(mem_outb[8]));

	SRAM SRAM_9_ (
		.D(bl[9]),
		.WE(wl[9]),
		.Q(mem_out[9]),
		.QN(mem_outb[9]));

	SRAM SRAM_10_ (
		.D(bl[10]),
		.WE(wl[10]),
		.Q(mem_out[10]),
		.QN(mem_outb[10]));

	SRAM SRAM_11_ (
		.D(bl[11]),
		.WE(wl[11]),
		.Q(mem_out[11]),
		.QN(mem_outb[11]));

	SRAM SRAM_12_ (
		.D(bl[12]),
		.WE(wl[12]),
		.Q(mem_out[12]),
		.QN(mem_outb[12]));

	SRAM SRAM_13_ (
		.D(bl[13]),
		.WE(wl[13]),
		.Q(mem_out[13]),
		.QN(mem_outb[13]));

	SRAM SRAM_14_ (
		.D(bl[14]),
		.WE(wl[14]),
		.Q(mem_out[14]),
		.QN(mem_outb[14]));

	SRAM SRAM_15_ (
		.D(bl[15]),
		.WE(wl[15]),
		.Q(mem_out[15]),
		.QN(mem_outb[15]));

	SRAM SRAM_16_ (
		.D(bl[16]),
		.WE(wl[16]),
		.Q(mem_out[16]),
		.QN(mem_outb[16]));

	SRAM SRAM_17_ (
		.D(bl[17]),
		.WE(wl[17]),
		.Q(mem_out[17]),
		.QN(mem_outb[17]));

	SRAM SRAM_18_ (
		.D(bl[18]),
		.WE(wl[18]),
		.Q(mem_out[18]),
		.QN(mem_outb[18]));

	SRAM SRAM_19_ (
		.D(bl[19]),
		.WE(wl[19]),
		.Q(mem_out[19]),
		.QN(mem_outb[19]));

	SRAM SRAM_20_ (
		.D(bl[20]),
		.WE(wl[20]),
		.Q(mem_out[20]),
		.QN(mem_outb[20]));

	SRAM SRAM_21_ (
		.D(bl[21]),
		.WE(wl[21]),
		.Q(mem_out[21]),
		.QN(mem_outb[21]));

	SRAM SRAM_22_ (
		.D(bl[22]),
		.WE(wl[22]),
		.Q(mem_out[22]),
		.QN(mem_outb[22]));

	SRAM SRAM_23_ (
		.D(bl[23]),
		.WE(wl[23]),
		.Q(mem_out[23]),
		.QN(mem_outb[23]));

	SRAM SRAM_24_ (
		.D(bl[24]),
		.WE(wl[24]),
		.Q(mem_out[24]),
		.QN(mem_outb[24]));

	SRAM SRAM_25_ (
		.D(bl[25]),
		.WE(wl[25]),
		.Q(mem_out[25]),
		.QN(mem_outb[25]));

	SRAM SRAM_26_ (
		.D(bl[26]),
		.WE(wl[26]),
		.Q(mem_out[26]),
		.QN(mem_outb[26]));

	SRAM SRAM_27_ (
		.D(bl[27]),
		.WE(wl[27]),
		.Q(mem_out[27]),
		.QN(mem_outb[27]));

	SRAM SRAM_28_ (
		.D(bl[28]),
		.WE(wl[28]),
		.Q(mem_out[28]),
		.QN(mem_outb[28]));

	SRAM SRAM_29_ (
		.D(bl[29]),
		.WE(wl[29]),
		.Q(mem_out[29]),
		.QN(mem_outb[29]));

	SRAM SRAM_30_ (
		.D(bl[30]),
		.WE(wl[30]),
		.Q(mem_out[30]),
		.QN(mem_outb[30]));

	SRAM SRAM_31_ (
		.D(bl[31]),
		.WE(wl[31]),
		.Q(mem_out[31]),
		.QN(mem_outb[31]));

	SRAM SRAM_32_ (
		.D(bl[32]),
		.WE(wl[32]),
		.Q(mem_out[32]),
		.QN(mem_outb[32]));

	SRAM SRAM_33_ (
		.D(bl[33]),
		.WE(wl[33]),
		.Q(mem_out[33]),
		.QN(mem_outb[33]));

	SRAM SRAM_34_ (
		.D(bl[34]),
		.WE(wl[34]),
		.Q(mem_out[34]),
		.QN(mem_outb[34]));

	SRAM SRAM_35_ (
		.D(bl[35]),
		.WE(wl[35]),
		.Q(mem_out[35]),
		.QN(mem_outb[35]));

	SRAM SRAM_36_ (
		.D(bl[36]),
		.WE(wl[36]),
		.Q(mem_out[36]),
		.QN(mem_outb[36]));

	SRAM SRAM_37_ (
		.D(bl[37]),
		.WE(wl[37]),
		.Q(mem_out[37]),
		.QN(mem_outb[37]));

	SRAM SRAM_38_ (
		.D(bl[38]),
		.WE(wl[38]),
		.Q(mem_out[38]),
		.QN(mem_outb[38]));

	SRAM SRAM_39_ (
		.D(bl[39]),
		.WE(wl[39]),
		.Q(mem_out[39]),
		.QN(mem_outb[39]));

	SRAM SRAM_40_ (
		.D(bl[40]),
		.WE(wl[40]),
		.Q(mem_out[40]),
		.QN(mem_outb[40]));

	SRAM SRAM_41_ (
		.D(bl[41]),
		.WE(wl[41]),
		.Q(mem_out[41]),
		.QN(mem_outb[41]));

	SRAM SRAM_42_ (
		.D(bl[42]),
		.WE(wl[42]),
		.Q(mem_out[42]),
		.QN(mem_outb[42]));

	SRAM SRAM_43_ (
		.D(bl[43]),
		.WE(wl[43]),
		.Q(mem_out[43]),
		.QN(mem_outb[43]));

	SRAM SRAM_44_ (
		.D(bl[44]),
		.WE(wl[44]),
		.Q(mem_out[44]),
		.QN(mem_outb[44]));

	SRAM SRAM_45_ (
		.D(bl[45]),
		.WE(wl[45]),
		.Q(mem_out[45]),
		.QN(mem_outb[45]));

	SRAM SRAM_46_ (
		.D(bl[46]),
		.WE(wl[46]),
		.Q(mem_out[46]),
		.QN(mem_outb[46]));

	SRAM SRAM_47_ (
		.D(bl[47]),
		.WE(wl[47]),
		.Q(mem_out[47]),
		.QN(mem_outb[47]));

	SRAM SRAM_48_ (
		.D(bl[48]),
		.WE(wl[48]),
		.Q(mem_out[48]),
		.QN(mem_outb[48]));

	SRAM SRAM_49_ (
		.D(bl[49]),
		.WE(wl[49]),
		.Q(mem_out[49]),
		.QN(mem_outb[49]));

	SRAM SRAM_50_ (
		.D(bl[50]),
		.WE(wl[50]),
		.Q(mem_out[50]),
		.QN(mem_outb[50]));

	SRAM SRAM_51_ (
		.D(bl[51]),
		.WE(wl[51]),
		.Q(mem_out[51]),
		.QN(mem_outb[51]));

	SRAM SRAM_52_ (
		.D(bl[52]),
		.WE(wl[52]),
		.Q(mem_out[52]),
		.QN(mem_outb[52]));

	SRAM SRAM_53_ (
		.D(bl[53]),
		.WE(wl[53]),
		.Q(mem_out[53]),
		.QN(mem_outb[53]));

	SRAM SRAM_54_ (
		.D(bl[54]),
		.WE(wl[54]),
		.Q(mem_out[54]),
		.QN(mem_outb[54]));

	SRAM SRAM_55_ (
		.D(bl[55]),
		.WE(wl[55]),
		.Q(mem_out[55]),
		.QN(mem_outb[55]));

	SRAM SRAM_56_ (
		.D(bl[56]),
		.WE(wl[56]),
		.Q(mem_out[56]),
		.QN(mem_outb[56]));

	SRAM SRAM_57_ (
		.D(bl[57]),
		.WE(wl[57]),
		.Q(mem_out[57]),
		.QN(mem_outb[57]));

	SRAM SRAM_58_ (
		.D(bl[58]),
		.WE(wl[58]),
		.Q(mem_out[58]),
		.QN(mem_outb[58]));

	SRAM SRAM_59_ (
		.D(bl[59]),
		.WE(wl[59]),
		.Q(mem_out[59]),
		.QN(mem_outb[59]));

	SRAM SRAM_60_ (
		.D(bl[60]),
		.WE(wl[60]),
		.Q(mem_out[60]),
		.QN(mem_outb[60]));

	SRAM SRAM_61_ (
		.D(bl[61]),
		.WE(wl[61]),
		.Q(mem_out[61]),
		.QN(mem_outb[61]));

	SRAM SRAM_62_ (
		.D(bl[62]),
		.WE(wl[62]),
		.Q(mem_out[62]),
		.QN(mem_outb[62]));

	SRAM SRAM_63_ (
		.D(bl[63]),
		.WE(wl[63]),
		.Q(mem_out[63]),
		.QN(mem_outb[63]));

endmodule
// ----- END Verilog module for lut6_SRAM_mem -----

//----- Default net type -----
// `default_nettype none




//----- Default net type -----
// `default_nettype wire

// ----- Verilog module for GPIO_SRAM_mem -----
module GPIO_SRAM_mem(bl,
                     wl,
                     mem_out,
                     mem_outb);
//----- INPUT PORTS -----
input [0:0] bl;
//----- INPUT PORTS -----
input [0:0] wl;
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

	SRAM SRAM_0_ (
		.D(bl),
		.WE(wl),
		.Q(mem_out),
		.QN(mem_outb));

endmodule
// ----- END Verilog module for GPIO_SRAM_mem -----

//----- Default net type -----
// `default_nettype none




