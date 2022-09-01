
SHELL = bash
PYTHON_EXEC ?= python3.8
OPTIONS =
OPENFPGA_PATH ?=
DESIGN_NAME = FPGA44

.SILENT:
.ONESHELL:

runOpenFPGA:
	SECONDS=0
	source $${OPENFPGA_PATH}/openfpga.sh
	run-task ${DESIGN_NAME}_Task --remove_run_dir all
	run-task ${DESIGN_NAME}_Task
	rm -rf ${DESIGN_NAME}_Verilog && mkdir ${DESIGN_NAME}_Verilog
	rm -rf ${DESIGN_NAME}_gsb && mkdir ${DESIGN_NAME}_gsb
	rm -rf ${DESIGN_NAME}_bitstreams && mkdir ${DESIGN_NAME}_bitstreams
	cp -R ${DESIGN_NAME}_Task/latest/k6_N10_tileable/top/MIN_ROUTE_CHAN_WIDTH/${DESIGN_NAME}_Verilog .
	cp -R ${DESIGN_NAME}_Task/CustomModules/ ${DESIGN_NAME}_Verilog/
	cp -R ${DESIGN_NAME}_Task/latest/k6_N10_tileable/top/MIN_ROUTE_CHAN_WIDTH/${DESIGN_NAME}_gsb/ .
	cp ${DESIGN_NAME}_Task/latest/k6_N10_tileable/top/MIN_ROUTE_CHAN_WIDTH/fabric_key_output.xml ${DESIGN_NAME}_bitstreams/
#	Copy bitsream files
	for file in ${DESIGN_NAME}_Task/latest/k6_N10_tileable/**/*_bitstream.xml; do
		benchmark=$$(basename $$(dirname $$(dirname "$$file")))
		mkdir -p ${DESIGN_NAME}_bitstreams/$${benchmark}
		cp $$file ${DESIGN_NAME}_bitstreams/$${benchmark}/
	done
	sed -i "/Author:.*/d" ${DESIGN_NAME}_bitstreams/*/*.xml
	sed -i "/Organization:.*/d" ${DESIGN_NAME}_bitstreams/*/*.xml
	sed -i "/Date:.*/d" ${DESIGN_NAME}_bitstreams/*/*.xml
	# for file in ${DESIGN_NAME}_gsb/*.xml; do mv "$$file" "$${file/\//\/_}"; done
	find ./${DESIGN_NAME}_Verilog -name "*.v" -exec sed -i "s/.*default_nettype/\/\/ \`default_nettype/g" '{}' \;
	find ./${DESIGN_NAME}_Verilog -type f -name "*.v" -print0 | xargs -0  sed -i "/^\/\/.*Date.*/d"
	find ./${DESIGN_NAME}_Verilog -type f -name "*.v" -print0 | xargs -0  sed -i "/^\/\/.*Author.*/d"
	$${PYTHON_EXEC} -c "import spydrnet as sdn; import yaml; from pathlib import Path; import os;\
			netlist = sdn.parse('${DESIGN_NAME}_Verilog/fpga_top.v'); \
			modules = sorted([e for e in netlist.top_instance.reference.get_definitions()], key=lambda x: x.name); \
			instances = {m.name:sorted([i.name for i in m.references]) for m in modules}; \
			yaml.dump(instances, open('top_hierarchy.yml', 'w'))"
	rm -rf split_bitstreams
	$${PYTHON_EXEC} -c "from spydrnet_physical.util import split_fabric_bitstream;
					split_fabric_bitstream('${DESIGN_NAME}_bitstreams/top/fabric_independent_bitstream.xml', \
										'top_hierarchy.yml', output_dir='split_bitstreams', unique=True)"
	find ./${DESIGN_NAME}_gsb -name "*.xml" -type f -exec xmllint --output '{}' --format '{}' \;
	duration=$$SECONDS
	echo "$$(($$duration / 60)) minutes and $$(($$duration % 60)) seconds elapsed." >> runOpenFPGA

clean:
	rm -rf runOpenFPGA
	source $${OPENFPGA_PATH}/openfpga.sh
	run-task ${DESIGN_NAME}_Task --remove_run_dir all