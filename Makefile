SHELLO = bash
DOCKER = docker
PYTHON_EXEC   ?= python3.8
BUILD_ARGS =

.SILENT:
.ONESHELL:
.DEFAULT:help

docker_docs:
# Build a docker image for documentation building (also used in the CI)
	${DOCKER} build ${BUILD_ARGS} -f .github/dockerfile -t ghcr.io/ganeshgore/sdpphy-docs-image .

docker_binder_base:
# Build base image for binder this is pulled as it is on binder
	${DOCKER} build ${BUILD_ARGS} --squash -f .github/dockerfile_binder -t ghcr.io/ganeshgore/sdpphy-binder-base-image .

binder:
# Build binder image as its build on binder platform
	${DOCKER} build ${BUILD_ARGS} -f Dockerfile -t ghcr.io/ganeshgore/sdpphy-binder-image .

push_docker_docs:
# Push docker_docs image to ghcr.io/ganeshgore/sdpphy-docs-image
	${DOCKER} push ghcr.io/ganeshgore/sdpphy-docs-image

push_docker_binder_base:
# Push docker_binder_base image to ghcr.io/ganeshgore/sdpphy-binder-base-image
	${DOCKER} push ghcr.io/ganeshgore/sdpphy-binder-base-image

start_local_binder:
# Start a local jupyter-lab/Binder server to test
	${DOCKER} run -it --rm -p 8000:8000 \
		-e JUPYTER_ENABLE_LAB=yes \
		ghcr.io/ganeshgore/sdpphy-binder-image \
		jupyter notebook --NotebookApp.default_url=/vscode/ --ip=0.0.0.0 --port=8000 -e JUPYTER_ENABLE_LAB=yes

export COMMENT_EXTRACT
help:
# Prints help message for this makefile
	@${PYTHON_EXEC} -c "$$COMMENT_EXTRACT"

define COMMENT_EXTRACT
import re
with open ('Makefile', 'r' ) as f:
	matches = re.finditer('^([a-zA-Z-_]*):.*\n#(.*)', f.read(), flags=re.M)
	space, help = 0, []
	for _, match in enumerate(matches, start=1):
		space = max(space, len(match[1]))
		help.append((match[1], match[2]))
	print("\n".join([(a.ljust(space) + b) for a, b in help]))
endef