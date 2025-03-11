// `timescale 1ns/1ps

`celldefine
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// A wrapper for 2-input MUX BUILT
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module MUX2(IN0, IN1, SEL, OUT);
  input IN0;
  input IN1;
  input SEL;
  output OUT;

  assign OUT = SEL ? IN1 : IN0;
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// A wrapper for 4-input MUX BUILT
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module MUX4(IN0, IN1, IN2, IN3, SEL, OUT);
  input IN0;
  input IN1;
  input IN2;
  input IN3;
  input [1:0]SEL;
  output OUT;

  assign OUT = (SEL[1] ? (SEL[0] ? IN3 : IN2) : (SEL[0] ? IN1 : IN0));
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// 2 input MUX WITH SCAN_ENABLE INPUT
// if scan_enable=1, sel=x, out=in0
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module MUX2_SCAN(IN0, IN1, SEL, SCAN_EN, OUT);
  input IN0;
  input IN1;
  input SEL;
  input SCAN_EN;
  output OUT;

  assign OUT = (SEL&SCAN_EN) ? IN1 : IN0;
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// Inverter
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module INV (IN, OUT);
  input IN;
  output OUT;

  assign OUT = ~IN;
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// Buffer
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module BUF (IN, OUT);
  input IN;
  output OUT;

  assign OUT = IN;
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// 2-input AND
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module AND2 (IN0, IN1, OUT);
  input IN0;
  input IN1;
  output OUT;

  assign OUT = IN0 & IN1;
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// 2-input OR
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module OR2 (IN0, IN1, OUT);
  input IN0;
  input IN1;
  output OUT;

  assign OUT = IN0 | IN1;
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// 2-input NAND
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module NAND2 (IN0, IN1, OUT);
  input IN0;
  input IN1;
  output OUT;

  assign OUT = ~(IN0 & IN1);
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// 2-input NOR
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module NOR2 (IN0, IN1, OUT);
  input IN0;
  input IN1;
  output OUT;

  assign OUT = ~(IN0 | IN1);
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// D-Flipflop without control signals
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module DFF(D, CLK, Q, QN);
  input D;
  input CLK;
  output reg Q;
  output QN;

  assign QN = ~Q;
  always@(posedge CLK)
    Q <= D;
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// D-Flipflop with active low reset signal
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module DFF_NR(D, CLK, RESET, Q, QN);
  input D;
  input CLK;
  input RESET;
  output reg Q;
  output QN;

  assign QN = ~Q;
  always@(posedge CLK)
    if (RESET)
      Q <= D;
    else
      Q <= 0;
endmodule
// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
// D-Flipflop with active low reset signal and enable signal
// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
module DFF_NR_EN(D, CLK, RESET, ENABLE, Q, QN);
  input D;
  input CLK;
  input RESET;
  input ENABLE;
  output Q;
  output QN;

  reg q_int;

  assign QN = ~Q;
  assign Q = (ENABLE) ? q_int : 0;
  always@(posedge CLK)
    if (RESET)
      q_int <= D;
    else
      q_int <= 0;

endmodule
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// De-MUX
// SEL = 0, OUT0 = IN; SEL = 1, OUT1 = IN;
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module DEMUX2(IN, SEL, OUT0, OUT1);
  input IN;
  input SEL;
  output OUT0;
  output OUT1;
  reg OUT0;
  reg OUT1;

  always @(*) begin
    case (SEL)
    1'b0: begin
          OUT0=IN;
          OUT1=1'b0;
    end
    1'b1: begin
          OUT0=1'b0;
          OUT1=IN;
    end
    endcase
  end
endmodule

// = = = = = = = = = = = = = = = = = = = = = = = = = = =
// LATCH
// = = = = = = = = = = = = = = = = = = = = = = = = = = =
module HOLD_LATCH (D, G, Q);
  input D;    // Data input
  input G;    // Gate input
  output Q;     // Latch output
  reg Q;

  always @(G or D) begin
    if (!G)      // When G is low (0), latch is enabled
      Q = D;       // Q follows the data input
  end
endmodule

`endcelldefine