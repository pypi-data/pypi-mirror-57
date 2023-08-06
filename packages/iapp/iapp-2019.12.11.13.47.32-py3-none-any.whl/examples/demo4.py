#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-Python.
# @File         : demo
# @Time         : 2019-08-15 10:20
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :
import time
import logging
from datetime import datetime
datetime.now()
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

dic = {}


@scheduler.scheduled_job('cron', second='*/10', next_run_time=None)
def task():
    """更新变量"""
    logging.warning('Tick! The time is: %s' % time.ctime())


scheduler.start()
while 1:
    print(time.ctime())
    print(datetime.now())
    print(datetime.today())

    time.sleep(1)
