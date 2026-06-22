#!/bin/bash
pkg update && pkg upgrade -y
pkg install python git -y
pip install requests
git clone https://github.com/nj3918410-creator/fb-tool.git
cd fb-tool
python run.py
