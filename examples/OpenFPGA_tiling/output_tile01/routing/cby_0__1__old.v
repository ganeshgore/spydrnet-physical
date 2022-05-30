//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module cby_0__1__old
(
    chany_bottom_in,
    chany_top_in,
    bl,
    wl,
    chany_bottom_out,
    chany_top_out,
    grid_right_out,
    grid_left_outpad
);

    input [0:19]chany_bottom_in;
    input [0:19]chany_top_in;
    input [0:71]bl;
    input [0:71]wl;
    output [0:19]chany_bottom_out;
    output [0:19]chany_top_out;
    output [0:9]grid_right_out;
    output [0:7]grid_left_outpad;

    wire [0:19]chany_bottom_in;
    wire [0:19]chany_top_in;
    wire [0:71]bl;
    wire [0:71]wl;
    wire [0:19]chany_bottom_out;
    wire [0:19]chany_top_out;
    wire [0:3]mux2_size8_0_sram;
    wire [0:3]mux2_size8_0_sram_inv;
    wire [0:3]mux2_size8_10_sram;
    wire [0:3]mux2_size8_10_sram_inv;
    wire [0:3]mux2_size8_11_sram;
    wire [0:3]mux2_size8_11_sram_inv;
    wire [0:3]mux2_size8_12_sram;
    wire [0:3]mux2_size8_12_sram_inv;
    wire [0:3]mux2_size8_13_sram;
    wire [0:3]mux2_size8_13_sram_inv;
    wire [0:3]mux2_size8_14_sram;
    wire [0:3]mux2_size8_14_sram_inv;
    wire [0:3]mux2_size8_15_sram;
    wire [0:3]mux2_size8_15_sram_inv;
    wire [0:3]mux2_size8_16_sram;
    wire [0:3]mux2_size8_16_sram_inv;
    wire [0:3]mux2_size8_17_sram;
    wire [0:3]mux2_size8_17_sram_inv;
    wire [0:3]mux2_size8_1_sram;
    wire [0:3]mux2_size8_1_sram_inv;
    wire [0:3]mux2_size8_2_sram;
    wire [0:3]mux2_size8_2_sram_inv;
    wire [0:3]mux2_size8_3_sram;
    wire [0:3]mux2_size8_3_sram_inv;
    wire [0:3]mux2_size8_4_sram;
    wire [0:3]mux2_size8_4_sram_inv;
    wire [0:3]mux2_size8_5_sram;
    wire [0:3]mux2_size8_5_sram_inv;
    wire [0:3]mux2_size8_6_sram;
    wire [0:3]mux2_size8_6_sram_inv;
    wire [0:3]mux2_size8_7_sram;
    wire [0:3]mux2_size8_7_sram_inv;
    wire [0:3]mux2_size8_8_sram;
    wire [0:3]mux2_size8_8_sram_inv;
    wire [0:3]mux2_size8_9_sram;
    wire [0:3]mux2_size8_9_sram_inv;
    wire [0:9]grid_right_out;
    wire [0:7]grid_left_outpad;

assign chany_top_out[0] = chany_bottom_in[0];
assign chany_top_out[1] = chany_bottom_in[1];
assign chany_top_out[2] = chany_bottom_in[2];
assign chany_top_out[3] = chany_bottom_in[3];
assign chany_top_out[4] = chany_bottom_in[4];
assign chany_top_out[5] = chany_bottom_in[5];
assign chany_top_out[6] = chany_bottom_in[6];
assign chany_top_out[7] = chany_bottom_in[7];
assign chany_top_out[8] = chany_bottom_in[8];
assign chany_top_out[9] = chany_bottom_in[9];
assign chany_top_out[10] = chany_bottom_in[10];
assign chany_top_out[11] = chany_bottom_in[11];
assign chany_top_out[12] = chany_bottom_in[12];
assign chany_top_out[13] = chany_bottom_in[13];
assign chany_top_out[14] = chany_bottom_in[14];
assign chany_top_out[15] = chany_bottom_in[15];
assign chany_top_out[16] = chany_bottom_in[16];
assign chany_top_out[17] = chany_bottom_in[17];
assign chany_top_out[18] = chany_bottom_in[18];
assign chany_top_out[19] = chany_bottom_in[19];
assign chany_bottom_out[0] = chany_top_in[0];
assign chany_bottom_out[1] = chany_top_in[1];
assign chany_bottom_out[2] = chany_top_in[2];
assign chany_bottom_out[3] = chany_top_in[3];
assign chany_bottom_out[4] = chany_top_in[4];
assign chany_bottom_out[5] = chany_top_in[5];
assign chany_bottom_out[6] = chany_top_in[6];
assign chany_bottom_out[7] = chany_top_in[7];
assign chany_bottom_out[8] = chany_top_in[8];
assign chany_bottom_out[9] = chany_top_in[9];
assign chany_bottom_out[10] = chany_top_in[10];
assign chany_bottom_out[11] = chany_top_in[11];
assign chany_bottom_out[12] = chany_top_in[12];
assign chany_bottom_out[13] = chany_top_in[13];
assign chany_bottom_out[14] = chany_top_in[14];
assign chany_bottom_out[15] = chany_top_in[15];
assign chany_bottom_out[16] = chany_top_in[16];
assign chany_bottom_out[17] = chany_top_in[17];
assign chany_bottom_out[18] = chany_top_in[18];
assign chany_bottom_out[19] = chany_top_in[19];
    mux2_size8 mux_left_ipin_0
    (
        .in({chany_bottom_in[0], chany_top_in[0], chany_bottom_in[6], chany_top_in[6], chany_bottom_in[12], chany_top_in[12], chany_bottom_in[18], chany_top_in[18]}),
        .sram(mux2_size8_0_sram),
        .sram_inv(mux2_size8_0_sram_inv),
        .out(grid_right_out[0])
    );
    mux2_size8 mux_left_ipin_1
    (
        .in({chany_bottom_in[1], chany_top_in[1], chany_bottom_in[7], chany_top_in[7], chany_bottom_in[13], chany_top_in[13], chany_bottom_in[19], chany_top_in[19]}),
        .sram(mux2_size8_1_sram),
        .sram_inv(mux2_size8_1_sram_inv),
        .out(grid_right_out[1])
    );
    mux2_size8 mux_left_ipin_2
    (
        .in({chany_bottom_in[0], chany_top_in[0], chany_bottom_in[2], chany_top_in[2], chany_bottom_in[8], chany_top_in[8], chany_bottom_in[14], chany_top_in[14]}),
        .sram(mux2_size8_2_sram),
        .sram_inv(mux2_size8_2_sram_inv),
        .out(grid_right_out[2])
    );
    mux2_size8 mux_left_ipin_3
    (
        .in({chany_bottom_in[1], chany_top_in[1], chany_bottom_in[3], chany_top_in[3], chany_bottom_in[9], chany_top_in[9], chany_bottom_in[15], chany_top_in[15]}),
        .sram(mux2_size8_3_sram),
        .sram_inv(mux2_size8_3_sram_inv),
        .out(grid_right_out[3])
    );
    mux2_size8 mux_left_ipin_4
    (
        .in({chany_bottom_in[2], chany_top_in[2], chany_bottom_in[4], chany_top_in[4], chany_bottom_in[10], chany_top_in[10], chany_bottom_in[16], chany_top_in[16]}),
        .sram(mux2_size8_4_sram),
        .sram_inv(mux2_size8_4_sram_inv),
        .out(grid_right_out[4])
    );
    mux2_size8 mux_left_ipin_5
    (
        .in({chany_bottom_in[3], chany_top_in[3], chany_bottom_in[5], chany_top_in[5], chany_bottom_in[11], chany_top_in[11], chany_bottom_in[17], chany_top_in[17]}),
        .sram(mux2_size8_5_sram),
        .sram_inv(mux2_size8_5_sram_inv),
        .out(grid_right_out[5])
    );
    mux2_size8 mux_left_ipin_6
    (
        .in({chany_bottom_in[4], chany_top_in[4], chany_bottom_in[6], chany_top_in[6], chany_bottom_in[12], chany_top_in[12], chany_bottom_in[18], chany_top_in[18]}),
        .sram(mux2_size8_6_sram),
        .sram_inv(mux2_size8_6_sram_inv),
        .out(grid_right_out[6])
    );
    mux2_size8 mux_left_ipin_7
    (
        .in({chany_bottom_in[5], chany_top_in[5], chany_bottom_in[7], chany_top_in[7], chany_bottom_in[13], chany_top_in[13], chany_bottom_in[19], chany_top_in[19]}),
        .sram(mux2_size8_7_sram),
        .sram_inv(mux2_size8_7_sram_inv),
        .out(grid_right_out[7])
    );
    mux2_size8 mux_left_ipin_8
    (
        .in({chany_bottom_in[0], chany_top_in[0], chany_bottom_in[6], chany_top_in[6], chany_bottom_in[8], chany_top_in[8], chany_bottom_in[14], chany_top_in[14]}),
        .sram(mux2_size8_8_sram),
        .sram_inv(mux2_size8_8_sram_inv),
        .out(grid_right_out[8])
    );
    mux2_size8 mux_left_ipin_9
    (
        .in({chany_bottom_in[1], chany_top_in[1], chany_bottom_in[7], chany_top_in[7], chany_bottom_in[9], chany_top_in[9], chany_bottom_in[15], chany_top_in[15]}),
        .sram(mux2_size8_9_sram),
        .sram_inv(mux2_size8_9_sram_inv),
        .out(grid_right_out[9])
    );
    mux2_size8 mux_right_ipin_0
    (
        .in({chany_bottom_in[2], chany_top_in[2], chany_bottom_in[8], chany_top_in[8], chany_bottom_in[10], chany_top_in[10], chany_bottom_in[16], chany_top_in[16]}),
        .sram(mux2_size8_10_sram),
        .sram_inv(mux2_size8_10_sram_inv),
        .out(grid_left_outpad[0])
    );
    mux2_size8 mux_right_ipin_1
    (
        .in({chany_bottom_in[3], chany_top_in[3], chany_bottom_in[9], chany_top_in[9], chany_bottom_in[11], chany_top_in[11], chany_bottom_in[17], chany_top_in[17]}),
        .sram(mux2_size8_11_sram),
        .sram_inv(mux2_size8_11_sram_inv),
        .out(grid_left_outpad[1])
    );
    mux2_size8 mux_right_ipin_2
    (
        .in({chany_bottom_in[4], chany_top_in[4], chany_bottom_in[10], chany_top_in[10], chany_bottom_in[12], chany_top_in[12], chany_bottom_in[18], chany_top_in[18]}),
        .sram(mux2_size8_12_sram),
        .sram_inv(mux2_size8_12_sram_inv),
        .out(grid_left_outpad[2])
    );
    mux2_size8 mux_right_ipin_3
    (
        .in({chany_bottom_in[5], chany_top_in[5], chany_bottom_in[11], chany_top_in[11], chany_bottom_in[13], chany_top_in[13], chany_bottom_in[19], chany_top_in[19]}),
        .sram(mux2_size8_13_sram),
        .sram_inv(mux2_size8_13_sram_inv),
        .out(grid_left_outpad[3])
    );
    mux2_size8 mux_right_ipin_4
    (
        .in({chany_bottom_in[0], chany_top_in[0], chany_bottom_in[6], chany_top_in[6], chany_bottom_in[12], chany_top_in[12], chany_bottom_in[14], chany_top_in[14]}),
        .sram(mux2_size8_14_sram),
        .sram_inv(mux2_size8_14_sram_inv),
        .out(grid_left_outpad[4])
    );
    mux2_size8 mux_right_ipin_5
    (
        .in({chany_bottom_in[1], chany_top_in[1], chany_bottom_in[7], chany_top_in[7], chany_bottom_in[13], chany_top_in[13], chany_bottom_in[15], chany_top_in[15]}),
        .sram(mux2_size8_15_sram),
        .sram_inv(mux2_size8_15_sram_inv),
        .out(grid_left_outpad[5])
    );
    mux2_size8 mux_right_ipin_6
    (
        .in({chany_bottom_in[2], chany_top_in[2], chany_bottom_in[8], chany_top_in[8], chany_bottom_in[14], chany_top_in[14], chany_bottom_in[16], chany_top_in[16]}),
        .sram(mux2_size8_16_sram),
        .sram_inv(mux2_size8_16_sram_inv),
        .out(grid_left_outpad[6])
    );
    mux2_size8 mux_right_ipin_7
    (
        .in({chany_bottom_in[3], chany_top_in[3], chany_bottom_in[9], chany_top_in[9], chany_bottom_in[15], chany_top_in[15], chany_bottom_in[17], chany_top_in[17]}),
        .sram(mux2_size8_17_sram),
        .sram_inv(mux2_size8_17_sram_inv),
        .out(grid_left_outpad[7])
    );
    mux2_size8_mem mem_left_ipin_0
    (
        .bl(bl[0:3]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_0_sram),
        .mem_outb(mux2_size8_0_sram_inv)
    );
    mux2_size8_mem mem_left_ipin_1
    (
        .bl(bl[4:7]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_1_sram),
        .mem_outb(mux2_size8_1_sram_inv)
    );
    mux2_size8_mem mem_left_ipin_2
    (
        .bl(bl[8:11]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_2_sram),
        .mem_outb(mux2_size8_2_sram_inv)
    );
    mux2_size8_mem mem_left_ipin_3
    (
        .bl(bl[12:15]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_3_sram),
        .mem_outb(mux2_size8_3_sram_inv)
    );
    mux2_size8_mem mem_left_ipin_4
    (
        .bl(bl[16:19]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_4_sram),
        .mem_outb(mux2_size8_4_sram_inv)
    );
    mux2_size8_mem mem_left_ipin_5
    (
        .bl(bl[20:23]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_5_sram),
        .mem_outb(mux2_size8_5_sram_inv)
    );
    mux2_size8_mem mem_left_ipin_6
    (
        .bl(bl[24:27]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_6_sram),
        .mem_outb(mux2_size8_6_sram_inv)
    );
    mux2_size8_mem mem_left_ipin_7
    (
        .bl(bl[28:31]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_7_sram),
        .mem_outb(mux2_size8_7_sram_inv)
    );
    mux2_size8_mem mem_left_ipin_8
    (
        .bl(bl[32:35]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_8_sram),
        .mem_outb(mux2_size8_8_sram_inv)
    );
    mux2_size8_mem mem_left_ipin_9
    (
        .bl(bl[36:39]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_9_sram),
        .mem_outb(mux2_size8_9_sram_inv)
    );
    mux2_size8_mem mem_right_ipin_0
    (
        .bl(bl[40:43]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_10_sram),
        .mem_outb(mux2_size8_10_sram_inv)
    );
    mux2_size8_mem mem_right_ipin_1
    (
        .bl(bl[44:47]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_11_sram),
        .mem_outb(mux2_size8_11_sram_inv)
    );
    mux2_size8_mem mem_right_ipin_2
    (
        .bl(bl[48:51]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_12_sram),
        .mem_outb(mux2_size8_12_sram_inv)
    );
    mux2_size8_mem mem_right_ipin_3
    (
        .bl(bl[52:55]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_13_sram),
        .mem_outb(mux2_size8_13_sram_inv)
    );
    mux2_size8_mem mem_right_ipin_4
    (
        .bl(bl[56:59]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_14_sram),
        .mem_outb(mux2_size8_14_sram_inv)
    );
    mux2_size8_mem mem_right_ipin_5
    (
        .bl(bl[60:63]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_15_sram),
        .mem_outb(mux2_size8_15_sram_inv)
    );
    mux2_size8_mem mem_right_ipin_6
    (
        .bl(bl[64:67]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_16_sram),
        .mem_outb(mux2_size8_16_sram_inv)
    );
    mux2_size8_mem mem_right_ipin_7
    (
        .bl(bl[68:71]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_17_sram),
        .mem_outb(mux2_size8_17_sram_inv)
    );
endmodule

