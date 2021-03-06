FROM python:3.9.3-alpine3.13

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk update \
    && apk add postgresql-dev gcc musl-dev \
    && pip3 install -r requirements.txt \
    && rm -rf /var/cache/apk \
    && mkdir static

COPY . .
