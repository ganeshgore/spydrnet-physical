
SHELL = bash
PYTHON_EXEC ?= python3.8
OPTIONS =
OPENFPGA_PATH ?=

.SILENT:
.ONESHELL:

runOpenFPGA:
	SECONDS=0
	source $${OPENFPGA_PATH}/openfpga.sh
	run-task FPGA88_hetero_Task --remove_run_dir all
	run-task FPGA88_hetero_Task
	rm -rf FPGA88_hetero_Verilog && mkdir FPGA88_hetero_Verilog
	rm -rf FPGA88_hetero_gsb && mkdir FPGA88_hetero_gsb
	cp -R FPGA88_hetero_Task/latest/k6_N10_tileable/top/MIN_ROUTE_CHAN_WIDTH/FPGA88_hetero_Verilog .
	cp -R FPGA88_hetero_Task/CustomModules/ FPGA88_hetero_Verilog/
	cp -R FPGA88_hetero_Task/latest/k6_N10_tileable/top/MIN_ROUTE_CHAN_WIDTH/FPGA88_hetero_gsb/ .
	for file in FPGA88_hetero_gsb/*.xml; do mv "$$file" "$${file/sb_/_sb_}"; done
	find ./FPGA88_hetero_Verilog -name "*.v" -exec sed -i "s/.*default_nettype/\/\/ \`default_nettype/g" '{}' \;
	find ./FPGA88_hetero_Verilog -type f -name "*.v" -print0 | xargs -0  sed -i "/^\/\/.*Date.*/d"
	find ./FPGA88_hetero_Verilog -type f -name "*.v" -print0 | xargs -0  sed -i "/^\/\/.*Author.*/d"
	${PYTHON_EXEC} clean_gsb.py
	find ./FPGA88_hetero_gsb -name "*.xml" -type f -exec xmllint --output '{}' --format '{}' \;
	duration=$$SECONDS
	echo "$$(($$duration / 60)) minutes and $$(($$duration % 60)) seconds elapsed." >> runOpenFPGA

clean:
	rm -rf runOpenFPGA
	source $${OPENFPGA_PATH}/openfpga.sh
	run-task FPGA88_hetero_Task --remove_run_dir all