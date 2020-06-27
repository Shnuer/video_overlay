#!/bin/bash

dpkg -s ffmpeg &>/dev/null
if [ $? -eq 0 ]; then
    echo "Package ffmpeg is installed!"
else
    echo "Package  ffmpeg not installed!"
    while true; do 
        read -p "Do you wish to install ffmpeg? (y/n) " yn
        case $yn in 
            [Yy]* ) sudo apt install ffmpeg -y; break;;
            [Nn]* )exit;;
            *  ) echo "Please answer yes or no.";;
        esac
    done  
fi

dpkg -s python3 &>/dev/null
if [ $? -eq 0 ]; then
    echo "Package python3 is installed!"
else
    echo "Package  python3 not installed!"
    while true; do 
        read -p "Do you wish to install python3? (y/n) " yn
        case $yn in 
            [Yy]* ) sudo apt install python3 -y; break;;
            [Nn]* )exit;;
            *  ) echo "Please answer yes or no.";;
        esac
    done  
fi

dpkg -s python3-pip &>/dev/null
if [ $? -eq 0 ]; then
    echo "Package pip3 is installed!"
else
    echo "Package  pip3 not installed!"
    while true; do 
        read -p "Do you wish to install pip3? (y/n) " yn
        case $yn in 
            [Yy]* ) sudo apt install python3-pip -y; break;;
            [Nn]* )exit;;
            *  ) echo "Please answer yes or no.";;
        esac
    done  
fi

pip3 install -r requirements.txt; 
python3 main.py -i $1 -o $2 -d $3