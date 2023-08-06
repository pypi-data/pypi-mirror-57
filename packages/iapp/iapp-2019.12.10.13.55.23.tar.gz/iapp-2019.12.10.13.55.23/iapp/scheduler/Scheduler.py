#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-App.
# @File         : Scheduler
# @Time         : 2019-12-10 13:50
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 
from apscheduler.schedulers.background import BackgroundScheduler


class Scheduler(object):
    """learning: https://blog.csdn.net/somezz/article/details/83104368"""

    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def add_job(self, func, trigger='interval', **trigger_args):
        assert callable(func), "TODO: callable function"

        self.scheduler.add_job(func, trigger, **trigger_args)

    def start(self):
        self.scheduler.start()


if __name__ == '__main__':
    def task1():
        import logging
        import time
        logging.warning(f'Task1: {time.ctime()}')


    def task2():
        import logging
        import time
        logging.warning(f'Task2: {time.ctime()}')


    scheduler = Scheduler()
    scheduler.add_job(task1, 'interval', seconds=3)
    scheduler.add_job(task2, 'interval', seconds=10)
    scheduler.start()

    while 1:
        pass
