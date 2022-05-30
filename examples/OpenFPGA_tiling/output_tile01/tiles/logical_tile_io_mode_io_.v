//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module logical_tile_io_mode_io_
(
    gfpga_pad_GPIO_PAD,
    io_outpad,
    bl,
    wl,
    io_inpad
);

    inout gfpga_pad_GPIO_PAD;
    input io_outpad;
    input bl;
    input wl;
    output io_inpad;

    wire gfpga_pad_GPIO_PAD;
    wire io_outpad;
    wire bl;
    wire wl;
    wire io_inpad;
    wire direct_interc_1_out;
    wire logical_tile_io_mode_physical__iopad_0_iopad_inpad;

    logical_tile_io_mode_physical__iopad logical_tile_io_mode_physical__iopad_0
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD),
        .iopad_outpad(direct_interc_1_out),
        .bl(bl),
        .wl(wl),
        .iopad_inpad(logical_tile_io_mode_physical__iopad_0_iopad_inpad)
    );
    direct_interc direct_interc_0_
    (
        .in(logical_tile_io_mode_physical__iopad_0_iopad_inpad),
        .out(io_inpad)
    );
    direct_interc direct_interc_1_
    (
        .in(io_outpad),
        .out(direct_interc_1_out)
    );
endmodule

