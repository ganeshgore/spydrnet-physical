#!/bin/bash

python3 -m venv /tmp/buildenv
source /tmp/buildenv/bin/activate
python3 -m pip install --upgrade --no-cache-dir pip
if [ -f "docs/requirements.txt" ]; then
    cat docs/requirements.txt | xargs -n 1 pip install
    cat docs/requirements.txt | xargs -n 1 pip install --upgrade
fi
pip install --upgrade Cython

sed -i 's/tempclone\[2\]\[2\].*/tempclone[2][2] = this.key;/' /usr/lib/node_modules/netlistsvg/built/Cell.js