# -*- coding: UTF-8 -*-
import sys

sys.path.append('..') # 添加自己指定的搜索路径

from package_db.DBUtils import DBUtils

def main():
  host = '10.10.8.52'
  username = 'zhaobaojue8061'
  password = 'Passw0rdS2_zhaobaojue147'
  port = 30001
  db = 'SENSOR1'
  conn = DBUtils(host, username, password, port, db);
  sql = 'select GOOGLELONGITUDE, GOOGLELATITUDE from MEASURE_POINT where id = "2260";'
  result = conn.select(sql)
  print(result)

if __name__ == '__main__':
  main()