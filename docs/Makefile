# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS        =
SPHINXRELOADOPTS  =
SPHINXBUILD       = sphinx-build
SPHINXRELOAD      ?= sphinx-autobuild
SOURCEDIR         = source
BUILDDIR          = build
AUTO_BUILD_DIR    = "auto_.*\/.*"

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

install:
	@pip3 install -U -r requirements.txt

reload:
	@$(SPHINXRELOAD) "$(SOURCEDIR)" "${BUILDDIR}" \
	--watch "../examples/**" \
	--re-ignore ${AUTO_BUILD_DIR} $(SPHINXRELOADOPTS) $(SPHINXOPTS) $(O)

clean:
	rm -rf build source/auto_*
	find . -type d -name "generated" -exec rm -rf "{}" \; || true


.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)