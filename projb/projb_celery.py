# coding:utf-8
from celery import Celery

app = Celery(__name__, include=['projb.projb_tasks'])

app.config_from_object('projb.celeryconfig')

if __name__ == '__main__':
    app.start()
