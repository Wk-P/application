#!/bin/bash
source /home/ecs-user/application/DjangoProject/.venv/bin/activate &&
    uwsgi --stop /home/ecs-user/application/scripts/run/uwsgi.pid

uwsgi --ini /home/ecs-user/application/scripts/uwsgi.ini &&
    sudo systemctl restart nginx &&
    sudo systemctl reload nginx
