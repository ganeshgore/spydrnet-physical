//Generated from netlist by SpyDrNet
//netlist name: SDN_VERILOG_NETLIST_logical_tile_io_mode_physical__iopad
module logical_tile_clb_mode_clb_
(
    reset,
    clk,
    clb_I,
    clb_clk,
    bl,
    wl,
    clb_O
);

    input reset;
    input clk;
    input [0:39]clb_I;
    input clb_clk;
    input [0:1019]bl;
    input [0:1019]wl;
    output [0:9]clb_O;

    wire reset;
    wire clk;
    wire [0:39]clb_I;
    wire clb_clk;
    wire [0:1019]bl;
    wire [0:1019]wl;
    wire [0:9]clb_O;
    wire [0:5]mux2_size50_0_sram;
    wire [0:5]mux2_size50_0_sram_inv;
    wire [0:5]mux2_size50_10_sram;
    wire [0:5]mux2_size50_10_sram_inv;
    wire [0:5]mux2_size50_11_sram;
    wire [0:5]mux2_size50_11_sram_inv;
    wire [0:5]mux2_size50_12_sram;
    wire [0:5]mux2_size50_12_sram_inv;
    wire [0:5]mux2_size50_13_sram;
    wire [0:5]mux2_size50_13_sram_inv;
    wire [0:5]mux2_size50_14_sram;
    wire [0:5]mux2_size50_14_sram_inv;
    wire [0:5]mux2_size50_15_sram;
    wire [0:5]mux2_size50_15_sram_inv;
    wire [0:5]mux2_size50_16_sram;
    wire [0:5]mux2_size50_16_sram_inv;
    wire [0:5]mux2_size50_17_sram;
    wire [0:5]mux2_size50_17_sram_inv;
    wire [0:5]mux2_size50_18_sram;
    wire [0:5]mux2_size50_18_sram_inv;
    wire [0:5]mux2_size50_19_sram;
    wire [0:5]mux2_size50_19_sram_inv;
    wire [0:5]mux2_size50_1_sram;
    wire [0:5]mux2_size50_1_sram_inv;
    wire [0:5]mux2_size50_20_sram;
    wire [0:5]mux2_size50_20_sram_inv;
    wire [0:5]mux2_size50_21_sram;
    wire [0:5]mux2_size50_21_sram_inv;
    wire [0:5]mux2_size50_22_sram;
    wire [0:5]mux2_size50_22_sram_inv;
    wire [0:5]mux2_size50_23_sram;
    wire [0:5]mux2_size50_23_sram_inv;
    wire [0:5]mux2_size50_24_sram;
    wire [0:5]mux2_size50_24_sram_inv;
    wire [0:5]mux2_size50_25_sram;
    wire [0:5]mux2_size50_25_sram_inv;
    wire [0:5]mux2_size50_26_sram;
    wire [0:5]mux2_size50_26_sram_inv;
    wire [0:5]mux2_size50_27_sram;
    wire [0:5]mux2_size50_27_sram_inv;
    wire [0:5]mux2_size50_28_sram;
    wire [0:5]mux2_size50_28_sram_inv;
    wire [0:5]mux2_size50_29_sram;
    wire [0:5]mux2_size50_29_sram_inv;
    wire [0:5]mux2_size50_2_sram;
    wire [0:5]mux2_size50_2_sram_inv;
    wire [0:5]mux2_size50_30_sram;
    wire [0:5]mux2_size50_30_sram_inv;
    wire [0:5]mux2_size50_31_sram;
    wire [0:5]mux2_size50_31_sram_inv;
    wire [0:5]mux2_size50_32_sram;
    wire [0:5]mux2_size50_32_sram_inv;
    wire [0:5]mux2_size50_33_sram;
    wire [0:5]mux2_size50_33_sram_inv;
    wire [0:5]mux2_size50_34_sram;
    wire [0:5]mux2_size50_34_sram_inv;
    wire [0:5]mux2_size50_35_sram;
    wire [0:5]mux2_size50_35_sram_inv;
    wire [0:5]mux2_size50_36_sram;
    wire [0:5]mux2_size50_36_sram_inv;
    wire [0:5]mux2_size50_37_sram;
    wire [0:5]mux2_size50_37_sram_inv;
    wire [0:5]mux2_size50_38_sram;
    wire [0:5]mux2_size50_38_sram_inv;
    wire [0:5]mux2_size50_39_sram;
    wire [0:5]mux2_size50_39_sram_inv;
    wire [0:5]mux2_size50_3_sram;
    wire [0:5]mux2_size50_3_sram_inv;
    wire [0:5]mux2_size50_40_sram;
    wire [0:5]mux2_size50_40_sram_inv;
    wire [0:5]mux2_size50_41_sram;
    wire [0:5]mux2_size50_41_sram_inv;
    wire [0:5]mux2_size50_42_sram;
    wire [0:5]mux2_size50_42_sram_inv;
    wire [0:5]mux2_size50_43_sram;
    wire [0:5]mux2_size50_43_sram_inv;
    wire [0:5]mux2_size50_44_sram;
    wire [0:5]mux2_size50_44_sram_inv;
    wire [0:5]mux2_size50_45_sram;
    wire [0:5]mux2_size50_45_sram_inv;
    wire [0:5]mux2_size50_46_sram;
    wire [0:5]mux2_size50_46_sram_inv;
    wire [0:5]mux2_size50_47_sram;
    wire [0:5]mux2_size50_47_sram_inv;
    wire [0:5]mux2_size50_48_sram;
    wire [0:5]mux2_size50_48_sram_inv;
    wire [0:5]mux2_size50_49_sram;
    wire [0:5]mux2_size50_49_sram_inv;
    wire [0:5]mux2_size50_4_sram;
    wire [0:5]mux2_size50_4_sram_inv;
    wire [0:5]mux2_size50_50_sram;
    wire [0:5]mux2_size50_50_sram_inv;
    wire [0:5]mux2_size50_51_sram;
    wire [0:5]mux2_size50_51_sram_inv;
    wire [0:5]mux2_size50_52_sram;
    wire [0:5]mux2_size50_52_sram_inv;
    wire [0:5]mux2_size50_53_sram;
    wire [0:5]mux2_size50_53_sram_inv;
    wire [0:5]mux2_size50_54_sram;
    wire [0:5]mux2_size50_54_sram_inv;
    wire [0:5]mux2_size50_55_sram;
    wire [0:5]mux2_size50_55_sram_inv;
    wire [0:5]mux2_size50_56_sram;
    wire [0:5]mux2_size50_56_sram_inv;
    wire [0:5]mux2_size50_57_sram;
    wire [0:5]mux2_size50_57_sram_inv;
    wire [0:5]mux2_size50_58_sram;
    wire [0:5]mux2_size50_58_sram_inv;
    wire [0:5]mux2_size50_59_sram;
    wire [0:5]mux2_size50_59_sram_inv;
    wire [0:5]mux2_size50_5_sram;
    wire [0:5]mux2_size50_5_sram_inv;
    wire [0:5]mux2_size50_6_sram;
    wire [0:5]mux2_size50_6_sram_inv;
    wire [0:5]mux2_size50_7_sram;
    wire [0:5]mux2_size50_7_sram_inv;
    wire [0:5]mux2_size50_8_sram;
    wire [0:5]mux2_size50_8_sram_inv;
    wire [0:5]mux2_size50_9_sram;
    wire [0:5]mux2_size50_9_sram_inv;
    wire mux2_size50_0_out;
    wire mux2_size50_1_out;
    wire mux2_size50_2_out;
    wire mux2_size50_3_out;
    wire mux2_size50_4_out;
    wire mux2_size50_5_out;
    wire direct_interc_10_out;
    wire logical_tile_clb_mode_default__fle_0_fle_out;
    wire mux2_size50_6_out;
    wire mux2_size50_7_out;
    wire mux2_size50_8_out;
    wire mux2_size50_9_out;
    wire mux2_size50_10_out;
    wire mux2_size50_11_out;
    wire direct_interc_11_out;
    wire logical_tile_clb_mode_default__fle_1_fle_out;
    wire mux2_size50_12_out;
    wire mux2_size50_13_out;
    wire mux2_size50_14_out;
    wire mux2_size50_15_out;
    wire mux2_size50_16_out;
    wire mux2_size50_17_out;
    wire direct_interc_12_out;
    wire logical_tile_clb_mode_default__fle_2_fle_out;
    wire mux2_size50_18_out;
    wire mux2_size50_19_out;
    wire mux2_size50_20_out;
    wire mux2_size50_21_out;
    wire mux2_size50_22_out;
    wire mux2_size50_23_out;
    wire direct_interc_13_out;
    wire logical_tile_clb_mode_default__fle_3_fle_out;
    wire mux2_size50_24_out;
    wire mux2_size50_25_out;
    wire mux2_size50_26_out;
    wire mux2_size50_27_out;
    wire mux2_size50_28_out;
    wire mux2_size50_29_out;
    wire direct_interc_14_out;
    wire logical_tile_clb_mode_default__fle_4_fle_out;
    wire mux2_size50_30_out;
    wire mux2_size50_31_out;
    wire mux2_size50_32_out;
    wire mux2_size50_33_out;
    wire mux2_size50_34_out;
    wire mux2_size50_35_out;
    wire direct_interc_15_out;
    wire logical_tile_clb_mode_default__fle_5_fle_out;
    wire mux2_size50_36_out;
    wire mux2_size50_37_out;
    wire mux2_size50_38_out;
    wire mux2_size50_39_out;
    wire mux2_size50_40_out;
    wire mux2_size50_41_out;
    wire direct_interc_16_out;
    wire logical_tile_clb_mode_default__fle_6_fle_out;
    wire mux2_size50_42_out;
    wire mux2_size50_43_out;
    wire mux2_size50_44_out;
    wire mux2_size50_45_out;
    wire mux2_size50_46_out;
    wire mux2_size50_47_out;
    wire direct_interc_17_out;
    wire logical_tile_clb_mode_default__fle_7_fle_out;
    wire mux2_size50_48_out;
    wire mux2_size50_49_out;
    wire mux2_size50_50_out;
    wire mux2_size50_51_out;
    wire mux2_size50_52_out;
    wire mux2_size50_53_out;
    wire direct_interc_18_out;
    wire logical_tile_clb_mode_default__fle_8_fle_out;
    wire mux2_size50_54_out;
    wire mux2_size50_55_out;
    wire mux2_size50_56_out;
    wire mux2_size50_57_out;
    wire mux2_size50_58_out;
    wire mux2_size50_59_out;
    wire direct_interc_19_out;
    wire logical_tile_clb_mode_default__fle_9_fle_out;

    logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_0
    (
        .reset(reset),
        .clk(clk),
        .fle_in({mux2_size50_0_out, mux2_size50_1_out, mux2_size50_2_out, mux2_size50_3_out, mux2_size50_4_out, mux2_size50_5_out}),
        .fle_clk(direct_interc_10_out),
        .bl(bl[0:65]),
        .wl(wl[0:65]),
        .fle_out(logical_tile_clb_mode_default__fle_0_fle_out)
    );
    logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_1
    (
        .reset(reset),
        .clk(clk),
        .fle_in({mux2_size50_6_out, mux2_size50_7_out, mux2_size50_8_out, mux2_size50_9_out, mux2_size50_10_out, mux2_size50_11_out}),
        .fle_clk(direct_interc_11_out),
        .bl(bl[66:131]),
        .wl(wl[66:131]),
        .fle_out(logical_tile_clb_mode_default__fle_1_fle_out)
    );
    logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_2
    (
        .reset(reset),
        .clk(clk),
        .fle_in({mux2_size50_12_out, mux2_size50_13_out, mux2_size50_14_out, mux2_size50_15_out, mux2_size50_16_out, mux2_size50_17_out}),
        .fle_clk(direct_interc_12_out),
        .bl(bl[132:197]),
        .wl(wl[132:197]),
        .fle_out(logical_tile_clb_mode_default__fle_2_fle_out)
    );
    logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_3
    (
        .reset(reset),
        .clk(clk),
        .fle_in({mux2_size50_18_out, mux2_size50_19_out, mux2_size50_20_out, mux2_size50_21_out, mux2_size50_22_out, mux2_size50_23_out}),
        .fle_clk(direct_interc_13_out),
        .bl(bl[198:263]),
        .wl(wl[198:263]),
        .fle_out(logical_tile_clb_mode_default__fle_3_fle_out)
    );
    logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_4
    (
        .reset(reset),
        .clk(clk),
        .fle_in({mux2_size50_24_out, mux2_size50_25_out, mux2_size50_26_out, mux2_size50_27_out, mux2_size50_28_out, mux2_size50_29_out}),
        .fle_clk(direct_interc_14_out),
        .bl(bl[264:329]),
        .wl(wl[264:329]),
        .fle_out(logical_tile_clb_mode_default__fle_4_fle_out)
    );
    logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_5
    (
        .reset(reset),
        .clk(clk),
        .fle_in({mux2_size50_30_out, mux2_size50_31_out, mux2_size50_32_out, mux2_size50_33_out, mux2_size50_34_out, mux2_size50_35_out}),
        .fle_clk(direct_interc_15_out),
        .bl(bl[330:395]),
        .wl(wl[330:395]),
        .fle_out(logical_tile_clb_mode_default__fle_5_fle_out)
    );
    logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_6
    (
        .reset(reset),
        .clk(clk),
        .fle_in({mux2_size50_36_out, mux2_size50_37_out, mux2_size50_38_out, mux2_size50_39_out, mux2_size50_40_out, mux2_size50_41_out}),
        .fle_clk(direct_interc_16_out),
        .bl(bl[396:461]),
        .wl(wl[396:461]),
        .fle_out(logical_tile_clb_mode_default__fle_6_fle_out)
    );
    logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_7
    (
        .reset(reset),
        .clk(clk),
        .fle_in({mux2_size50_42_out, mux2_size50_43_out, mux2_size50_44_out, mux2_size50_45_out, mux2_size50_46_out, mux2_size50_47_out}),
        .fle_clk(direct_interc_17_out),
        .bl(bl[462:527]),
        .wl(wl[462:527]),
        .fle_out(logical_tile_clb_mode_default__fle_7_fle_out)
    );
    logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_8
    (
        .reset(reset),
        .clk(clk),
        .fle_in({mux2_size50_48_out, mux2_size50_49_out, mux2_size50_50_out, mux2_size50_51_out, mux2_size50_52_out, mux2_size50_53_out}),
        .fle_clk(direct_interc_18_out),
        .bl(bl[528:593]),
        .wl(wl[528:593]),
        .fle_out(logical_tile_clb_mode_default__fle_8_fle_out)
    );
    logical_tile_clb_mode_default__fle logical_tile_clb_mode_default__fle_9
    (
        .reset(reset),
        .clk(clk),
        .fle_in({mux2_size50_54_out, mux2_size50_55_out, mux2_size50_56_out, mux2_size50_57_out, mux2_size50_58_out, mux2_size50_59_out}),
        .fle_clk(direct_interc_19_out),
        .bl(bl[594:659]),
        .wl(wl[594:659]),
        .fle_out(logical_tile_clb_mode_default__fle_9_fle_out)
    );
    direct_interc direct_interc_0_
    (
        .in(logical_tile_clb_mode_default__fle_0_fle_out),
        .out(clb_O[0])
    );
    direct_interc direct_interc_1_
    (
        .in(logical_tile_clb_mode_default__fle_1_fle_out),
        .out(clb_O[1])
    );
    direct_interc direct_interc_2_
    (
        .in(logical_tile_clb_mode_default__fle_2_fle_out),
        .out(clb_O[2])
    );
    direct_interc direct_interc_3_
    (
        .in(logical_tile_clb_mode_default__fle_3_fle_out),
        .out(clb_O[3])
    );
    direct_interc direct_interc_4_
    (
        .in(logical_tile_clb_mode_default__fle_4_fle_out),
        .out(clb_O[4])
    );
    direct_interc direct_interc_5_
    (
        .in(logical_tile_clb_mode_default__fle_5_fle_out),
        .out(clb_O[5])
    );
    direct_interc direct_interc_6_
    (
        .in(logical_tile_clb_mode_default__fle_6_fle_out),
        .out(clb_O[6])
    );
    direct_interc direct_interc_7_
    (
        .in(logical_tile_clb_mode_default__fle_7_fle_out),
        .out(clb_O[7])
    );
    direct_interc direct_interc_8_
    (
        .in(logical_tile_clb_mode_default__fle_8_fle_out),
        .out(clb_O[8])
    );
    direct_interc direct_interc_9_
    (
        .in(logical_tile_clb_mode_default__fle_9_fle_out),
        .out(clb_O[9])
    );
    direct_interc direct_interc_10_
    (
        .in(clb_clk),
        .out(direct_interc_10_out)
    );
    direct_interc direct_interc_11_
    (
        .in(clb_clk),
        .out(direct_interc_11_out)
    );
    direct_interc direct_interc_12_
    (
        .in(clb_clk),
        .out(direct_interc_12_out)
    );
    direct_interc direct_interc_13_
    (
        .in(clb_clk),
        .out(direct_interc_13_out)
    );
    direct_interc direct_interc_14_
    (
        .in(clb_clk),
        .out(direct_interc_14_out)
    );
    direct_interc direct_interc_15_
    (
        .in(clb_clk),
        .out(direct_interc_15_out)
    );
    direct_interc direct_interc_16_
    (
        .in(clb_clk),
        .out(direct_interc_16_out)
    );
    direct_interc direct_interc_17_
    (
        .in(clb_clk),
        .out(direct_interc_17_out)
    );
    direct_interc direct_interc_18_
    (
        .in(clb_clk),
        .out(direct_interc_18_out)
    );
    direct_interc direct_interc_19_
    (
        .in(clb_clk),
        .out(direct_interc_19_out)
    );
    mux2_size50 mux_fle_0_in_0
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_0_sram),
        .sram_inv(mux2_size50_0_sram_inv),
        .out(mux2_size50_0_out)
    );
    mux2_size50 mux_fle_0_in_1
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_1_sram),
        .sram_inv(mux2_size50_1_sram_inv),
        .out(mux2_size50_1_out)
    );
    mux2_size50 mux_fle_0_in_2
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_2_sram),
        .sram_inv(mux2_size50_2_sram_inv),
        .out(mux2_size50_2_out)
    );
    mux2_size50 mux_fle_0_in_3
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_3_sram),
        .sram_inv(mux2_size50_3_sram_inv),
        .out(mux2_size50_3_out)
    );
    mux2_size50 mux_fle_0_in_4
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_4_sram),
        .sram_inv(mux2_size50_4_sram_inv),
        .out(mux2_size50_4_out)
    );
    mux2_size50 mux_fle_0_in_5
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_5_sram),
        .sram_inv(mux2_size50_5_sram_inv),
        .out(mux2_size50_5_out)
    );
    mux2_size50 mux_fle_1_in_0
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_6_sram),
        .sram_inv(mux2_size50_6_sram_inv),
        .out(mux2_size50_6_out)
    );
    mux2_size50 mux_fle_1_in_1
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_7_sram),
        .sram_inv(mux2_size50_7_sram_inv),
        .out(mux2_size50_7_out)
    );
    mux2_size50 mux_fle_1_in_2
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_8_sram),
        .sram_inv(mux2_size50_8_sram_inv),
        .out(mux2_size50_8_out)
    );
    mux2_size50 mux_fle_1_in_3
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_9_sram),
        .sram_inv(mux2_size50_9_sram_inv),
        .out(mux2_size50_9_out)
    );
    mux2_size50 mux_fle_1_in_4
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_10_sram),
        .sram_inv(mux2_size50_10_sram_inv),
        .out(mux2_size50_10_out)
    );
    mux2_size50 mux_fle_1_in_5
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_11_sram),
        .sram_inv(mux2_size50_11_sram_inv),
        .out(mux2_size50_11_out)
    );
    mux2_size50 mux_fle_2_in_0
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_12_sram),
        .sram_inv(mux2_size50_12_sram_inv),
        .out(mux2_size50_12_out)
    );
    mux2_size50 mux_fle_2_in_1
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_13_sram),
        .sram_inv(mux2_size50_13_sram_inv),
        .out(mux2_size50_13_out)
    );
    mux2_size50 mux_fle_2_in_2
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_14_sram),
        .sram_inv(mux2_size50_14_sram_inv),
        .out(mux2_size50_14_out)
    );
    mux2_size50 mux_fle_2_in_3
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_15_sram),
        .sram_inv(mux2_size50_15_sram_inv),
        .out(mux2_size50_15_out)
    );
    mux2_size50 mux_fle_2_in_4
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_16_sram),
        .sram_inv(mux2_size50_16_sram_inv),
        .out(mux2_size50_16_out)
    );
    mux2_size50 mux_fle_2_in_5
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_17_sram),
        .sram_inv(mux2_size50_17_sram_inv),
        .out(mux2_size50_17_out)
    );
    mux2_size50 mux_fle_3_in_0
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_18_sram),
        .sram_inv(mux2_size50_18_sram_inv),
        .out(mux2_size50_18_out)
    );
    mux2_size50 mux_fle_3_in_1
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_19_sram),
        .sram_inv(mux2_size50_19_sram_inv),
        .out(mux2_size50_19_out)
    );
    mux2_size50 mux_fle_3_in_2
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_20_sram),
        .sram_inv(mux2_size50_20_sram_inv),
        .out(mux2_size50_20_out)
    );
    mux2_size50 mux_fle_3_in_3
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_21_sram),
        .sram_inv(mux2_size50_21_sram_inv),
        .out(mux2_size50_21_out)
    );
    mux2_size50 mux_fle_3_in_4
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_22_sram),
        .sram_inv(mux2_size50_22_sram_inv),
        .out(mux2_size50_22_out)
    );
    mux2_size50 mux_fle_3_in_5
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_23_sram),
        .sram_inv(mux2_size50_23_sram_inv),
        .out(mux2_size50_23_out)
    );
    mux2_size50 mux_fle_4_in_0
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_24_sram),
        .sram_inv(mux2_size50_24_sram_inv),
        .out(mux2_size50_24_out)
    );
    mux2_size50 mux_fle_4_in_1
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_25_sram),
        .sram_inv(mux2_size50_25_sram_inv),
        .out(mux2_size50_25_out)
    );
    mux2_size50 mux_fle_4_in_2
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_26_sram),
        .sram_inv(mux2_size50_26_sram_inv),
        .out(mux2_size50_26_out)
    );
    mux2_size50 mux_fle_4_in_3
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_27_sram),
        .sram_inv(mux2_size50_27_sram_inv),
        .out(mux2_size50_27_out)
    );
    mux2_size50 mux_fle_4_in_4
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_28_sram),
        .sram_inv(mux2_size50_28_sram_inv),
        .out(mux2_size50_28_out)
    );
    mux2_size50 mux_fle_4_in_5
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_29_sram),
        .sram_inv(mux2_size50_29_sram_inv),
        .out(mux2_size50_29_out)
    );
    mux2_size50 mux_fle_5_in_0
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_30_sram),
        .sram_inv(mux2_size50_30_sram_inv),
        .out(mux2_size50_30_out)
    );
    mux2_size50 mux_fle_5_in_1
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_31_sram),
        .sram_inv(mux2_size50_31_sram_inv),
        .out(mux2_size50_31_out)
    );
    mux2_size50 mux_fle_5_in_2
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_32_sram),
        .sram_inv(mux2_size50_32_sram_inv),
        .out(mux2_size50_32_out)
    );
    mux2_size50 mux_fle_5_in_3
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_33_sram),
        .sram_inv(mux2_size50_33_sram_inv),
        .out(mux2_size50_33_out)
    );
    mux2_size50 mux_fle_5_in_4
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_34_sram),
        .sram_inv(mux2_size50_34_sram_inv),
        .out(mux2_size50_34_out)
    );
    mux2_size50 mux_fle_5_in_5
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_35_sram),
        .sram_inv(mux2_size50_35_sram_inv),
        .out(mux2_size50_35_out)
    );
    mux2_size50 mux_fle_6_in_0
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_36_sram),
        .sram_inv(mux2_size50_36_sram_inv),
        .out(mux2_size50_36_out)
    );
    mux2_size50 mux_fle_6_in_1
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_37_sram),
        .sram_inv(mux2_size50_37_sram_inv),
        .out(mux2_size50_37_out)
    );
    mux2_size50 mux_fle_6_in_2
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_38_sram),
        .sram_inv(mux2_size50_38_sram_inv),
        .out(mux2_size50_38_out)
    );
    mux2_size50 mux_fle_6_in_3
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_39_sram),
        .sram_inv(mux2_size50_39_sram_inv),
        .out(mux2_size50_39_out)
    );
    mux2_size50 mux_fle_6_in_4
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_40_sram),
        .sram_inv(mux2_size50_40_sram_inv),
        .out(mux2_size50_40_out)
    );
    mux2_size50 mux_fle_6_in_5
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_41_sram),
        .sram_inv(mux2_size50_41_sram_inv),
        .out(mux2_size50_41_out)
    );
    mux2_size50 mux_fle_7_in_0
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_42_sram),
        .sram_inv(mux2_size50_42_sram_inv),
        .out(mux2_size50_42_out)
    );
    mux2_size50 mux_fle_7_in_1
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_43_sram),
        .sram_inv(mux2_size50_43_sram_inv),
        .out(mux2_size50_43_out)
    );
    mux2_size50 mux_fle_7_in_2
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_44_sram),
        .sram_inv(mux2_size50_44_sram_inv),
        .out(mux2_size50_44_out)
    );
    mux2_size50 mux_fle_7_in_3
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_45_sram),
        .sram_inv(mux2_size50_45_sram_inv),
        .out(mux2_size50_45_out)
    );
    mux2_size50 mux_fle_7_in_4
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_46_sram),
        .sram_inv(mux2_size50_46_sram_inv),
        .out(mux2_size50_46_out)
    );
    mux2_size50 mux_fle_7_in_5
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_47_sram),
        .sram_inv(mux2_size50_47_sram_inv),
        .out(mux2_size50_47_out)
    );
    mux2_size50 mux_fle_8_in_0
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_48_sram),
        .sram_inv(mux2_size50_48_sram_inv),
        .out(mux2_size50_48_out)
    );
    mux2_size50 mux_fle_8_in_1
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_49_sram),
        .sram_inv(mux2_size50_49_sram_inv),
        .out(mux2_size50_49_out)
    );
    mux2_size50 mux_fle_8_in_2
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_50_sram),
        .sram_inv(mux2_size50_50_sram_inv),
        .out(mux2_size50_50_out)
    );
    mux2_size50 mux_fle_8_in_3
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_51_sram),
        .sram_inv(mux2_size50_51_sram_inv),
        .out(mux2_size50_51_out)
    );
    mux2_size50 mux_fle_8_in_4
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_52_sram),
        .sram_inv(mux2_size50_52_sram_inv),
        .out(mux2_size50_52_out)
    );
    mux2_size50 mux_fle_8_in_5
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_53_sram),
        .sram_inv(mux2_size50_53_sram_inv),
        .out(mux2_size50_53_out)
    );
    mux2_size50 mux_fle_9_in_0
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_54_sram),
        .sram_inv(mux2_size50_54_sram_inv),
        .out(mux2_size50_54_out)
    );
    mux2_size50 mux_fle_9_in_1
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_55_sram),
        .sram_inv(mux2_size50_55_sram_inv),
        .out(mux2_size50_55_out)
    );
    mux2_size50 mux_fle_9_in_2
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_56_sram),
        .sram_inv(mux2_size50_56_sram_inv),
        .out(mux2_size50_56_out)
    );
    mux2_size50 mux_fle_9_in_3
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_57_sram),
        .sram_inv(mux2_size50_57_sram_inv),
        .out(mux2_size50_57_out)
    );
    mux2_size50 mux_fle_9_in_4
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_58_sram),
        .sram_inv(mux2_size50_58_sram_inv),
        .out(mux2_size50_58_out)
    );
    mux2_size50 mux_fle_9_in_5
    (
        .in({clb_I[0], clb_I[1], clb_I[2], clb_I[3], clb_I[4], clb_I[5], clb_I[6], clb_I[7], clb_I[8], clb_I[9], clb_I[10], clb_I[11], clb_I[12], clb_I[13], clb_I[14], clb_I[15], clb_I[16], clb_I[17], clb_I[18], clb_I[19], clb_I[20], clb_I[21], clb_I[22], clb_I[23], clb_I[24], clb_I[25], clb_I[26], clb_I[27], clb_I[28], clb_I[29], clb_I[30], clb_I[31], clb_I[32], clb_I[33], clb_I[34], clb_I[35], clb_I[36], clb_I[37], clb_I[38], clb_I[39], logical_tile_clb_mode_default__fle_0_fle_out, logical_tile_clb_mode_default__fle_1_fle_out, logical_tile_clb_mode_default__fle_2_fle_out, logical_tile_clb_mode_default__fle_3_fle_out, logical_tile_clb_mode_default__fle_4_fle_out, logical_tile_clb_mode_default__fle_5_fle_out, logical_tile_clb_mode_default__fle_6_fle_out, logical_tile_clb_mode_default__fle_7_fle_out, logical_tile_clb_mode_default__fle_8_fle_out, logical_tile_clb_mode_default__fle_9_fle_out}),
        .sram(mux2_size50_59_sram),
        .sram_inv(mux2_size50_59_sram_inv),
        .out(mux2_size50_59_out)
    );
    mux2_size50_mem mem_fle_0_in_0
    (
        .bl(bl[660:665]),
        .wl(wl[660:665]),
        .mem_out(mux2_size50_0_sram),
        .mem_outb(mux2_size50_0_sram_inv)
    );
    mux2_size50_mem mem_fle_0_in_1
    (
        .bl(bl[666:671]),
        .wl(wl[666:671]),
        .mem_out(mux2_size50_1_sram),
        .mem_outb(mux2_size50_1_sram_inv)
    );
    mux2_size50_mem mem_fle_0_in_2
    (
        .bl(bl[672:677]),
        .wl(wl[672:677]),
        .mem_out(mux2_size50_2_sram),
        .mem_outb(mux2_size50_2_sram_inv)
    );
    mux2_size50_mem mem_fle_0_in_3
    (
        .bl(bl[678:683]),
        .wl(wl[678:683]),
        .mem_out(mux2_size50_3_sram),
        .mem_outb(mux2_size50_3_sram_inv)
    );
    mux2_size50_mem mem_fle_0_in_4
    (
        .bl(bl[684:689]),
        .wl(wl[684:689]),
        .mem_out(mux2_size50_4_sram),
        .mem_outb(mux2_size50_4_sram_inv)
    );
    mux2_size50_mem mem_fle_0_in_5
    (
        .bl(bl[690:695]),
        .wl(wl[690:695]),
        .mem_out(mux2_size50_5_sram),
        .mem_outb(mux2_size50_5_sram_inv)
    );
    mux2_size50_mem mem_fle_1_in_0
    (
        .bl(bl[696:701]),
        .wl(wl[696:701]),
        .mem_out(mux2_size50_6_sram),
        .mem_outb(mux2_size50_6_sram_inv)
    );
    mux2_size50_mem mem_fle_1_in_1
    (
        .bl(bl[702:707]),
        .wl(wl[702:707]),
        .mem_out(mux2_size50_7_sram),
        .mem_outb(mux2_size50_7_sram_inv)
    );
    mux2_size50_mem mem_fle_1_in_2
    (
        .bl(bl[708:713]),
        .wl(wl[708:713]),
        .mem_out(mux2_size50_8_sram),
        .mem_outb(mux2_size50_8_sram_inv)
    );
    mux2_size50_mem mem_fle_1_in_3
    (
        .bl(bl[714:719]),
        .wl(wl[714:719]),
        .mem_out(mux2_size50_9_sram),
        .mem_outb(mux2_size50_9_sram_inv)
    );
    mux2_size50_mem mem_fle_1_in_4
    (
        .bl(bl[720:725]),
        .wl(wl[720:725]),
        .mem_out(mux2_size50_10_sram),
        .mem_outb(mux2_size50_10_sram_inv)
    );
    mux2_size50_mem mem_fle_1_in_5
    (
        .bl(bl[726:731]),
        .wl(wl[726:731]),
        .mem_out(mux2_size50_11_sram),
        .mem_outb(mux2_size50_11_sram_inv)
    );
    mux2_size50_mem mem_fle_2_in_0
    (
        .bl(bl[732:737]),
        .wl(wl[732:737]),
        .mem_out(mux2_size50_12_sram),
        .mem_outb(mux2_size50_12_sram_inv)
    );
    mux2_size50_mem mem_fle_2_in_1
    (
        .bl(bl[738:743]),
        .wl(wl[738:743]),
        .mem_out(mux2_size50_13_sram),
        .mem_outb(mux2_size50_13_sram_inv)
    );
    mux2_size50_mem mem_fle_2_in_2
    (
        .bl(bl[744:749]),
        .wl(wl[744:749]),
        .mem_out(mux2_size50_14_sram),
        .mem_outb(mux2_size50_14_sram_inv)
    );
    mux2_size50_mem mem_fle_2_in_3
    (
        .bl(bl[750:755]),
        .wl(wl[750:755]),
        .mem_out(mux2_size50_15_sram),
        .mem_outb(mux2_size50_15_sram_inv)
    );
    mux2_size50_mem mem_fle_2_in_4
    (
        .bl(bl[756:761]),
        .wl(wl[756:761]),
        .mem_out(mux2_size50_16_sram),
        .mem_outb(mux2_size50_16_sram_inv)
    );
    mux2_size50_mem mem_fle_2_in_5
    (
        .bl(bl[762:767]),
        .wl(wl[762:767]),
        .mem_out(mux2_size50_17_sram),
        .mem_outb(mux2_size50_17_sram_inv)
    );
    mux2_size50_mem mem_fle_3_in_0
    (
        .bl(bl[768:773]),
        .wl(wl[768:773]),
        .mem_out(mux2_size50_18_sram),
        .mem_outb(mux2_size50_18_sram_inv)
    );
    mux2_size50_mem mem_fle_3_in_1
    (
        .bl(bl[774:779]),
        .wl(wl[774:779]),
        .mem_out(mux2_size50_19_sram),
        .mem_outb(mux2_size50_19_sram_inv)
    );
    mux2_size50_mem mem_fle_3_in_2
    (
        .bl(bl[780:785]),
        .wl(wl[780:785]),
        .mem_out(mux2_size50_20_sram),
        .mem_outb(mux2_size50_20_sram_inv)
    );
    mux2_size50_mem mem_fle_3_in_3
    (
        .bl(bl[786:791]),
        .wl(wl[786:791]),
        .mem_out(mux2_size50_21_sram),
        .mem_outb(mux2_size50_21_sram_inv)
    );
    mux2_size50_mem mem_fle_3_in_4
    (
        .bl(bl[792:797]),
        .wl(wl[792:797]),
        .mem_out(mux2_size50_22_sram),
        .mem_outb(mux2_size50_22_sram_inv)
    );
    mux2_size50_mem mem_fle_3_in_5
    (
        .bl(bl[798:803]),
        .wl(wl[798:803]),
        .mem_out(mux2_size50_23_sram),
        .mem_outb(mux2_size50_23_sram_inv)
    );
    mux2_size50_mem mem_fle_4_in_0
    (
        .bl(bl[804:809]),
        .wl(wl[804:809]),
        .mem_out(mux2_size50_24_sram),
        .mem_outb(mux2_size50_24_sram_inv)
    );
    mux2_size50_mem mem_fle_4_in_1
    (
        .bl(bl[810:815]),
        .wl(wl[810:815]),
        .mem_out(mux2_size50_25_sram),
        .mem_outb(mux2_size50_25_sram_inv)
    );
    mux2_size50_mem mem_fle_4_in_2
    (
        .bl(bl[816:821]),
        .wl(wl[816:821]),
        .mem_out(mux2_size50_26_sram),
        .mem_outb(mux2_size50_26_sram_inv)
    );
    mux2_size50_mem mem_fle_4_in_3
    (
        .bl(bl[822:827]),
        .wl(wl[822:827]),
        .mem_out(mux2_size50_27_sram),
        .mem_outb(mux2_size50_27_sram_inv)
    );
    mux2_size50_mem mem_fle_4_in_4
    (
        .bl(bl[828:833]),
        .wl(wl[828:833]),
        .mem_out(mux2_size50_28_sram),
        .mem_outb(mux2_size50_28_sram_inv)
    );
    mux2_size50_mem mem_fle_4_in_5
    (
        .bl(bl[834:839]),
        .wl(wl[834:839]),
        .mem_out(mux2_size50_29_sram),
        .mem_outb(mux2_size50_29_sram_inv)
    );
    mux2_size50_mem mem_fle_5_in_0
    (
        .bl(bl[840:845]),
        .wl(wl[840:845]),
        .mem_out(mux2_size50_30_sram),
        .mem_outb(mux2_size50_30_sram_inv)
    );
    mux2_size50_mem mem_fle_5_in_1
    (
        .bl(bl[846:851]),
        .wl(wl[846:851]),
        .mem_out(mux2_size50_31_sram),
        .mem_outb(mux2_size50_31_sram_inv)
    );
    mux2_size50_mem mem_fle_5_in_2
    (
        .bl(bl[852:857]),
        .wl(wl[852:857]),
        .mem_out(mux2_size50_32_sram),
        .mem_outb(mux2_size50_32_sram_inv)
    );
    mux2_size50_mem mem_fle_5_in_3
    (
        .bl(bl[858:863]),
        .wl(wl[858:863]),
        .mem_out(mux2_size50_33_sram),
        .mem_outb(mux2_size50_33_sram_inv)
    );
    mux2_size50_mem mem_fle_5_in_4
    (
        .bl(bl[864:869]),
        .wl(wl[864:869]),
        .mem_out(mux2_size50_34_sram),
        .mem_outb(mux2_size50_34_sram_inv)
    );
    mux2_size50_mem mem_fle_5_in_5
    (
        .bl(bl[870:875]),
        .wl(wl[870:875]),
        .mem_out(mux2_size50_35_sram),
        .mem_outb(mux2_size50_35_sram_inv)
    );
    mux2_size50_mem mem_fle_6_in_0
    (
        .bl(bl[876:881]),
        .wl(wl[876:881]),
        .mem_out(mux2_size50_36_sram),
        .mem_outb(mux2_size50_36_sram_inv)
    );
    mux2_size50_mem mem_fle_6_in_1
    (
        .bl(bl[882:887]),
        .wl(wl[882:887]),
        .mem_out(mux2_size50_37_sram),
        .mem_outb(mux2_size50_37_sram_inv)
    );
    mux2_size50_mem mem_fle_6_in_2
    (
        .bl(bl[888:893]),
        .wl(wl[888:893]),
        .mem_out(mux2_size50_38_sram),
        .mem_outb(mux2_size50_38_sram_inv)
    );
    mux2_size50_mem mem_fle_6_in_3
    (
        .bl(bl[894:899]),
        .wl(wl[894:899]),
        .mem_out(mux2_size50_39_sram),
        .mem_outb(mux2_size50_39_sram_inv)
    );
    mux2_size50_mem mem_fle_6_in_4
    (
        .bl(bl[900:905]),
        .wl(wl[900:905]),
        .mem_out(mux2_size50_40_sram),
        .mem_outb(mux2_size50_40_sram_inv)
    );
    mux2_size50_mem mem_fle_6_in_5
    (
        .bl(bl[906:911]),
        .wl(wl[906:911]),
        .mem_out(mux2_size50_41_sram),
        .mem_outb(mux2_size50_41_sram_inv)
    );
    mux2_size50_mem mem_fle_7_in_0
    (
        .bl(bl[912:917]),
        .wl(wl[912:917]),
        .mem_out(mux2_size50_42_sram),
        .mem_outb(mux2_size50_42_sram_inv)
    );
    mux2_size50_mem mem_fle_7_in_1
    (
        .bl(bl[918:923]),
        .wl(wl[918:923]),
        .mem_out(mux2_size50_43_sram),
        .mem_outb(mux2_size50_43_sram_inv)
    );
    mux2_size50_mem mem_fle_7_in_2
    (
        .bl(bl[924:929]),
        .wl(wl[924:929]),
        .mem_out(mux2_size50_44_sram),
        .mem_outb(mux2_size50_44_sram_inv)
    );
    mux2_size50_mem mem_fle_7_in_3
    (
        .bl(bl[930:935]),
        .wl(wl[930:935]),
        .mem_out(mux2_size50_45_sram),
        .mem_outb(mux2_size50_45_sram_inv)
    );
    mux2_size50_mem mem_fle_7_in_4
    (
        .bl(bl[936:941]),
        .wl(wl[936:941]),
        .mem_out(mux2_size50_46_sram),
        .mem_outb(mux2_size50_46_sram_inv)
    );
    mux2_size50_mem mem_fle_7_in_5
    (
        .bl(bl[942:947]),
        .wl(wl[942:947]),
        .mem_out(mux2_size50_47_sram),
        .mem_outb(mux2_size50_47_sram_inv)
    );
    mux2_size50_mem mem_fle_8_in_0
    (
        .bl(bl[948:953]),
        .wl(wl[948:953]),
        .mem_out(mux2_size50_48_sram),
        .mem_outb(mux2_size50_48_sram_inv)
    );
    mux2_size50_mem mem_fle_8_in_1
    (
        .bl(bl[954:959]),
        .wl(wl[954:959]),
        .mem_out(mux2_size50_49_sram),
        .mem_outb(mux2_size50_49_sram_inv)
    );
    mux2_size50_mem mem_fle_8_in_2
    (
        .bl(bl[960:965]),
        .wl(wl[960:965]),
        .mem_out(mux2_size50_50_sram),
        .mem_outb(mux2_size50_50_sram_inv)
    );
    mux2_size50_mem mem_fle_8_in_3
    (
        .bl(bl[966:971]),
        .wl(wl[966:971]),
        .mem_out(mux2_size50_51_sram),
        .mem_outb(mux2_size50_51_sram_inv)
    );
    mux2_size50_mem mem_fle_8_in_4
    (
        .bl(bl[972:977]),
        .wl(wl[972:977]),
        .mem_out(mux2_size50_52_sram),
        .mem_outb(mux2_size50_52_sram_inv)
    );
    mux2_size50_mem mem_fle_8_in_5
    (
        .bl(bl[978:983]),
        .wl(wl[978:983]),
        .mem_out(mux2_size50_53_sram),
        .mem_outb(mux2_size50_53_sram_inv)
    );
    mux2_size50_mem mem_fle_9_in_0
    (
        .bl(bl[984:989]),
        .wl(wl[984:989]),
        .mem_out(mux2_size50_54_sram),
        .mem_outb(mux2_size50_54_sram_inv)
    );
    mux2_size50_mem mem_fle_9_in_1
    (
        .bl(bl[990:995]),
        .wl(wl[990:995]),
        .mem_out(mux2_size50_55_sram),
        .mem_outb(mux2_size50_55_sram_inv)
    );
    mux2_size50_mem mem_fle_9_in_2
    (
        .bl(bl[996:1001]),
        .wl(wl[996:1001]),
        .mem_out(mux2_size50_56_sram),
        .mem_outb(mux2_size50_56_sram_inv)
    );
    mux2_size50_mem mem_fle_9_in_3
    (
        .bl(bl[1002:1007]),
        .wl(wl[1002:1007]),
        .mem_out(mux2_size50_57_sram),
        .mem_outb(mux2_size50_57_sram_inv)
    );
    mux2_size50_mem mem_fle_9_in_4
    (
        .bl(bl[1008:1013]),
        .wl(wl[1008:1013]),
        .mem_out(mux2_size50_58_sram),
        .mem_outb(mux2_size50_58_sram_inv)
    );
    mux2_size50_mem mem_fle_9_in_5
    (
        .bl(bl[1014:1019]),
        .wl(wl[1014:1019]),
        .mem_out(mux2_size50_59_sram),
        .mem_outb(mux2_size50_59_sram_inv)
    );
endmodule

