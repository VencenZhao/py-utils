# -*- coding: UTF-8 -*-

import os
import configparser
import sys
sys.path.append('..')

from package_db.DBUtils import DBUtils
from package_file.FileUtils import FileUtils
from package_gdal.GDALUtils import GDALUtils
from package_log.LoggerUtils import LoggerUtils

class BlockLayer(object):
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
    self.log.logger.info('==================> create block_level{} <=================='.format(level))
    self.__initDB__()
    self.__getProvinceList__()
    self.__formatBlockSQL__()
    self.__formatGridSQL__()
    pass

  def __getProvinceList__(self):
    sqlOption = 'PROVINCESQL'
    levelOption = 'LEVEL{}'.format(self.level)
    self.cf.read(self.root_dir + '/config/block.ini', encoding="utf-8")
    sql = self.cf.get(sqlOption, 'sql')
    tableName = self.cf.get(levelOption, 'tableName')
    self.layerName = self.cf.get(levelOption, 'layerName')
    sql = sql.format(tableName)
    self.log.logger.info('create SQL *********** {} **********'.format(sql))
    result = self.conn.select(sql)
    for row in result:
      row['sql'] = []
    self.provinceList = result
    print(self.provinceList)
    # self.provinceList = [{'PROVINCEID': 1}]
    pass

  def __formatGridSQL__(self):
    sqlOption = 'GRIDSQL'
    levelOption = 'LEVEL{}'.format(self.level)
    self.cf.read(self.root_dir + '/config/block.ini', encoding="utf-8")
    sql = self.cf.get(sqlOption, 'sql')
    tableName = self.cf.get(levelOption, 'tableName')
    for row in self.provinceList:
      provinceId = row['PROVINCEID']
      fsql = sql.format(tableName, tableName, provinceId)
      self.log.logger.info('create SQL *********** {} **********'.format(fsql))
      row['sql'].append(fsql)
      # self.sqlList.append(obj)
    pass

  def __formatBlockSQL__(self):
    sqlOption = 'BLOCKSQL'
    levelOption = 'LEVEL{}'.format(self.level)
    self.cf.read(self.root_dir + '/config/block.ini', encoding="utf-8")
    sql = self.cf.get(sqlOption, 'sql')
    tableName = self.cf.get(levelOption, 'tableName')
    for row in self.provinceList:
      provinceId = row['PROVINCEID']
      fsql = sql.format(provinceId, tableName, provinceId)
      self.log.logger.info('create SQL *********** {} **********'.format(fsql))
      row['sql'].append(fsql)
    pass

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
    self.cf.read(self.root_dir + '/config/block.ini', encoding="utf-8")
    properties = self.cf.get(propertyOption, 'properties')
    propertiesList = properties.split(',')
    filePath = self.cf.get(propertyOption, 'filePath')
    filePath = filePath.format(self.root_dir, os.sep, os.sep)
    fileUtils = FileUtils()
    fileUtils.createDir(filePath)
    self.log.logger.info('filePath =============> {}  <==========='.format(filePath))
    self.log.logger.info('layerName =============> {}  <==========='.format(self.layerName))
    self.log.logger.info('isGCJ =============> {}  <==========='.format(self.isGCJ))
    for item in self.provinceList:
      result = []
      provinceId = item['PROVINCEID']
      sqlList = item['sql']
      layerName = self.layerName.format(provinceId)
      for sql in sqlList:
        result1 = self.conn.select(sql)
        for row in result1:
          result.append(row)
      gd = GDALUtils(propertiesList, 0, filePath, layerName, isGCJ = self.isGCJ)
      gd.initShapeFile()
      gd.initShapeFileProperties(result)
    self.log.logger.info('=============> Job Finshed! <===========')

def main():
  pass

if __name__ == '__main__':
  main()
