//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module sb_0__1_
(
    chany_top_in,
    chanx_right_in,
    chany_bottom_in,
    bl,
    wl,
    chany_top_out,
    chanx_right_out,
    chany_bottom_out,
    grid_top_r_in,
    grid_top_l_inpad,
    grid_right_t_in,
    grid_right_b_in,
    grid_bottom_r_in,
    grid_bottom_l_inpad
);

    input [0:19]chany_top_in;
    input [0:19]chanx_right_in;
    input [0:19]chany_bottom_in;
    input [0:77]bl;
    input [0:77]wl;
    output [0:19]chany_top_out;
    output [0:19]chanx_right_out;
    output [0:19]chany_bottom_out;
    input [0:1]grid_top_r_in;
    input [0:7]grid_top_l_inpad;
    input [0:1]grid_right_t_in;
    input [0:2]grid_right_b_in;
    input [0:1]grid_bottom_r_in;
    input [0:7]grid_bottom_l_inpad;

    wire [0:19]chany_top_in;
    wire [0:19]chanx_right_in;
    wire [0:19]chany_bottom_in;
    wire [0:77]bl;
    wire [0:77]wl;
    wire [0:19]chany_top_out;
    wire [0:19]chanx_right_out;
    wire [0:19]chany_bottom_out;
    wire [0:1]mux2_size2_0_sram;
    wire [0:1]mux2_size2_0_sram_inv;
    wire [0:1]mux2_size2_1_sram;
    wire [0:1]mux2_size2_1_sram_inv;
    wire [0:1]mux2_size2_2_sram;
    wire [0:1]mux2_size2_2_sram_inv;
    wire [0:1]mux2_size2_3_sram;
    wire [0:1]mux2_size2_3_sram_inv;
    wire [0:1]mux2_size2_4_sram;
    wire [0:1]mux2_size2_4_sram_inv;
    wire [0:1]mux2_size2_5_sram;
    wire [0:1]mux2_size2_5_sram_inv;
    wire [0:1]mux2_size2_6_sram;
    wire [0:1]mux2_size2_6_sram_inv;
    wire [0:1]mux2_size3_0_sram;
    wire [0:1]mux2_size3_0_sram_inv;
    wire [0:1]mux2_size3_1_sram;
    wire [0:1]mux2_size3_1_sram_inv;
    wire [0:1]mux2_size3_2_sram;
    wire [0:1]mux2_size3_2_sram_inv;
    wire [0:1]mux2_size3_3_sram;
    wire [0:1]mux2_size3_3_sram_inv;
    wire [0:1]mux2_size3_4_sram;
    wire [0:1]mux2_size3_4_sram_inv;
    wire [0:1]mux2_size3_5_sram;
    wire [0:1]mux2_size3_5_sram_inv;
    wire [0:1]mux2_size3_6_sram;
    wire [0:1]mux2_size3_6_sram_inv;
    wire [0:1]mux2_size3_7_sram;
    wire [0:1]mux2_size3_7_sram_inv;
    wire [0:1]mux2_size3_8_sram;
    wire [0:1]mux2_size3_8_sram_inv;
    wire [0:2]mux2_size4_0_sram;
    wire [0:2]mux2_size4_0_sram_inv;
    wire [0:2]mux2_size4_1_sram;
    wire [0:2]mux2_size4_1_sram_inv;
    wire [0:3]mux2_size9_0_sram;
    wire [0:3]mux2_size9_0_sram_inv;
    wire [0:3]mux2_size9_1_sram;
    wire [0:3]mux2_size9_1_sram_inv;
    wire [0:3]mux2_size9_2_sram;
    wire [0:3]mux2_size9_2_sram_inv;
    wire [0:3]mux2_size9_3_sram;
    wire [0:3]mux2_size9_3_sram_inv;
    wire [0:3]mux2_size9_4_sram;
    wire [0:3]mux2_size9_4_sram_inv;
    wire [0:3]mux2_size9_5_sram;
    wire [0:3]mux2_size9_5_sram_inv;
    wire [0:3]mux2_size9_6_sram;
    wire [0:3]mux2_size9_6_sram_inv;
    wire [0:3]mux2_size9_7_sram;
    wire [0:3]mux2_size9_7_sram_inv;
    wire [0:3]mux2_size9_8_sram;
    wire [0:3]mux2_size9_8_sram_inv;
    wire [0:3]mux2_size9_9_sram;
    wire [0:3]mux2_size9_9_sram_inv;
    wire [0:1]grid_top_r_in;
    wire [0:7]grid_top_l_inpad;
    wire [0:1]grid_right_t_in;
    wire [0:2]grid_right_b_in;
    wire [0:1]grid_bottom_r_in;
    wire [0:7]grid_bottom_l_inpad;

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
assign chanx_right_out[0] = grid_right_t_in[0];
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
    mux2_size9 mux_top_track_0
    (
        .in({grid_top_l_inpad[0], grid_top_l_inpad[5], chanx_right_in[1], chanx_right_in[6], chanx_right_in[11], chanx_right_in[16], chany_bottom_in[0], chany_bottom_in[6], chany_bottom_in[13]}),
        .sram(mux2_size9_0_sram),
        .sram_inv(mux2_size9_0_sram_inv),
        .out(chany_top_out[0])
    );
    mux2_size9 mux_top_track_8
    (
        .in({grid_top_l_inpad[1], grid_top_l_inpad[6], chanx_right_in[2], chanx_right_in[7], chanx_right_in[12], chanx_right_in[17], chany_bottom_in[1], chany_bottom_in[8], chany_bottom_in[14]}),
        .sram(mux2_size9_1_sram),
        .sram_inv(mux2_size9_1_sram_inv),
        .out(chany_top_out[4])
    );
    mux2_size9 mux_top_track_16
    (
        .in({grid_top_l_inpad[2], grid_top_l_inpad[7], chanx_right_in[3], chanx_right_in[8], chanx_right_in[13], chanx_right_in[18], chany_bottom_in[2], chany_bottom_in[9], chany_bottom_in[16]}),
        .sram(mux2_size9_2_sram),
        .sram_inv(mux2_size9_2_sram_inv),
        .out(chany_top_out[8])
    );
    mux2_size9 mux_top_track_24
    (
        .in({grid_top_l_inpad[3], grid_top_r_in[0], chanx_right_in[4], chanx_right_in[9], chanx_right_in[14], chanx_right_in[19], chany_bottom_in[4], chany_bottom_in[10], chany_bottom_in[17]}),
        .sram(mux2_size9_3_sram),
        .sram_inv(mux2_size9_3_sram_inv),
        .out(chany_top_out[12])
    );
    mux2_size9 mux_top_track_32
    (
        .in({grid_top_l_inpad[4], grid_top_r_in[1], chanx_right_in[0], chanx_right_in[5], chanx_right_in[10], chanx_right_in[15], chany_bottom_in[5], chany_bottom_in[12], chany_bottom_in[18]}),
        .sram(mux2_size9_4_sram),
        .sram_inv(mux2_size9_4_sram_inv),
        .out(chany_top_out[16])
    );
    mux2_size9 mux_bottom_track_1
    (
        .in({chany_top_in[0], chany_top_in[6], chany_top_in[13], chanx_right_in[3], chanx_right_in[8], chanx_right_in[13], chanx_right_in[18], grid_bottom_r_in[0], grid_bottom_l_inpad[3]}),
        .sram(mux2_size9_5_sram),
        .sram_inv(mux2_size9_5_sram_inv),
        .out(chany_bottom_out[0])
    );
    mux2_size9 mux_bottom_track_9
    (
        .in({chany_top_in[1], chany_top_in[8], chany_top_in[14], chanx_right_in[2], chanx_right_in[7], chanx_right_in[12], chanx_right_in[17], grid_bottom_r_in[1], grid_bottom_l_inpad[4]}),
        .sram(mux2_size9_6_sram),
        .sram_inv(mux2_size9_6_sram_inv),
        .out(chany_bottom_out[4])
    );
    mux2_size9 mux_bottom_track_17
    (
        .in({chany_top_in[2], chany_top_in[9], chany_top_in[16], chanx_right_in[1], chanx_right_in[6], chanx_right_in[11], chanx_right_in[16], grid_bottom_l_inpad[0], grid_bottom_l_inpad[5]}),
        .sram(mux2_size9_7_sram),
        .sram_inv(mux2_size9_7_sram_inv),
        .out(chany_bottom_out[8])
    );
    mux2_size9 mux_bottom_track_25
    (
        .in({chany_top_in[4], chany_top_in[10], chany_top_in[17], chanx_right_in[0], chanx_right_in[5], chanx_right_in[10], chanx_right_in[15], grid_bottom_l_inpad[1], grid_bottom_l_inpad[6]}),
        .sram(mux2_size9_8_sram),
        .sram_inv(mux2_size9_8_sram_inv),
        .out(chany_bottom_out[12])
    );
    mux2_size9 mux_bottom_track_33
    (
        .in({chany_top_in[5], chany_top_in[12], chany_top_in[18], chanx_right_in[4], chanx_right_in[9], chanx_right_in[14], chanx_right_in[19], grid_bottom_l_inpad[2], grid_bottom_l_inpad[7]}),
        .sram(mux2_size9_9_sram),
        .sram_inv(mux2_size9_9_sram_inv),
        .out(chany_bottom_out[16])
    );
    mux2_size9_mem mem_top_track_0
    (
        .bl(bl[0:3]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_0_sram),
        .mem_outb(mux2_size9_0_sram_inv)
    );
    mux2_size9_mem mem_top_track_8
    (
        .bl(bl[4:7]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_1_sram),
        .mem_outb(mux2_size9_1_sram_inv)
    );
    mux2_size9_mem mem_top_track_16
    (
        .bl(bl[8:11]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_2_sram),
        .mem_outb(mux2_size9_2_sram_inv)
    );
    mux2_size9_mem mem_top_track_24
    (
        .bl(bl[12:15]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_3_sram),
        .mem_outb(mux2_size9_3_sram_inv)
    );
    mux2_size9_mem mem_top_track_32
    (
        .bl(bl[16:19]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_4_sram),
        .mem_outb(mux2_size9_4_sram_inv)
    );
    mux2_size9_mem mem_bottom_track_1
    (
        .bl(bl[58:61]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_5_sram),
        .mem_outb(mux2_size9_5_sram_inv)
    );
    mux2_size9_mem mem_bottom_track_9
    (
        .bl(bl[62:65]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_6_sram),
        .mem_outb(mux2_size9_6_sram_inv)
    );
    mux2_size9_mem mem_bottom_track_17
    (
        .bl(bl[66:69]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_7_sram),
        .mem_outb(mux2_size9_7_sram_inv)
    );
    mux2_size9_mem mem_bottom_track_25
    (
        .bl(bl[70:73]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_8_sram),
        .mem_outb(mux2_size9_8_sram_inv)
    );
    mux2_size9_mem mem_bottom_track_33
    (
        .bl(bl[74:77]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_9_sram),
        .mem_outb(mux2_size9_9_sram_inv)
    );
    mux2_size3 mux_right_track_2
    (
        .in({chany_top_in[0], chany_top_in[3], grid_right_t_in[1]}),
        .sram(mux2_size3_0_sram),
        .sram_inv(mux2_size3_0_sram_inv),
        .out(chanx_right_out[1])
    );
    mux2_size3 mux_right_track_4
    (
        .in({chany_top_in[1], chany_top_in[7], grid_right_b_in[0]}),
        .sram(mux2_size3_1_sram),
        .sram_inv(mux2_size3_1_sram_inv),
        .out(chanx_right_out[2])
    );
    mux2_size3 mux_right_track_6
    (
        .in({chany_top_in[2], chany_top_in[11], grid_right_b_in[1]}),
        .sram(mux2_size3_2_sram),
        .sram_inv(mux2_size3_2_sram_inv),
        .out(chanx_right_out[3])
    );
    mux2_size3 mux_right_track_10
    (
        .in({chany_top_in[5], chany_top_in[19], chany_bottom_in[17]}),
        .sram(mux2_size3_3_sram),
        .sram_inv(mux2_size3_3_sram_inv),
        .out(chanx_right_out[5])
    );
    mux2_size3 mux_right_track_20
    (
        .in({chany_top_in[12], grid_right_t_in[0], chany_bottom_in[10]}),
        .sram(mux2_size3_4_sram),
        .sram_inv(mux2_size3_4_sram_inv),
        .out(chanx_right_out[10])
    );
    mux2_size3 mux_right_track_22
    (
        .in({chany_top_in[13], grid_right_t_in[1], chany_bottom_in[9]}),
        .sram(mux2_size3_5_sram),
        .sram_inv(mux2_size3_5_sram_inv),
        .out(chanx_right_out[11])
    );
    mux2_size3 mux_right_track_24
    (
        .in({chany_top_in[14], grid_right_b_in[0], chany_bottom_in[8]}),
        .sram(mux2_size3_6_sram),
        .sram_inv(mux2_size3_6_sram_inv),
        .out(chanx_right_out[12])
    );
    mux2_size3 mux_right_track_26
    (
        .in({chany_top_in[16], grid_right_b_in[1], chany_bottom_in[6]}),
        .sram(mux2_size3_7_sram),
        .sram_inv(mux2_size3_7_sram_inv),
        .out(chanx_right_out[13])
    );
    mux2_size3 mux_right_track_30
    (
        .in({chany_top_in[18], chany_bottom_in[4], chany_bottom_in[15]}),
        .sram(mux2_size3_8_sram),
        .sram_inv(mux2_size3_8_sram_inv),
        .out(chanx_right_out[15])
    );
    mux2_size3_mem mem_right_track_2
    (
        .bl(bl[20:21]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_0_sram),
        .mem_outb(mux2_size3_0_sram_inv)
    );
    mux2_size3_mem mem_right_track_4
    (
        .bl(bl[22:23]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_1_sram),
        .mem_outb(mux2_size3_1_sram_inv)
    );
    mux2_size3_mem mem_right_track_6
    (
        .bl(bl[24:25]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_2_sram),
        .mem_outb(mux2_size3_2_sram_inv)
    );
    mux2_size3_mem mem_right_track_10
    (
        .bl(bl[29:30]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_3_sram),
        .mem_outb(mux2_size3_3_sram_inv)
    );
    mux2_size3_mem mem_right_track_20
    (
        .bl(bl[39:40]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_4_sram),
        .mem_outb(mux2_size3_4_sram_inv)
    );
    mux2_size3_mem mem_right_track_22
    (
        .bl(bl[41:42]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_5_sram),
        .mem_outb(mux2_size3_5_sram_inv)
    );
    mux2_size3_mem mem_right_track_24
    (
        .bl(bl[43:44]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_6_sram),
        .mem_outb(mux2_size3_6_sram_inv)
    );
    mux2_size3_mem mem_right_track_26
    (
        .bl(bl[45:46]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_7_sram),
        .mem_outb(mux2_size3_7_sram_inv)
    );
    mux2_size3_mem mem_right_track_30
    (
        .bl(bl[50:51]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_8_sram),
        .mem_outb(mux2_size3_8_sram_inv)
    );
    mux2_size4 mux_right_track_8
    (
        .in({chany_top_in[4], chany_top_in[15], grid_right_b_in[2], chany_bottom_in[18]}),
        .sram(mux2_size4_0_sram),
        .sram_inv(mux2_size4_0_sram_inv),
        .out(chanx_right_out[4])
    );
    mux2_size4 mux_right_track_28
    (
        .in({chany_top_in[17], grid_right_b_in[2], chany_bottom_in[5], chany_bottom_in[19]}),
        .sram(mux2_size4_1_sram),
        .sram_inv(mux2_size4_1_sram_inv),
        .out(chanx_right_out[14])
    );
    mux2_size4_mem mem_right_track_8
    (
        .bl(bl[26:28]),
        .wl({wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size4_0_sram),
        .mem_outb(mux2_size4_0_sram_inv)
    );
    mux2_size4_mem mem_right_track_28
    (
        .bl(bl[47:49]),
        .wl({wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size4_1_sram),
        .mem_outb(mux2_size4_1_sram_inv)
    );
    mux2_size2 mux_right_track_12
    (
        .in({chany_top_in[6], chany_bottom_in[16]}),
        .sram(mux2_size2_0_sram),
        .sram_inv(mux2_size2_0_sram_inv),
        .out(chanx_right_out[6])
    );
    mux2_size2 mux_right_track_14
    (
        .in({chany_top_in[8], chany_bottom_in[14]}),
        .sram(mux2_size2_1_sram),
        .sram_inv(mux2_size2_1_sram_inv),
        .out(chanx_right_out[7])
    );
    mux2_size2 mux_right_track_16
    (
        .in({chany_top_in[9], chany_bottom_in[13]}),
        .sram(mux2_size2_2_sram),
        .sram_inv(mux2_size2_2_sram_inv),
        .out(chanx_right_out[8])
    );
    mux2_size2 mux_right_track_18
    (
        .in({chany_top_in[10], chany_bottom_in[12]}),
        .sram(mux2_size2_3_sram),
        .sram_inv(mux2_size2_3_sram_inv),
        .out(chanx_right_out[9])
    );
    mux2_size2 mux_right_track_32
    (
        .in({chany_bottom_in[2], chany_bottom_in[11]}),
        .sram(mux2_size2_4_sram),
        .sram_inv(mux2_size2_4_sram_inv),
        .out(chanx_right_out[16])
    );
    mux2_size2 mux_right_track_34
    (
        .in({chany_bottom_in[1], chany_bottom_in[7]}),
        .sram(mux2_size2_5_sram),
        .sram_inv(mux2_size2_5_sram_inv),
        .out(chanx_right_out[17])
    );
    mux2_size2 mux_right_track_36
    (
        .in({chany_bottom_in[0], chany_bottom_in[3]}),
        .sram(mux2_size2_6_sram),
        .sram_inv(mux2_size2_6_sram_inv),
        .out(chanx_right_out[18])
    );
    mux2_size2_mem mem_right_track_12
    (
        .bl(bl[31:32]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_0_sram),
        .mem_outb(mux2_size2_0_sram_inv)
    );
    mux2_size2_mem mem_right_track_14
    (
        .bl(bl[33:34]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_1_sram),
        .mem_outb(mux2_size2_1_sram_inv)
    );
    mux2_size2_mem mem_right_track_16
    (
        .bl(bl[35:36]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_2_sram),
        .mem_outb(mux2_size2_2_sram_inv)
    );
    mux2_size2_mem mem_right_track_18
    (
        .bl(bl[37:38]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_3_sram),
        .mem_outb(mux2_size2_3_sram_inv)
    );
    mux2_size2_mem mem_right_track_32
    (
        .bl(bl[52:53]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_4_sram),
        .mem_outb(mux2_size2_4_sram_inv)
    );
    mux2_size2_mem mem_right_track_34
    (
        .bl(bl[54:55]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_5_sram),
        .mem_outb(mux2_size2_5_sram_inv)
    );
    mux2_size2_mem mem_right_track_36
    (
        .bl(bl[56:57]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_6_sram),
        .mem_outb(mux2_size2_6_sram_inv)
    );
endmodule

