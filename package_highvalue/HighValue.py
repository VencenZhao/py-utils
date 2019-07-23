# -*- conding: UTF-8 -*-

import os
import configparser
import sys
sys.path.append('..')

from package_date.DateUtils import DateUtils
from package_db.DBUtils import DBUtils
from package_file.FileUtils import FileUtils
from package_gdal.GDALUtils import GDALUtils
from package_log.LoggerUtils import LoggerUtils

class HighValue(object):
  '''
  @params dbType 访问数据库账号类型 0 生产 1 个人 default 0
  @params timeType 时间类型 daily weekly monthly
  @params regionType BEIJING 北京 JINGWAIV2 京外v2 JINGWAIV1 京外v1
  @params isGCJ 是否为高德坐标系 default False
  '''
  def __init__(self, dbType, timeType, regionType, isGCJ = False):
    self.cf = configparser.ConfigParser()
    self.log = LoggerUtils()
    self.dbType = dbType
    self.timeType = timeType
    self.regionType = regionType
    self.isGCJ = isGCJ
    self.result = []
    self.root_dir = os.path.dirname(os.path.abspath('.'))
    self.log.logger.info('=============> Job Started! <===========')
    # self.log.logger.info('==================> create highvaluebeijing_level{} <=================='.format(level))
    self.__formatSQL__()
    self.__initDB__()
    self.__getData__()
    pass
  '''
    format SQL 
    Read the '.ini' config files 
  '''
  def __formatSQL__(self):
    regionOption = self.regionType
    self.cf.read(self.root_dir + '/config/{}.ini'.format(self.timeType), encoding="utf-8")
    self.properties = self.cf.get(regionOption, 'properties')
    self.provinces = self.cf.get(regionOption, 'provinces')
    isMonthly = bool(int(self.cf.get(regionOption, 'isMonthly')))
    self.needDelta = bool(int(self.cf.get(regionOption, 'needDelta')))
    self.layerName = self.cf.get(regionOption, 'layerName')
    self.tableNames = self.cf.get(regionOption, 'tableName')
    timeDetla = int(self.cf.get('PROPERTY', 'timeDetla'))
    self.sql = self.cf.get(regionOption, 'sql')
    # print(self.sql)
    dateUtils = DateUtils()
    endDate = dateUtils.getNowDate()
    timeList = dateUtils.getStartDate(endDate, timeDetla)
    # print(timeList)
    self.__setSqlList__(isMonthly, timeList)

  def __setSqlList__(self, isMonthly, timeList):
    print(isMonthly)
    self.sqlList = []
    if isMonthly:
      for item in timeList:
        for tableName in self.tableNames.split(','):
          tmpTableName = tableName + '_' + item['month']
          tmpSql = self.sql.format("'%Y-%m-%d'", tmpTableName, item['starttime'])
          self.log.logger.info('create SQL *********** {} **********'.format(tmpSql))
          self.sqlList.append(tmpSql)
    else:
      for p in self.provinces.split(','):
        for tableName in self.tableNames.split(','):
          tmpSql = self.sql.format("'%Y-%m-%d'", tableName, p, timeList[0]['starttime'])
          self.log.logger.info('create SQL *********** {} **********'.format(tmpSql))
          self.sqlList.append(tmpSql)

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
    self.conn = DBUtils(host, username, password, port, db)

  def __getData__(self):
    for sql in self.sqlList:
      result = self.conn.select(sql)
      self.result.extend(result)
  
  def createLayer(self):
    propertyOption = 'PROPERTY'
    self.cf.read(self.root_dir + '/config/{}.ini'.format(self.timeType), encoding="utf-8")
    propertiesList = self.properties.split(',')
    filePath = self.cf.get(propertyOption, 'filePath')
    filePath = filePath.format(self.root_dir, os.sep, os.sep, os.sep)
    fileUtils = FileUtils()
    fileUtils.createDir(filePath)
    self.log.logger.info('filePath =============> {}  <==========='.format(filePath))
    self.log.logger.info('layerName =============> {}  <==========='.format(self.layerName))
    self.log.logger.info('isGCJ =============> {}  <==========='.format(self.isGCJ))
    gd = GDALUtils(propertiesList, 0, filePath, self.layerName, needDelta = self.needDelta, isGCJ = self.isGCJ)
    gd.initShapeFile()
    gd.initShapeFileProperties(self.result)
    self.log.logger.info('=============> Job Finshed! <===========')
