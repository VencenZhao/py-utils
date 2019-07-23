# -*- coding: UTF-8 -*-
'''
Create on 2019-06-14

@author zhao
'''

import pymysql
import sys
sys.path.append('..')

from package_db.DBInterface import DBInterface
from package_log.LoggerUtils import LoggerUtils

print(DBInterface)

class DBUtils(DBInterface):
  def __init__(self, host = 0, username = 0, passwd = 0, port = 0, db = 0):
    self.host = host
    self.username = username
    self.passwd = passwd
    self.port = port
    self.db = db
    self.log = LoggerUtils()
    self.connect(host = host, username = username, passwd = passwd, port = port, db = db)
    pass

  def connect(self, host, username, passwd, port, db):
    self.log.logger.info('HOST ======================> {}'.format(host))
    self.log.logger.info('USERNAME ======================> {}'.format(username))
    self.log.logger.info('PASSWORD ======================> {}'.format(passwd))
    self.log.logger.info('PORT ======================> {}'.format(port))
    self.log.logger.info('DATABASE ======================> {}'.format(db))
    conn = self.mysqlConnect(host = host, user = username, passwd = passwd, port = port, db = db)
    self.conn = conn

  def select(self, sql):
    result = None
    try:
      cursor = self.conn.cursor()
      result = cursor.execute(sql)
      result = cursor.fetchall()
    except Exception as err:
      print(err)
      self.connect(self.host, self.username, self.passwd, self.host, self.db)
      cursor = self.conn.cursor()
      result = cursor.execute(sql)
      result = cursor.fetchall()
      pass
    return result

  def execute(self, sql):
    self.log.logger.info('SQL ======================> {}'.format(sql))
    cursor = self.conn.cursor()
    cursor.execute(sql)
    pass

  def disclose(self):
    self.conn.close()

  def mysqlConnect(self, host, user, passwd, port, db):
    conn = pymysql.connect(host = host, port = port, user = user, password = passwd, db = db, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)
    return conn
    pass
