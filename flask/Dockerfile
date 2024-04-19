FROM python:3.11-alpine

WORKDIR /app

RUN apk update && \
    rm -rf /var/cache/**

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /src ./src

COPY flask/start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]