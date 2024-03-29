from flask import Flask, request
from celery import Celery
celery = Celery('tasks', broker='amqp://guest:guest@localhost//')
@celery.task
def process_request(request_data):
    print("Received request data:", request_data)

def handle_request(request):
   
    request_data = request.get_json()
    process_request.delay(request_data)
    return "Request processed and added to the queue"
if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/process_request', methods=['POST'])
    def process_request_route():
        return handle_request(request)
    
    app.run()
