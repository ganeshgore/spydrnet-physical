//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff
(
    reset,
    clk,
    ff_D,
    ff_Q,
    ff_clk
);

    input reset;
    input clk;
    input ff_D;
    output ff_Q;
    input ff_clk;

    wire reset;
    wire clk;
    wire ff_D;
    wire ff_Q;
    wire ff_clk;

    DFF DFF_0_
    (
        .reset(reset),
        .clk(clk),
        .D(ff_D),
        .Q(ff_Q)
    );
endmodule

