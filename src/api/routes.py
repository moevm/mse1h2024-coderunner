from flask import Blueprint
from flask import request

from src.settings import LANGUAGES, API_KEY
from src.tasks import mailer

api = Blueprint('api', __name__, url_prefix='/jobe/index.php/restapi')


@api.before_request
def api_key_validation():
    if API_KEY == '*':
        return
    key = request.headers.get('X-API-KEY')
    if key != API_KEY:
        return "Invalid API-key", 403


@api.post('/runs')
def submit_run():
    request_data = request.get_json()
    task_result = mailer.delay(request_data)
    try:
        result, status_code = task_result.get(timeout=30)
        return result, status_code
    except TimeoutError:
        return "Time limit exceeded", 500


@api.get('/languages')
def get_languages():
    return LANGUAGES


@api.get('/runresults/<run_id>')
def get_run_status(run_id):
    return "runresults_get: unimplemented, as all submissions run immediately."


@api.post('/files')
def post_file():
    return "file_post: not implemented on this server", 403


@api.route('/files/<file_id>', methods=["PUT", "HEAD"])
def put_or_check_file(file_id):
    return 'unimplemented', 404
