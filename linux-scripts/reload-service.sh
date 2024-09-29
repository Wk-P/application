sudo systemctl stop nginx

cd ~/application/linux-scripts/ && \
./reload-uwsgi.sh
./vue-reload.sh && \

sudo chmod 777 -R ~/application/

sudo systemctl start nginx