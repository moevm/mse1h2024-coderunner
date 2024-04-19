import os

INSTALLED_APPS = [
    'src',
]
CELERY_TASK_ROUTES = {
    'src.tasks.mailer': {'queue': 'tasks-queue'},
    'src.tasks.uploader': {'queue': 'replies-queue'},
}

JOBE_SERVER_URL = os.getenv('JOBE_SERVER_URL', 'http://jobe:80')
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/1")


# If specified *, API_KEY is not required
API_KEY = os.getenv("API_KEY", "*")

# List of languages supported by the Jobe server
LANGUAGES = [
    [
        "c",
        "11.4.0"
    ],
    [
        "cpp",
        "11.4.0"
    ],
    [
        "java",
        "11.0.22"
    ],
    [
        "nodejs",
        "12.22.9"
    ],
    [
        "octave",
        "6.4.0"
    ],
    [
        "pascal",
        "3.2.2"
    ],
    [
        "php",
        "8.1.2"
    ],
    [
        "python3",
        "3.10.12"
    ]
]
