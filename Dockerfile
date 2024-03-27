FROM python:3.11-alpine

WORKDIR /app

RUN apk update && \
    rm -rf /var/cache/**

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./src ./src

COPY ./flask/start.sh ./start.sh
RUN chmod +x ./start.sh

COPY ./celery/worker/start.sh ./start-celeryworker.sh
RUN chmod +x ./start-celeryworker.sh

COPY ./celery/flower/start.sh ./start-flower.sh
RUN chmod +x ./start-flower.sh
