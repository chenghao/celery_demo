# coding:utf-8

from celery import Celery

app = Celery(__name__)
app.config_from_object('celeryconfig')
r1 = app.send_task("tasks_test.add", (1, 4), queue="celery")
print "r1 =>  %s" % r1.get()
