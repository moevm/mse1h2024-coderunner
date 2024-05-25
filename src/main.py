import requests
from flask import Flask

from src.api.routes import api
from src.settings import JOBE_SERVERS, FLOWER_URL

app = Flask(__name__)

app.register_blueprint(api)


@app.get('/status')
def get_status():
    result = {"jobe_servers": [], "celery": {}}
    try:
        workers_info = requests.get(FLOWER_URL + "/api/workers", params={"status": 1}).json()
        result["celery"]["workers"] = dict((k, "active" if v else "not available") for k, v in workers_info.items())

        queues_info = requests.get(FLOWER_URL + "/api/queues/length").json()
        result["celery"]["queues"] = queues_info["active_queues"]

    except requests.exceptions.RequestException:
        result["celery"]["flower"] = "not available"

    for url in JOBE_SERVERS:
        try:
            status = requests.get(url + "/jobe/index.php/restapi/languages").ok
            jobe_response = "active" if status else "not available"
        except requests.exceptions.RequestException:
            jobe_response = "not available"
        result["jobe_servers"].append({
            "url": url,
            "status": jobe_response
        })

    return result
