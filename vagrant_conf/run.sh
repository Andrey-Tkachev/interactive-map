#!/bin/bash

cd interactive_map/frontend_app
npm install
npm run build

cd ../..
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8042
