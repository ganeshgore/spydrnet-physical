`timescale 1ns/1ps

// //---------------------------
// // Simple LUT6 Implementation
// //---------------------------
module lut6 (in,out, sram, sram_inv);

  input [5:0]in;
  input [63:0]sram;
  input [63:0]sram_inv;
  output out;

  wire [15:0] I0;
  wire [3:0] I1;

  MUX4_X1 MUX4_X1_01 (.A0(sram[0])  ,.A1(sram[1])  ,.A2(sram[2])  ,.A3(sram[3])  ,.S(in[1:0]) ,.Y(I0[0]));
  MUX4_X1 MUX4_X1_02 (.A0(sram[4])  ,.A1(sram[5])  ,.A2(sram[6])  ,.A3(sram[7])  ,.S(in[1:0]) ,.Y(I0[1]));
  MUX4_X1 MUX4_X1_03 (.A0(sram[8])  ,.A1(sram[9])  ,.A2(sram[10]) ,.A3(sram[11]) ,.S(in[1:0]) ,.Y(I0[2]));
  MUX4_X1 MUX4_X1_04 (.A0(sram[12]) ,.A1(sram[13]) ,.A2(sram[14]) ,.A3(sram[15]) ,.S(in[1:0]) ,.Y(I0[3]));
  MUX4_X1 MUX4_X1_05 (.A0(sram[16]) ,.A1(sram[17]) ,.A2(sram[18]) ,.A3(sram[19]) ,.S(in[1:0]) ,.Y(I0[4]));
  MUX4_X1 MUX4_X1_06 (.A0(sram[20]) ,.A1(sram[21]) ,.A2(sram[22]) ,.A3(sram[23]) ,.S(in[1:0]) ,.Y(I0[5]));
  MUX4_X1 MUX4_X1_07 (.A0(sram[24]) ,.A1(sram[25]) ,.A2(sram[26]) ,.A3(sram[27]) ,.S(in[1:0]) ,.Y(I0[6]));
  MUX4_X1 MUX4_X1_08 (.A0(sram[28]) ,.A1(sram[29]) ,.A2(sram[30]) ,.A3(sram[31]) ,.S(in[1:0]) ,.Y(I0[7]));
  MUX4_X1 MUX4_X1_09 (.A0(sram[32]) ,.A1(sram[33]) ,.A2(sram[34]) ,.A3(sram[35]) ,.S(in[1:0]) ,.Y(I0[8]));
  MUX4_X1 MUX4_X1_10 (.A0(sram[36]) ,.A1(sram[37]) ,.A2(sram[38]) ,.A3(sram[39]) ,.S(in[1:0]) ,.Y(I0[9]));
  MUX4_X1 MUX4_X1_11 (.A0(sram[40]) ,.A1(sram[41]) ,.A2(sram[42]) ,.A3(sram[43]) ,.S(in[1:0]) ,.Y(I0[10]));
  MUX4_X1 MUX4_X1_12 (.A0(sram[44]) ,.A1(sram[45]) ,.A2(sram[46]) ,.A3(sram[47]) ,.S(in[1:0]) ,.Y(I0[11]));
  MUX4_X1 MUX4_X1_13 (.A0(sram[48]) ,.A1(sram[49]) ,.A2(sram[50]) ,.A3(sram[51]) ,.S(in[1:0]) ,.Y(I0[12]));
  MUX4_X1 MUX4_X1_14 (.A0(sram[52]) ,.A1(sram[53]) ,.A2(sram[54]) ,.A3(sram[55]) ,.S(in[1:0]) ,.Y(I0[13]));
  MUX4_X1 MUX4_X1_15 (.A0(sram[56]) ,.A1(sram[57]) ,.A2(sram[58]) ,.A3(sram[59]) ,.S(in[1:0]) ,.Y(I0[14]));
  MUX4_X1 MUX4_X1_16 (.A0(sram[60]) ,.A1(sram[61]) ,.A2(sram[62]) ,.A3(sram[63]) ,.S(in[1:0]) ,.Y(I0[15]));

  MUX4_X1 MUX4_X1_2_01 (.A0(I0[0])  ,.A1(I0[1])  ,.A2(I0[2])  ,.A3(I0[3])  ,.S(in[3:2]) ,.Y(I1[0]));
  MUX4_X1 MUX4_X1_2_02 (.A0(I0[4])  ,.A1(I0[5])  ,.A2(I0[6])  ,.A3(I0[7])  ,.S(in[3:2]) ,.Y(I1[1]));
  MUX4_X1 MUX4_X1_2_03 (.A0(I0[8])  ,.A1(I0[9])  ,.A2(I0[10]) ,.A3(I0[11]) ,.S(in[3:2]) ,.Y(I1[2]));
  MUX4_X1 MUX4_X1_2_04 (.A0(I0[12]) ,.A1(I0[13]) ,.A2(I0[14]) ,.A3(I0[15]) ,.S(in[3:2]) ,.Y(I1[3]));

  MUX4_X1 MUX4_X1_3_01 (.A0(sram[0])  ,.A1(sram[1])  ,.A2(sram[2])  ,.A3(sram[3])  ,.S(in[5:4]) ,.Y(out));
endmodule