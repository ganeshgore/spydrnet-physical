#!/bin/bash

python3 -m venv buildenv
source buildenv/bin/activate
python3 -m pip install --upgrade --no-cache-dir pip
if [ -f "docs/requirements.txt" ]; then
    python3 -m pip install --upgrade --no-cache-dir -r docs/requirements.txt
fi
pip install --upgrade Cython

sed -i 's/tempclone\[2\]\[2\].*/tempclone[2][2] = this.key;/' /usr/lib/node_modules/netlistsvg/built/Cell.js 