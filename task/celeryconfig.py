# coding:utf-8

# BROKER_URL = 'amqp://gaunt:gaunt@192.168.0.122:5672'  # 使用RabbitMQ作为消息代理
BROKER_URL = 'redis://:lym123..@192.168.0.122:6379/0'  # 使用Redis作为消息代理

# CELERY_RESULT_BACKEND = 'redis://:lym123..@192.168.0.122:6379/2'  # 把任务结果存在了Redis
CELERY_RESULT_BACKEND = 'mongodb://admin:lym123..@192.168.0.122:27017/'  # 把任务结果存在了Mongodb
CELERY_MONGODB_BACKEND_SETTINGS = {
        "database": "jobs",
        "taskmeta_collection": "stock_taskmeta_collection",
}

# 不需要返回任务状态，即设置以下参数为True
CELERY_IGNORE_RESULT = False

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True

CELERY_TASK_SERIALIZER = 'json'  # 任务序列化和反序列化使用msgpack方案

CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显

CELERY_ACCEPT_CONTENT = ['json', 'msgpack']  # 指定接受的内容类型