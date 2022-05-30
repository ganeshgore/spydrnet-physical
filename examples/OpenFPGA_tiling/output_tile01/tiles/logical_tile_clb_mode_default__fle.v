//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module logical_tile_clb_mode_default__fle
(
    reset,
    clk,
    fle_in,
    fle_clk,
    bl,
    wl,
    fle_out
);

    input reset;
    input clk;
    input [0:5]fle_in;
    input fle_clk;
    input [0:65]bl;
    input [0:65]wl;
    output fle_out;

    wire reset;
    wire clk;
    wire [0:5]fle_in;
    wire fle_clk;
    wire [0:65]bl;
    wire [0:65]wl;
    wire fle_out;
    wire direct_interc_1_out;
    wire direct_interc_2_out;
    wire direct_interc_3_out;
    wire direct_interc_4_out;
    wire direct_interc_5_out;
    wire direct_interc_6_out;
    wire direct_interc_7_out;
    wire logical_tile_clb_mode_default__fle_mode_physical__ble6_0_ble6_out;

    logical_tile_clb_mode_default__fle_mode_physical__ble6 logical_tile_clb_mode_default__fle_mode_physical__ble6_0
    (
        .reset(reset),
        .clk(clk),
        .ble6_in({direct_interc_1_out, direct_interc_2_out, direct_interc_3_out, direct_interc_4_out, direct_interc_5_out, direct_interc_6_out}),
        .ble6_clk(direct_interc_7_out),
        .bl(bl),
        .wl(wl),
        .ble6_out(logical_tile_clb_mode_default__fle_mode_physical__ble6_0_ble6_out)
    );
    direct_interc direct_interc_0_
    (
        .in(logical_tile_clb_mode_default__fle_mode_physical__ble6_0_ble6_out),
        .out(fle_out)
    );
    direct_interc direct_interc_1_
    (
        .in(fle_in[0]),
        .out(direct_interc_1_out)
    );
    direct_interc direct_interc_2_
    (
        .in(fle_in[1]),
        .out(direct_interc_2_out)
    );
    direct_interc direct_interc_3_
    (
        .in(fle_in[2]),
        .out(direct_interc_3_out)
    );
    direct_interc direct_interc_4_
    (
        .in(fle_in[3]),
        .out(direct_interc_4_out)
    );
    direct_interc direct_interc_5_
    (
        .in(fle_in[4]),
        .out(direct_interc_5_out)
    );
    direct_interc direct_interc_6_
    (
        .in(fle_in[5]),
        .out(direct_interc_6_out)
    );
    direct_interc direct_interc_7_
    (
        .in(fle_clk),
        .out(direct_interc_7_out)
    );
endmodule

