python3 -m pip install --upgrade python3 -m pip wheel setuptools
python3 -m pip install --upgrade Cython
apt-get update
apt-get -y install metis parallel libxml2-utils
ln -s ../lib/node_modules/netlistsvg/bin/netlistsvg.js /usr/bin/netlistsvg-hierarchy

if [ -f "requirements.txt" ]; then
    cat requirements.txt | xargs -n 1 python3 -m pip install --upgrade
fi
if [ -f "docs/requirements.txt" ]; then
    cat docs/requirements.txt | xargs -n 1 python3 -m pip install --upgrade
fi
if [ -f "requirements_extra.txt" ]; then
    cat requirements_extra.txt | xargs -n 1 python3 -m pip install --upgrade
fi
echo "spydrnet_physical" >~/.spydrnet
python3 -c "import spydrnet as sdn;print(sdn.get_active_plugins());print(dir(sdn.ir.Cable))"
