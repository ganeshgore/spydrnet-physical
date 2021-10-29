
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
	cp -r FPGA44_Task/latest/k6_N10_tileable/top/MIN_ROUTE_CHAN_WIDTH/SRC \
	FPGA44_Verilog
	find ./FPGA44_Verilog -name "*.v" -exec sed -i "s/.*default_nettype/\/\/ \`default_nettype/g" '{}' \;
	duration=$$SECONDS
	echo "$$(($$duration / 60)) minutes and $$(($$duration % 60)) seconds elapsed." >> runOpenFPGA

clean:
	rm -rf runOpenFPGA
	source $${OPENFPGA_PATH}/openfpga.sh
	run-task FPGA44_Task --remove_run_dir all