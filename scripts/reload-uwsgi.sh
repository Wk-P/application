#!/bin/bash
source ~/application/DjangoProject/.venv/bin/activate && \
    uwsgi --stop ~/application/scripts/run/uwsgi.pid && \

python3 ~/application/DjangoProject/BackendService/manage.py makemigrations && \
python3 ~/application/DjangoProject/BackendService/manage.py migrate

uwsgi --ini ~/application/scripts/uwsgi.ini && \
    sudo systemctl restart nginx && \
    sudo systemctl reload nginx
