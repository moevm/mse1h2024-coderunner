import os

INSTALLED_APPS = [
    'src',
]
CELERY_TASK_ROUTES = {
    'src.tasks.jobe_1_task': {'queue': 'jobe-1-queue'},
    'src.tasks.jobe_2_task': {'queue': 'jobe-2-queue'},
    'src.tasks.jobe_3_task': {'queue': 'jobe-3-queue'},
    'src.tasks.jobe_4_task': {'queue': 'jobe-4-queue'},
}

JOBE_1_SERVER_URL = os.getenv('JOBE_1_SERVER_URL', 'http://jobe-1:8881')
JOBE_2_SERVER_URL = os.getenv('JOBE_2_SERVER_URL', 'http://jobe-2:8882')
JOBE_3_SERVER_URL = os.getenv('JOBE_3_SERVER_URL', 'http://jobe-3:8883')
JOBE_4_SERVER_URL = os.getenv('JOBE_4_SERVER_URL', 'http://jobe-4:8884')
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/1")

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
