FROM nginx:1.21.6 as nginx_proxy

#COPY ./compose/staging/nginx/htpasswd.dev /etc/nginx/htpasswd.dev
COPY ./compose/production/nginx/nginx.conf /etc/nginx/nginx.conf
#COPY ./compose/production/nginx/sites-available/*.conf /etc/nginx/sites-enabled/
COPY ./compose/production/nginx/conf.d/headers.conf /etc/nginx/headers.conf
COPY ./compose/production/nginx/conf.d/ssl.conf /etc/nginx/ssl.conf
COPY ./compose/production/nginx/conf.d/mime.types /etc/nginx/mime.types
