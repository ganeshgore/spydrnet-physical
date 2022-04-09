# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SHELL             = bash
SPHINXOPTS        =
SPHINXRELOADOPTS  =
SPHINXBUILD       = sphinx-build
SPHINXRELOAD      ?= sphinx-autobuild
SOURCEDIR         = source
BUILDDIR          = build
AUTO_BUILD_DIR    = "auto_.*\/.*"
PYTHON_EXEC       ?= "python3.8"

.SILENT:

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

install:
	@pip3 install -U -r requirements.txt

reload:
	@$(SPHINXRELOAD) "$(SOURCEDIR)" "${BUILDDIR}" \
	--watch "../examples/**" \
	--watch "../spydrnet_physical/support_files/**" \
	--re-ignore ${AUTO_BUILD_DIR} $(SPHINXRELOADOPTS) $(SPHINXOPTS) $(O)

generate_schematics:
	find ../spydrnet_physical/support_files/sample_verilog/ -type f -name "*.v" | \
	parallel -j 4  'filename={}; \
	topmodule=$$(sed -n "s/module \(.*\)(.*/\1/p" $${filename} | head -1); \
	echo "Generating schematic for [$$topmodule]  $$filename"; \
	yosys -p "prep -top $$topmodule; write_json $${filename%.*}.json;" {} > $${filename%.*}.log; \
	netlistsvg $${filename%.*}.json -o $${filename%.*}.svg'

run_examples: generate_schematics
	find ../examples -type f -name "*.py" | \
	parallel -j 4 'cd $$(dirname {}) ; \
	${PYTHON_EXEC} $$(basename {}) &> /dev/null; \
	if [ $$? -eq 0 ]; then echo "--- " {}; else echo "ERROR" {}; fi;'

# run_examples:
# 	find ../examples -type f -name "*.py" \
# 	-exec echo "Running : " "$$? {} " \; \
# 	-execdir bash -c "${PYTHON_EXEC} {} > /dev/null" \; \
# 	 || true

clean:
	rm -rf build source/auto_*
	find . -type d -name "generated" -exec rm -rf "{}" \; || true
	find ../examples -type f -name "_*.*" -exec rm -rf "{}" \; || true


.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)