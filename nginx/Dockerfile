FROM nginx:1.19.10-alpine

RUN rm /etc/nginx/conf.d/default.conf \
    && mkdir -p /data/www/static

COPY nginx.conf /etc/nginx/conf.d