FROM python:3.11-alpine

WORKDIR /app

RUN apk update && \
    rm -rf /var/cache/**

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./flask/start /start
RUN chmod +x /start

COPY ./celery/worker/start /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./celery/flower/start /start-flower
RUN chmod +x /start-flower
