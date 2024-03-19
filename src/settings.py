import os

INSTALLED_APPS = [
    'src',
]
CELERY_TASK_ROUTES = {
    'src.tasks.mailer': {'queue': 'tasks-queue'},
    'src.tasks.uploader': {'queue': 'replies-queue'},
}

JOBE_SERVER_URL = os.getenv('JOBE_SERVER_URL', 'http://localhost:8000')

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
