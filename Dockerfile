FROM ghcr.io/ganeshgore/sdpphy-binder-image:latest

RUN git clone https://github.com/ganeshgore/spydrnet-physical
WORKDIR /home/docs/spydrnet-physical

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension formulahendry.code-runner
RUN python3 -m pip install --user --no-cache-dir -r requirements.txt

# Set up terminal
RUN echo "spydrnet_physical" > ~/.spydrnet
RUN echo 'alias codeopen="code-server -r "' >> ~/.bashrc
RUN echo 'export PYTHONPATH=/home/docs/spydrnet-physical' >> ~/.bashrc
RUN mkdir -p .vscode
RUN echo 'PYTHONPATH=/home/docs/spydrnet-physical' > .vscode/.env
RUN echo '{
        "workbench.colorTheme": "Monokai",
        "python.envFile": "${workspaceFolder}/.vscode/.env",
        "code-runner.runInTerminal": true,
        "code-runner.executorMap": {
            "python": "cd $dirWithoutTrailingSlash && python3.8 -u $fileName",
        },
    }' > .vscode/settings.json
