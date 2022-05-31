//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module bottom_right_tile
(
    gfpga_pad_GPIO_PAD,
    io_top_in,
    chanx_left_in,
    chanx_left_out,
    grid_top_out,
    chany_top_in,
    chany_top_out,
    grid_top_r_inpad,
    grid_top_l_in,
    grid_left_t_in,
    wl_in,
    wl_out,
    bl_in,
    bl_out
);

    inout [7:0]gfpga_pad_GPIO_PAD;
    output [0:7]io_top_in;
    input [19:0]chanx_left_in;
    output [19:0]chanx_left_out;
    output [0:9]grid_top_out;
    input [19:0]chany_top_in;
    output [19:0]chany_top_out;
    input [0:7]grid_top_r_inpad;
    input [0:2]grid_top_l_in;
    input [0:1]grid_left_t_in;
    input [3:0]wl_in;
    output [3:0]wl_out;
    input [314:0]bl_in;
    output [314:0]bl_out;

    wire [7:0]gfpga_pad_GPIO_PAD;
    wire [0:7]io_top_in;
    wire [19:0]chanx_left_in;
    wire [19:0]chanx_right_in;
    wire [19:0]chanx_left_out;
    wire [19:0]chanx_right_out;
    wire [0:9]grid_top_out;
    wire [19:0]chany_top_in;
    wire [19:0]chany_top_out;
    wire [0:7]grid_top_r_inpad;
    wire [0:2]grid_top_l_in;
    wire [0:1]grid_left_t_in;
    wire [0:159]bl;
    wire [0:159]wl;
    wire [3:0]wl_in;
    wire [3:0]wl_out;
    wire [314:0]bl_in;
    wire [314:0]bl_out;

assign wl_out = wl_in;
assign bl_out = bl_in;
    cbx_1__0_ cbx_4__0_
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD),
        .bl(bl[0:7]),
        .wl(wl[0:7]),
        .io_top_in(io_top_in),
        .chanx_left_in(chanx_left_in),
        .chanx_right_in(chanx_right_in),
        .bl_0(bl[8:79]),
        .wl_0(wl[8:79]),
        .chanx_left_out(chanx_left_out),
        .chanx_right_out(chanx_right_out),
        .grid_top_out(grid_top_out)
    );
    sb_4__0_ sb_4__0_
    (
        .chany_top_in(chany_top_in),
        .chanx_left_in(chanx_right_out),
        .bl(bl[80:159]),
        .wl(wl[80:159]),
        .chany_top_out(chany_top_out),
        .chanx_left_out(chanx_right_in),
        .grid_top_r_inpad(grid_top_r_inpad),
        .grid_top_l_in(grid_top_l_in),
        .grid_left_t_in(grid_left_t_in),
        .grid_left_b_inpad(io_top_in)
    );
endmodule

