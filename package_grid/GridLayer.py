# -*- coding: UTF-8 -*-

import os
import configparser
import sys
sys.path.append('..')

from package_db.DBUtils import DBUtils
from package_file.FileUtils import FileUtils
from package_gdal.GDALUtils import GDALUtils
from package_log.LoggerUtils import LoggerUtils

class GridLayer(object):
  '''
  @params level 热点网格级别 0 部级 1 省级 2 市级 3 区县级
  @params dbType 访问数据库账号类型 0 生产 1 个人 default 0
  @params isGCJ 是否为高德坐标系 default False
  '''
  def __init__(self, level, dbType = 0, isGCJ = False):
    self.cf = configparser.ConfigParser()
    self.log = LoggerUtils()
    self.level = level
    self.dbType = dbType
    self.isGCJ = isGCJ
    self.root_dir = os.path.dirname(os.path.abspath('.'))
    self.log.logger.info('=============> Job Started! <===========')
    self.log.logger.info('==================> create grid_level{} <=================='.format(level))
    self.__formatSQL__()
    self.__initDB__()
    pass

  def __formatSQL__(self):
    sqlOption = 'SQL'
    levelOption = 'LEVEL{}'.format(self.level)
    self.cf.read(self.root_dir + '/config/grid.ini', encoding="utf-8")
    sql = self.cf.get(sqlOption, 'sql')
    tableName = self.cf.get(levelOption, 'tableName')
    self.layerName = self.cf.get(levelOption, 'layerName')
    self.sql = sql.format(tableName)
    self.log.logger.info('create SQL *********** {} **********'.format(self.sql))

  def __initDB__(self):
    dataOption = 'SENSOR1-m1'
    if self.dbType == 1:
      dataOption = 'LOCAL_SENSOR1-m1'
    self.cf.read(self.root_dir + '/config/database.ini', encoding="utf-8")
    host = self.cf.get(dataOption, 'host')
    username = self.cf.get(dataOption, 'username')
    password = self.cf.get(dataOption, 'password')
    port = int(self.cf.get(dataOption, 'port'))
    db = self.cf.get(dataOption, 'database')
    # print(host)
    self.conn = DBUtils(host, username, password, port, db)

  def createLayer(self):
    propertyOption = 'PROPERTY'
    self.cf.read(self.root_dir + '/config/grid.ini', encoding="utf-8")
    properties = self.cf.get(propertyOption, 'properties')
    propertiesList = properties.split(',')
    filePath = self.cf.get(propertyOption, 'filePath')
    filePath = filePath.format(self.root_dir, os.sep, os.sep)
    fileUtils = FileUtils()
    fileUtils.createDir(filePath)
    self.log.logger.info('filePath =============> {}  <==========='.format(filePath))
    self.log.logger.info('layerName =============> {}  <==========='.format(self.layerName))
    self.log.logger.info('isGCJ =============> {}  <==========='.format(self.isGCJ))
    
    result = self.conn.select(self.sql)
    gd = GDALUtils(propertiesList, 0, filePath, self.layerName, isGCJ = self.isGCJ)
    gd.initShapeFile()
    gd.initShapeFileProperties(result)
    self.log.logger.info('=============> Job Finshed! <===========')

def main():
  root_dir = os.path.dirname(os.path.abspath('.'))
  dataOption = 'SQL'
  cf = configparser.ConfigParser()
  cf.read(root_dir + '/config/grid.ini')
  sql = cf.get(dataOption, 'sql')
  print(sql.format('tableName'))

if __name__ == '__main__':
  main()

