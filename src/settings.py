INSTALLED_APPS = [
    'src',
]
CELERY_TASK_ROUTES = {
    'src.tasks.mailer': {'queue': 'tasks-queue'},
    'src.tasks.uploader': {'queue': 'replies-queue'},
}
