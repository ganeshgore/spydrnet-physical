.. _openfpga_physical_directory_structure:

OpenFPGA Physical- Directory Structure
======================================



Creating Tapeout Project
^^^^^^^^^^^^^^^^^^^^^^^^

The hierarchical flow of the OpenFPGA-Physical recommends incrementally building the large FPGA fabric. In that methodology, the larger fabric such as a 100x100 FPGA design can be derived from a smaller replica 4x4. The OpenFPGA-Tapeout directory is designed to support such a design hierarchy

.. rst-class:: ascii

::

   OpenFPGA-Physical-Tapeout-Template
   ├ <project_1_directory>
   ├ <project_2_directory>
   |   ├ CommonFiles
   |   |   ├ config.sh
   |   |   ├ common_task/
   |   |   |   ├ arch/
   |   |   |   ├ config/
   |   |   |   ├ custom_modules/
   |   |   |   ├ IPs/
   |   |   |   ├ micro_benchmark/
   |   |   |   └ sc_verilog/
   |   |   ├ icc2_custom_project_dp_scripts/
   |   |   └ icc2_custom_project_pnr_scripts/
   |   ├ FPGA4x4_k4n8_design_pnr
   |   |   ├ config.sh
   |   |   ├ FPGA4x4_k4n8_design_task/
   |   |   ├ FPGA4x4_k4n8_design_verilog/
   |   |   ├ dp
   |   |   |   └ fpga_top
   |   |   |       ├ dp_setup/
   |   |   |       ├ icc2_dp_scripts/
   |   |   |       ├ icc2_custom_dp_scripts/
   |   |   |       ├ icc2_custom_project_dp_scripts/
   |   |   |       └ Makefile
   |   |   ├ pnr
   |   |   |   ├ <tile1_name>
   |   |   |   └ <tile2_name>
   |   |   |       ├ pnr_setup/
   |   |   |       ├ icc2_pnr_scripts/
   |   |   |       ├ icc2_custom_pnr_scripts/
   |   |   |       ├ icc2_custom_project_pnr_scripts/
   |   |   |       └ Makefile
   |   |   ├ release
   |   |   |   ├ ConnectNets
   |   |   |   ├ rpts
   |   |   |   ├ SVG
   |   |   |   ├ TCL
   |   |   |   ├ dp
   |   |   |   ├ pnr
   |   |   └ Makefile
   |   └ FPGA16x16_k4n8_design_pnr
   |       └ ....
   └ OpenFPGAPhysicalDesign-ICC2
      ├ LoadTools.sh
      ├ dp
      |   └ fpga_top
      |       ├ dp_setup/
      |       ├ icc2_dp_scripts/
      |       ├ icc2_custom_dp_scripts/
      ├ pnr
      |   ├ pnr_setup/
      |   ├ icc2_pnr_scripts/
      |   └ icc2_custom_pnr_scripts/
      ├ Makefile
      └ scripts


+-----------------+------------------------------------+---------------------------------------------------------+
| Module          |               Scripts              |                       Remark                            |
| Place and Route |                                    |                                                         |
+=================+====================================+=========================================================+
|                 | SH_PRE_INIT_DESIGN                 | Sourced before launching init_design icc2_shell         |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_TAP_CELL_ADDITION         | Module level tap cell addition                          |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_PG_CREATION_FILE          | Power grid connections                                  |
|                 +------------------------------------+---------------------------------------------------------+
|   init design   | TCL_USER_INIT_DESIGN_POST_SCRIPT   | Physical hierarchical restructuring if required         |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_SET_SDC                   | This script set the explicit SDCs for the module        |
|                 +------------------------------------+---------------------------------------------------------+
|                 | SH_POST_INIT_DESIGN                | Sourced after finishing init_design phase in icc2_shell |
+-----------------+------------------------------------+---------------------------------------------------------+
|                 | SH_PRE_PLACE_OPT                   | Sourced before launching place_opt phase in icc2_shell  |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_LIB_CELL_PURPOSE_FILE          | Setting cell purpose for the library cells              |
|                 +------------------------------------+---------------------------------------------------------+
|    place_out    | TCL_USER_PLACE_OPT_PRE_SCRIPT      | Sourced before running detailed placement               |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_PLACE_OPT_SCRIPT          | Overwrites the existing placement flow                  |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_PLACE_OPT_POST_SCRIPT     | Sourced after running detailed placement                |
|                 +------------------------------------+---------------------------------------------------------+
|                 | SH_POST_PLACE_OPT                  | Sourced after launching place_opt phase in icc2_shell   |
+-----------------+------------------------------------+---------------------------------------------------------+
|                 | SH_PRE_CLOCK_OPT_SCRIPT            | Sourced before running clock synthesis                  |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_CLOCK_OPT_CTS_PRE_SCRIPT  | Sourced before running clock synthesis                  |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_CLOCK_OPT_CTS_SCRIPT      | Overwrite the clock synthesis    run                    |
|    clock_opt    +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_CLOCK_OPT_CTS_POST_SCRIPT | Sourced after running clock synthesis                   |
|                 +------------------------------------+---------------------------------------------------------+
|                 | SH_POST_CLOCK_OPT_SCRIPT           | Sourced after clock synthesis                           |
+-----------------+------------------------------------+---------------------------------------------------------+
|                 | SH_PRE_CLOCK_OPT_SCRIPT            | Sourced before running clock optimization               |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_CLOCK_OPT_CTS_PRE_SCRIPT  | Sourced before running clock optimization               |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_CLOCK_OPT_CTS_SCRIPT      | Overwrite the clock optimization run                    |
| clock_opt_opto  +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_CLOCK_OPT_CTS_POST_SCRIPT | Sourced after running clock optimization                |
|                 +------------------------------------+---------------------------------------------------------+
|                 | SH_POST_CLOCK_OPT_SCRIPT           | Sourced after clock optimization                        |
+-----------------+------------------------------------+---------------------------------------------------------+
|                 | SH_PRE_ROUTE_AUTO_SCRIPT           | Sourced before running detailed routing                 |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_ROUTE_AUTO_PRE_SCRIPT     | Sourced before running detailed routing                 |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_ROUTE_AUTO_SCRIPT         | Overwrite the detailed routing run                      |
|    route_auto   +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_ROUTE_AUTO_POST_SCRIPT    | Sourced after running detailed routing                  |
|                 +------------------------------------+---------------------------------------------------------+
|                 | SH_POST_ROUTE_AUTO_SCRIPT          | Sourced after detailed routing                          |
+-----------------+------------------------------------+---------------------------------------------------------+
|                 | SH_PRE_ROUTE_OPT_SCRIPT            | Sourced before running route optimization               |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_ROUTE_OPT_PRE_SCRIPT      | Sourced before running route optimization               |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_ROUTE_OPT_SCRIPT          | Overwrite the route optimization run                    |
|   route_opt     +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_ROUTE_OPT_POST_SCRIPT     | Sourced after running route optimization                |
|                 +------------------------------------+---------------------------------------------------------+
|                 | SH_POST_ROUTE_OPT_SCRIPT           | Sourced after route optimization                        |
+-----------------+------------------------------------+---------------------------------------------------------+
|                 | SH_PRE_ROUTE_OPT_SCRIPT            | Sourced before running route optimization               |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_CHIP_FINISH_PRE_SCRIPT    | Sourced before running route optimization               |
|   chip_finish   +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_CHIP_FINISH_POST_SCRIPT   | Sourced after running route optimization                |
|                 +------------------------------------+---------------------------------------------------------+
|                 | SH_POST_ROUTE_OPT_SCRIPT           | Sourced after route optimization                        |
+-----------------+------------------------------------+---------------------------------------------------------+
|                 | SH_PRE_ICV_IN_DESIGN_SCRIPT        | Sourced before running route optimization               |
|                 +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_ICV_IN_DESIGN_PRE_SCRIPT  | Sourced before running route optimization               |
|  icv_in_design  +------------------------------------+---------------------------------------------------------+
|                 | TCL_USER_ICV_IN_DESIGN_POST_SCRIPT | Sourced after running route optimization                |
|                 +------------------------------------+---------------------------------------------------------+
|                 | SH_POST_ICV_IN_DESIGN_SCRIPT       | Sourced after route optimization                        |
+-----------------+------------------------------------+---------------------------------------------------------+

