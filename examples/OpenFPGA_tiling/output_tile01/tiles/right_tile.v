//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module right_tile
(
    reset,
    clk,
    bottom_width_0_height_0_subtile_0__pin_clk_0_,
    top_width_0_height_0_subtile_0__pin_O_0_,
    top_width_0_height_0_subtile_0__pin_O_4_,
    top_width_0_height_0_subtile_0__pin_O_8_,
    right_width_0_height_0_subtile_0__pin_O_1_,
    right_width_0_height_0_subtile_0__pin_O_5_,
    right_width_0_height_0_subtile_0__pin_O_9_,
    bottom_width_0_height_0_subtile_0__pin_O_2_,
    bottom_width_0_height_0_subtile_0__pin_O_6_,
    left_width_0_height_0_subtile_0__pin_O_3_,
    left_width_0_height_0_subtile_0__pin_O_7_,
    grid_left_in,
    grid_bottom_in,
    chanx_left_in,
    chanx_left_out,
    grid_top_out,
    gfpga_pad_GPIO_PAD,
    io_left_in,
    chany_bottom_in,
    chany_bottom_out,
    chany_top_in_0,
    chany_top_out_0,
    grid_top_r_inpad,
    grid_top_l_in,
    grid_bottom_l_in,
    grid_left_t_in,
    grid_left_b_in,
    bl,
    wl,
    wl_in,
    wl_out,
    bl_in,
    bl_out
);

    input reset;
    input clk;
    input bottom_width_0_height_0_subtile_0__pin_clk_0_;
    output top_width_0_height_0_subtile_0__pin_O_0_;
    output top_width_0_height_0_subtile_0__pin_O_4_;
    output top_width_0_height_0_subtile_0__pin_O_8_;
    output right_width_0_height_0_subtile_0__pin_O_1_;
    output right_width_0_height_0_subtile_0__pin_O_5_;
    output right_width_0_height_0_subtile_0__pin_O_9_;
    output bottom_width_0_height_0_subtile_0__pin_O_2_;
    output bottom_width_0_height_0_subtile_0__pin_O_6_;
    output left_width_0_height_0_subtile_0__pin_O_3_;
    output left_width_0_height_0_subtile_0__pin_O_7_;
    input [0:9]grid_left_in;
    input [0:9]grid_bottom_in;
    input [19:0]chanx_left_in;
    output [19:0]chanx_left_out;
    output [0:9]grid_top_out;
    inout [7:0]gfpga_pad_GPIO_PAD;
    output [0:7]io_left_in;
    input [19:0]chany_bottom_in;
    output [19:0]chany_bottom_out;
    input [19:0]chany_top_in_0;
    output [19:0]chany_top_out_0;
    input [0:7]grid_top_r_inpad;
    input [0:2]grid_top_l_in;
    input [0:2]grid_bottom_l_in;
    input [0:1]grid_left_t_in;
    input [0:2]grid_left_b_in;
    input [0:1259]bl;
    input [0:1259]wl;
    input [3:0]wl_in;
    output [3:0]wl_out;
    input [314:0]bl_in;
    output [314:0]bl_out;

    wire reset;
    wire clk;
    wire bottom_width_0_height_0_subtile_0__pin_clk_0_;
    wire top_width_0_height_0_subtile_0__pin_O_0_;
    wire top_width_0_height_0_subtile_0__pin_O_4_;
    wire top_width_0_height_0_subtile_0__pin_O_8_;
    wire right_width_0_height_0_subtile_0__pin_O_1_;
    wire right_width_0_height_0_subtile_0__pin_O_5_;
    wire right_width_0_height_0_subtile_0__pin_O_9_;
    wire bottom_width_0_height_0_subtile_0__pin_O_2_;
    wire bottom_width_0_height_0_subtile_0__pin_O_6_;
    wire left_width_0_height_0_subtile_0__pin_O_3_;
    wire left_width_0_height_0_subtile_0__pin_O_7_;
    wire [0:9]grid_left_in;
    wire [0:9]grid_top_in;
    wire [0:9]grid_right_in;
    wire [0:9]grid_bottom_in;
    wire [19:0]chanx_left_in;
    wire [19:0]chanx_right_in;
    wire [19:0]chanx_left_out;
    wire [19:0]chanx_right_out;
    wire [0:9]grid_top_out;
    wire [7:0]gfpga_pad_GPIO_PAD;
    wire [0:7]io_left_in;
    wire [19:0]chany_bottom_in;
    wire [19:0]chany_top_in;
    wire [19:0]chany_bottom_out;
    wire [19:0]chany_top_out;
    wire [19:0]chany_top_in_0;
    wire [19:0]chany_top_out_0;
    wire [0:7]grid_top_r_inpad;
    wire [0:2]grid_top_l_in;
    wire [0:2]grid_bottom_l_in;
    wire [0:1]grid_left_t_in;
    wire [0:2]grid_left_b_in;
    wire [0:1259]bl;
    wire [0:1259]wl;
    wire [3:0]wl_in;
    wire [3:0]wl_out;
    wire [314:0]bl_in;
    wire [314:0]bl_out;

assign wl_out = wl_in;
assign bl_out = bl_in;
    grid_clb grid_clb_4__1_
    (
        .reset(reset),
        .clk(clk),
        .bottom_width_0_height_0_subtile_0__pin_clk_0_(bottom_width_0_height_0_subtile_0__pin_clk_0_),
        .bl(bl[0:1019]),
        .wl(wl[0:1019]),
        .top_width_0_height_0_subtile_0__pin_O_0_(top_width_0_height_0_subtile_0__pin_O_0_),
        .top_width_0_height_0_subtile_0__pin_O_4_(top_width_0_height_0_subtile_0__pin_O_4_),
        .top_width_0_height_0_subtile_0__pin_O_8_(top_width_0_height_0_subtile_0__pin_O_8_),
        .right_width_0_height_0_subtile_0__pin_O_1_(right_width_0_height_0_subtile_0__pin_O_1_),
        .right_width_0_height_0_subtile_0__pin_O_5_(right_width_0_height_0_subtile_0__pin_O_5_),
        .right_width_0_height_0_subtile_0__pin_O_9_(right_width_0_height_0_subtile_0__pin_O_9_),
        .bottom_width_0_height_0_subtile_0__pin_O_2_(bottom_width_0_height_0_subtile_0__pin_O_2_),
        .bottom_width_0_height_0_subtile_0__pin_O_6_(bottom_width_0_height_0_subtile_0__pin_O_6_),
        .left_width_0_height_0_subtile_0__pin_O_3_(left_width_0_height_0_subtile_0__pin_O_3_),
        .left_width_0_height_0_subtile_0__pin_O_7_(left_width_0_height_0_subtile_0__pin_O_7_),
        .grid_left_in(grid_left_in),
        .grid_top_in(grid_top_in),
        .grid_right_in(grid_right_in),
        .grid_bottom_in(grid_bottom_in)
    );
    cbx_1__1_ cbx_4__1_
    (
        .chanx_left_in(chanx_left_in),
        .chanx_right_in(chanx_right_in),
        .bl(bl[1020:1099]),
        .wl(wl[1020:1099]),
        .chanx_left_out(chanx_left_out),
        .chanx_right_out(chanx_right_out),
        .grid_top_out(grid_top_out),
        .grid_bottom_out(grid_top_in)
    );
    cby_4__1_ cby_4__1_
    (
        .gfpga_pad_GPIO_PAD(gfpga_pad_GPIO_PAD),
        .bl(bl[1100:1107]),
        .wl(wl[1100:1107]),
        .io_left_in(io_left_in),
        .chany_bottom_in(chany_bottom_in),
        .chany_top_in(chany_top_in),
        .bl_0(bl[1108:1179]),
        .wl_0(wl[1108:1179]),
        .chany_bottom_out(chany_bottom_out),
        .chany_top_out(chany_top_out),
        .grid_left_out(grid_right_in)
    );
    sb_4__1_ sb_4__1_
    (
        .chany_top_in(chany_top_in_0),
        .chany_bottom_in(chany_top_out),
        .chanx_left_in(chanx_right_out),
        .bl(bl[1180:1259]),
        .wl(wl[1180:1259]),
        .chany_top_out(chany_top_out_0),
        .chany_bottom_out(chany_top_in),
        .chanx_left_out(chanx_right_in),
        .grid_top_r_inpad(grid_top_r_inpad),
        .grid_top_l_in(grid_top_l_in),
        .grid_bottom_r_inpad(io_left_in),
        .grid_bottom_l_in(grid_bottom_l_in),
        .grid_left_t_in(grid_left_t_in),
        .grid_left_b_in(grid_left_b_in)
    );
endmodule

