//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module sb_1__0_
(
    chany_top_in,
    chanx_right_in,
    chanx_left_in,
    bl,
    wl,
    chany_top_out,
    chanx_right_out,
    chanx_left_out,
    grid_top_r_in,
    grid_top_l_in,
    grid_right_t_in,
    grid_right_b_inpad,
    grid_left_t_in,
    grid_left_b_inpad
);

    input [0:19]chany_top_in;
    input [0:19]chanx_right_in;
    input [0:19]chanx_left_in;
    input [0:77]bl;
    input [0:77]wl;
    output [0:19]chany_top_out;
    output [0:19]chanx_right_out;
    output [0:19]chanx_left_out;
    input [0:1]grid_top_r_in;
    input [0:2]grid_top_l_in;
    input [0:1]grid_right_t_in;
    input [0:7]grid_right_b_inpad;
    input [0:1]grid_left_t_in;
    input [0:7]grid_left_b_inpad;

    wire [0:19]chany_top_in;
    wire [0:19]chanx_right_in;
    wire [0:19]chanx_left_in;
    wire [0:77]bl;
    wire [0:77]wl;
    wire [0:19]chany_top_out;
    wire [0:19]chanx_right_out;
    wire [0:19]chanx_left_out;
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
    wire [0:1]mux2_size2_7_sram;
    wire [0:1]mux2_size2_7_sram_inv;
    wire [0:1]mux2_size2_8_sram;
    wire [0:1]mux2_size2_8_sram_inv;
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
    wire [0:2]mux2_size4_0_sram;
    wire [0:2]mux2_size4_0_sram_inv;
    wire [0:2]mux2_size5_0_sram;
    wire [0:2]mux2_size5_0_sram_inv;
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
    wire [0:2]grid_top_l_in;
    wire [0:1]grid_right_t_in;
    wire [0:7]grid_right_b_inpad;
    wire [0:1]grid_left_t_in;
    wire [0:7]grid_left_b_inpad;

assign chanx_left_out[1] = chanx_right_in[0];
assign chanx_left_out[2] = chanx_right_in[1];
assign chanx_left_out[3] = chanx_right_in[2];
assign chanx_left_out[5] = chanx_right_in[4];
assign chanx_left_out[6] = chanx_right_in[5];
assign chanx_left_out[7] = chanx_right_in[6];
assign chany_top_out[5] = chanx_right_in[8];
assign chanx_left_out[9] = chanx_right_in[8];
assign chanx_left_out[10] = chanx_right_in[9];
assign chanx_left_out[11] = chanx_right_in[10];
assign chanx_left_out[13] = chanx_right_in[12];
assign chanx_left_out[14] = chanx_right_in[13];
assign chanx_left_out[15] = chanx_right_in[14];
assign chanx_left_out[17] = chanx_right_in[16];
assign chanx_left_out[18] = chanx_right_in[17];
assign chanx_left_out[19] = chanx_right_in[18];
assign chanx_right_out[1] = chanx_left_in[0];
assign chanx_right_out[2] = chanx_left_in[1];
assign chanx_right_out[3] = chanx_left_in[2];
assign chanx_right_out[5] = chanx_left_in[4];
assign chanx_right_out[6] = chanx_left_in[5];
assign chany_top_out[15] = chanx_left_in[6];
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
assign chanx_left_out[9] = chany_top_out[5];
assign chanx_right_out[7] = chany_top_out[15];
    mux2_size5 mux_top_track_0
    (
        .in({grid_top_l_in[0], chanx_right_in[1], chanx_right_in[7], chanx_left_in[0], chanx_left_in[3]}),
        .sram(mux2_size5_0_sram),
        .sram_inv(mux2_size5_0_sram_inv),
        .out(chany_top_out[0])
    );
    mux2_size5_mem mem_top_track_0
    (
        .bl(bl[0:2]),
        .wl({wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size5_0_sram),
        .mem_outb(mux2_size5_0_sram_inv)
    );
    mux2_size3 mux_top_track_2
    (
        .in({grid_top_l_in[1], chanx_right_in[2], chanx_right_in[11]}),
        .sram(mux2_size3_0_sram),
        .sram_inv(mux2_size3_0_sram_inv),
        .out(chany_top_out[1])
    );
    mux2_size3 mux_top_track_4
    (
        .in({grid_top_l_in[2], chanx_right_in[4], chanx_right_in[15]}),
        .sram(mux2_size3_1_sram),
        .sram_inv(mux2_size3_1_sram_inv),
        .out(chany_top_out[2])
    );
    mux2_size3 mux_top_track_6
    (
        .in({grid_top_r_in[0], chanx_right_in[5], chanx_right_in[19]}),
        .sram(mux2_size3_2_sram),
        .sram_inv(mux2_size3_2_sram_inv),
        .out(chany_top_out[3])
    );
    mux2_size3 mux_top_track_20
    (
        .in({grid_top_l_in[0], chanx_right_in[14], chanx_left_in[13]}),
        .sram(mux2_size3_3_sram),
        .sram_inv(mux2_size3_3_sram_inv),
        .out(chany_top_out[10])
    );
    mux2_size3 mux_top_track_22
    (
        .in({grid_top_l_in[1], chanx_right_in[16], chanx_left_in[12]}),
        .sram(mux2_size3_4_sram),
        .sram_inv(mux2_size3_4_sram_inv),
        .out(chany_top_out[11])
    );
    mux2_size3 mux_top_track_24
    (
        .in({grid_top_l_in[2], chanx_right_in[17], chanx_left_in[10]}),
        .sram(mux2_size3_5_sram),
        .sram_inv(mux2_size3_5_sram_inv),
        .out(chany_top_out[12])
    );
    mux2_size3 mux_top_track_26
    (
        .in({grid_top_r_in[0], chanx_right_in[18], chanx_left_in[9]}),
        .sram(mux2_size3_6_sram),
        .sram_inv(mux2_size3_6_sram_inv),
        .out(chany_top_out[13])
    );
    mux2_size3_mem mem_top_track_2
    (
        .bl(bl[3:4]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_0_sram),
        .mem_outb(mux2_size3_0_sram_inv)
    );
    mux2_size3_mem mem_top_track_4
    (
        .bl(bl[5:6]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_1_sram),
        .mem_outb(mux2_size3_1_sram_inv)
    );
    mux2_size3_mem mem_top_track_6
    (
        .bl(bl[7:8]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_2_sram),
        .mem_outb(mux2_size3_2_sram_inv)
    );
    mux2_size3_mem mem_top_track_20
    (
        .bl(bl[19:20]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_3_sram),
        .mem_outb(mux2_size3_3_sram_inv)
    );
    mux2_size3_mem mem_top_track_22
    (
        .bl(bl[21:22]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_4_sram),
        .mem_outb(mux2_size3_4_sram_inv)
    );
    mux2_size3_mem mem_top_track_24
    (
        .bl(bl[23:24]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_5_sram),
        .mem_outb(mux2_size3_5_sram_inv)
    );
    mux2_size3_mem mem_top_track_26
    (
        .bl(bl[25:26]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_6_sram),
        .mem_outb(mux2_size3_6_sram_inv)
    );
    mux2_size2 mux_top_track_8
    (
        .in({grid_top_r_in[1], chanx_right_in[6]}),
        .sram(mux2_size2_0_sram),
        .sram_inv(mux2_size2_0_sram_inv),
        .out(chany_top_out[4])
    );
    mux2_size2 mux_top_track_12
    (
        .in({chanx_right_in[9], chanx_left_in[18]}),
        .sram(mux2_size2_1_sram),
        .sram_inv(mux2_size2_1_sram_inv),
        .out(chany_top_out[6])
    );
    mux2_size2 mux_top_track_14
    (
        .in({chanx_right_in[10], chanx_left_in[17]}),
        .sram(mux2_size2_2_sram),
        .sram_inv(mux2_size2_2_sram_inv),
        .out(chany_top_out[7])
    );
    mux2_size2 mux_top_track_16
    (
        .in({chanx_right_in[12], chanx_left_in[16]}),
        .sram(mux2_size2_3_sram),
        .sram_inv(mux2_size2_3_sram_inv),
        .out(chany_top_out[8])
    );
    mux2_size2 mux_top_track_18
    (
        .in({chanx_right_in[13], chanx_left_in[14]}),
        .sram(mux2_size2_4_sram),
        .sram_inv(mux2_size2_4_sram_inv),
        .out(chany_top_out[9])
    );
    mux2_size2 mux_top_track_28
    (
        .in({grid_top_r_in[1], chanx_left_in[8]}),
        .sram(mux2_size2_5_sram),
        .sram_inv(mux2_size2_5_sram_inv),
        .out(chany_top_out[14])
    );
    mux2_size2 mux_top_track_32
    (
        .in({chanx_left_in[5], chanx_left_in[19]}),
        .sram(mux2_size2_6_sram),
        .sram_inv(mux2_size2_6_sram_inv),
        .out(chany_top_out[16])
    );
    mux2_size2 mux_top_track_34
    (
        .in({chanx_left_in[4], chanx_left_in[15]}),
        .sram(mux2_size2_7_sram),
        .sram_inv(mux2_size2_7_sram_inv),
        .out(chany_top_out[17])
    );
    mux2_size2 mux_top_track_36
    (
        .in({chanx_left_in[2], chanx_left_in[11]}),
        .sram(mux2_size2_8_sram),
        .sram_inv(mux2_size2_8_sram_inv),
        .out(chany_top_out[18])
    );
    mux2_size2_mem mem_top_track_8
    (
        .bl(bl[9:10]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_0_sram),
        .mem_outb(mux2_size2_0_sram_inv)
    );
    mux2_size2_mem mem_top_track_12
    (
        .bl(bl[11:12]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_1_sram),
        .mem_outb(mux2_size2_1_sram_inv)
    );
    mux2_size2_mem mem_top_track_14
    (
        .bl(bl[13:14]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_2_sram),
        .mem_outb(mux2_size2_2_sram_inv)
    );
    mux2_size2_mem mem_top_track_16
    (
        .bl(bl[15:16]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_3_sram),
        .mem_outb(mux2_size2_3_sram_inv)
    );
    mux2_size2_mem mem_top_track_18
    (
        .bl(bl[17:18]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_4_sram),
        .mem_outb(mux2_size2_4_sram_inv)
    );
    mux2_size2_mem mem_top_track_28
    (
        .bl(bl[27:28]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_5_sram),
        .mem_outb(mux2_size2_5_sram_inv)
    );
    mux2_size2_mem mem_top_track_32
    (
        .bl(bl[29:30]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_6_sram),
        .mem_outb(mux2_size2_6_sram_inv)
    );
    mux2_size2_mem mem_top_track_34
    (
        .bl(bl[31:32]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_7_sram),
        .mem_outb(mux2_size2_7_sram_inv)
    );
    mux2_size2_mem mem_top_track_36
    (
        .bl(bl[33:34]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_8_sram),
        .mem_outb(mux2_size2_8_sram_inv)
    );
    mux2_size4 mux_top_track_38
    (
        .in({chanx_right_in[0], chanx_right_in[3], chanx_left_in[1], chanx_left_in[7]}),
        .sram(mux2_size4_0_sram),
        .sram_inv(mux2_size4_0_sram_inv),
        .out(chany_top_out[19])
    );
    mux2_size4_mem mem_top_track_38
    (
        .bl(bl[35:37]),
        .wl({wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size4_0_sram),
        .mem_outb(mux2_size4_0_sram_inv)
    );
    mux2_size9 mux_right_track_0
    (
        .in({chany_top_in[4], chany_top_in[9], chany_top_in[14], chany_top_in[19], grid_right_t_in[0], grid_right_b_inpad[3], chanx_left_in[0], chanx_left_in[6], chanx_left_in[13]}),
        .sram(mux2_size9_0_sram),
        .sram_inv(mux2_size9_0_sram_inv),
        .out(chanx_right_out[0])
    );
    mux2_size9 mux_right_track_8
    (
        .in({chany_top_in[0], chany_top_in[5], chany_top_in[10], chany_top_in[15], grid_right_t_in[1], grid_right_b_inpad[4], chanx_left_in[1], chanx_left_in[8], chanx_left_in[14]}),
        .sram(mux2_size9_1_sram),
        .sram_inv(mux2_size9_1_sram_inv),
        .out(chanx_right_out[4])
    );
    mux2_size9 mux_right_track_16
    (
        .in({chany_top_in[1], chany_top_in[6], chany_top_in[11], chany_top_in[16], grid_right_b_inpad[0], grid_right_b_inpad[5], chanx_left_in[2], chanx_left_in[9], chanx_left_in[16]}),
        .sram(mux2_size9_2_sram),
        .sram_inv(mux2_size9_2_sram_inv),
        .out(chanx_right_out[8])
    );
    mux2_size9 mux_right_track_24
    (
        .in({chany_top_in[2], chany_top_in[7], chany_top_in[12], chany_top_in[17], grid_right_b_inpad[1], grid_right_b_inpad[6], chanx_left_in[4], chanx_left_in[10], chanx_left_in[17]}),
        .sram(mux2_size9_3_sram),
        .sram_inv(mux2_size9_3_sram_inv),
        .out(chanx_right_out[12])
    );
    mux2_size9 mux_right_track_32
    (
        .in({chany_top_in[3], chany_top_in[8], chany_top_in[13], chany_top_in[18], grid_right_b_inpad[2], grid_right_b_inpad[7], chanx_left_in[5], chanx_left_in[12], chanx_left_in[18]}),
        .sram(mux2_size9_4_sram),
        .sram_inv(mux2_size9_4_sram_inv),
        .out(chanx_right_out[16])
    );
    mux2_size9 mux_left_track_1
    (
        .in({chany_top_in[0], chany_top_in[5], chany_top_in[10], chany_top_in[15], chanx_right_in[0], chanx_right_in[6], chanx_right_in[13], grid_left_t_in[0], grid_left_b_inpad[3]}),
        .sram(mux2_size9_5_sram),
        .sram_inv(mux2_size9_5_sram_inv),
        .out(chanx_left_out[0])
    );
    mux2_size9 mux_left_track_9
    (
        .in({chany_top_in[4], chany_top_in[9], chany_top_in[14], chany_top_in[19], chanx_right_in[1], chanx_right_in[8], chanx_right_in[14], grid_left_t_in[1], grid_left_b_inpad[4]}),
        .sram(mux2_size9_6_sram),
        .sram_inv(mux2_size9_6_sram_inv),
        .out(chanx_left_out[4])
    );
    mux2_size9 mux_left_track_17
    (
        .in({chany_top_in[3], chany_top_in[8], chany_top_in[13], chany_top_in[18], chanx_right_in[2], chanx_right_in[9], chanx_right_in[16], grid_left_b_inpad[0], grid_left_b_inpad[5]}),
        .sram(mux2_size9_7_sram),
        .sram_inv(mux2_size9_7_sram_inv),
        .out(chanx_left_out[8])
    );
    mux2_size9 mux_left_track_25
    (
        .in({chany_top_in[2], chany_top_in[7], chany_top_in[12], chany_top_in[17], chanx_right_in[4], chanx_right_in[10], chanx_right_in[17], grid_left_b_inpad[1], grid_left_b_inpad[6]}),
        .sram(mux2_size9_8_sram),
        .sram_inv(mux2_size9_8_sram_inv),
        .out(chanx_left_out[12])
    );
    mux2_size9 mux_left_track_33
    (
        .in({chany_top_in[1], chany_top_in[6], chany_top_in[11], chany_top_in[16], chanx_right_in[5], chanx_right_in[12], chanx_right_in[18], grid_left_b_inpad[2], grid_left_b_inpad[7]}),
        .sram(mux2_size9_9_sram),
        .sram_inv(mux2_size9_9_sram_inv),
        .out(chanx_left_out[16])
    );
    mux2_size9_mem mem_right_track_0
    (
        .bl(bl[38:41]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_0_sram),
        .mem_outb(mux2_size9_0_sram_inv)
    );
    mux2_size9_mem mem_right_track_8
    (
        .bl(bl[42:45]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_1_sram),
        .mem_outb(mux2_size9_1_sram_inv)
    );
    mux2_size9_mem mem_right_track_16
    (
        .bl(bl[46:49]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_2_sram),
        .mem_outb(mux2_size9_2_sram_inv)
    );
    mux2_size9_mem mem_right_track_24
    (
        .bl(bl[50:53]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_3_sram),
        .mem_outb(mux2_size9_3_sram_inv)
    );
    mux2_size9_mem mem_right_track_32
    (
        .bl(bl[54:57]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_4_sram),
        .mem_outb(mux2_size9_4_sram_inv)
    );
    mux2_size9_mem mem_left_track_1
    (
        .bl(bl[58:61]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_5_sram),
        .mem_outb(mux2_size9_5_sram_inv)
    );
    mux2_size9_mem mem_left_track_9
    (
        .bl(bl[62:65]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_6_sram),
        .mem_outb(mux2_size9_6_sram_inv)
    );
    mux2_size9_mem mem_left_track_17
    (
        .bl(bl[66:69]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_7_sram),
        .mem_outb(mux2_size9_7_sram_inv)
    );
    mux2_size9_mem mem_left_track_25
    (
        .bl(bl[70:73]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_8_sram),
        .mem_outb(mux2_size9_8_sram_inv)
    );
    mux2_size9_mem mem_left_track_33
    (
        .bl(bl[74:77]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_9_sram),
        .mem_outb(mux2_size9_9_sram_inv)
    );
endmodule

