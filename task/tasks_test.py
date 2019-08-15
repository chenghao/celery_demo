#coding:utf-8

from celery_task import app
from celery.utils.log import get_task_logger
import random

logger = get_task_logger(__name__)


@app.task
def add(x, y):
    return x + y


@app.task(bind=True, max_retries=3)
def div(self, x, y):
    """
    备注： max_retries是重试次数，countdown每次重试的间隔秒数（2-5随机 ** 次数）
    每次重试的秒数递增
    :param self:
    :param x:
    :param y:
    :return:
    """
    logger.info(('Executing task id {0.id}, args: {0.args!r}, kwargs: {0.kwargs!r}').format(self.request))
    try:
        result = x / y
    except ZeroDivisionError as e:
        raise self.retry(exc=e, countdown=int(random.uniform(2, 4) ** self.request.retries))
    return result


@app.task(bind=True, max_retries=3)
def mult(self, x, y):
    """
    备注： max_retries是重试次数，countdown每次重试的间隔秒数（2-5随机 ** 次数）
    每次重试的秒数递增
    :param self:
    :param x:
    :param y:
    :return:
    """
    res = x * y
    if res % 100 != 0:
        raise self.retry(exc=ValueError("not 100 multiple."),
                         countdown=int(random.uniform(2, 4) ** self.request.retries))
    return res
