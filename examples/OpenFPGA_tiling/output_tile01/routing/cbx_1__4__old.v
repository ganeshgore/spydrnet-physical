//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module cbx_1__4__old
(
    chanx_left_in,
    chanx_right_in,
    bl,
    wl,
    chanx_left_out,
    chanx_right_out,
    grid_top_outpad,
    grid_bottom_out
);

    input [0:19]chanx_left_in;
    input [0:19]chanx_right_in;
    input [0:71]bl;
    input [0:71]wl;
    output [0:19]chanx_left_out;
    output [0:19]chanx_right_out;
    output [0:7]grid_top_outpad;
    output [0:9]grid_bottom_out;

    wire [0:19]chanx_left_in;
    wire [0:19]chanx_right_in;
    wire [0:71]bl;
    wire [0:71]wl;
    wire [0:19]chanx_left_out;
    wire [0:19]chanx_right_out;
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
    wire [0:7]grid_top_outpad;
    wire [0:9]grid_bottom_out;

assign chanx_right_out[0] = chanx_left_in[0];
assign chanx_right_out[1] = chanx_left_in[1];
assign chanx_right_out[2] = chanx_left_in[2];
assign chanx_right_out[3] = chanx_left_in[3];
assign chanx_right_out[4] = chanx_left_in[4];
assign chanx_right_out[5] = chanx_left_in[5];
assign chanx_right_out[6] = chanx_left_in[6];
assign chanx_right_out[7] = chanx_left_in[7];
assign chanx_right_out[8] = chanx_left_in[8];
assign chanx_right_out[9] = chanx_left_in[9];
assign chanx_right_out[10] = chanx_left_in[10];
assign chanx_right_out[11] = chanx_left_in[11];
assign chanx_right_out[12] = chanx_left_in[12];
assign chanx_right_out[13] = chanx_left_in[13];
assign chanx_right_out[14] = chanx_left_in[14];
assign chanx_right_out[15] = chanx_left_in[15];
assign chanx_right_out[16] = chanx_left_in[16];
assign chanx_right_out[17] = chanx_left_in[17];
assign chanx_right_out[18] = chanx_left_in[18];
assign chanx_right_out[19] = chanx_left_in[19];
assign chanx_left_out[0] = chanx_right_in[0];
assign chanx_left_out[1] = chanx_right_in[1];
assign chanx_left_out[2] = chanx_right_in[2];
assign chanx_left_out[3] = chanx_right_in[3];
assign chanx_left_out[4] = chanx_right_in[4];
assign chanx_left_out[5] = chanx_right_in[5];
assign chanx_left_out[6] = chanx_right_in[6];
assign chanx_left_out[7] = chanx_right_in[7];
assign chanx_left_out[8] = chanx_right_in[8];
assign chanx_left_out[9] = chanx_right_in[9];
assign chanx_left_out[10] = chanx_right_in[10];
assign chanx_left_out[11] = chanx_right_in[11];
assign chanx_left_out[12] = chanx_right_in[12];
assign chanx_left_out[13] = chanx_right_in[13];
assign chanx_left_out[14] = chanx_right_in[14];
assign chanx_left_out[15] = chanx_right_in[15];
assign chanx_left_out[16] = chanx_right_in[16];
assign chanx_left_out[17] = chanx_right_in[17];
assign chanx_left_out[18] = chanx_right_in[18];
assign chanx_left_out[19] = chanx_right_in[19];
    mux2_size8 mux_bottom_ipin_0
    (
        .in({chanx_left_in[0], chanx_right_in[0], chanx_left_in[6], chanx_right_in[6], chanx_left_in[12], chanx_right_in[12], chanx_left_in[18], chanx_right_in[18]}),
        .sram(mux2_size8_0_sram),
        .sram_inv(mux2_size8_0_sram_inv),
        .out(grid_top_outpad[0])
    );
    mux2_size8 mux_bottom_ipin_1
    (
        .in({chanx_left_in[1], chanx_right_in[1], chanx_left_in[7], chanx_right_in[7], chanx_left_in[13], chanx_right_in[13], chanx_left_in[19], chanx_right_in[19]}),
        .sram(mux2_size8_1_sram),
        .sram_inv(mux2_size8_1_sram_inv),
        .out(grid_top_outpad[1])
    );
    mux2_size8 mux_bottom_ipin_2
    (
        .in({chanx_left_in[0], chanx_right_in[0], chanx_left_in[2], chanx_right_in[2], chanx_left_in[8], chanx_right_in[8], chanx_left_in[14], chanx_right_in[14]}),
        .sram(mux2_size8_2_sram),
        .sram_inv(mux2_size8_2_sram_inv),
        .out(grid_top_outpad[2])
    );
    mux2_size8 mux_bottom_ipin_3
    (
        .in({chanx_left_in[1], chanx_right_in[1], chanx_left_in[3], chanx_right_in[3], chanx_left_in[9], chanx_right_in[9], chanx_left_in[15], chanx_right_in[15]}),
        .sram(mux2_size8_3_sram),
        .sram_inv(mux2_size8_3_sram_inv),
        .out(grid_top_outpad[3])
    );
    mux2_size8 mux_bottom_ipin_4
    (
        .in({chanx_left_in[2], chanx_right_in[2], chanx_left_in[4], chanx_right_in[4], chanx_left_in[10], chanx_right_in[10], chanx_left_in[16], chanx_right_in[16]}),
        .sram(mux2_size8_4_sram),
        .sram_inv(mux2_size8_4_sram_inv),
        .out(grid_top_outpad[4])
    );
    mux2_size8 mux_bottom_ipin_5
    (
        .in({chanx_left_in[3], chanx_right_in[3], chanx_left_in[5], chanx_right_in[5], chanx_left_in[11], chanx_right_in[11], chanx_left_in[17], chanx_right_in[17]}),
        .sram(mux2_size8_5_sram),
        .sram_inv(mux2_size8_5_sram_inv),
        .out(grid_top_outpad[5])
    );
    mux2_size8 mux_bottom_ipin_6
    (
        .in({chanx_left_in[4], chanx_right_in[4], chanx_left_in[6], chanx_right_in[6], chanx_left_in[12], chanx_right_in[12], chanx_left_in[18], chanx_right_in[18]}),
        .sram(mux2_size8_6_sram),
        .sram_inv(mux2_size8_6_sram_inv),
        .out(grid_top_outpad[6])
    );
    mux2_size8 mux_bottom_ipin_7
    (
        .in({chanx_left_in[5], chanx_right_in[5], chanx_left_in[7], chanx_right_in[7], chanx_left_in[13], chanx_right_in[13], chanx_left_in[19], chanx_right_in[19]}),
        .sram(mux2_size8_7_sram),
        .sram_inv(mux2_size8_7_sram_inv),
        .out(grid_top_outpad[7])
    );
    mux2_size8 mux_top_ipin_0
    (
        .in({chanx_left_in[0], chanx_right_in[0], chanx_left_in[6], chanx_right_in[6], chanx_left_in[8], chanx_right_in[8], chanx_left_in[14], chanx_right_in[14]}),
        .sram(mux2_size8_8_sram),
        .sram_inv(mux2_size8_8_sram_inv),
        .out(grid_bottom_out[0])
    );
    mux2_size8 mux_top_ipin_1
    (
        .in({chanx_left_in[1], chanx_right_in[1], chanx_left_in[7], chanx_right_in[7], chanx_left_in[9], chanx_right_in[9], chanx_left_in[15], chanx_right_in[15]}),
        .sram(mux2_size8_9_sram),
        .sram_inv(mux2_size8_9_sram_inv),
        .out(grid_bottom_out[1])
    );
    mux2_size8 mux_top_ipin_2
    (
        .in({chanx_left_in[2], chanx_right_in[2], chanx_left_in[8], chanx_right_in[8], chanx_left_in[10], chanx_right_in[10], chanx_left_in[16], chanx_right_in[16]}),
        .sram(mux2_size8_10_sram),
        .sram_inv(mux2_size8_10_sram_inv),
        .out(grid_bottom_out[2])
    );
    mux2_size8 mux_top_ipin_3
    (
        .in({chanx_left_in[3], chanx_right_in[3], chanx_left_in[9], chanx_right_in[9], chanx_left_in[11], chanx_right_in[11], chanx_left_in[17], chanx_right_in[17]}),
        .sram(mux2_size8_11_sram),
        .sram_inv(mux2_size8_11_sram_inv),
        .out(grid_bottom_out[3])
    );
    mux2_size8 mux_top_ipin_4
    (
        .in({chanx_left_in[4], chanx_right_in[4], chanx_left_in[10], chanx_right_in[10], chanx_left_in[12], chanx_right_in[12], chanx_left_in[18], chanx_right_in[18]}),
        .sram(mux2_size8_12_sram),
        .sram_inv(mux2_size8_12_sram_inv),
        .out(grid_bottom_out[4])
    );
    mux2_size8 mux_top_ipin_5
    (
        .in({chanx_left_in[5], chanx_right_in[5], chanx_left_in[11], chanx_right_in[11], chanx_left_in[13], chanx_right_in[13], chanx_left_in[19], chanx_right_in[19]}),
        .sram(mux2_size8_13_sram),
        .sram_inv(mux2_size8_13_sram_inv),
        .out(grid_bottom_out[5])
    );
    mux2_size8 mux_top_ipin_6
    (
        .in({chanx_left_in[0], chanx_right_in[0], chanx_left_in[6], chanx_right_in[6], chanx_left_in[12], chanx_right_in[12], chanx_left_in[14], chanx_right_in[14]}),
        .sram(mux2_size8_14_sram),
        .sram_inv(mux2_size8_14_sram_inv),
        .out(grid_bottom_out[6])
    );
    mux2_size8 mux_top_ipin_7
    (
        .in({chanx_left_in[1], chanx_right_in[1], chanx_left_in[7], chanx_right_in[7], chanx_left_in[13], chanx_right_in[13], chanx_left_in[15], chanx_right_in[15]}),
        .sram(mux2_size8_15_sram),
        .sram_inv(mux2_size8_15_sram_inv),
        .out(grid_bottom_out[7])
    );
    mux2_size8 mux_top_ipin_8
    (
        .in({chanx_left_in[2], chanx_right_in[2], chanx_left_in[8], chanx_right_in[8], chanx_left_in[14], chanx_right_in[14], chanx_left_in[16], chanx_right_in[16]}),
        .sram(mux2_size8_16_sram),
        .sram_inv(mux2_size8_16_sram_inv),
        .out(grid_bottom_out[8])
    );
    mux2_size8 mux_top_ipin_9
    (
        .in({chanx_left_in[3], chanx_right_in[3], chanx_left_in[9], chanx_right_in[9], chanx_left_in[15], chanx_right_in[15], chanx_left_in[17], chanx_right_in[17]}),
        .sram(mux2_size8_17_sram),
        .sram_inv(mux2_size8_17_sram_inv),
        .out(grid_bottom_out[9])
    );
    mux2_size8_mem mem_bottom_ipin_0
    (
        .bl(bl[0:3]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_0_sram),
        .mem_outb(mux2_size8_0_sram_inv)
    );
    mux2_size8_mem mem_bottom_ipin_1
    (
        .bl(bl[4:7]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_1_sram),
        .mem_outb(mux2_size8_1_sram_inv)
    );
    mux2_size8_mem mem_bottom_ipin_2
    (
        .bl(bl[8:11]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_2_sram),
        .mem_outb(mux2_size8_2_sram_inv)
    );
    mux2_size8_mem mem_bottom_ipin_3
    (
        .bl(bl[12:15]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_3_sram),
        .mem_outb(mux2_size8_3_sram_inv)
    );
    mux2_size8_mem mem_bottom_ipin_4
    (
        .bl(bl[16:19]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_4_sram),
        .mem_outb(mux2_size8_4_sram_inv)
    );
    mux2_size8_mem mem_bottom_ipin_5
    (
        .bl(bl[20:23]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_5_sram),
        .mem_outb(mux2_size8_5_sram_inv)
    );
    mux2_size8_mem mem_bottom_ipin_6
    (
        .bl(bl[24:27]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_6_sram),
        .mem_outb(mux2_size8_6_sram_inv)
    );
    mux2_size8_mem mem_bottom_ipin_7
    (
        .bl(bl[28:31]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_7_sram),
        .mem_outb(mux2_size8_7_sram_inv)
    );
    mux2_size8_mem mem_top_ipin_0
    (
        .bl(bl[32:35]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_8_sram),
        .mem_outb(mux2_size8_8_sram_inv)
    );
    mux2_size8_mem mem_top_ipin_1
    (
        .bl(bl[36:39]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_9_sram),
        .mem_outb(mux2_size8_9_sram_inv)
    );
    mux2_size8_mem mem_top_ipin_2
    (
        .bl(bl[40:43]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_10_sram),
        .mem_outb(mux2_size8_10_sram_inv)
    );
    mux2_size8_mem mem_top_ipin_3
    (
        .bl(bl[44:47]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_11_sram),
        .mem_outb(mux2_size8_11_sram_inv)
    );
    mux2_size8_mem mem_top_ipin_4
    (
        .bl(bl[48:51]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_12_sram),
        .mem_outb(mux2_size8_12_sram_inv)
    );
    mux2_size8_mem mem_top_ipin_5
    (
        .bl(bl[52:55]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_13_sram),
        .mem_outb(mux2_size8_13_sram_inv)
    );
    mux2_size8_mem mem_top_ipin_6
    (
        .bl(bl[56:59]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_14_sram),
        .mem_outb(mux2_size8_14_sram_inv)
    );
    mux2_size8_mem mem_top_ipin_7
    (
        .bl(bl[60:63]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_15_sram),
        .mem_outb(mux2_size8_15_sram_inv)
    );
    mux2_size8_mem mem_top_ipin_8
    (
        .bl(bl[64:67]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_16_sram),
        .mem_outb(mux2_size8_16_sram_inv)
    );
    mux2_size8_mem mem_top_ipin_9
    (
        .bl(bl[68:71]),
        .wl({wl[0], wl[0], wl[0], wl[0]}),
        .mem_out(mux2_size8_17_sram),
        .mem_outb(mux2_size8_17_sram_inv)
    );
endmodule

