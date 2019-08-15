# coding:utf-8

from celery import Celery

app = Celery(__name__, include=['queues_tasks'])

app.config_from_object('celeryconfig')

if __name__ == '__main__':
    app.start()
