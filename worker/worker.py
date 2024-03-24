from flask import Flask, request
from celery import Celery
celery = Celery('tasks', broker='amqp://guest:guest@localhost//')


if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/process_request', methods=['POST'])
    def process_request_route():
        return handle_request(request)
    
    app.run()