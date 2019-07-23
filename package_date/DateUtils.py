# -*- coding: UTF-8 -*-

import datetime

class DateUtils(object):
  def __init__(self):
    self.config = {
      'month': '%Y%m',
      'day': '%Y-%m-%d'
    }
    pass

  def getNowDate(self):
    fmt = self.config['day']
    now = datetime.datetime.now()
    et = now.replace(hour=0,minute=0,second=0)
    targetDate = datetime.datetime.strftime(et, fmt)
    return targetDate

  def getStartDate(self, endDate, delta):
    result = []
    fmt = self.config['day']
    dt = datetime.datetime.strptime(endDate, fmt)
    dt = dt + datetime.timedelta(delta)
    beginDate = dt.strftime(fmt)
    monthList = self.monthRange(beginDate, endDate)
    for i in range(len(monthList)):
      obj = {
        'month': monthList[i]
      }
      if i == 0:
        obj['starttime'] = beginDate
      else:
        tmpTime = '{}-{}-01'.format(monthList[i][0:4], monthList[i][4:6])
        starttime = datetime.datetime.strptime(tmpTime, fmt)
        obj['starttime'] = starttime.strftime(fmt)
      result.append(obj)
    return result

  def dateRange(self, beginDate, endDate):
    print(beginDate)
    dates = []
    fmt = self.config['day']
    dt = datetime.datetime.strptime(beginDate, fmt)
    date = beginDate[:]
    while date <= endDate:
      dates.append(date)
      dt = dt + datetime.timedelta(1)
      date = dt.strftime(fmt)
    return dates

  def monthRange(self, beginDate, endDate):
    monthSet = set()
    for date in self.dateRange(beginDate, endDate):
      monthSet.add(date[0:7].replace('-', ''))
    result = sorted(list(monthSet))
    return result
