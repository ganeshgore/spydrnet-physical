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

run_examples:
	find ../examples -type f -name "*.py" \
	-execdir bash -c "${PYTHON_EXEC} {} > {}.log"  \; \
	-exec echo "Running : " "$$? {} " \; || true

clean:
	rm -rf build source/auto_*
	find . -type d -name "generated" -exec rm -rf "{}" \; || true
	find ../examples -type f -name "_*.*" -exec rm -rf "{}" \; || true


.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)