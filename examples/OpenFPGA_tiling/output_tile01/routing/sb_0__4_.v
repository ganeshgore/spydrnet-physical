//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module sb_0__4_
(
    chanx_right_in,
    chany_bottom_in,
    bl,
    wl,
    chanx_right_out,
    chany_bottom_out,
    grid_right_t_inpad,
    grid_right_b_in,
    grid_bottom_r_in,
    grid_bottom_l_inpad
);

    input [0:19]chanx_right_in;
    input [0:19]chany_bottom_in;
    input [0:79]bl;
    input [0:79]wl;
    output [0:19]chanx_right_out;
    output [0:19]chany_bottom_out;
    input [0:7]grid_right_t_inpad;
    input [0:2]grid_right_b_in;
    input [0:1]grid_bottom_r_in;
    input [0:7]grid_bottom_l_inpad;

    wire [0:19]chanx_right_in;
    wire [0:19]chany_bottom_in;
    wire [0:79]bl;
    wire [0:79]wl;
    wire [0:19]chanx_right_out;
    wire [0:19]chany_bottom_out;
    wire [0:1]mux2_size2_0_sram;
    wire [0:1]mux2_size2_0_sram_inv;
    wire [0:1]mux2_size2_10_sram;
    wire [0:1]mux2_size2_10_sram_inv;
    wire [0:1]mux2_size2_11_sram;
    wire [0:1]mux2_size2_11_sram_inv;
    wire [0:1]mux2_size2_12_sram;
    wire [0:1]mux2_size2_12_sram_inv;
    wire [0:1]mux2_size2_13_sram;
    wire [0:1]mux2_size2_13_sram_inv;
    wire [0:1]mux2_size2_14_sram;
    wire [0:1]mux2_size2_14_sram_inv;
    wire [0:1]mux2_size2_15_sram;
    wire [0:1]mux2_size2_15_sram_inv;
    wire [0:1]mux2_size2_16_sram;
    wire [0:1]mux2_size2_16_sram_inv;
    wire [0:1]mux2_size2_17_sram;
    wire [0:1]mux2_size2_17_sram_inv;
    wire [0:1]mux2_size2_18_sram;
    wire [0:1]mux2_size2_18_sram_inv;
    wire [0:1]mux2_size2_19_sram;
    wire [0:1]mux2_size2_19_sram_inv;
    wire [0:1]mux2_size2_1_sram;
    wire [0:1]mux2_size2_1_sram_inv;
    wire [0:1]mux2_size2_20_sram;
    wire [0:1]mux2_size2_20_sram_inv;
    wire [0:1]mux2_size2_21_sram;
    wire [0:1]mux2_size2_21_sram_inv;
    wire [0:1]mux2_size2_22_sram;
    wire [0:1]mux2_size2_22_sram_inv;
    wire [0:1]mux2_size2_23_sram;
    wire [0:1]mux2_size2_23_sram_inv;
    wire [0:1]mux2_size2_24_sram;
    wire [0:1]mux2_size2_24_sram_inv;
    wire [0:1]mux2_size2_25_sram;
    wire [0:1]mux2_size2_25_sram_inv;
    wire [0:1]mux2_size2_26_sram;
    wire [0:1]mux2_size2_26_sram_inv;
    wire [0:1]mux2_size2_27_sram;
    wire [0:1]mux2_size2_27_sram_inv;
    wire [0:1]mux2_size2_28_sram;
    wire [0:1]mux2_size2_28_sram_inv;
    wire [0:1]mux2_size2_29_sram;
    wire [0:1]mux2_size2_29_sram_inv;
    wire [0:1]mux2_size2_2_sram;
    wire [0:1]mux2_size2_2_sram_inv;
    wire [0:1]mux2_size2_30_sram;
    wire [0:1]mux2_size2_30_sram_inv;
    wire [0:1]mux2_size2_31_sram;
    wire [0:1]mux2_size2_31_sram_inv;
    wire [0:1]mux2_size2_32_sram;
    wire [0:1]mux2_size2_32_sram_inv;
    wire [0:1]mux2_size2_33_sram;
    wire [0:1]mux2_size2_33_sram_inv;
    wire [0:1]mux2_size2_34_sram;
    wire [0:1]mux2_size2_34_sram_inv;
    wire [0:1]mux2_size2_35_sram;
    wire [0:1]mux2_size2_35_sram_inv;
    wire [0:1]mux2_size2_36_sram;
    wire [0:1]mux2_size2_36_sram_inv;
    wire [0:1]mux2_size2_37_sram;
    wire [0:1]mux2_size2_37_sram_inv;
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
    wire [0:7]grid_right_t_inpad;
    wire [0:2]grid_right_b_in;
    wire [0:1]grid_bottom_r_in;
    wire [0:7]grid_bottom_l_inpad;

    mux2_size3 mux_right_track_0
    (
        .in({grid_right_t_inpad[0], grid_right_b_in[2], chany_bottom_in[18]}),
        .sram(mux2_size3_0_sram),
        .sram_inv(mux2_size3_0_sram_inv),
        .out(chanx_right_out[0])
    );
    mux2_size3 mux_right_track_20
    (
        .in({grid_right_t_inpad[0], grid_right_b_in[2], chany_bottom_in[8]}),
        .sram(mux2_size3_1_sram),
        .sram_inv(mux2_size3_1_sram_inv),
        .out(chanx_right_out[10])
    );
    mux2_size3_mem mem_right_track_0
    (
        .bl(bl[0:1]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_0_sram),
        .mem_outb(mux2_size3_0_sram_inv)
    );
    mux2_size3_mem mem_right_track_20
    (
        .bl(bl[20:21]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size3_1_sram),
        .mem_outb(mux2_size3_1_sram_inv)
    );
    mux2_size2 mux_right_track_2
    (
        .in({grid_right_t_inpad[1], chany_bottom_in[17]}),
        .sram(mux2_size2_0_sram),
        .sram_inv(mux2_size2_0_sram_inv),
        .out(chanx_right_out[1])
    );
    mux2_size2 mux_right_track_4
    (
        .in({grid_right_t_inpad[2], chany_bottom_in[16]}),
        .sram(mux2_size2_1_sram),
        .sram_inv(mux2_size2_1_sram_inv),
        .out(chanx_right_out[2])
    );
    mux2_size2 mux_right_track_6
    (
        .in({grid_right_t_inpad[3], chany_bottom_in[15]}),
        .sram(mux2_size2_2_sram),
        .sram_inv(mux2_size2_2_sram_inv),
        .out(chanx_right_out[3])
    );
    mux2_size2 mux_right_track_8
    (
        .in({grid_right_t_inpad[4], chany_bottom_in[14]}),
        .sram(mux2_size2_3_sram),
        .sram_inv(mux2_size2_3_sram_inv),
        .out(chanx_right_out[4])
    );
    mux2_size2 mux_right_track_10
    (
        .in({grid_right_t_inpad[5], chany_bottom_in[13]}),
        .sram(mux2_size2_4_sram),
        .sram_inv(mux2_size2_4_sram_inv),
        .out(chanx_right_out[5])
    );
    mux2_size2 mux_right_track_12
    (
        .in({grid_right_t_inpad[6], chany_bottom_in[12]}),
        .sram(mux2_size2_5_sram),
        .sram_inv(mux2_size2_5_sram_inv),
        .out(chanx_right_out[6])
    );
    mux2_size2 mux_right_track_14
    (
        .in({grid_right_t_inpad[7], chany_bottom_in[11]}),
        .sram(mux2_size2_6_sram),
        .sram_inv(mux2_size2_6_sram_inv),
        .out(chanx_right_out[7])
    );
    mux2_size2 mux_right_track_16
    (
        .in({grid_right_b_in[0], chany_bottom_in[10]}),
        .sram(mux2_size2_7_sram),
        .sram_inv(mux2_size2_7_sram_inv),
        .out(chanx_right_out[8])
    );
    mux2_size2 mux_right_track_18
    (
        .in({grid_right_b_in[1], chany_bottom_in[9]}),
        .sram(mux2_size2_8_sram),
        .sram_inv(mux2_size2_8_sram_inv),
        .out(chanx_right_out[9])
    );
    mux2_size2 mux_right_track_22
    (
        .in({grid_right_t_inpad[1], chany_bottom_in[7]}),
        .sram(mux2_size2_9_sram),
        .sram_inv(mux2_size2_9_sram_inv),
        .out(chanx_right_out[11])
    );
    mux2_size2 mux_right_track_24
    (
        .in({grid_right_t_inpad[2], chany_bottom_in[6]}),
        .sram(mux2_size2_10_sram),
        .sram_inv(mux2_size2_10_sram_inv),
        .out(chanx_right_out[12])
    );
    mux2_size2 mux_right_track_26
    (
        .in({grid_right_t_inpad[3], chany_bottom_in[5]}),
        .sram(mux2_size2_11_sram),
        .sram_inv(mux2_size2_11_sram_inv),
        .out(chanx_right_out[13])
    );
    mux2_size2 mux_right_track_28
    (
        .in({grid_right_t_inpad[4], chany_bottom_in[4]}),
        .sram(mux2_size2_12_sram),
        .sram_inv(mux2_size2_12_sram_inv),
        .out(chanx_right_out[14])
    );
    mux2_size2 mux_right_track_30
    (
        .in({grid_right_t_inpad[5], chany_bottom_in[3]}),
        .sram(mux2_size2_13_sram),
        .sram_inv(mux2_size2_13_sram_inv),
        .out(chanx_right_out[15])
    );
    mux2_size2 mux_right_track_32
    (
        .in({grid_right_t_inpad[6], chany_bottom_in[2]}),
        .sram(mux2_size2_14_sram),
        .sram_inv(mux2_size2_14_sram_inv),
        .out(chanx_right_out[16])
    );
    mux2_size2 mux_right_track_34
    (
        .in({grid_right_t_inpad[7], chany_bottom_in[1]}),
        .sram(mux2_size2_15_sram),
        .sram_inv(mux2_size2_15_sram_inv),
        .out(chanx_right_out[17])
    );
    mux2_size2 mux_right_track_36
    (
        .in({grid_right_b_in[0], chany_bottom_in[0]}),
        .sram(mux2_size2_16_sram),
        .sram_inv(mux2_size2_16_sram_inv),
        .out(chanx_right_out[18])
    );
    mux2_size2 mux_right_track_38
    (
        .in({grid_right_b_in[1], chany_bottom_in[19]}),
        .sram(mux2_size2_17_sram),
        .sram_inv(mux2_size2_17_sram_inv),
        .out(chanx_right_out[19])
    );
    mux2_size2 mux_bottom_track_1
    (
        .in({chanx_right_in[18], grid_bottom_r_in[0]}),
        .sram(mux2_size2_18_sram),
        .sram_inv(mux2_size2_18_sram_inv),
        .out(chany_bottom_out[0])
    );
    mux2_size2 mux_bottom_track_3
    (
        .in({chanx_right_in[17], grid_bottom_r_in[1]}),
        .sram(mux2_size2_19_sram),
        .sram_inv(mux2_size2_19_sram_inv),
        .out(chany_bottom_out[1])
    );
    mux2_size2 mux_bottom_track_5
    (
        .in({chanx_right_in[16], grid_bottom_l_inpad[0]}),
        .sram(mux2_size2_20_sram),
        .sram_inv(mux2_size2_20_sram_inv),
        .out(chany_bottom_out[2])
    );
    mux2_size2 mux_bottom_track_7
    (
        .in({chanx_right_in[15], grid_bottom_l_inpad[1]}),
        .sram(mux2_size2_21_sram),
        .sram_inv(mux2_size2_21_sram_inv),
        .out(chany_bottom_out[3])
    );
    mux2_size2 mux_bottom_track_9
    (
        .in({chanx_right_in[14], grid_bottom_l_inpad[2]}),
        .sram(mux2_size2_22_sram),
        .sram_inv(mux2_size2_22_sram_inv),
        .out(chany_bottom_out[4])
    );
    mux2_size2 mux_bottom_track_11
    (
        .in({chanx_right_in[13], grid_bottom_l_inpad[3]}),
        .sram(mux2_size2_23_sram),
        .sram_inv(mux2_size2_23_sram_inv),
        .out(chany_bottom_out[5])
    );
    mux2_size2 mux_bottom_track_13
    (
        .in({chanx_right_in[12], grid_bottom_l_inpad[4]}),
        .sram(mux2_size2_24_sram),
        .sram_inv(mux2_size2_24_sram_inv),
        .out(chany_bottom_out[6])
    );
    mux2_size2 mux_bottom_track_15
    (
        .in({chanx_right_in[11], grid_bottom_l_inpad[5]}),
        .sram(mux2_size2_25_sram),
        .sram_inv(mux2_size2_25_sram_inv),
        .out(chany_bottom_out[7])
    );
    mux2_size2 mux_bottom_track_17
    (
        .in({chanx_right_in[10], grid_bottom_l_inpad[6]}),
        .sram(mux2_size2_26_sram),
        .sram_inv(mux2_size2_26_sram_inv),
        .out(chany_bottom_out[8])
    );
    mux2_size2 mux_bottom_track_19
    (
        .in({chanx_right_in[9], grid_bottom_l_inpad[7]}),
        .sram(mux2_size2_27_sram),
        .sram_inv(mux2_size2_27_sram_inv),
        .out(chany_bottom_out[9])
    );
    mux2_size2 mux_bottom_track_21
    (
        .in({chanx_right_in[8], grid_bottom_r_in[0]}),
        .sram(mux2_size2_28_sram),
        .sram_inv(mux2_size2_28_sram_inv),
        .out(chany_bottom_out[10])
    );
    mux2_size2 mux_bottom_track_23
    (
        .in({chanx_right_in[7], grid_bottom_r_in[1]}),
        .sram(mux2_size2_29_sram),
        .sram_inv(mux2_size2_29_sram_inv),
        .out(chany_bottom_out[11])
    );
    mux2_size2 mux_bottom_track_25
    (
        .in({chanx_right_in[6], grid_bottom_l_inpad[0]}),
        .sram(mux2_size2_30_sram),
        .sram_inv(mux2_size2_30_sram_inv),
        .out(chany_bottom_out[12])
    );
    mux2_size2 mux_bottom_track_27
    (
        .in({chanx_right_in[5], grid_bottom_l_inpad[1]}),
        .sram(mux2_size2_31_sram),
        .sram_inv(mux2_size2_31_sram_inv),
        .out(chany_bottom_out[13])
    );
    mux2_size2 mux_bottom_track_29
    (
        .in({chanx_right_in[4], grid_bottom_l_inpad[2]}),
        .sram(mux2_size2_32_sram),
        .sram_inv(mux2_size2_32_sram_inv),
        .out(chany_bottom_out[14])
    );
    mux2_size2 mux_bottom_track_31
    (
        .in({chanx_right_in[3], grid_bottom_l_inpad[3]}),
        .sram(mux2_size2_33_sram),
        .sram_inv(mux2_size2_33_sram_inv),
        .out(chany_bottom_out[15])
    );
    mux2_size2 mux_bottom_track_33
    (
        .in({chanx_right_in[2], grid_bottom_l_inpad[4]}),
        .sram(mux2_size2_34_sram),
        .sram_inv(mux2_size2_34_sram_inv),
        .out(chany_bottom_out[16])
    );
    mux2_size2 mux_bottom_track_35
    (
        .in({chanx_right_in[1], grid_bottom_l_inpad[5]}),
        .sram(mux2_size2_35_sram),
        .sram_inv(mux2_size2_35_sram_inv),
        .out(chany_bottom_out[17])
    );
    mux2_size2 mux_bottom_track_37
    (
        .in({chanx_right_in[0], grid_bottom_l_inpad[6]}),
        .sram(mux2_size2_36_sram),
        .sram_inv(mux2_size2_36_sram_inv),
        .out(chany_bottom_out[18])
    );
    mux2_size2 mux_bottom_track_39
    (
        .in({chanx_right_in[19], grid_bottom_l_inpad[7]}),
        .sram(mux2_size2_37_sram),
        .sram_inv(mux2_size2_37_sram_inv),
        .out(chany_bottom_out[19])
    );
    mux2_size2_mem mem_right_track_2
    (
        .bl(bl[2:3]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_0_sram),
        .mem_outb(mux2_size2_0_sram_inv)
    );
    mux2_size2_mem mem_right_track_4
    (
        .bl(bl[4:5]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_1_sram),
        .mem_outb(mux2_size2_1_sram_inv)
    );
    mux2_size2_mem mem_right_track_6
    (
        .bl(bl[6:7]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_2_sram),
        .mem_outb(mux2_size2_2_sram_inv)
    );
    mux2_size2_mem mem_right_track_8
    (
        .bl(bl[8:9]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_3_sram),
        .mem_outb(mux2_size2_3_sram_inv)
    );
    mux2_size2_mem mem_right_track_10
    (
        .bl(bl[10:11]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_4_sram),
        .mem_outb(mux2_size2_4_sram_inv)
    );
    mux2_size2_mem mem_right_track_12
    (
        .bl(bl[12:13]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_5_sram),
        .mem_outb(mux2_size2_5_sram_inv)
    );
    mux2_size2_mem mem_right_track_14
    (
        .bl(bl[14:15]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_6_sram),
        .mem_outb(mux2_size2_6_sram_inv)
    );
    mux2_size2_mem mem_right_track_16
    (
        .bl(bl[16:17]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_7_sram),
        .mem_outb(mux2_size2_7_sram_inv)
    );
    mux2_size2_mem mem_right_track_18
    (
        .bl(bl[18:19]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_8_sram),
        .mem_outb(mux2_size2_8_sram_inv)
    );
    mux2_size2_mem mem_right_track_22
    (
        .bl(bl[22:23]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_9_sram),
        .mem_outb(mux2_size2_9_sram_inv)
    );
    mux2_size2_mem mem_right_track_24
    (
        .bl(bl[24:25]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_10_sram),
        .mem_outb(mux2_size2_10_sram_inv)
    );
    mux2_size2_mem mem_right_track_26
    (
        .bl(bl[26:27]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_11_sram),
        .mem_outb(mux2_size2_11_sram_inv)
    );
    mux2_size2_mem mem_right_track_28
    (
        .bl(bl[28:29]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_12_sram),
        .mem_outb(mux2_size2_12_sram_inv)
    );
    mux2_size2_mem mem_right_track_30
    (
        .bl(bl[30:31]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_13_sram),
        .mem_outb(mux2_size2_13_sram_inv)
    );
    mux2_size2_mem mem_right_track_32
    (
        .bl(bl[32:33]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_14_sram),
        .mem_outb(mux2_size2_14_sram_inv)
    );
    mux2_size2_mem mem_right_track_34
    (
        .bl(bl[34:35]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_15_sram),
        .mem_outb(mux2_size2_15_sram_inv)
    );
    mux2_size2_mem mem_right_track_36
    (
        .bl(bl[36:37]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_16_sram),
        .mem_outb(mux2_size2_16_sram_inv)
    );
    mux2_size2_mem mem_right_track_38
    (
        .bl(bl[38:39]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_17_sram),
        .mem_outb(mux2_size2_17_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_1
    (
        .bl(bl[40:41]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_18_sram),
        .mem_outb(mux2_size2_18_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_3
    (
        .bl(bl[42:43]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_19_sram),
        .mem_outb(mux2_size2_19_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_5
    (
        .bl(bl[44:45]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_20_sram),
        .mem_outb(mux2_size2_20_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_7
    (
        .bl(bl[46:47]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_21_sram),
        .mem_outb(mux2_size2_21_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_9
    (
        .bl(bl[48:49]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_22_sram),
        .mem_outb(mux2_size2_22_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_11
    (
        .bl(bl[50:51]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_23_sram),
        .mem_outb(mux2_size2_23_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_13
    (
        .bl(bl[52:53]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_24_sram),
        .mem_outb(mux2_size2_24_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_15
    (
        .bl(bl[54:55]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_25_sram),
        .mem_outb(mux2_size2_25_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_17
    (
        .bl(bl[56:57]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_26_sram),
        .mem_outb(mux2_size2_26_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_19
    (
        .bl(bl[58:59]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_27_sram),
        .mem_outb(mux2_size2_27_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_21
    (
        .bl(bl[60:61]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_28_sram),
        .mem_outb(mux2_size2_28_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_23
    (
        .bl(bl[62:63]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_29_sram),
        .mem_outb(mux2_size2_29_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_25
    (
        .bl(bl[64:65]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_30_sram),
        .mem_outb(mux2_size2_30_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_27
    (
        .bl(bl[66:67]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_31_sram),
        .mem_outb(mux2_size2_31_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_29
    (
        .bl(bl[68:69]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_32_sram),
        .mem_outb(mux2_size2_32_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_31
    (
        .bl(bl[70:71]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_33_sram),
        .mem_outb(mux2_size2_33_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_33
    (
        .bl(bl[72:73]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_34_sram),
        .mem_outb(mux2_size2_34_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_35
    (
        .bl(bl[74:75]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_35_sram),
        .mem_outb(mux2_size2_35_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_37
    (
        .bl(bl[76:77]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_36_sram),
        .mem_outb(mux2_size2_36_sram_inv)
    );
    mux2_size2_mem mem_bottom_track_39
    (
        .bl(bl[78:79]),
        .wl({wl[0], wl[0]}),
        .mem_out(mux2_size2_37_sram),
        .mem_outb(mux2_size2_37_sram_inv)
    );
endmodule

