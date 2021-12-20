pip install --upgrade pip
pip install --upgrade Cython
apt-get -y install metis 

if [ -f "requirements.txt" ]; then
    python3 -m pip install --upgrade \
    --no-cache-dir -r requirements.txt
fi