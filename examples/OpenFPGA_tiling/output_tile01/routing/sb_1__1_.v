//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module sb_1__1_
(
    chany_top_in,
    chanx_right_in,
    chany_bottom_in,
    chanx_left_in,
    bl,
    wl,
    chany_top_out,
    chanx_right_out,
    chany_bottom_out,
    chanx_left_out,
    grid_top_r_in,
    grid_top_l_in,
    grid_right_t_in,
    grid_right_b_in,
    grid_bottom_r_in,
    grid_bottom_l_in,
    grid_left_t_in,
    grid_left_b_in
);

    input [0:19]chany_top_in;
    input [0:19]chanx_right_in;
    input [0:19]chany_bottom_in;
    input [0:19]chanx_left_in;
    input [0:79]bl;
    input [0:79]wl;
    output [0:19]chany_top_out;
    output [0:19]chanx_right_out;
    output [0:19]chany_bottom_out;
    output [0:19]chanx_left_out;
    input [0:1]grid_top_r_in;
    input [0:2]grid_top_l_in;
    input [0:1]grid_right_t_in;
    input [0:2]grid_right_b_in;
    input [0:1]grid_bottom_r_in;
    input [0:2]grid_bottom_l_in;
    input [0:1]grid_left_t_in;
    input [0:2]grid_left_b_in;

    wire [0:19]chany_top_in;
    wire [0:19]chanx_right_in;
    wire [0:19]chany_bottom_in;
    wire [0:19]chanx_left_in;
    wire [0:79]bl;
    wire [0:79]wl;
    wire [0:19]chany_top_out;
    wire [0:19]chanx_right_out;
    wire [0:19]chany_bottom_out;
    wire [0:19]chanx_left_out;
    wire [0:3]mux2_size12_0_sram;
    wire [0:3]mux2_size12_0_sram_inv;
    wire [0:3]mux2_size12_10_sram;
    wire [0:3]mux2_size12_10_sram_inv;
    wire [0:3]mux2_size12_11_sram;
    wire [0:3]mux2_size12_11_sram_inv;
    wire [0:3]mux2_size12_12_sram;
    wire [0:3]mux2_size12_12_sram_inv;
    wire [0:3]mux2_size12_13_sram;
    wire [0:3]mux2_size12_13_sram_inv;
    wire [0:3]mux2_size12_14_sram;
    wire [0:3]mux2_size12_14_sram_inv;
    wire [0:3]mux2_size12_15_sram;
    wire [0:3]mux2_size12_15_sram_inv;
    wire [0:3]mux2_size12_16_sram;
    wire [0:3]mux2_size12_16_sram_inv;
    wire [0:3]mux2_size12_17_sram;
    wire [0:3]mux2_size12_17_sram_inv;
    wire [0:3]mux2_size12_18_sram;
    wire [0:3]mux2_size12_18_sram_inv;
    wire [0:3]mux2_size12_19_sram;
    wire [0:3]mux2_size12_19_sram_inv;
    wire [0:3]mux2_size12_1_sram;
    wire [0:3]mux2_size12_1_sram_inv;
    wire [0:3]mux2_size12_2_sram;
    wire [0:3]mux2_size12_2_sram_inv;
    wire [0:3]mux2_size12_3_sram;
    wire [0:3]mux2_size12_3_sram_inv;
    wire [0:3]mux2_size12_4_sram;
    wire [0:3]mux2_size12_4_sram_inv;
    wire [0:3]mux2_size12_5_sram;
    wire [0:3]mux2_size12_5_sram_inv;
    wire [0:3]mux2_size12_6_sram;
    wire [0:3]mux2_size12_6_sram_inv;
    wire [0:3]mux2_size12_7_sram;
    wire [0:3]mux2_size12_7_sram_inv;
    wire [0:3]mux2_size12_8_sram;
    wire [0:3]mux2_size12_8_sram_inv;
    wire [0:3]mux2_size12_9_sram;
    wire [0:3]mux2_size12_9_sram_inv;
    wire [0:1]grid_top_r_in;
    wire [0:2]grid_top_l_in;
    wire [0:1]grid_right_t_in;
    wire [0:2]grid_right_b_in;
    wire [0:1]grid_bottom_r_in;
    wire [0:2]grid_bottom_l_in;
    wire [0:1]grid_left_t_in;
    wire [0:2]grid_left_b_in;

assign chany_bottom_out[1] = chany_top_in[0];
assign chany_bottom_out[2] = chany_top_in[1];
assign chany_bottom_out[3] = chany_top_in[2];
assign chany_bottom_out[5] = chany_top_in[4];
assign chany_bottom_out[6] = chany_top_in[5];
assign chany_bottom_out[7] = chany_top_in[6];
assign chany_bottom_out[9] = chany_top_in[8];
assign chany_bottom_out[10] = chany_top_in[9];
assign chany_bottom_out[11] = chany_top_in[10];
assign chany_bottom_out[13] = chany_top_in[12];
assign chany_bottom_out[14] = chany_top_in[13];
assign chany_bottom_out[15] = chany_top_in[14];
assign chany_bottom_out[17] = chany_top_in[16];
assign chany_bottom_out[18] = chany_top_in[17];
assign chany_bottom_out[19] = chany_top_in[18];
assign chanx_left_out[1] = chanx_right_in[0];
assign chanx_left_out[2] = chanx_right_in[1];
assign chanx_left_out[3] = chanx_right_in[2];
assign chanx_left_out[5] = chanx_right_in[4];
assign chanx_left_out[6] = chanx_right_in[5];
assign chanx_left_out[7] = chanx_right_in[6];
assign chanx_left_out[9] = chanx_right_in[8];
assign chanx_left_out[10] = chanx_right_in[9];
assign chanx_left_out[11] = chanx_right_in[10];
assign chanx_left_out[13] = chanx_right_in[12];
assign chanx_left_out[14] = chanx_right_in[13];
assign chanx_left_out[15] = chanx_right_in[14];
assign chanx_left_out[17] = chanx_right_in[16];
assign chanx_left_out[18] = chanx_right_in[17];
assign chanx_left_out[19] = chanx_right_in[18];
assign chany_top_out[1] = chany_bottom_in[0];
assign chany_top_out[2] = chany_bottom_in[1];
assign chany_top_out[3] = chany_bottom_in[2];
assign chany_top_out[5] = chany_bottom_in[4];
assign chany_top_out[6] = chany_bottom_in[5];
assign chany_top_out[7] = chany_bottom_in[6];
assign chany_top_out[9] = chany_bottom_in[8];
assign chany_top_out[10] = chany_bottom_in[9];
assign chany_top_out[11] = chany_bottom_in[10];
assign chany_top_out[13] = chany_bottom_in[12];
assign chany_top_out[14] = chany_bottom_in[13];
assign chany_top_out[15] = chany_bottom_in[14];
assign chany_top_out[17] = chany_bottom_in[16];
assign chany_top_out[18] = chany_bottom_in[17];
assign chany_top_out[19] = chany_bottom_in[18];
assign chanx_right_out[1] = chanx_left_in[0];
assign chanx_right_out[2] = chanx_left_in[1];
assign chanx_right_out[3] = chanx_left_in[2];
assign chanx_right_out[5] = chanx_left_in[4];
assign chanx_right_out[6] = chanx_left_in[5];
assign chanx_right_out[7] = chanx_left_in[6];
assign chanx_right_out[9] = chanx_left_in[8];
assign chanx_right_out[10] = chanx_left_in[9];
assign chanx_right_out[11] = chanx_left_in[10];
assign chanx_right_out[13] = chanx_left_in[12];
assign chanx_right_out[14] = chanx_left_in[13];
assign chanx_right_out[15] = chanx_left_in[14];
assign chanx_right_out[17] = chanx_left_in[16];
assign chanx_right_out[18] = chanx_left_in[17];
assign chanx_right_out[19] = chanx_left_in[18];
    mux2_size12 mux_top_track_0
    (
        .in({grid_top_l_in[0], chanx_right_in[1], chanx_right_in[7], chanx_right_in[8], chanx_right_in[14], chany_bottom_in[0], chany_bottom_in[6], chany_bottom_in[13], chanx_left_in[0], chanx_left_in[3], chanx_left_in[6], chanx_left_in[13]}),
        .sram(mux2_size12_0_sram),
        .sram_inv(mux2_size12_0_sram_inv),
        .out(chany_top_out[0])
    );
    mux2_size12 mux_top_track_8
    (
        .in({grid_top_l_in[1], chanx_right_in[2], chanx_right_in[9], chanx_right_in[11], chanx_right_in[16], chany_bottom_in[1], chany_bottom_in[8], chany_bottom_in[14], chanx_left_in[5], chanx_left_in[12], chanx_left_in[18], chanx_left_in[19]}),
        .sram(mux2_size12_1_sram),
        .sram_inv(mux2_size12_1_sram_inv),
        .out(chany_top_out[4])
    );
    mux2_size12 mux_top_track_16
    (
        .in({grid_top_l_in[2], chanx_right_in[4], chanx_right_in[10], chanx_right_in[15], chanx_right_in[17], chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[16], chanx_left_in[4], chanx_left_in[10], chanx_left_in[15], chanx_left_in[17]}),
        .sram(mux2_size12_2_sram),
        .sram_inv(mux2_size12_2_sram_inv),
        .out(chany_top_out[8])
    );
    mux2_size12 mux_top_track_24
    (
        .in({grid_top_r_in[0], chanx_right_in[5], chanx_right_in[12], chanx_right_in[18], chanx_right_in[19], chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[17], chanx_left_in[2], chanx_left_in[9], chanx_left_in[11], chanx_left_in[16]}),
        .sram(mux2_size12_3_sram),
        .sram_inv(mux2_size12_3_sram_inv),
        .out(chany_top_out[12])
    );
    mux2_size12 mux_top_track_32
    (
        .in({grid_top_r_in[1], chanx_right_in[0], chanx_right_in[3], chanx_right_in[6], chanx_right_in[13], chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18], chanx_left_in[1], chanx_left_in[7], chanx_left_in[8], chanx_left_in[14]}),
        .sram(mux2_size12_4_sram),
        .sram_inv(mux2_size12_4_sram_inv),
        .out(chany_top_out[16])
    );
    mux2_size12 mux_right_track_0
    (
        .in({chany_top_in[5], chany_top_in[12], chany_top_in[18], chany_top_in[19], grid_right_t_in[0], chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[15], chany_bottom_in[17], chanx_left_in[0], chanx_left_in[6], chanx_left_in[13]}),
        .sram(mux2_size12_5_sram),
        .sram_inv(mux2_size12_5_sram_inv),
        .out(chanx_right_out[0])
    );
    mux2_size12 mux_right_track_8
    (
        .in({chany_top_in[0], chany_top_in[3], chany_top_in[6], chany_top_in[13], grid_right_t_in[1], chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[11], chany_bottom_in[16], chanx_left_in[1], chanx_left_in[8], chanx_left_in[14]}),
        .sram(mux2_size12_6_sram),
        .sram_inv(mux2_size12_6_sram_inv),
        .out(chanx_right_out[4])
    );
    mux2_size12 mux_right_track_16
    (
        .in({chany_top_in[1], chany_top_in[7], chany_top_in[8], chany_top_in[14], grid_right_b_in[0], chany_bottom_in[1], chany_bottom_in[7], chany_bottom_in[8], chany_bottom_in[14], chanx_left_in[2], chanx_left_in[9], chanx_left_in[16]}),
        .sram(mux2_size12_7_sram),
        .sram_inv(mux2_size12_7_sram_inv),
        .out(chanx_right_out[8])
    );
    mux2_size12 mux_right_track_24
    (
        .in({chany_top_in[2], chany_top_in[9], chany_top_in[11], chany_top_in[16], grid_right_b_in[1], chany_bottom_in[0], chany_bottom_in[3], chany_bottom_in[6], chany_bottom_in[13], chanx_left_in[4], chanx_left_in[10], chanx_left_in[17]}),
        .sram(mux2_size12_8_sram),
        .sram_inv(mux2_size12_8_sram_inv),
        .out(chanx_right_out[12])
    );
    mux2_size12 mux_right_track_32
    (
        .in({chany_top_in[4], chany_top_in[10], chany_top_in[15], chany_top_in[17], grid_right_b_in[2], chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18], chany_bottom_in[19], chanx_left_in[5], chanx_left_in[12], chanx_left_in[18]}),
        .sram(mux2_size12_9_sram),
        .sram_inv(mux2_size12_9_sram_inv),
        .out(chanx_right_out[16])
    );
    mux2_size12 mux_bottom_track_1
    (
        .in({chany_top_in[0], chany_top_in[6], chany_top_in[13], chanx_right_in[4], chanx_right_in[10], chanx_right_in[15], chanx_right_in[17], grid_bottom_r_in[0], chanx_left_in[1], chanx_left_in[7], chanx_left_in[8], chanx_left_in[14]}),
        .sram(mux2_size12_10_sram),
        .sram_inv(mux2_size12_10_sram_inv),
        .out(chany_bottom_out[0])
    );
    mux2_size12 mux_bottom_track_9
    (
        .in({chany_top_in[1], chany_top_in[8], chany_top_in[14], chanx_right_in[2], chanx_right_in[9], chanx_right_in[11], chanx_right_in[16], grid_bottom_r_in[1], chanx_left_in[2], chanx_left_in[9], chanx_left_in[11], chanx_left_in[16]}),
        .sram(mux2_size12_11_sram),
        .sram_inv(mux2_size12_11_sram_inv),
        .out(chany_bottom_out[4])
    );
    mux2_size12 mux_bottom_track_17
    (
        .in({chany_top_in[2], chany_top_in[9], chany_top_in[16], chanx_right_in[1], chanx_right_in[7], chanx_right_in[8], chanx_right_in[14], grid_bottom_l_in[0], chanx_left_in[4], chanx_left_in[10], chanx_left_in[15], chanx_left_in[17]}),
        .sram(mux2_size12_12_sram),
        .sram_inv(mux2_size12_12_sram_inv),
        .out(chany_bottom_out[8])
    );
    mux2_size12 mux_bottom_track_25
    (
        .in({chany_top_in[4], chany_top_in[10], chany_top_in[17], chanx_right_in[0], chanx_right_in[3], chanx_right_in[6], chanx_right_in[13], grid_bottom_l_in[1], chanx_left_in[5], chanx_left_in[12], chanx_left_in[18], chanx_left_in[19]}),
        .sram(mux2_size12_13_sram),
        .sram_inv(mux2_size12_13_sram_inv),
        .out(chany_bottom_out[12])
    );
    mux2_size12 mux_bottom_track_33
    (
        .in({chany_top_in[5], chany_top_in[12], chany_top_in[18], chanx_right_in[5], chanx_right_in[12], chanx_right_in[18], chanx_right_in[19], grid_bottom_l_in[2], chanx_left_in[0], chanx_left_in[3], chanx_left_in[6], chanx_left_in[13]}),
        .sram(mux2_size12_14_sram),
        .sram_inv(mux2_size12_14_sram_inv),
        .out(chany_bottom_out[16])
    );
    mux2_size12 mux_left_track_1
    (
        .in({chany_top_in[0], chany_top_in[3], chany_top_in[6], chany_top_in[13], chanx_right_in[0], chanx_right_in[6], chanx_right_in[13], chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18], chany_bottom_in[19], grid_left_t_in[0]}),
        .sram(mux2_size12_15_sram),
        .sram_inv(mux2_size12_15_sram_inv),
        .out(chanx_left_out[0])
    );
    mux2_size12 mux_left_track_9
    (
        .in({chany_top_in[5], chany_top_in[12], chany_top_in[18], chany_top_in[19], chanx_right_in[1], chanx_right_in[8], chanx_right_in[14], chany_bottom_in[0], chany_bottom_in[3], chany_bottom_in[6], chany_bottom_in[13], grid_left_t_in[1]}),
        .sram(mux2_size12_16_sram),
        .sram_inv(mux2_size12_16_sram_inv),
        .out(chanx_left_out[4])
    );
    mux2_size12 mux_left_track_17
    (
        .in({chany_top_in[4], chany_top_in[10], chany_top_in[15], chany_top_in[17], chanx_right_in[2], chanx_right_in[9], chanx_right_in[16], chany_bottom_in[1], chany_bottom_in[7], chany_bottom_in[8], chany_bottom_in[14], grid_left_b_in[0]}),
        .sram(mux2_size12_17_sram),
        .sram_inv(mux2_size12_17_sram_inv),
        .out(chanx_left_out[8])
    );
    mux2_size12 mux_left_track_25
    (
        .in({chany_top_in[2], chany_top_in[9], chany_top_in[11], chany_top_in[16], chanx_right_in[4], chanx_right_in[10], chanx_right_in[17], chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[11], chany_bottom_in[16], grid_left_b_in[1]}),
        .sram(mux2_size12_18_sram),
        .sram_inv(mux2_size12_18_sram_inv),
        .out(chanx_left_out[12])
    );
    mux2_size12 mux_left_track_33
    (
        .in({chany_top_in[1], chany_top_in[7], chany_top_in[8], chany_top_in[14], chanx_right_in[5], chanx_right_in[12], chanx_right_in[18], chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[15], chany_bottom_in[17], grid_left_b_in[2]}),
        .sram(mux2_size12_19_sram),
        .sram_inv(mux2_size12_19_sram_inv),
        .out(chanx_left_out[16])
    );
    mux2_size12_mem mem_top_track_0
    (
        .bl(bl[0:3]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_0_sram),
        .mem_outb(mux2_size12_0_sram_inv)
    );
    mux2_size12_mem mem_top_track_8
    (
        .bl(bl[4:7]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_1_sram),
        .mem_outb(mux2_size12_1_sram_inv)
    );
    mux2_size12_mem mem_top_track_16
    (
        .bl(bl[8:11]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_2_sram),
        .mem_outb(mux2_size12_2_sram_inv)
    );
    mux2_size12_mem mem_top_track_24
    (
        .bl(bl[12:15]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_3_sram),
        .mem_outb(mux2_size12_3_sram_inv)
    );
    mux2_size12_mem mem_top_track_32
    (
        .bl(bl[16:19]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_4_sram),
        .mem_outb(mux2_size12_4_sram_inv)
    );
    mux2_size12_mem mem_right_track_0
    (
        .bl(bl[20:23]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_5_sram),
        .mem_outb(mux2_size12_5_sram_inv)
    );
    mux2_size12_mem mem_right_track_8
    (
        .bl(bl[24:27]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_6_sram),
        .mem_outb(mux2_size12_6_sram_inv)
    );
    mux2_size12_mem mem_right_track_16
    (
        .bl(bl[28:31]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_7_sram),
        .mem_outb(mux2_size12_7_sram_inv)
    );
    mux2_size12_mem mem_right_track_24
    (
        .bl(bl[32:35]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_8_sram),
        .mem_outb(mux2_size12_8_sram_inv)
    );
    mux2_size12_mem mem_right_track_32
    (
        .bl(bl[36:39]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_9_sram),
        .mem_outb(mux2_size12_9_sram_inv)
    );
    mux2_size12_mem mem_bottom_track_1
    (
        .bl(bl[40:43]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_10_sram),
        .mem_outb(mux2_size12_10_sram_inv)
    );
    mux2_size12_mem mem_bottom_track_9
    (
        .bl(bl[44:47]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_11_sram),
        .mem_outb(mux2_size12_11_sram_inv)
    );
    mux2_size12_mem mem_bottom_track_17
    (
        .bl(bl[48:51]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_12_sram),
        .mem_outb(mux2_size12_12_sram_inv)
    );
    mux2_size12_mem mem_bottom_track_25
    (
        .bl(bl[52:55]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_13_sram),
        .mem_outb(mux2_size12_13_sram_inv)
    );
    mux2_size12_mem mem_bottom_track_33
    (
        .bl(bl[56:59]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_14_sram),
        .mem_outb(mux2_size12_14_sram_inv)
    );
    mux2_size12_mem mem_left_track_1
    (
        .bl(bl[60:63]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_15_sram),
        .mem_outb(mux2_size12_15_sram_inv)
    );
    mux2_size12_mem mem_left_track_9
    (
        .bl(bl[64:67]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_16_sram),
        .mem_outb(mux2_size12_16_sram_inv)
    );
    mux2_size12_mem mem_left_track_17
    (
        .bl(bl[68:71]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_17_sram),
        .mem_outb(mux2_size12_17_sram_inv)
    );
    mux2_size12_mem mem_left_track_25
    (
        .bl(bl[72:75]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_18_sram),
        .mem_outb(mux2_size12_18_sram_inv)
    );
    mux2_size12_mem mem_left_track_33
    (
        .bl(bl[76:79]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size12_19_sram),
        .mem_outb(mux2_size12_19_sram_inv)
    );
endmodule

