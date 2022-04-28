#!/usr/bin/env bash
# set up your web servers for the deployment of web_static

new_strings="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir data/web_static/shared/
echo "simple content" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "40 i $new_strings" /etc/nginx/sites-available/default
sudo service nginx restart
