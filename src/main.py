from flask import Flask
from src.tasks import mailer, uploader

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.get("/test_tasks_queue")
def test_tasks_queue():
    result = mailer.delay()
    return {"test_tasks_queue": f"{result.status}"}, 200

@app.get("/test_replies_queue")
def test_replies_queue():
    result = uploader.delay()
    return {"test_replies_queue": f"{result.status}"}, 200
