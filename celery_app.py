from celery import Celery
from web_scraping.myWeb import kun_uz_play

celery = Celery(
    'main',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)


@celery.task
def send_kun():
    informations = kun_uz_play()
    for information in informations:
        print(information)



celery.conf.beat_schedule = {
    'send-email': {
        'task': 'celery_app.send_kun',
        'schedule': 180.0
    }
}

