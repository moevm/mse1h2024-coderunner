import requests

from src.celery_configurator import app
from src.settings import (JOBE_1_SERVER_URL, JOBE_2_SERVER_URL,
                          JOBE_3_SERVER_URL, JOBE_4_SERVER_URL)
from src.utils import get_logger

log = get_logger(__name__)


def jobe_task(server_url: str, request_data):
    try:
        res = requests.post(
            server_url + "/jobe/index.php/restapi/runs", json=request_data
        )
        return res.json(), res.status_code
    except Exception as e:
        return {"error": str(e)}, 500


@app.task
def jobe_1_task(request_data):
    result = jobe_task(JOBE_1_SERVER_URL, request_data)
    return result


@app.task
def jobe_2_task(request_data):
    result = jobe_task(JOBE_2_SERVER_URL, request_data)
    return result


@app.task
def jobe_3_task(request_data):
    result = jobe_task(JOBE_3_SERVER_URL, request_data)
    return result


@app.task
def jobe_4_task(request_data):
    result = jobe_task(JOBE_4_SERVER_URL, request_data)
    return result
