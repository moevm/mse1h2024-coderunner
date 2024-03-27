import requests
from src.celery_configurator import app
from src.settings import JOBE_SERVER_URL


@app.task
def mailer(request_data):
    try:
        res = requests.post(JOBE_SERVER_URL + '/jobe/index.php/restapi/runs', json=request_data)
        return res.json(), res.status_code
    except Exception as e:
        return {"error": str(e)}, 500
