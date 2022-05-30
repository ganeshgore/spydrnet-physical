//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module grid_io_bottom
(
    gfpga_pad_GPIO_PAD,
    bl,
    wl,
    io_top_in,
    io_top_out
);

    inout [0:7]gfpga_pad_GPIO_PAD;
    input [0:7]bl;
    input [0:7]wl;
    output [0:7]io_top_in;
    input [0:7]io_top_out;

    wire [0:7]gfpga_pad_GPIO_PAD;
    wire [0:7]bl;
    wire [0:7]wl;
    wire [0:7]io_top_in;
    wire [0:7]io_top_out;

    logical_tile_io_mode_io_ logical_tile_io_mode_io__0
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD[0]),
        .io_outpad(io_top_out[0]),
        .bl(bl[0]),
        .wl(wl[0]),
        .io_inpad(io_top_in[0])
    );
    logical_tile_io_mode_io_ logical_tile_io_mode_io__1
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD[1]),
        .io_outpad(io_top_out[1]),
        .bl(bl[1]),
        .wl(wl[0]),
        .io_inpad(io_top_in[1])
    );
    logical_tile_io_mode_io_ logical_tile_io_mode_io__2
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD[2]),
        .io_outpad(io_top_out[2]),
        .bl(bl[2]),
        .wl(wl[0]),
        .io_inpad(io_top_in[2])
    );
    logical_tile_io_mode_io_ logical_tile_io_mode_io__3
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD[3]),
        .io_outpad(io_top_out[3]),
        .bl(bl[3]),
        .wl(wl[0]),
        .io_inpad(io_top_in[3])
    );
    logical_tile_io_mode_io_ logical_tile_io_mode_io__4
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD[4]),
        .io_outpad(io_top_out[4]),
        .bl(bl[4]),
        .wl(wl[0]),
        .io_inpad(io_top_in[4])
    );
    logical_tile_io_mode_io_ logical_tile_io_mode_io__5
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD[5]),
        .io_outpad(io_top_out[5]),
        .bl(bl[5]),
        .wl(wl[0]),
        .io_inpad(io_top_in[5])
    );
    logical_tile_io_mode_io_ logical_tile_io_mode_io__6
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD[6]),
        .io_outpad(io_top_out[6]),
        .bl(bl[6]),
        .wl(wl[0]),
        .io_inpad(io_top_in[6])
    );
    logical_tile_io_mode_io_ logical_tile_io_mode_io__7
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD[7]),
        .io_outpad(io_top_out[7]),
        .bl(bl[7]),
        .wl(wl[0]),
        .io_inpad(io_top_in[7])
    );
endmodule

