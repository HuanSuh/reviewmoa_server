#!/bin/bash
echo "started start script"
cd /home/shoepik_footmeasurement
pkill -9 uwsgi
pip install -r requirements.txt --no-cache-dir
/usr/local/bin/uwsgi --ini wsgi.ini
service nginx restart
echo "finished start script"
