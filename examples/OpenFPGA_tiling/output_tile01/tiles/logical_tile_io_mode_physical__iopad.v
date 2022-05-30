//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module logical_tile_io_mode_physical__iopad
(
    gfpga_pad_GPIO_PAD,
    iopad_outpad,
    bl,
    wl,
    iopad_inpad
);

    inout gfpga_pad_GPIO_PAD;
    input iopad_outpad;
    input bl;
    input wl;
    output iopad_inpad;

    wire gfpga_pad_GPIO_PAD;
    wire iopad_outpad;
    wire bl;
    wire wl;
    wire iopad_inpad;
    wire GPIO_0_DIR;
    wire GPIO_SRAM_mem_undriven_mem_outb;

    GPIO GPIO_0_
    (
        .PAD(gfpga_pad_GPIO_PAD),
        .outpad(iopad_outpad),
        .DIR(GPIO_0_DIR),
        .inpad(iopad_inpad)
    );
    GPIO_SRAM_mem GPIO_SRAM_mem
    (
        .bl(bl),
        .wl(wl),
        .mem_out(GPIO_0_DIR),
        .mem_outb(GPIO_SRAM_mem_undriven_mem_outb)
    );
endmodule

