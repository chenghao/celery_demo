# coding:utf-8

from celery_test import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def add(x, y):
    return x + y


@app.task(bind=True)
def div(self, x, y):
    logger.info(('Executing task id {0.id}, args: {0.args!r} '
                 'kwargs: {0.kwargs!r}').format(self.request))

    try:
        result = x / y
    except ZeroDivisionError as e:
        raise self.retry(exc=e, countdown=5, max_retries=5,
                         retry_policy={'interval_start': 5, 'interval_step': 10, 'interval_max': 120})
    return result