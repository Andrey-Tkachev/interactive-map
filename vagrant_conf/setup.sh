#!/bin/bash

set -x

sudo apt-get install build-essential libssl-dev libffi-dev python3-dev python3-setuptools -y
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

sudo apt-get update
sudo apt-get install -y mongodb-org
sudo service mongod start

if [ ! -f "/vagrant/tomita/bin/tomita-linux64" ]; then
    echo "Download tomita...";
    mkdir /vagrant/tomita/bin
    wget -q -O /vagrant/tomita/bin/tomita-linux64.bz2 http://download.cdn.yandex.net/tomita/tomita-linux64.bz2
    bzip2 -d /vagrant/tomita/bin/tomita-linux64.bz2
fi

chmod 777 /vagrant/tomita/bin/tomita-linux64

sudo easy_install3 pip
pip install scrapy pymongo xmltodict

cat >> /home/vagrant/.bashrc <<EOF
export MONGO_URI='127.0.0.1:27017'
export MONGO_DB='news'
export MONGO_RNEWS_COLLECTION='raw'
export TOMITA_BIN='./bin/tomita-linux64'
cd /vagrant/
rm ./*.log
EOF

set +x
