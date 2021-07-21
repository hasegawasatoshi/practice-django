FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code

RUN apk add --no-cache postgresql-libs postgresql-client && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt && \
    apk --purge del .build-deps

COPY . /code
RUN chmod 755 ./wait-for-postgres.sh