//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module top_left_tile
(
    chanx_right_in,
    chanx_right_out,
    grid_right_t_inpad,
    grid_right_b_in,
    grid_bottom_r_in,
    grid_bottom_l_inpad,
    gfpga_pad_GPIO_PAD,
    chany_bottom_in_0,
    chany_bottom_out_0,
    grid_right_out,
    bl,
    wl,
    wl_in,
    wl_out,
    bl_in,
    bl_out
);

    input [19:0]chanx_right_in;
    output [19:0]chanx_right_out;
    input [0:7]grid_right_t_inpad;
    input [0:2]grid_right_b_in;
    input [0:1]grid_bottom_r_in;
    input [0:7]grid_bottom_l_inpad;
    inout [7:0]gfpga_pad_GPIO_PAD;
    input [19:0]chany_bottom_in_0;
    output [19:0]chany_bottom_out_0;
    output [0:9]grid_right_out;
    input [0:159]bl;
    input [0:159]wl;
    input [3:0]wl_in;
    output [3:0]wl_out;
    input [39:0]bl_in;
    output [39:0]bl_out;

    wire [19:0]chanx_right_in;
    wire [19:0]chany_bottom_in;
    wire [19:0]chanx_right_out;
    wire [19:0]chany_bottom_out;
    wire [0:7]grid_right_t_inpad;
    wire [0:2]grid_right_b_in;
    wire [0:1]grid_bottom_r_in;
    wire [0:7]grid_bottom_l_inpad;
    wire [7:0]gfpga_pad_GPIO_PAD;
    wire [19:0]chany_bottom_in_0;
    wire [19:0]chany_bottom_out_0;
    wire [0:9]grid_right_out;
    wire [0:159]bl;
    wire [0:159]wl;
    wire [3:0]wl_in;
    wire [3:0]wl_out;
    wire [39:0]bl_in;
    wire [39:0]bl_out;

assign wl_out = wl_in;
assign bl_out = bl_in;
    sb_0__4_ sb_0__4_
    (
        .chanx_right_in(chanx_right_in),
        .chany_bottom_in(chany_bottom_in),
        .bl(bl[0:79]),
        .wl(wl[0:79]),
        .chanx_right_out(chanx_right_out),
        .chany_bottom_out(chany_bottom_out),
        .grid_right_t_inpad(grid_right_t_inpad),
        .grid_right_b_in(grid_right_b_in),
        .grid_bottom_r_in(grid_bottom_r_in),
        .grid_bottom_l_inpad(grid_bottom_l_inpad)
    );
    cby_0__1_ cby_0__4_
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD),
        .bl(bl[80:87]),
        .wl(wl[80:87]),
        .io_right_in(grid_bottom_l_inpad),
        .chany_bottom_in(chany_bottom_in_0),
        .chany_top_in(chany_bottom_out),
        .bl_0(bl[88:159]),
        .wl_0(wl[88:159]),
        .chany_bottom_out(chany_bottom_out_0),
        .chany_top_out(chany_bottom_in),
        .grid_right_out(grid_right_out)
    );
endmodule

