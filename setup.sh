#!/bin/bash

if ! [ "$UID" -eq 0 ]; then
    echo "You are not running as root. Please run this script with sudo or as root."
    exit 1
fi

if ! ping -c 1 github.com > /dev/null; then
    echo -e "You must have an internet connection!" && exit 1
fi

! [[ -d /lib/func4bash ]] && bash -c "$(curl -sSfL https://raw.githubusercontent.com/func4bash/bash-utilities-library/main/setup.sh)"
source /lib/func4bash/logging.lib
source /lib/func4bash/static_progress_bar.lib

# PATH setup
log.info "Setting up /opt/FacialRecognition path..."
progress "0"
git clone https://github.com/the-abra/FacialRecognition /opt/FacialRecognition 1> /dev/null 2> /tmp/fcr_error.log || { log.error "Git Clone process failed" ; cat /tmp/fcr_error.log; exit 1; }
progress "50"
python3 -m venv /opt/FacialRecognition &> /dev/null
progress "100" && progress_done

# Virtualization
log.info "VENV Activated."
source /opt/FacialRecognition/bin/activate

# Depends Installing
log.info "Installing dependencies..."
pip install --upgrade pip
pip install setuptools pillow opencv-python opencv-contrib-python

log.done "SYSTEM INSTALLED to /opt/FacialRecognition"