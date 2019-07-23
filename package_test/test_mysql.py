# -*- coding: UTF-8 -*-

import configparser
import os
import sys
sys.path.append('..')

from package_db.DBUtils import DBUtils
from package_gdal.GDALUtils import GDALUtils

def main():
  root_dir = os.path.dirname(os.path.abspath('.'))
  dataOption = 'LOCAL_SENSOR1-m1'
  cf = configparser.ConfigParser()
  cf.read(root_dir + '/config/database.ini')
  host = cf.get(dataOption, 'host')
  username = cf.get(dataOption, 'username')
  password = cf.get(dataOption, 'password')
  port = int(cf.get(dataOption, 'port'))
  db = cf.get(dataOption, 'database')
  # print(host)
  conn = DBUtils(host, username, password, port, db)
  sql = '''
    SELECT 
      a.LONGITUDE AS lng,
      a.LATITUDE AS lat,
      a.STAND_GRIDID AS stand_gridid,
      a.PROVINCEID AS provinceid,
      a.CITYID AS cityid,
      a.COUNTYID AS countyid,
      b.county_id AS countyid2,
      a.LONGITUDE_DOWN_LEFT AS minlng,
      a.LATITUDE_DOWN_LEFT AS minlat,
      a.LONGITUDE_UP_RIGHT AS maxlng,
      a.LATITUDE_UP_RIGHT AS maxlat
    FROM 
      T_GRID_CURRENT_HOT_GROUP a
    LEFT JOIN 
      T_GRID_CURRENT_HOT_GROUP_REGION b
    ON  a.STAND_GRIDID = b.STAND_GRIDID 
    WHERE SELECTED_FLAG = 1
    AND a.CITYID = 1;
  '''

  '''
    SELECT 
      GOOGLELONGITUDE as lng, 
      GOOGLELATITUDE as lat,
      NAME as name,
      ADRESS as address,
      TYPENAME as typename
    FROM
      MEASURE_POINT 
    WHERE id IN ('2260', '115', '116', '117', '118');
  '''
  result = conn.select(sql)
  # gd = GDALUtils(['lng', 'lat', 'name', 'address', 'typename'], 0, './', 'polygonLayer', True)
  gd = GDALUtils(['lng', 'lat', 'stand_gridid', 'provinceid', 'cityid', 'countyid', 'countyid2'], 0, './', 'polygonWithMinMaxLayer', isGCJ = False)
  gd.initShapeFile()
  gd.initShapeFileProperties(result)
  print(result)

if __name__ == '__main__':
  main()
