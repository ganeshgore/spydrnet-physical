//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module grid_clb
(
    reset,
    clk,
    bottom_width_0_height_0_subtile_0__pin_clk_0_,
    bl,
    wl,
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
    grid_top_in,
    grid_right_in,
    grid_bottom_in
);

    input reset;
    input clk;
    input bottom_width_0_height_0_subtile_0__pin_clk_0_;
    input [0:1019]bl;
    input [0:1019]wl;
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
    input [0:9]grid_top_in;
    input [0:9]grid_right_in;
    input [0:9]grid_bottom_in;

    wire reset;
    wire clk;
    wire bottom_width_0_height_0_subtile_0__pin_clk_0_;
    wire [0:1019]bl;
    wire [0:1019]wl;
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

    logical_tile_clb_mode_clb_ logical_tile_clb_mode_clb__0
    (
        .reset(reset),
        .clk(clk),
        .clb_I({grid_top_in[0], grid_right_in[0], grid_bottom_in[0], grid_left_in[0], grid_top_in[1], grid_right_in[1], grid_bottom_in[1], grid_left_in[1], grid_top_in[2], grid_right_in[2], grid_bottom_in[2], grid_left_in[2], grid_top_in[3], grid_right_in[3], grid_bottom_in[3], grid_left_in[3], grid_top_in[4], grid_right_in[4], grid_bottom_in[4], grid_left_in[4], grid_top_in[5], grid_right_in[5], grid_bottom_in[5], grid_left_in[5], grid_top_in[6], grid_right_in[6], grid_bottom_in[6], grid_left_in[6], grid_top_in[7], grid_right_in[7], grid_bottom_in[7], grid_left_in[7], grid_top_in[8], grid_right_in[8], grid_bottom_in[8], grid_left_in[8], grid_top_in[9], grid_right_in[9], grid_bottom_in[9], grid_left_in[9]}),
        .clb_clk(bottom_width_0_height_0_subtile_0__pin_clk_0_),
        .bl(bl),
        .wl({wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0], wl[0]}),
        .clb_O({top_width_0_height_0_subtile_0__pin_O_0_, right_width_0_height_0_subtile_0__pin_O_1_, bottom_width_0_height_0_subtile_0__pin_O_2_, left_width_0_height_0_subtile_0__pin_O_3_, top_width_0_height_0_subtile_0__pin_O_4_, right_width_0_height_0_subtile_0__pin_O_5_, bottom_width_0_height_0_subtile_0__pin_O_6_, left_width_0_height_0_subtile_0__pin_O_7_, top_width_0_height_0_subtile_0__pin_O_8_, right_width_0_height_0_subtile_0__pin_O_9_})
    );
endmodule

