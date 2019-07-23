# -*- coding: UTF-8 -*-

import configparser
import os
import sys
sys.path.append('..')

from package_date.DateUtils import DateUtils

def main():
  root_dir = os.path.dirname(os.path.abspath('.'))
  regionLevel = 2
  regionOption = 'JINGWAIV1'
  cf = configparser.ConfigParser()
  cf.read(root_dir + '/config/daily.ini', encoding="utf-8")
  # properties = cf.get(regionOption, 'properties')
  # isMonthly = int(cf.get(regionOption, 'isMonthly'))
  # layerName = cf.get(regionOption, 'layerName').format(regionLevel)
  # tableName = cf.get(regionOption, 'tableName{}'.format(regionLevel))
  # sql = cf.get(regionOption, 'sql')

  cf.set(regionOption, 'provinceList', '1,2,3,4,5')  # 写入中文
  cf.write(open(root_dir + '/config/daily.ini', "r+", encoding="utf-8"))  # r+模
  dateUtils = DateUtils()
  result = dateUtils.getStartDate('2019-06-18', -2)
  # sqlList = []
  # if isMonthly == 1:
  #   for item in result:
  #     print(item)
  #     tmpTableName = tableName + '_' + item['month']
  #     tmpSql = sql.format("'%Y-%m-%d'",tmpTableName, item['starttime'], regionLevel)
      # print(tmpSql)
  #     sqlList.append(tmpSql)
  # print(layerName)
  # print(tableName)
  # monthList = dateUtils.monthRange(beginDate, endDate)
  print(result)

if __name__ == '__main__':
  main()
