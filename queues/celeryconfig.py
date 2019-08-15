# coding:utf-8

from kombu import Queue

BROKER_URL = 'amqp://gaunt:gaunt@192.168.0.122:5672'  # 使用RabbitMQ作为消息代理

CELERY_RESULT_BACKEND = 'redis://:lym123..@192.168.0.122:6379/2'  # 把任务结果存在了Redis
# 不需要返回任务状态，即设置以下参数为True
CELERY_IGNORE_RESULT = False

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True

CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化和反序列化使用msgpack方案

CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显

CELERY_ACCEPT_CONTENT = ['json', 'msgpack']  # 指定接受的内容类型

############################################################################################################
CELERY_QUEUES = (  # 定义任务队列

    Queue('default', routing_key='task.#'),  # 路由键以“task.”开头的消息都进default队列

    Queue('web_tasks', routing_key='web.#'),  # 路由键以“web.”开头的消息都进web_tasks队列

)

CELERY_DEFAULT_EXCHANGE = 'tasks'  # 默认的交换机名字为tasks

CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'  # 默认的交换类型是topic

CELERY_DEFAULT_ROUTING_KEY = 'task.default'  # 默认的路由键是task.default，这个路由键符合上面的default队列