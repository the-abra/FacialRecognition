# FacialRecognition

# Getting Started 🚀

| File Name           | Description                                                                                                                      |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------|
| face_dataset.py     | Take 30 pictures with detected faces using `haarcascade_frontalface_default.xml` for training and save them to the `dataset/` path. |
| face_training.py    | Get pictures from the `dataset/` path for training and save the `trainer.yml` file to the `trainer/` path.                          |
| face_recognition.py | Live detect and recognize faces using trainer/trainer.yml

### Prerequisites 📋

- WebCam
- python3 
- python3-pip
- python3.11-venv

- Root Perm
    > Sometimes you have to be a root for access camera.

### Depends Installation (DEBIAN)

    apt install -y python3 python3-pip python3.11-venv

### Depends Installation (ARCH) 🛠️

    pacman -Syu --needed python python-pip python-virtualenv

# VENV And PIP Depends Setup

    python3 -m venv FacialRecognition
    source FacialRecognition/bin/activate
    pip install --upgrade pip
    pip install setuptools pillow opencv-python opencv-contrib-python

### Tested On 🖥️

<img width="66px" src="https://github.com/ProjectHostingTool/PHT/assets/83769871/53eec4ac-2e9c-41a1-9210-d009a5553c56" alt="ICON">
<img width="76px" src="https://github.com/ProjectHostingTool/PHT/assets/83769871/e15238d7-4a0e-47ea-a4d5-a0016000722b" alt="ICON">
