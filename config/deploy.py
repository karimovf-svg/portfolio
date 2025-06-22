"""
1.
ssh-keygen
2.
cat .ssh/id_rsa.pub

3.

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

4.

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/portfolio
ExecStart=/var/www/portfolio/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target



5.


server {
    listen 80;
    server_name 134.209.233.107;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
       root /var/www/portfolio;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
"""
