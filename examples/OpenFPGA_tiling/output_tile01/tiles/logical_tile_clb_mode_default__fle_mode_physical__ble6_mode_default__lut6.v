//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module logical_tile_clb_mode_default__fle_mode_physical__ble6_mode_default__lut6
(
    lut6_in,
    bl,
    wl,
    lut6_out
);

    input [0:5]lut6_in;
    input [0:63]bl;
    input [0:63]wl;
    output lut6_out;

    wire [0:5]lut6_in;
    wire [0:63]bl;
    wire [0:63]wl;
    wire lut6_out;
    wire [0:63]lut6_0_sram;
    wire [0:63]lut6_SRAM_mem_undriven_mem_outb;

    lut6 lut6_0_
    (
        .in(lut6_in),
        .sram(lut6_0_sram),
        .out(lut6_out)
    );
    lut6_SRAM_mem lut6_SRAM_mem
    (
        .bl(bl),
        .wl(wl),
        .mem_out(lut6_0_sram),
        .mem_outb(lut6_SRAM_mem_undriven_mem_outb)
    );
endmodule

