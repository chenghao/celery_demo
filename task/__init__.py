#coding:utf-8

# 示例：简单示例
# 启动　Worker 进程 (前台)
# 进入 task 目录,  celery -A celery_task worker -P eventlet -l info
# 使用 eventlet 运行
# 在执行 test.py 中的方法　

# 启动　Worker 进程 (后台 / 守护进程) (类unix)
# 进入 task 目录,  celery multi start w1 -A celery_task -l info --logfile=task.log