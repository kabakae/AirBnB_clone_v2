#!/usr/bin/env bash
# script that sets up web servers for deployment

# Update package index
sudo apt-get update

# Install Nginx
sudo apt-get -y install nginx

# Allow Nginx HTTP traffic
sudo ufw allow 'Nginx HTTP'

# Create necessary directories
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create index.html file
sudo tee /data/web_static/releases/test/index.html >/dev/null <<EOF
<html>
<head>
</head>
<body>
  Holberton School
</body>
</html>
EOF

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static {alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
