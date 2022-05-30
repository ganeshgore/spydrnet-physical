//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module cby_4__1_
(
    gfpga_pad_GPIO_PAD,
    bl,
    wl,
    io_left_in,
    chany_bottom_in,
    chany_top_in,
    bl_0,
    wl_0,
    chany_bottom_out,
    chany_top_out,
    grid_left_out
);

    inout [7:0]gfpga_pad_GPIO_PAD;
    input [7:0]bl;
    input [7:0]wl;
    output [0:7]io_left_in;
    input [19:0]chany_bottom_in;
    input [19:0]chany_top_in;
    input [71:0]bl_0;
    input [71:0]wl_0;
    output [19:0]chany_bottom_out;
    output [19:0]chany_top_out;
    output [0:9]grid_left_out;

    wire [7:0]gfpga_pad_GPIO_PAD;
    wire [7:0]bl;
    wire [7:0]wl;
    wire [0:7]io_left_in;
    wire [0:7]io_left_out;
    wire [19:0]chany_bottom_in;
    wire [19:0]chany_top_in;
    wire [71:0]bl_0;
    wire [71:0]wl_0;
    wire [19:0]chany_bottom_out;
    wire [19:0]chany_top_out;
    wire [0:9]grid_left_out;

    grid_io_right grid_io_right_5__4_
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD),
        .bl(bl),
        .wl(wl),
        .io_left_in(io_left_in),
        .io_left_out(io_left_out)
    );
    cby_4__1__old cby_4__4_
    (
        .chany_bottom_in(chany_bottom_in),
        .chany_top_in(chany_top_in),
        .bl(bl_0),
        .wl(wl_0),
        .chany_bottom_out(chany_bottom_out),
        .chany_top_out(chany_top_out),
        .grid_right_outpad(io_left_out),
        .grid_left_out(grid_left_out)
    );
endmodule

