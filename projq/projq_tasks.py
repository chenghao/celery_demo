# coding:utf-8

from projq.projq_celery import app


@app.task(queue="web_tasks")
def add(x, y):
    """
    指定 add 函数使用 web_tasks 队列
    :param x:
    :param y:
    :return:
    """
    return x + y


@app.task(bind=True, queue="default")
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
        raise self.retry(exc=e, countdown=5, max_retries=5)
    return result


@app.task
def mult(x, y):
    return x * y
