//-------------------------------------------
//	FPGA Synthesizable Verilog Netlist
//	Description: Netlist Summary
//	Author: Xifan TANG
//	Organization: University of Utah
//	Date: Thu Oct 28 18:40:07 2021
//-------------------------------------------
//----- Time scale -----
`timescale 1ns / 1ps

// ------ Include fabric top-level netlists -----
`include "./SRC/fabric_netlists.v"

`include "top_output_verilog.v"

`include "./SRC/top_top_formal_verification.v"
`include "./SRC/top_formal_random_top_tb.v"
