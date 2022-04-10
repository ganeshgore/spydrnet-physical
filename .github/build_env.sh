pip install --upgrade pip
pip install --upgrade Cython
apt-get -y install metis parallel

if [ -f "requirements.txt" ]; then
    python3 -m pip install --upgrade \
    --no-cache-dir -r requirements.txt
fi
echo "spydrnet_physical" > ~/.spydrnet
python3 -c "import spydrnet as sdn;print(sdn.get_active_plugins());print(dir(sdn.ir.Cable))"