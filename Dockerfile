FROM ghcr.io/ganeshgore/sdpphy-binder-base-image:latest

RUN git clone https://github.com/ganeshgore/spydrnet-physical
WORKDIR /home/docs/spydrnet-physical

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension formulahendry.code-runner
RUN code-server --install-extension jock.svg
ENV PATH="/tmp/buildenv/bin:$PATH"

#  SVG preview extension did not work in browser
# RUN wget https://github.com/SimonSiefke/vscode-svg-preview/releases/download/v1.6.2/extension.vsix -O /tmp/svg_preview_extension.vsix
# RUN code-server --install-extension /tmp/svg_preview_extension.vsix
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Set up terminal
RUN echo "spydrnet_physical" > ~/.spydrnet
RUN echo 'alias codeopen="code-server -r "' >> ~/.bashrc
RUN echo 'export PATH="/tmp/buildenv/bin:$PATH"' >> ~/.bashrc
RUN echo 'export PYTHONPATH=/home/docs/spydrnet-physical' >> ~/.bashrc
RUN mkdir -p .vscode
RUN echo 'PYTHONPATH=/home/docs/spydrnet-physical' > .vscode/.env
RUN echo '{"workbench.colorTheme": "Monokai","python.envFile": "${workspaceFolder}/.vscode/.env","code-runner.runInTerminal": true,"code-runner.executorMap": {"python": "cd $dirWithoutTrailingSlash && python3.8 -u $fileName",},}' > .vscode/settings.json
