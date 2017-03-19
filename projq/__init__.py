# coding:utf-8

# 示例：指定队列
# 启动　Worker 进程
# 进入 celery_demo 目录,  celery -A projq.projq_celery worker -P gevent  -l info
# 使用 gevent 运行, 启动所有队列
# 在执行 test.py 中的方法