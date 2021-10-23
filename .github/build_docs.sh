#!/bin/bash

python3 -m venv buildenv
source buildenv/bin/activate
python3 -m pip install --upgrade --no-cache-dir pip
python3 -m pip install --upgrade --no-cache-dir \
        mock==1.0.1 \
        pillow==6.2.0 \
        alabaster \
        sphinx_rtd_theme==1.0.0 \
        six \
        commonmark==0.8.1 \
        recommonmark==0.5.0 \
        sphinx==3.4.0 \
        pybtex \
        sphinx-gallery==0.10.0 \
        matplotlib==3.4.3 \
        networkx==2.5

if [ -f "docs/requirements.txt" ]; then
    pip install -r docs/requirements.txt
fi
cd docs && make html