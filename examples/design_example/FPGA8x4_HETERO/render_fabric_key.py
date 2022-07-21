"""
"""
import logging
from os import environ
import pickle
from glob import glob
from os.path import basename, dirname, realpath, join

import spydrnet as sdn
from spydrnet_physical.util import FabricKeyGenCCFF, FPGAGridGen

logger = logging.getLogger("spydrnet_logs")


LAYOUT = environ.get("LAYOUT", "dp")


class custom_fabric_key(FabricKeyGenCCFF):
    fkey: list = []

    def __init__(self, fpga_grid=None, design_name=None, arch_file=None, layout=None):

        if not fpga_grid:
            self.design_name = design_name
            self.arch_file = arch_file
            self.layout = layout
            fpga_grid = FPGAGridGen(
                design_name="", arch_file=arch_file, release_root="", layout=layout
            )
            fpga_grid.enumerate_grid()
            fpga_grid.render_layout()

        self.fpga_grid = fpga_grid
        self.dwg = fpga_grid.dwg
        self.dwg_shapes = fpga_grid.dwg_shapes
        self.dwg_text = fpga_grid.dwg_text

    # FIXME: Technically we would like to have DP and ultimate as a same same function
    # with minimum arguments (check how we modified reder_fabric.py)

    def create_custom_fabric_key_dp(self):

        fkey1 = []
        self.create_bot2top_connection(2, 0, 1, fkey_name=fkey1)
        self.create_right2left_connection(2, 1, 1, fkey_name=fkey1)

        for ypt in range(2, (self.fpga_grid.get_height() * 4), 2):
            for xpt in [2, 1]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey1 += [(xpt, ypt, inst_name)]
            for xpt in [1, 2]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt + 1)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey1 += [(xpt, ypt + 1, inst_name)]
        for xpt in range(3, (self.fpga_grid.get_width() - 4), 1):
            for ypt in range((self.fpga_grid.get_height() * 2) + 3)[::-1]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey1 += [(xpt, ypt, inst_name)]

        fkey2 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - 4, fkey_name=fkey2
        )

        fkey3 = []
        self.create_bot2top_connection(
            self.fpga_grid.get_width() - 2, 0, 1, fkey_name=fkey3
        )

        # FIXME: Creating small unit fucntions is a good idea but i would suggest
        # dont pass fkey_name argument recturn tuple from function and extend
        # fkey3 in this script

        # FIXME: Also you should think about more generic function instead of creating
        # lefttoight rightoleft ..... functions, we will need many such small functions in future
        self.create_left2right_connection(
            self.fpga_grid.get_width() - 2,
            self.fpga_grid.get_width() - 1,
            self.fpga_grid.get_height() - 3,
            fkey_name=fkey3,
        )

        self.create_left2right_connection(
            self.fpga_grid.get_width() - 2,
            self.fpga_grid.get_width() - 1,
            self.fpga_grid.get_height() + 1,
            fkey_name=fkey3,
        )

        self.create_bot2top_connection(
            self.fpga_grid.get_width() - 2,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2) + 2,
            fkey_name=fkey3,
        )

        self.create_top2bot_connection(
            self.fpga_grid.get_width() - 1,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2),
            fkey_name=fkey3,
        )

        self.create_left2right_connection(
            self.fpga_grid.get_width() - 2,
            self.fpga_grid.get_width() - 1,
            (self.fpga_grid.get_height() * 2) - 1,
            fkey_name=fkey3,
        )

        # self.create_top2bot_connection(self.fpga_grid.get_width()-1, self.fpga_grid.get_height()+3, self.fpga_grid.get_height(), fkey_name=fkey3)

        for xpt in [self.fpga_grid.get_width() - 1]:
            for ypt in range(
                self.fpga_grid.get_height() + 3, self.fpga_grid.get_height() - 1, -1
            ):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                if ypt != self.fpga_grid.get_height() + 1:
                    fkey3 += [(xpt, ypt, inst_name)]

        self.create_left2right_connection(
            self.fpga_grid.get_width() - 2,
            self.fpga_grid.get_width() - 1,
            self.fpga_grid.get_height() - 1,
            fkey_name=fkey3,
        )

        self.create_top2bot_connection(
            self.fpga_grid.get_width() - 1,
            self.fpga_grid.get_height() - 1,
            self.fpga_grid.get_height() - 2,
            fkey_name=fkey3,
        )

        fkey4 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width(), fkey_name=fkey4
        )

        fkey5 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() + 2, fkey_name=fkey5
        )

        fkey6 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() + 4, fkey_name=fkey6
        )

        fkey7 = []
        self.create_bot2top_connection(
            (self.fpga_grid.get_width() * 2) - 2, 0, 1, fkey_name=fkey7
        )

        self.create_left2right_connection(
            (self.fpga_grid.get_width() * 2) - 2,
            (self.fpga_grid.get_width() * 2) - 1,
            self.fpga_grid.get_height() - 3,
            fkey_name=fkey7,
        )

        self.create_left2right_connection(
            (self.fpga_grid.get_width() * 2) - 2,
            (self.fpga_grid.get_width() * 2) - 1,
            self.fpga_grid.get_height() + 1,
            fkey_name=fkey7,
        )

        self.create_bot2top_connection(
            (self.fpga_grid.get_width() * 2) - 2,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2) + 2,
            fkey_name=fkey7,
        )

        self.create_top2bot_connection(
            (self.fpga_grid.get_width() * 2) - 1,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2),
            fkey_name=fkey7,
        )

        self.create_left2right_connection(
            (self.fpga_grid.get_width() * 2) - 2,
            (self.fpga_grid.get_width() * 2) - 1,
            (self.fpga_grid.get_height() * 2) - 1,
            fkey_name=fkey7,
        )

        for xpt in [(self.fpga_grid.get_width() * 2) - 1]:
            for ypt in range(
                self.fpga_grid.get_height() + 3, self.fpga_grid.get_height() - 1, -1
            ):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                if ypt != self.fpga_grid.get_height() + 1:
                    fkey7 += [(xpt, ypt, inst_name)]

        self.create_left2right_connection(
            (self.fpga_grid.get_width() * 2) - 2,
            (self.fpga_grid.get_width() * 2) - 1,
            self.fpga_grid.get_height() - 1,
            fkey_name=fkey7,
        )

        self.create_top2bot_connection(
            (self.fpga_grid.get_width() * 2) - 1,
            self.fpga_grid.get_height() - 1,
            self.fpga_grid.get_height() - 2,
            fkey_name=fkey7,
        )

        fkey8 = []
        for xpt in range(
            (self.fpga_grid.get_width() * 2), (self.fpga_grid.get_width() * 2) + 2, 1
        ):
            if xpt == (self.fpga_grid.get_width() * 2):
                for ypt in range((self.fpga_grid.get_height() * 2) + 3):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    fkey8 += [(xpt, ypt, inst_name)]

            for ypt in [(self.fpga_grid.get_height() * 2) + 1]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt + 1, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey8 += [(xpt + 1, ypt, inst_name)]

        self.create_left2right_connection(
            (self.fpga_grid.get_width() * 2) + 1,
            (self.fpga_grid.get_width() * 2) + 2,
            self.fpga_grid.get_height() * 2,
            fkey_name=fkey8,
        )

        self.create_top2bot_connection(
            (self.fpga_grid.get_width() * 2) + 1,
            (self.fpga_grid.get_height() + 3),
            self.fpga_grid.get_height() + 2,
            fkey_name=fkey8,
        )

        self.create_left2right_connection(
            (self.fpga_grid.get_width() * 2) + 1,
            (self.fpga_grid.get_width() * 2) + 2,
            (self.fpga_grid.get_height() * 2) - 2,
            fkey_name=fkey8,
        )

        self.create_top2bot_connection(
            (self.fpga_grid.get_width() * 2) + 1,
            (self.fpga_grid.get_height() + 1),
            self.fpga_grid.get_height(),
            fkey_name=fkey8,
        )

        self.create_left2right_connection(
            (self.fpga_grid.get_width() * 2) + 1,
            (self.fpga_grid.get_width() * 2) + 2,
            self.fpga_grid.get_height(),
            fkey_name=fkey8,
        )

        self.create_top2bot_connection(
            (self.fpga_grid.get_width() * 2) + 1,
            (self.fpga_grid.get_height() - 1),
            self.fpga_grid.get_height() - 2,
            fkey_name=fkey8,
        )

        self.create_left2right_connection(
            (self.fpga_grid.get_width() * 2) + 1,
            (self.fpga_grid.get_width() * 2) + 2,
            self.fpga_grid.get_height() - 2,
            fkey_name=fkey8,
        )

        self.create_diagonal_connection(
            (self.fpga_grid.get_width() * 2) + 2,
            (self.fpga_grid.get_width() * 2) + 1,
            self.fpga_grid.get_height() - 3,
            self.fpga_grid.get_height() - 2,
            fkey_name=fkey8,
        )

        self.fkey.append(fkey1)
        self.fkey.append(fkey2)
        self.fkey.append(fkey3)
        self.fkey.append(fkey4)
        self.fkey.append(fkey5)
        self.fkey.append(fkey6)
        self.fkey.append(fkey7)
        self.fkey.append(fkey8)
        return self.fkey

    def create_custom_fabric_key_ultimate(self):
        fkey1 = []
        self.create_bot2top_connection(2, 0, 1, fkey_name=fkey1)
        self.create_right2left_connection(2, 1, 1, fkey_name=fkey1)

        for ypt in range(2, (self.fpga_grid.get_height() * 4), 2):
            for xpt in [2, 1]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey1 += [(xpt, ypt, inst_name)]
            for xpt in [1, 2]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt + 1)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey1 += [(xpt, ypt + 1, inst_name)]
        for xpt in range(
            3, (self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 4)), 1
        ):
            for ypt in range((self.fpga_grid.get_height() * 2) + 3)[::-1]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey1 += [(xpt, ypt, inst_name)]

        fkey2 = []
        self.create_sel_serpentine_connection(
            (self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 4)),
            fkey_name=fkey2,
        )

        fkey3 = []
        self.create_bot2top_connection(
            self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 6),
            0,
            1,
            fkey_name=fkey3,
        )

        for y in range(1, (self.fpga_grid.get_height() * 2) - 2, 4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 6),
                self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 7),
                y,
                fkey_name=fkey3,
            )

        self.create_bot2top_connection(
            self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 6),
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2) + 2,
            fkey_name=fkey3,
        )

        self.create_top2bot_connection(
            self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 7),
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2),
            fkey_name=fkey3,
        )

        for y in range((self.fpga_grid.get_height() * 2) - 1, 1, -4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 6),
                self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 7),
                y,
                fkey_name=fkey3,
            )

            for xpt in [self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 7)]:
                for ypt in range(y, y - 4, -1):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    if ypt != y - 2:
                        fkey3 += [(xpt, ypt, inst_name)]

        fkey4 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 8),
            fkey_name=fkey4,
        )

        fkey5 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 10),
            fkey_name=fkey5,
        )

        fkey6 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - (self.fpga_grid.get_width() - 12),
            fkey_name=fkey6,
        )

        fkey7 = []
        self.create_bot2top_connection(
            self.fpga_grid.get_width() - (self.fpga_grid.get_width() / 2) - 2,
            0,
            1,
            fkey_name=fkey7,
        )

        for y in range(1, (self.fpga_grid.get_height() * 2) - 2, 4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() - int(self.fpga_grid.get_width() / 2) - 2,
                self.fpga_grid.get_width() - int(self.fpga_grid.get_width() / 2) - 1,
                y,
                fkey_name=fkey7,
            )

        self.create_bot2top_connection(
            self.fpga_grid.get_width() - int(self.fpga_grid.get_width() / 2) - 2,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2) + 2,
            fkey_name=fkey7,
        )

        self.create_top2bot_connection(
            self.fpga_grid.get_width() - int(self.fpga_grid.get_width() / 2) - 1,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2),
            fkey_name=fkey7,
        )

        for y in range((self.fpga_grid.get_height() * 2) - 1, 1, -4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() - int(self.fpga_grid.get_width() / 2) - 2,
                self.fpga_grid.get_width() - int(self.fpga_grid.get_width() / 2) - 1,
                y,
                fkey_name=fkey7,
            )

            for xpt in [
                self.fpga_grid.get_width() - int(self.fpga_grid.get_width() / 2) - 1
            ]:
                for ypt in range(y, y - 4, -1):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    if ypt != y - 2:
                        fkey7 += [(xpt, ypt, inst_name)]

        fkey8 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - (self.fpga_grid.get_width() / 2),
            fkey_name=fkey8,
        )

        fkey9 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - ((self.fpga_grid.get_width() / 2) - 2),
            fkey_name=fkey9,
        )

        fkey10 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - ((self.fpga_grid.get_width() / 2) - 4),
            fkey_name=fkey10,
        )

        fkey11 = []
        self.create_bot2top_connection(
            self.fpga_grid.get_width() - 10, 0, 1, fkey_name=fkey11
        )

        for y in range(1, (self.fpga_grid.get_height() * 2) - 2, 4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() - 10,
                self.fpga_grid.get_width() - 9,
                y,
                fkey_name=fkey11,
            )

        self.create_bot2top_connection(
            self.fpga_grid.get_width() - 10,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2) + 2,
            fkey_name=fkey11,
        )

        self.create_top2bot_connection(
            self.fpga_grid.get_width() - 9,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2),
            fkey_name=fkey11,
        )

        for y in range((self.fpga_grid.get_height() * 2) - 1, 1, -4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() - 10,
                self.fpga_grid.get_width() - 9,
                y,
                fkey_name=fkey11,
            )

            for xpt in [self.fpga_grid.get_width() - 9]:
                for ypt in range(y, y - 4, -1):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    if ypt != y - 2:
                        fkey11 += [(xpt, ypt, inst_name)]

        fkey12 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - 8, fkey_name=fkey12
        )

        fkey13 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - 6, fkey_name=fkey13
        )

        fkey14 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - 4, fkey_name=fkey14
        )

        fkey15 = []
        self.create_bot2top_connection(
            self.fpga_grid.get_width() - 2, 0, 1, fkey_name=fkey15
        )

        for y in range(1, (self.fpga_grid.get_height() * 2) - 2, 4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() - 2,
                self.fpga_grid.get_width() - 1,
                y,
                fkey_name=fkey15,
            )

        self.create_bot2top_connection(
            self.fpga_grid.get_width() - 2,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2) + 2,
            fkey_name=fkey15,
        )

        self.create_top2bot_connection(
            self.fpga_grid.get_width() - 1,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2),
            fkey_name=fkey15,
        )

        for y in range((self.fpga_grid.get_height() * 2) - 1, 1, -4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() - 2,
                self.fpga_grid.get_width() - 1,
                y,
                fkey_name=fkey15,
            )

            for xpt in [self.fpga_grid.get_width() - 1]:
                for ypt in range(y, y - 4, -1):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    if ypt != y - 2:
                        fkey15 += [(xpt, ypt, inst_name)]

        fkey16 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() - 4, fkey_name=fkey16
        )

        fkey17 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width(), fkey_name=fkey17
        )

        fkey18 = []
        self.create_bot2top_connection(
            self.fpga_grid.get_width() + 4, 0, 1, fkey_name=fkey18
        )

        for y in range(1, (self.fpga_grid.get_height() * 2) - 2, 4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() + 4,
                self.fpga_grid.get_width() + 5,
                y,
                fkey_name=fkey18,
            )

        self.create_bot2top_connection(
            self.fpga_grid.get_width() + 4,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2) + 2,
            fkey_name=fkey18,
        )

        self.create_top2bot_connection(
            self.fpga_grid.get_width() + 5,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2),
            fkey_name=fkey18,
        )

        for y in range((self.fpga_grid.get_height() * 2) - 1, 1, -4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() + 4,
                self.fpga_grid.get_width() + 5,
                y,
                fkey_name=fkey18,
            )

            for xpt in [self.fpga_grid.get_width() + 5]:
                for ypt in range(y, y - 4, -1):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    if ypt != y - 2:
                        fkey18 += [(xpt, ypt, inst_name)]

        fkey19 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() + 2, fkey_name=fkey19
        )

        fkey20 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() + 6, fkey_name=fkey20
        )

        fkey21 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() + 8, fkey_name=fkey21
        )

        fkey22 = []
        self.create_bot2top_connection(
            self.fpga_grid.get_width() + 12, 0, 1, fkey_name=fkey22
        )

        for y in range(1, (self.fpga_grid.get_height() * 2) - 2, 4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() + 12,
                self.fpga_grid.get_width() + 13,
                y,
                fkey_name=fkey22,
            )

        self.create_bot2top_connection(
            self.fpga_grid.get_width() + 12,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2) + 2,
            fkey_name=fkey22,
        )

        self.create_top2bot_connection(
            self.fpga_grid.get_width() + 13,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2),
            fkey_name=fkey22,
        )

        for y in range((self.fpga_grid.get_height() * 2) - 1, 1, -4):
            self.create_left2right_connection(
                self.fpga_grid.get_width() + 12,
                self.fpga_grid.get_width() + 13,
                y,
                fkey_name=fkey22,
            )

            for xpt in [self.fpga_grid.get_width() + 13]:
                for ypt in range(y, y - 4, -1):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    if ypt != y - 2:
                        fkey22 += [(xpt, ypt, inst_name)]

        fkey23 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() + 10, fkey_name=fkey23
        )

        fkey24 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() + (self.fpga_grid.get_width() / 2) - 2,
            fkey_name=fkey24,
        )

        fkey25 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() + (self.fpga_grid.get_width() / 2),
            fkey_name=fkey25,
        )

        fkey26 = []
        self.create_bot2top_connection(
            (self.fpga_grid.get_width() * 2) - 12, 0, 1, fkey_name=fkey26
        )

        for y in range(1, (self.fpga_grid.get_height() * 2) - 2, 4):
            self.create_left2right_connection(
                (self.fpga_grid.get_width() * 2) - 12,
                (self.fpga_grid.get_width() * 2) - 11,
                y,
                fkey_name=fkey26,
            )

        self.create_bot2top_connection(
            (self.fpga_grid.get_width() * 2) - 12,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2) + 2,
            fkey_name=fkey26,
        )

        self.create_top2bot_connection(
            (self.fpga_grid.get_width() * 2) - 11,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2),
            fkey_name=fkey26,
        )

        for y in range((self.fpga_grid.get_height() * 2) - 1, 1, -4):
            self.create_left2right_connection(
                (self.fpga_grid.get_width() * 2) - 12,
                (self.fpga_grid.get_width() * 2) - 11,
                y,
                fkey_name=fkey26,
            )

            for xpt in [(self.fpga_grid.get_width() * 2) - 11]:
                for ypt in range(y, y - 4, -1):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    if ypt != y - 2:
                        fkey26 += [(xpt, ypt, inst_name)]

        fkey27 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() + (self.fpga_grid.get_width() / 2) + 2,
            fkey_name=fkey27,
        )

        fkey28 = []
        self.create_sel_serpentine_connection(
            self.fpga_grid.get_width() + (self.fpga_grid.get_width() / 2) + 6,
            fkey_name=fkey28,
        )

        fkey29 = []
        self.create_sel_serpentine_connection(
            (self.fpga_grid.get_width() * 2) - 8, fkey_name=fkey29
        )

        fkey30 = []
        self.create_bot2top_connection(
            (self.fpga_grid.get_width() * 2) - 4, 0, 1, fkey_name=fkey30
        )

        for y in range(1, (self.fpga_grid.get_height() * 2) - 2, 4):
            self.create_left2right_connection(
                (self.fpga_grid.get_width() * 2) - 4,
                (self.fpga_grid.get_width() * 2) - 3,
                y,
                fkey_name=fkey30,
            )

        self.create_bot2top_connection(
            (self.fpga_grid.get_width() * 2) - 4,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2) + 2,
            fkey_name=fkey30,
        )

        self.create_top2bot_connection(
            (self.fpga_grid.get_width() * 2) - 3,
            (self.fpga_grid.get_height() * 2) + 1,
            (self.fpga_grid.get_height() * 2),
            fkey_name=fkey30,
        )

        for y in range((self.fpga_grid.get_height() * 2) - 1, 1, -4):
            self.create_left2right_connection(
                (self.fpga_grid.get_width() * 2) - 4,
                (self.fpga_grid.get_width() * 2) - 3,
                y,
                fkey_name=fkey30,
            )

            for xpt in [(self.fpga_grid.get_width() * 2) - 3]:
                for ypt in range(y, y - 4, -1):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    if ypt != y - 2:
                        fkey30 += [(xpt, ypt, inst_name)]

        fkey31 = []
        self.create_sel_serpentine_connection(
            (self.fpga_grid.get_width() * 2) - 6, fkey_name=fkey31
        )

        fkey32 = []
        self.create_sel_serpentine_connection(
            (self.fpga_grid.get_width() * 2) - 2, fkey_name=fkey32
        )

        fkey33 = []
        for xpt in range(
            (self.fpga_grid.get_width() * 2), (self.fpga_grid.get_width() * 2) + 2, 1
        ):
            if xpt == (self.fpga_grid.get_width() * 2):
                for ypt in range((self.fpga_grid.get_height() * 2) + 3):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    fkey33 += [(xpt, ypt, inst_name)]

            for ypt in [(self.fpga_grid.get_height() * 2) + 1]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt + 1, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey33 += [(xpt + 1, ypt, inst_name)]

        for y in range((self.fpga_grid.get_height() * 2), 1, -2):

            self.create_left2right_connection(
                (self.fpga_grid.get_width() * 2) + 1,
                (self.fpga_grid.get_width() * 2) + 2,
                y,
                fkey_name=fkey33,
            )

            self.create_top2bot_connection(
                (self.fpga_grid.get_width() * 2) + 1, y - 1, y - 2, fkey_name=fkey33
            )

        # FIXME: This is not scalable at all you need to find better ways to do
        # such fabric key generation
        fkey_list = [
            fkey1,
            fkey2,
            fkey3,
            fkey4,
            fkey5,
            fkey6,
            fkey7,
            fkey8,
            fkey9,
            fkey10,
            fkey11,
            fkey12,
            fkey13,
            fkey14,
            fkey15,
            fkey16,
            fkey17,
            fkey18,
            fkey19,
            fkey20,
            fkey21,
            fkey22,
            fkey23,
            fkey24,
            fkey25,
            fkey26,
            fkey27,
            fkey28,
            fkey29,
            fkey30,
            fkey31,
            fkey32,
            fkey33,
        ]

        for key in fkey_list:
            self.fkey.append(key)
        return self.fkey

    # FIXME: I moved this functions from fabric_key_ccff, lets tray to generalise
    # them before adding into fabric_key_ccff
    def create_sel_serpentine_connection(self, x, fkey_name):
        for xpt in [x]:
            for ypt in range((self.fpga_grid.get_height() * 2) + 3):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey_name += [(xpt, ypt, inst_name)]
            for ypt in range((self.fpga_grid.get_height() * 2) + 3)[::-1]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt + 1, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey_name += [(xpt + 1, ypt, inst_name)]

    def create_bot2top_connection(self, x, y1, y2, fkey_name):
        for xpt in [x]:
            for ypt in range(y1, y2 + 1, 1):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey_name += [(xpt, ypt, inst_name)]

    def create_top2bot_connection(self, x, y1, y2, fkey_name):
        for xpt in [x]:
            for ypt in range(y1, y2 - 1, -1):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey_name += [(xpt, ypt, inst_name)]

    def create_left2right_connection(self, x1, x2, y, fkey_name):
        for ypt in [y]:
            for xpt in range(x1, x2 + 1, 1):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey_name += [(xpt, ypt, inst_name)]

    def create_right2left_connection(self, x1, x2, y, fkey_name):
        for ypt in [y]:
            for xpt in range(x1, x2 - 1, -1):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey_name += [(xpt, ypt, inst_name)]

    def create_diagonal_connection(self, x1, x2, y1, y2, fkey_name):

        for ypt in [y1, y2]:
            for xpt in [x1, x2]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                if (x1 and y1) or (x2 and y2):
                    fkey_name += [(xpt, ypt, inst_name)]


def main():
    """
    Main method to execute function
    """
    # Parse architecture file and get layput block
    try:
        VPR_ARCH_FILE = glob(("task/arch/*vpr*"))[0]
        PROJ_NAME = basename(dirname(realpath(__file__)))
    except IndexError:
        logger.exception("Architecture file not found ['task/arch/*vpr*']")

    # Load the existing grid from generate shapes
    fpga = pickle.load(open(f"{PROJ_NAME}_{LAYOUT}_fpgagridgen.pickle", "rb"))

    # Uncomment this to recreate the FPGA grid
    # Note: it will remove all the physical planning from image
    # fpga.enumerate_grid()
    # fpga.render_layout(grid_io=True)

    fabric_key = custom_fabric_key(fpga)
    if LAYOUT == "ultimate":
        fabric_key.create_custom_fabric_key_ultimate()
    else:
        fabric_key.create_custom_fabric_key_dp()

    filename = join(f"{PROJ_NAME}_{LAYOUT}_CCFF_Chain.svg")
    fabric_key.render_svg(filename=filename)
    fabric_key.save_fabric_key(filename="fabric_key.xml")


if __name__ == "__main__":
    main()
