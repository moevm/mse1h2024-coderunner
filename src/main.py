import requests
from flask import Flask

from src.api.routes import api
from src.settings import JOBE_SERVERS

app = Flask(__name__)

app.register_blueprint(api)


@app.get('/status')
def get_status():
    result = {"jobe_servers": [], "celery": []}
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
