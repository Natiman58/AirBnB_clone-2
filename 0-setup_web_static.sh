#!/usr/bin/env bash

# install nginx iff not installed already
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# make dir called data
mkdir -p /data/

# create the folder web_static
mkdir -p /data/web_static/

# add the dir release
mkdir -p /data/web_static/releases/

# create the folder shared
mkdir -p /data/web_static/shared/

# create the folder called test
mkdir -p /data/web_static/releases/test/

# create a fake HTML file that prints Holberton School
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html> " > /data/web_static/releases/test/index.html

# create a symbolik b/n current and test 
ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of the /data/ folder to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# update the config of nginx to serve the content of /data/web_static/current/ to hbnb_static
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
exit 0
