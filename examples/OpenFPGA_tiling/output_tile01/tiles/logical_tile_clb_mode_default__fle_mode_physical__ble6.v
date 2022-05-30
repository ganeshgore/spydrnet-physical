//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module logical_tile_clb_mode_default__fle_mode_physical__ble6
(
    reset,
    clk,
    ble6_in,
    ble6_clk,
    bl,
    wl,
    ble6_out
);

    input reset;
    input clk;
    input [0:5]ble6_in;
    input ble6_clk;
    input [0:65]bl;
    input [0:65]wl;
    output ble6_out;

    wire reset;
    wire clk;
    wire [0:5]ble6_in;
    wire ble6_clk;
    wire [0:65]bl;
    wire [0:65]wl;
    wire ble6_out;
    wire [0:1]mux2_size2_0_sram;
    wire [0:1]mux2_size2_0_sram_inv;
    wire direct_interc_0_out;
    wire direct_interc_1_out;
    wire direct_interc_2_out;
    wire direct_interc_3_out;
    wire direct_interc_4_out;
    wire direct_interc_5_out;
    wire logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6_0_lut6_out;
    wire direct_interc_6_out;
    wire logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff_0_ff_Q;
    wire direct_interc_7_out;

    logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6 logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6_0
    (
        .lut6_in({direct_interc_0_out, direct_interc_1_out, direct_interc_2_out, direct_interc_3_out, direct_interc_4_out, direct_interc_5_out}),
        .bl(bl[0:63]),
        .wl(wl[0:63]),
        .lut6_out(logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6_0_lut6_out)
    );
    logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff_0
    (
        .reset(reset),
        .clk(clk),
        .ff_D(direct_interc_6_out),
        .ff_Q(logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff_0_ff_Q),
        .ff_clk(direct_interc_7_out)
    );
    mux2_size2 mux_ble6_out_0
    (
        .in({logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__ff_0_ff_Q, logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6_0_lut6_out}),
        .sram(mux2_size2_0_sram),
        .sram_inv(mux2_size2_0_sram_inv),
        .out(ble6_out)
    );
    mux2_size2_mem mem_ble6_out_0
    (
        .bl(bl[64:65]),
        .wl(wl[64:65]),
        .mem_out(mux2_size2_0_sram),
        .mem_outb(mux2_size2_0_sram_inv)
    );
    direct_interc direct_interc_0_
    (
        .in(ble6_in[0]),
        .out(direct_interc_0_out)
    );
    direct_interc direct_interc_1_
    (
        .in(ble6_in[1]),
        .out(direct_interc_1_out)
    );
    direct_interc direct_interc_2_
    (
        .in(ble6_in[2]),
        .out(direct_interc_2_out)
    );
    direct_interc direct_interc_3_
    (
        .in(ble6_in[3]),
        .out(direct_interc_3_out)
    );
    direct_interc direct_interc_4_
    (
        .in(ble6_in[4]),
        .out(direct_interc_4_out)
    );
    direct_interc direct_interc_5_
    (
        .in(ble6_in[5]),
        .out(direct_interc_5_out)
    );
    direct_interc direct_interc_6_
    (
        .in(logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6_0_lut6_out),
        .out(direct_interc_6_out)
    );
    direct_interc direct_interc_7_
    (
        .in(ble6_clk),
        .out(direct_interc_7_out)
    );
endmodule

