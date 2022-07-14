"""
This script renders the FPGA architecure before restructuring
"""
import logging
import pickle
from glob import glob
from os.path import basename, dirname, realpath
import spydrnet as sdn
from spydrnet_physical.util import FPGAGridGen

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")


def main():
    """
    Architecture render method
    """
    try:
        VPR_ARCH_FILE = glob(("/home/users/saad.khalil/Documents/RS/spydrnet-physical_des_exam/examples/design_example/FPGA8x4_HETERO/task/arch/vpr_arch.xml"))[0]
        PROJ_NAME = basename(dirname(realpath(__file__)))
    except IndexError:
        logger.exception("Architecture file not found ['task/arch/*vpr*']")
    fpga = FPGAGridGen(
        design_name=PROJ_NAME,
        arch_file=VPR_ARCH_FILE,
        release_root="_release",
        layout="dp",
    )
    fpga.enumerate_grid()

    # This is dummy remove this in future
    #fpga.default_parameters["cbx"][0] = 10  # uncomment to force square plan
    #fpga.default_parameters["cby"][1] = 10  # uncomment to force square plan

    dwg = fpga.render_layout(
        filename=f"_{PROJ_NAME}_render.svg", grid_io=True, markers=True
    )
    dwg.save(pretty=True, indent=4)
    pickle.dump(dwg, open(f"{PROJ_NAME}_render.pickle", "wb"))
    logger.info("Saving file %s_render.svg ", PROJ_NAME)

    # ============ Modify your floorplan here ============
    # Adding stylesheet
    fpga.add_style("symbol[id*='ram9k'] * { fill:#599fff; opacity:0.5 }")
    fpga.add_style("symbol[id*='dsp'] * { fill:#a8dd00; opacity:0.5 }")
    fpga.add_style("symbol[id*='merged_interface'] * { fill:#ceefe4; opacity:0.5 }")
    fpga.add_style("symbol[id*='merged_interface'] * { fill:red; opacity:0.5 }")
    fpga.add_style("symbol[id*='sides_merged'] * { fill:green; opacity:0.5 }")
    fpga.add_style("symbol[id*='corner'] * { fill:grey; opacity:0.5 }")

    # Extract width and height
    w = fpga.get_width()
    h = fpga.get_height()

    for x in [3, 7]:
        for y in range(1, 4 + 2, 2):
            hetero = "dsp" if x in (7,) else "ram9k"
            if y < 4:
                fpga.merge_symbol(
                    [
                        f"{hetero}_{x}__{y}_",
                        f"sb_{x-1}__{y}_",
                        f"sb_{x}__{y}_",
                        f"cby_{x-1}__{y}_",
                        f"cby_{x}__{y}_",
                        f"cby_{x-1}__{y+1}_",
                        f"cby_{x}__{y+1}_",
                    ],
                    f"merged_{hetero}_block_at_{x}_{y}",
                )

            fpga.merge_symbol(
                [f"cbx_{x}__{y-1}_", f"sb_{x-1}__{y-1}_", f"sb_{x}__{y-1}_"],
                f"merged_interface_cb_{x}_{y}",
            )

    for y in range(1, h):
        for x in [0, w]:
            instances = [f"cby_{x}__{y}_", f"sb_{x}__{y}_"]
            fpga.merge_symbol(instances, f"sides_merged_at_{x}_{y}")

    # Corner Tiles
    fpga.merge_symbol([f"cby_0__{h}_", f"sb_0__{h}_"], f"corner_ltop")
    fpga.merge_symbol([f"cby_{w}__{h}_", f"sb_{w}__{h}_"], f"corner_rtop")
    # ====================== END =========================

    dwg.saveas(filename=f"{PROJ_NAME}_restruct_render.svg", pretty=True, indent=4)
    pickle.dump(dwg, open(f"{PROJ_NAME}_restruct_render.pickle", "wb"))
    pickle.dump(fpga, open(f"{PROJ_NAME}_fpgagridgen.pickle", "wb"))
    logger.info("Saving file %s_restruct_render.svg", PROJ_NAME)


if __name__ == "__main__":
    main()
