#!/bin/bash
cd /vagrant
rm -rf dev_env
mkdir dev_env
python manage.py migrate
python manage.py easy_crawl
python manage.py populate_models
