//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module sb_1__4_
(
    chanx_right_in,
    chany_bottom_in,
    chanx_left_in,
    bl,
    wl,
    chanx_right_out,
    chany_bottom_out,
    chanx_left_out,
    grid_right_t_inpad,
    grid_right_b_in,
    grid_bottom_r_in,
    grid_bottom_l_in,
    grid_left_t_inpad,
    grid_left_b_in
);

    input [0:19]chanx_right_in;
    input [0:19]chany_bottom_in;
    input [0:19]chanx_left_in;
    input [0:79]bl;
    input [0:79]wl;
    output [0:19]chanx_right_out;
    output [0:19]chany_bottom_out;
    output [0:19]chanx_left_out;
    input [0:7]grid_right_t_inpad;
    input [0:2]grid_right_b_in;
    input [0:1]grid_bottom_r_in;
    input [0:2]grid_bottom_l_in;
    input [0:7]grid_left_t_inpad;
    input [0:2]grid_left_b_in;

    wire [0:19]chanx_right_in;
    wire [0:19]chany_bottom_in;
    wire [0:19]chanx_left_in;
    wire [0:79]bl;
    wire [0:79]wl;
    wire [0:19]chanx_right_out;
    wire [0:19]chany_bottom_out;
    wire [0:19]chanx_left_out;
    wire [0:3]mux2_size10_0_sram;
    wire [0:3]mux2_size10_0_sram_inv;
    wire [0:3]mux2_size10_1_sram;
    wire [0:3]mux2_size10_1_sram_inv;
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
    wire [0:1]mux2_size2_9_sram;
    wire [0:1]mux2_size2_9_sram_inv;
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
    wire [0:1]mux2_size3_9_sram;
    wire [0:1]mux2_size3_9_sram_inv;
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
    wire [0:7]grid_right_t_inpad;
    wire [0:2]grid_right_b_in;
    wire [0:1]grid_bottom_r_in;
    wire [0:2]grid_bottom_l_in;
    wire [0:7]grid_left_t_inpad;
    wire [0:2]grid_left_b_in;

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
    mux2_size10 mux_right_track_0
    (
        .in({grid_right_t_inpad[0], grid_right_t_inpad[5], grid_right_b_in[2], chany_bottom_in[3], chany_bottom_in[8], chany_bottom_in[13], chany_bottom_in[18], chanx_left_in[0], chanx_left_in[6], chanx_left_in[13]}),
        .sram(mux2_size10_0_sram),
        .sram_inv(mux2_size10_0_sram_inv),
        .out(chanx_right_out[0])
    );
    mux2_size10 mux_left_track_1
    (
        .in({chanx_right_in[0], chanx_right_in[6], chanx_right_in[13], chany_bottom_in[4], chany_bottom_in[9], chany_bottom_in[14], chany_bottom_in[19], grid_left_t_inpad[0], grid_left_t_inpad[5], grid_left_b_in[2]}),
        .sram(mux2_size10_1_sram),
        .sram_inv(mux2_size10_1_sram_inv),
        .out(chanx_left_out[0])
    );
    mux2_size10_mem mem_right_track_0
    (
        .bl(bl[0:3]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size10_0_sram),
        .mem_outb(mux2_size10_0_sram_inv)
    );
    mux2_size10_mem mem_left_track_1
    (
        .bl(bl[60:63]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size10_1_sram),
        .mem_outb(mux2_size10_1_sram_inv)
    );
    mux2_size9 mux_right_track_8
    (
        .in({grid_right_t_inpad[1], grid_right_t_inpad[6], chany_bottom_in[2], chany_bottom_in[7], chany_bottom_in[12], chany_bottom_in[17], chanx_left_in[1], chanx_left_in[8], chanx_left_in[14]}),
        .sram(mux2_size9_0_sram),
        .sram_inv(mux2_size9_0_sram_inv),
        .out(chanx_right_out[4])
    );
    mux2_size9 mux_right_track_16
    (
        .in({grid_right_t_inpad[2], grid_right_t_inpad[7], chany_bottom_in[1], chany_bottom_in[6], chany_bottom_in[11], chany_bottom_in[16], chanx_left_in[2], chanx_left_in[9], chanx_left_in[16]}),
        .sram(mux2_size9_1_sram),
        .sram_inv(mux2_size9_1_sram_inv),
        .out(chanx_right_out[8])
    );
    mux2_size9 mux_right_track_24
    (
        .in({grid_right_t_inpad[3], grid_right_b_in[0], chany_bottom_in[0], chany_bottom_in[5], chany_bottom_in[10], chany_bottom_in[15], chanx_left_in[4], chanx_left_in[10], chanx_left_in[17]}),
        .sram(mux2_size9_2_sram),
        .sram_inv(mux2_size9_2_sram_inv),
        .out(chanx_right_out[12])
    );
    mux2_size9 mux_right_track_32
    (
        .in({grid_right_t_inpad[4], grid_right_b_in[1], chany_bottom_in[4], chany_bottom_in[9], chany_bottom_in[14], chany_bottom_in[19], chanx_left_in[5], chanx_left_in[12], chanx_left_in[18]}),
        .sram(mux2_size9_3_sram),
        .sram_inv(mux2_size9_3_sram_inv),
        .out(chanx_right_out[16])
    );
    mux2_size9 mux_left_track_9
    (
        .in({chanx_right_in[1], chanx_right_in[8], chanx_right_in[14], chany_bottom_in[0], chany_bottom_in[5], chany_bottom_in[10], chany_bottom_in[15], grid_left_t_inpad[1], grid_left_t_inpad[6]}),
        .sram(mux2_size9_4_sram),
        .sram_inv(mux2_size9_4_sram_inv),
        .out(chanx_left_out[4])
    );
    mux2_size9 mux_left_track_17
    (
        .in({chanx_right_in[2], chanx_right_in[9], chanx_right_in[16], chany_bottom_in[1], chany_bottom_in[6], chany_bottom_in[11], chany_bottom_in[16], grid_left_t_inpad[2], grid_left_t_inpad[7]}),
        .sram(mux2_size9_5_sram),
        .sram_inv(mux2_size9_5_sram_inv),
        .out(chanx_left_out[8])
    );
    mux2_size9 mux_left_track_25
    (
        .in({chanx_right_in[4], chanx_right_in[10], chanx_right_in[17], chany_bottom_in[2], chany_bottom_in[7], chany_bottom_in[12], chany_bottom_in[17], grid_left_t_inpad[3], grid_left_b_in[0]}),
        .sram(mux2_size9_6_sram),
        .sram_inv(mux2_size9_6_sram_inv),
        .out(chanx_left_out[12])
    );
    mux2_size9 mux_left_track_33
    (
        .in({chanx_right_in[5], chanx_right_in[12], chanx_right_in[18], chany_bottom_in[3], chany_bottom_in[8], chany_bottom_in[13], chany_bottom_in[18], grid_left_t_inpad[4], grid_left_b_in[1]}),
        .sram(mux2_size9_7_sram),
        .sram_inv(mux2_size9_7_sram_inv),
        .out(chanx_left_out[16])
    );
    mux2_size9_mem mem_right_track_8
    (
        .bl(bl[4:7]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_0_sram),
        .mem_outb(mux2_size9_0_sram_inv)
    );
    mux2_size9_mem mem_right_track_16
    (
        .bl(bl[8:11]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_1_sram),
        .mem_outb(mux2_size9_1_sram_inv)
    );
    mux2_size9_mem mem_right_track_24
    (
        .bl(bl[12:15]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_2_sram),
        .mem_outb(mux2_size9_2_sram_inv)
    );
    mux2_size9_mem mem_right_track_32
    (
        .bl(bl[16:19]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_3_sram),
        .mem_outb(mux2_size9_3_sram_inv)
    );
    mux2_size9_mem mem_left_track_9
    (
        .bl(bl[64:67]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_4_sram),
        .mem_outb(mux2_size9_4_sram_inv)
    );
    mux2_size9_mem mem_left_track_17
    (
        .bl(bl[68:71]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_5_sram),
        .mem_outb(mux2_size9_5_sram_inv)
    );
    mux2_size9_mem mem_left_track_25
    (
        .bl(bl[72:75]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_6_sram),
        .mem_outb(mux2_size9_6_sram_inv)
    );
    mux2_size9_mem mem_left_track_33
    (
        .bl(bl[76:79]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size9_7_sram),
        .mem_outb(mux2_size9_7_sram_inv)
    );
    mux2_size3 mux_bottom_track_1
    (
        .in({grid_bottom_r_in[0], chanx_left_in[1], chanx_left_in[7]}),
        .sram(mux2_size3_0_sram),
        .sram_inv(mux2_size3_0_sram_inv),
        .out(chany_bottom_out[0])
    );
    mux2_size3 mux_bottom_track_3
    (
        .in({grid_bottom_r_in[1], chanx_left_in[2], chanx_left_in[11]}),
        .sram(mux2_size3_1_sram),
        .sram_inv(mux2_size3_1_sram_inv),
        .out(chany_bottom_out[1])
    );
    mux2_size3 mux_bottom_track_5
    (
        .in({grid_bottom_l_in[0], chanx_left_in[4], chanx_left_in[15]}),
        .sram(mux2_size3_2_sram),
        .sram_inv(mux2_size3_2_sram_inv),
        .out(chany_bottom_out[2])
    );
    mux2_size3 mux_bottom_track_7
    (
        .in({grid_bottom_l_in[1], chanx_left_in[5], chanx_left_in[19]}),
        .sram(mux2_size3_3_sram),
        .sram_inv(mux2_size3_3_sram_inv),
        .out(chany_bottom_out[3])
    );
    mux2_size3 mux_bottom_track_9
    (
        .in({chanx_right_in[18], grid_bottom_l_in[2], chanx_left_in[6]}),
        .sram(mux2_size3_4_sram),
        .sram_inv(mux2_size3_4_sram_inv),
        .out(chany_bottom_out[4])
    );
    mux2_size3 mux_bottom_track_21
    (
        .in({chanx_right_in[10], grid_bottom_r_in[0], chanx_left_in[14]}),
        .sram(mux2_size3_5_sram),
        .sram_inv(mux2_size3_5_sram_inv),
        .out(chany_bottom_out[10])
    );
    mux2_size3 mux_bottom_track_23
    (
        .in({chanx_right_in[9], grid_bottom_r_in[1], chanx_left_in[16]}),
        .sram(mux2_size3_6_sram),
        .sram_inv(mux2_size3_6_sram_inv),
        .out(chany_bottom_out[11])
    );
    mux2_size3 mux_bottom_track_25
    (
        .in({chanx_right_in[8], grid_bottom_l_in[0], chanx_left_in[17]}),
        .sram(mux2_size3_7_sram),
        .sram_inv(mux2_size3_7_sram_inv),
        .out(chany_bottom_out[12])
    );
    mux2_size3 mux_bottom_track_27
    (
        .in({chanx_right_in[6], grid_bottom_l_in[1], chanx_left_in[18]}),
        .sram(mux2_size3_8_sram),
        .sram_inv(mux2_size3_8_sram_inv),
        .out(chany_bottom_out[13])
    );
    mux2_size3 mux_bottom_track_29
    (
        .in({chanx_right_in[5], chanx_right_in[19], grid_bottom_l_in[2]}),
        .sram(mux2_size3_9_sram),
        .sram_inv(mux2_size3_9_sram_inv),
        .out(chany_bottom_out[14])
    );
    mux2_size3_mem mem_bottom_track_1
    (
        .bl(bl[20:21]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_0_sram),
        .mem_outb(mux2_size3_0_sram_inv)
    );
    mux2_size3_mem mem_bottom_track_3
    (
        .bl(bl[22:23]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_1_sram),
        .mem_outb(mux2_size3_1_sram_inv)
    );
    mux2_size3_mem mem_bottom_track_5
    (
        .bl(bl[24:25]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_2_sram),
        .mem_outb(mux2_size3_2_sram_inv)
    );
    mux2_size3_mem mem_bottom_track_7
    (
        .bl(bl[26:27]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_3_sram),
        .mem_outb(mux2_size3_3_sram_inv)
    );
    mux2_size3_mem mem_bottom_track_9
    (
        .bl(bl[28:29]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_4_sram),
        .mem_outb(mux2_size3_4_sram_inv)
    );
    mux2_size3_mem mem_bottom_track_21
    (
        .bl(bl[40:41]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_5_sram),
        .mem_outb(mux2_size3_5_sram_inv)
    );
    mux2_size3_mem mem_bottom_track_23
    (
        .bl(bl[42:43]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_6_sram),
        .mem_outb(mux2_size3_6_sram_inv)
    );
    mux2_size3_mem mem_bottom_track_25
    (
        .bl(bl[44:45]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_7_sram),
        .mem_outb(mux2_size3_7_sram_inv)
    );
    mux2_size3_mem mem_bottom_track_27
    (
        .bl(bl[46:47]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_8_sram),
        .mem_outb(mux2_size3_8_sram_inv)
    );
    mux2_size3_mem mem_bottom_track_29
    (
        .bl(bl[48:49]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_9_sram),
        .mem_outb(mux2_size3_9_sram_inv)
    );
    mux2_size2 mux_bottom_track_11
    (
        .in({chanx_right_in[17], chanx_left_in[8]}),
        .sram(mux2_size2_0_sram),
        .sram_inv(mux2_size2_0_sram_inv),
        .out(chany_bottom_out[5])
    );
    mux2_size2 mux_bottom_track_13
    (
        .in({chanx_right_in[16], chanx_left_in[9]}),
        .sram(mux2_size2_1_sram),
        .sram_inv(mux2_size2_1_sram_inv),
        .out(chany_bottom_out[6])
    );
    mux2_size2 mux_bottom_track_15
    (
        .in({chanx_right_in[14], chanx_left_in[10]}),
        .sram(mux2_size2_2_sram),
        .sram_inv(mux2_size2_2_sram_inv),
        .out(chany_bottom_out[7])
    );
    mux2_size2 mux_bottom_track_17
    (
        .in({chanx_right_in[13], chanx_left_in[12]}),
        .sram(mux2_size2_3_sram),
        .sram_inv(mux2_size2_3_sram_inv),
        .out(chany_bottom_out[8])
    );
    mux2_size2 mux_bottom_track_19
    (
        .in({chanx_right_in[12], chanx_left_in[13]}),
        .sram(mux2_size2_4_sram),
        .sram_inv(mux2_size2_4_sram_inv),
        .out(chany_bottom_out[9])
    );
    mux2_size2 mux_bottom_track_31
    (
        .in({chanx_right_in[4], chanx_right_in[15]}),
        .sram(mux2_size2_5_sram),
        .sram_inv(mux2_size2_5_sram_inv),
        .out(chany_bottom_out[15])
    );
    mux2_size2 mux_bottom_track_33
    (
        .in({chanx_right_in[2], chanx_right_in[11]}),
        .sram(mux2_size2_6_sram),
        .sram_inv(mux2_size2_6_sram_inv),
        .out(chany_bottom_out[16])
    );
    mux2_size2 mux_bottom_track_35
    (
        .in({chanx_right_in[1], chanx_right_in[7]}),
        .sram(mux2_size2_7_sram),
        .sram_inv(mux2_size2_7_sram_inv),
        .out(chany_bottom_out[17])
    );
    mux2_size2 mux_bottom_track_37
    (
        .in({chanx_right_in[0], chanx_right_in[3]}),
        .sram(mux2_size2_8_sram),
        .sram_inv(mux2_size2_8_sram_inv),
        .out(chany_bottom_out[18])
    );
    mux2_size2 mux_bottom_track_39
    (
        .in({chanx_left_in[0], chanx_left_in[3]}),
        .sram(mux2_size2_9_sram),
        .sram_inv(mux2_size2_9_sram_inv),
        .out(chany_bottom_out[19])
    );
    mux2_size2_mem mem_bottom_track_11
    (
        .bl(bl[30:31]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_0_sram),
        .mem_outb(mux2_size2_0_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_13
    (
        .bl(bl[32:33]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_1_sram),
        .mem_outb(mux2_size2_1_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_15
    (
        .bl(bl[34:35]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_2_sram),
        .mem_outb(mux2_size2_2_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_17
    (
        .bl(bl[36:37]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_3_sram),
        .mem_outb(mux2_size2_3_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_19
    (
        .bl(bl[38:39]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_4_sram),
        .mem_outb(mux2_size2_4_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_31
    (
        .bl(bl[50:51]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_5_sram),
        .mem_outb(mux2_size2_5_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_33
    (
        .bl(bl[52:53]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_6_sram),
        .mem_outb(mux2_size2_6_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_35
    (
        .bl(bl[54:55]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_7_sram),
        .mem_outb(mux2_size2_7_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_37
    (
        .bl(bl[56:57]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_8_sram),
        .mem_outb(mux2_size2_8_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_39
    (
        .bl(bl[58:59]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_9_sram),
        .mem_outb(mux2_size2_9_sram_inv)
    );
endmodule

