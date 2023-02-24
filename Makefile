SHELLO = bash
DOCKER = docker
BUILD_ARGS =

docker_docs:
	${DOCKER} build ${BUILD_ARGS} -f .github/dockerfile -t ghcr.io/ganeshgore/sdpphy-docs-image .

docker_binder_base:
	${DOCKER} build ${BUILD_ARGS} --squash -f .github/dockerfile_binder -t ghcr.io/ganeshgore/sdpphy-binder-base-image .

binder:
	${DOCKER} build ${BUILD_ARGS} -f Dockerfile -t ghcr.io/ganeshgore/sdpphy-binder-image .

push_docker_docs:
	${DOCKER} push ghcr.io/ganeshgore/sdpphy-docs-image

push_docker_binder_base:
	${DOCKER} push ghcr.io/ganeshgore/sdpphy-binder-base-image

start_local_binder:
	${DOCKER} run -it --rm -p 8000:8000 \
		-e JUPYTER_ENABLE_LAB=yes \
		ghcr.io/ganeshgore/sdpphy-binder-image \
		jupyter notebook --NotebookApp.default_url=/vscode/ --ip=0.0.0.0 --port=8000 -e JUPYTER_ENABLE_LAB=yes