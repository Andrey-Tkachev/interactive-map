#!/bin/bash

set -x

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

sudo apt-get update
sudo apt-get install -y mongodb-org

if [ ! -f "/vagrant/tomita/bin/tomita-linux64" ]; then
    echo "Download tomita...";
    mkdir /vagrant/tomita/bin
    wget -q -O /vagrant/tomita/bin/tomita-linux64.bz2 http://download.cdn.yandex.net/tomita/tomita-linux64.bz2
    bzip2 -d /vagrant/tomita/bin/tomita-linux64.bz2
fi

chmod 777 /vagrant/tomita/bin/tomita-linux64
chmod 777 /vagrant/vagrant_conf/run.sh

curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs

cat >> /home/vagrant/.bashrc <<EOF
export MONGO_URI='127.0.0.1:27017'
export MONGO_DJANGO_DB='django'
export MONGO_SCRAPY_DB='scrapy'
export MONGO_CRAWLED_COLLECTION='raw_news'
export TOMITA_BIN='./bin/tomita-linux64'
sudo service mongod restart
cd /vagrant/
EOF

set +x
