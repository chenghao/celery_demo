# coding:utf-8
from gevent import monkey

monkey.patch_all()
from celery import Celery

app = Celery(__name__, include=['projq.projq_tasks'])

app.config_from_object('projq.celeryconfig')

if __name__ == '__main__':
    app.start()
