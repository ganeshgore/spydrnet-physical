FROM ghcr.io/ganeshgore/sdpphy-binder-image:latest

RUN git clone https://github.com/ganeshgore/spydrnet-physical
WORKDIR /home/docs/spydrnet-physical
# Set up terminal
RUN echo 'alias codeopen="code-server -r "' >> ~/.bashrc
RUN mkdir -p .vscode && echo '{"workbench.colorTheme": "Monokai"}' > .vscode/settings.json