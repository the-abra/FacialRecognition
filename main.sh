# Setup
apt update
apt install -y python3 python3-pip
python3 -m venv /opt/FacialRecognition
source /opt/FacialRecognition/bin/activate
pip install --upgrade pip
pip install setuptools pillow opencv-python opencv-contrib-python
