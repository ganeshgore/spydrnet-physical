//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module cbx_1__0_
(
    gfpga_pad_GPIO_PAD,
    bl,
    wl,
    io_top_in,
    chanx_left_in,
    chanx_right_in,
    bl_0,
    wl_0,
    chanx_left_out,
    chanx_right_out,
    grid_top_out
);

    inout [7:0]gfpga_pad_GPIO_PAD;
    input [7:0]bl;
    input [7:0]wl;
    output [0:7]io_top_in;
    input [19:0]chanx_left_in;
    input [19:0]chanx_right_in;
    input [71:0]bl_0;
    input [71:0]wl_0;
    output [19:0]chanx_left_out;
    output [19:0]chanx_right_out;
    output [0:9]grid_top_out;

    wire [7:0]gfpga_pad_GPIO_PAD;
    wire [7:0]bl;
    wire [7:0]wl;
    wire [0:7]io_top_in;
    wire [0:7]io_top_out;
    wire [19:0]chanx_left_in;
    wire [19:0]chanx_right_in;
    wire [71:0]bl_0;
    wire [71:0]wl_0;
    wire [19:0]chanx_left_out;
    wire [19:0]chanx_right_out;
    wire [0:9]grid_top_out;

    grid_io_bottom grid_io_bottom_4__0_
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD),
        .bl(bl),
        .wl(wl),
        .io_top_in(io_top_in),
        .io_top_out(io_top_out)
    );
    cbx_1__0__old cbx_4__0_
    (
        .chanx_left_in(chanx_left_in),
        .chanx_right_in(chanx_right_in),
        .bl(bl_0),
        .wl(wl_0),
        .chanx_left_out(chanx_left_out),
        .chanx_right_out(chanx_right_out),
        .grid_top_out(grid_top_out),
        .grid_bottom_outpad(io_top_out)
    );
endmodule

