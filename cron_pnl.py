# -*- coding: utf-8 -*-

from crontab import CronTab
from datetime import datetime, timedelta
import logging
import math
from multiprocessing import Pool
import time
from pytz import timezone
import subprocess
import os
import sys
 
class JobConfig(object):
  
  def __init__(self, crontab, job):
 
    self._crontab = crontab
    self.job = job
 
  def schedule(self):
 
    crontab = self._crontab
    return datetime.now() + timedelta(seconds=math.ceil(crontab.next(default_utc=False)))
 
  def next(self):
 
    crontab = self._crontab
    return math.ceil(crontab.next(default_utc=False))
 
def job_controller(jobConfig):
 
  logging.info("->- 処理を開始しました。")
 
  while True:
 
    try:
 
      # 次実行日時を表示
      logging.info("-?- 次回実行日時\tschedule:%s" %
        jobConfig.schedule().strftime("%Y-%m-%d %H:%M:%S"))
 
      # 次実行時刻まで待機
      time.sleep(jobConfig.next())
 
      logging.info("-!> 処理を実行します。")
 
      # 処理を実行する。
      jobConfig.job()
 
      logging.info("-!< 処理を実行しました。")
 
    except KeyboardInterrupt:
      break
 
  logging.info("-<- 処理を終了終了しました。")
 
 
def job1():
    
  logging.debug("save")
  
  subprocess.Popen(['python3', 'pyliquid_pnl.py','save'])
 
 
def job2():
  logging.debug("send_discord")
  
  subprocess.Popen(['python3', 'pyliquid_pnl.py','send_discord'])
 
 
def main():
  
  logging.basicConfig(level=logging.DEBUG,
    format="time:%(asctime)s.%(msecs)03d\tprocess:%(process)d" +
      "\tmessage:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")
 
  # 毎分実行設定
  jobConfigs = [
 
    # 処理1を2分毎に実行する。
    JobConfig(CronTab("*/2 * * * *"), job1),
 
    # 処理2を23時45分に実行する。
    JobConfig(CronTab("45 23 * * *"), job2)
  ]
 
  # 処理を並列に実行
  p = Pool(len(jobConfigs))
  try:
    p.map(job_controller, jobConfigs)
  except KeyboardInterrupt:
    pass
 
 
if __name__ == "__main__":
 
  main()