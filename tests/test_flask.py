import requests
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.settings import FLASK_APP_URL


class TestFlask(unittest.TestCase):
    """A class that tests the basic functionality of the wrapper server
    """
    def test_hello_world(self):
        """Tests successful execution of a basic C program "Hello, World!"

           Sends a request to the wrapper server. It sends the request for
           processing to the appropriate Celery queue - by default to 1,
           unless another is specified in {"parameters": {"queue": N}}.
           Next, the celery task sends a requests to the corresponding Jobe server.
           Jobe returns code 200 and JSON-object with a field "outcome" of 15,
           which means the run completed without any exceptions.
        """
        data = {
            "run_spec": {
                "language_id": "c",
                "sourcecode": '\n#include <stdio.h>\n\nint main() {\n    printf("Hello world\\n");\n}\n',
                "sourcefilename": "test.c",
            }
        }

        response = requests.post(FLASK_APP_URL, json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["outcome"], 15)

    def test_sqr(self):
        data = {
            "run_spec": {
                "language_id": "python3",
                "sourcecode": 'def sqr(n):\r\n    return n * n\n\n__student_answer__ = """def sqr(n):\r\n    return n * n"""\n\nSEPARATOR = "#<ab@17943918#@>#"\n\nprint(sqr(5))\nprint(SEPARATOR)\nprint(sqr(0))\nprint(SEPARATOR)\nprint(sqr(9))\nprint(SEPARATOR)\nprint(sqr(2))\n',
                "sourcefilename": "__tester__.python3",
                "input": "\n",
                "file_list": [],
                "parameters": [],
            }
        }

        response = requests.post(FLASK_APP_URL, json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["outcome"], 15)

    def test_compilation_error(self):
        data = {
            "run_spec": {
                "language_id": "c",
                "sourcecode": '\n#include <stdio.h\n\nint main() {\n    printf("Hello world\\n");\n}\n',
                "sourcefilename": "test.c",
            }
        }

        response = requests.post(FLASK_APP_URL, json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["outcome"], 11)

    def test_time_limit_exceeded(self):
        data = {
            "run_spec": {
                "language_id": "c",
                "sourcecode": "\n#include <stdio.h>\n\nint main() {\n    while(1){}\n}\n",
                "sourcefilename": "test.c",
            }
        }

        response = requests.post(FLASK_APP_URL, json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["outcome"], 13)


if __name__ == "__main__":
    unittest.main()
