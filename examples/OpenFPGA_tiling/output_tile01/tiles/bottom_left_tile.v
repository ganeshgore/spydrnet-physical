//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module bottom_left_tile
(
    chany_top_in,
    chanx_right_in,
    chany_top_out,
    chanx_right_out,
    grid_top_r_in,
    grid_top_l_inpad,
    grid_right_t_in,
    grid_right_b_inpad,
    wl_in,
    wl_out,
    bl_in,
    bl_out
);

    input [19:0]chany_top_in;
    input [19:0]chanx_right_in;
    output [19:0]chany_top_out;
    output [19:0]chanx_right_out;
    input [0:1]grid_top_r_in;
    input [0:7]grid_top_l_inpad;
    input [0:1]grid_right_t_in;
    input [0:7]grid_right_b_inpad;
    input [3:0]wl_in;
    output [3:0]wl_out;
    input [39:0]bl_in;
    output [39:0]bl_out;

    wire [19:0]chany_top_in;
    wire [19:0]chanx_right_in;
    wire [19:0]chany_top_out;
    wire [19:0]chanx_right_out;
    wire [0:1]grid_top_r_in;
    wire [0:7]grid_top_l_inpad;
    wire [0:1]grid_right_t_in;
    wire [0:7]grid_right_b_inpad;
    wire [0:79]bl;
    wire [0:79]wl;
    wire [3:0]wl_in;
    wire [3:0]wl_out;
    wire [39:0]bl_in;
    wire [39:0]bl_out;

assign wl_out = wl_in;
assign bl_out = bl_in;
    sb_0__0_ sb_0__0_
    (
        .chany_top_in(chany_top_in),
        .chanx_right_in(chanx_right_in),
        .bl(bl),
        .wl(wl),
        .chany_top_out(chany_top_out),
        .chanx_right_out(chanx_right_out),
        .grid_top_r_in(grid_top_r_in),
        .grid_top_l_inpad(grid_top_l_inpad),
        .grid_right_t_in(grid_right_t_in),
        .grid_right_b_inpad(grid_right_b_inpad)
    );
endmodule

