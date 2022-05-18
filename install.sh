#!/bin/bash

sudo ln -s -f $PWD/bin/ovpn.py /usr/local/bin/ovpn

if [ ! -d /opt/easy-rsa ]
then
    sudo mkdir -p /opt/easy-rsa/
    sudo wget -P /opt/easy-rsa/ https://github.com/OpenVPN/easy-rsa/releases/download/v3.0.6/EasyRSA-unix-v3.0.6.tgz
    cd /opt/easy-rsa/
    sudo tar xvf EasyRSA-unix-v3.0.6.tgz
    sudo chown -R root:root .
fi
