# coding:utf-8

# 示例：指定队列
# 启动　Worker 进程
# 进入 queues 目录,  celery -A celery_queues worker -P eventlet  -l info
# 使用 eventlet 运行, 启动所有队列
# 在执行 test.py 中的方法

# 只启动 web_tasks 队列： celery -A celery_queues worker -P eventlet  -l info -Q web_tasks