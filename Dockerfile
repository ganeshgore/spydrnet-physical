FROM ghcr.io/ganeshgore/sdpphy-binder-image:latest

RUN git clone https://github.com/ganeshgore/spydrnet-physical
WORKDIR /home/docs/spydrnet-physical

RUN code-server --install-extension ms-python.python
RUN python3 -m pip install --user --no-cache-dir -r requirements.txt 

# Set up terminal
RUN echo "spydrnet_physical" > .spydrnet
RUN echo 'alias codeopen="code-server -r "' >> ~/.bashrc
RUN mkdir -p .vscode && echo '{"workbench.colorTheme": "Monokai"}' > .vscode/settings.json