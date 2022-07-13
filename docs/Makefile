# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SHELL             = bash
SPHINXOPTS        = -D plot_gallery=0
SPHINXRELOADOPTS  = 
SPHINXBUILD       = sphinx-build
SPHINXRELOAD      ?= sphinx-autobuild
SOURCEDIR         = source
BUILDDIR          = build
AUTO_BUILD_DIR    = "auto_.*\/.*"
PYTHON_EXEC       ?= "python3.8"
RUN_EXAMPLE_WC    ?= 

.SILENT:
.ONESHELL:

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

install:
	@pip3 install -U -r requirements.txt

reload:
	@$(SPHINXRELOAD) "$(SOURCEDIR)" "${BUILDDIR}" \
	--watch "../examples/**/*.py" \
	--watch "../spydrnet_physical/support_files/**" \
	--re-ignore ${AUTO_BUILD_DIR} $(SPHINXRELOADOPTS) $(SPHINXOPTS) $(O)

generate_schematics:
	mkdir -p source/auto_sample_verilog
	find ../spydrnet_physical/support_files/sample_verilog -name \*.svg -exec cp {} ./source/auto_sample_verilog \;
	find ../spydrnet_physical/support_files/sample_verilog/ -type f -name "*.v" | \
	parallel -j 4  'filename={}; \
	topmodule=$$(sed -n "s/module \(.*\)(.*/\1/p" $${filename} | head -1); \
	echo "Generating schematic for [$$topmodule]  $$filename"; \
	yosys -p "prep -top $$topmodule; write_json $${filename%.*}.json;" {} > $${filename%.*}.log; \
	netlistsvg $${filename%.*}.json -o $${filename%.*}.svg; \
	cp $${filename%.*}.svg source/auto_sample_verilog/'

run_examples: generate_schematics
	export PYTHONPATH=$${PYTHONPATH}:$$(pwd)/..
	log_dir=$$(pwd)/_run_examples_logs
	mkdir -p $$log_dir
	rm -rf $${log_dir}/failed.log 
	find ../examples/OpenFPGA_${RUN_EXAMPLE_WC} -type f -name "*.py" | \
	parallel -j 4 'log_dir=$$(pwd); \
	cd $$(dirname {}); filename=$$(basename {}); \
	${PYTHON_EXEC} $$(basename {}) 1> "$${log_dir}/_run_examples_logs/$${filename%.*}.log"; \
	if [ $$? -eq 0 ]; then echo "--- " {}; \
		else echo {} > "$${log_dir}/_run_examples_logs/failed.log"; \
	echo "ERROR" {}; fi;'
	if [[ -f $${log_dir}/failed.log ]]; then return 1; fi

design_examples:
# Write a script to run a  design example before documentation
# mainly every design project will consist of a shell script to execute code
# design_examples execution is different from run_examples execution because the 
# each script is not independent, and it needs to executed sequentially 
	echo "Not implemented yet"

# run_examples:
# 	find ../examples -type f -name "*.py" \
# 	-exec echo "Running : " "$$? {} " \; \
# 	-execdir bash -c "${PYTHON_EXEC} {} > /dev/null" \; \
# 	 || true

clean:
	rm -rf build source/auto_*
	find . -type d -name "generated" -exec rm -rf "{}" \; || true

clean_all: clean
	find ../examples -type f -name "_*.*" -exec rm -rf "{}" \; || true
	find ../examples -type f -name "*.log" -exec rm -rf "{}" \; || true


.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)