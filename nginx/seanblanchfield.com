server {
    listen 80 default_server;
    server_name seanblanchfield.com;
    return 301 https://seanblanchfield.com$request_uri;
}

server {
    listen 443 ssl;
    server_name .seanblanchfield.com;
    ssl_certificate /etc/letsencrypt/live/seanblanchfield.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/seanblanchfield.com/privkey.pem; # managed by Certbot
    
    root /var/www/seanblanchfield.com;
    index index.html;
    
    
    location / {
        try_files $uri $uri.html $uri/ /index.html;
    }

    error_page 404 /404.html;

    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
