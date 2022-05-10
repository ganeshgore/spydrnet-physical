
SHELL = bash
PYTHON_EXEC ?= python3.8
OPTIONS =
OPENFPGA_PATH ?=

.SILENT:
.ONESHELL:

runOpenFPGA:
	SECONDS=0
	source $${OPENFPGA_PATH}/openfpga.sh
	run-task FPGA44_Task --remove_run_dir all
	run-task FPGA44_Task
	rm -rf FPGA44_Verilog && mkdir FPGA44_Verilog
	rm -rf FPGA44_gsb && mkdir FPGA44_gsb
	cp -R FPGA44_Task/latest/k6_N10_tileable/top/MIN_ROUTE_CHAN_WIDTH/FPGA44_Verilog .
	cp -R FPGA44_Task/CustomModules/ FPGA44_Verilog/
	cp -R FPGA44_Task/latest/k6_N10_tileable/top/MIN_ROUTE_CHAN_WIDTH/FPGA44_gsb/ .
	for file in FPGA44_gsb/*.xml; do mv "$$file" "$${file/sb_/_sb_}"; done
	find ./FPGA44_Verilog -name "*.v" -exec sed -i "s/.*default_nettype/\/\/ \`default_nettype/g" '{}' \;
	find ./FPGA44_Verilog -type f -name "*.v" -print0 | xargs -0  sed -i "/^\/\/.*Date.*/d"
	find ./FPGA44_Verilog -type f -name "*.v" -print0 | xargs -0  sed -i "/^\/\/.*Author.*/d"
	clean_gsb --top_level_design FPGA44_Verilog/fpga_top.v --gsb_dir FPGA44_gsb/
	find ./FPGA44_gsb -name "*.xml" -type f -exec xmllint --output '{}' --format '{}' \;
	duration=$$SECONDS
	echo "$$(($$duration / 60)) minutes and $$(($$duration % 60)) seconds elapsed." >> runOpenFPGA

clean:
	rm -rf runOpenFPGA
	source $${OPENFPGA_PATH}/openfpga.sh
	run-task FPGA44_Task --remove_run_dir all