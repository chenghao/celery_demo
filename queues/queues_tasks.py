# coding:utf-8

from celery_queues import app
import random


@app.task(queue="web_tasks")
def add(x, y):
    """
    指定 add 函数使用 web_tasks 队列
    :param x:
    :param y:
    :return:
    """
    return x + y


@app.task(bind=True, queue="default", max_retries=3)
def div(self, x, y):
    """
    指定 div 函数使用 default 队列
    :param x:
    :param y:
    :return:
    """
    try:
        result = x / y
    except ZeroDivisionError as e:
        raise self.retry(exc=e, countdown=int(random.uniform(2, 4) ** self.request.retries))
    return result


@app.task
def mult(x, y):
    return x * y
