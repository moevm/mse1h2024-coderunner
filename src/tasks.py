import time
from celery import shared_task


@shared_task
def mailer():
    print(">>> Sending mails...")
    for i in range(1, 5):
        time.sleep(3)
        print(f">>> Mail-{i} sent")
    return "Mailer success"


@shared_task
def uploader():
    print(">>> Uploading started...")
    for i in range(1, 6):
        time.sleep(2)
        print(f">>> File-{i} uploaded")
    return "Uploader success"
