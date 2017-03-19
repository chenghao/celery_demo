# coding:utf-8

from projb.projb_celery import app


@app.task
def mult():
    x = 2227
    y = 5332
    return x * y
