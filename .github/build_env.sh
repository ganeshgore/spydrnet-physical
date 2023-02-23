pip install --upgrade pip
pip install --upgrade Cython
apt-get update
apt-get -y install metis parallel libxml2-utils
cp /usr/bin/netlistsvg /usr/bin/netlistsvg-hierarchy

if [ -f "requirements.txt" ]; then
    python3 -m pip install --upgrade \
    --no-cache-dir -r requirements.txt
fi
if [ -f "requirements_extra.txt" ]; then
    python3 -m pip install --upgrade \
    --no-cache-dir -r requirements_extra.txt
fi
echo "spydrnet_physical" > ~/.spydrnet
python3 -c "import spydrnet as sdn;print(sdn.get_active_plugins());print(dir(sdn.ir.Cable))"