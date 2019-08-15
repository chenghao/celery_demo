#coding:utf-8

from celery import Celery

# 远程rpc调用方式
app = Celery(__name__)
app.config_from_object('celeryconfig')

r1 = app.send_task("tasks_test.add", (10, 4))
print "r1 =>  %s" % r1.get()
r2 = app.send_task("tasks_test.div", (10, 4.0))
print "r2 =>  %s" % r2.get()
