//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module left_tile
(
    gfpga_pad_GPIO_PAD,
    io_right_in,
    chany_bottom_in,
    chany_bottom_out,
    grid_right_out,
    chany_top_in_0,
    chanx_right_in,
    chany_top_out_0,
    chanx_right_out,
    grid_top_r_in,
    grid_top_l_inpad,
    grid_right_t_in,
    grid_right_b_in,
    grid_bottom_r_in,
    wl_in,
    wl_out,
    bl_in,
    bl_out
);

    inout [7:0]gfpga_pad_GPIO_PAD;
    output [0:7]io_right_in;
    input [19:0]chany_bottom_in;
    output [19:0]chany_bottom_out;
    output [0:9]grid_right_out;
    input [19:0]chany_top_in_0;
    input [19:0]chanx_right_in;
    output [19:0]chany_top_out_0;
    output [19:0]chanx_right_out;
    input [0:1]grid_top_r_in;
    input [0:7]grid_top_l_inpad;
    input [0:1]grid_right_t_in;
    input [0:2]grid_right_b_in;
    input [0:1]grid_bottom_r_in;
    input [3:0]wl_in;
    output [3:0]wl_out;
    input [39:0]bl_in;
    output [39:0]bl_out;

    wire [7:0]gfpga_pad_GPIO_PAD;
    wire [0:7]io_right_in;
    wire [19:0]chany_bottom_in;
    wire [19:0]chany_top_in;
    wire [19:0]chany_bottom_out;
    wire [19:0]chany_top_out;
    wire [0:9]grid_right_out;
    wire [19:0]chany_top_in_0;
    wire [19:0]chanx_right_in;
    wire [19:0]chany_top_out_0;
    wire [19:0]chanx_right_out;
    wire [0:1]grid_top_r_in;
    wire [0:7]grid_top_l_inpad;
    wire [0:1]grid_right_t_in;
    wire [0:2]grid_right_b_in;
    wire [0:1]grid_bottom_r_in;
    wire [0:157]bl;
    wire [0:157]wl;
    wire [3:0]wl_in;
    wire [3:0]wl_out;
    wire [39:0]bl_in;
    wire [39:0]bl_out;

assign wl_out = wl_in;
assign bl_out = bl_in;
    cby_0__1_ cby_0__1_
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD),
        .bl(bl[0:7]),
        .wl(wl[0:7]),
        .io_right_in(io_right_in),
        .chany_bottom_in(chany_bottom_in),
        .chany_top_in(chany_top_in),
        .bl_0(bl[8:79]),
        .wl_0(wl[8:79]),
        .chany_bottom_out(chany_bottom_out),
        .chany_top_out(chany_top_out),
        .grid_right_out(grid_right_out)
    );
    sb_0__1_ sb_0__1_
    (
        .chany_top_in(chany_top_in_0),
        .chanx_right_in(chanx_right_in),
        .chany_bottom_in(chany_top_out),
        .bl(bl[80:157]),
        .wl(wl[80:157]),
        .chany_top_out(chany_top_out_0),
        .chanx_right_out(chanx_right_out),
        .chany_bottom_out(chany_top_in),
        .grid_top_r_in(grid_top_r_in),
        .grid_top_l_inpad(grid_top_l_inpad),
        .grid_right_t_in(grid_right_t_in),
        .grid_right_b_in(grid_right_b_in),
        .grid_bottom_r_in(grid_bottom_r_in),
        .grid_bottom_l_inpad(io_right_in)
    );
endmodule

