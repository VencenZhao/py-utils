# -*- coding: UTF-8 -*-

from package_db.DBUtils import DBUtils

def shapefile_and_friends(path):
    return dict((ext, path + "." + ext) for ext in ['shx', 'shp', 'dbf', 'prj'])

def main():
  # print(shapefile_and_friends('/data/zhaobaojue/gisdata/hotgrid/test_layer'))
  # host = '10.10.8.52'
  # username = 'zhaobaojue8061'
  # password = 'Passw0rdS2_zhaobaojue147'
  # port = 30001
  # db = 'SENSOR1'
  # conn = DBUtils(host, username, password, port, db);
  # sql = 'select GOOGLELONGITUDE, GOOGLELATITUDE from MEASURE_POINT where id = "2260";'
  # result = conn.select(sql)
  # print(result)
  # properties = ['lng', 'lat', 'name', 'address', 'typename', 'minlng', 'minlat', 'maxlng', 'maxlat']
  # length = len(properties)
  # print(properties[length - 4])
  # print(properties[length - 3])
  # print(properties[length - 2])
  # print(properties[length - 1])
  # sql = '''
  #   SELECT
  #     b.LONGITUDE AS lng,
  #     b.LATITUDE AS lat,
  #     a.BLOCK_VALUE AS pm25,
  #     a.LEVEL AS level,
  #     a.PROVINCE_ID AS provinceid,
  #     a.CITY_ID AS cityid,
  #     a.COUNTY_ID AS regionid,
  #     b.TOWN_ID AS townid,
  #     DATE_FORMAT(a.END_TIME, {}) as endtime,
  #     a.VAR_TYPE as vartypeid,
  #     b.longitude_down_left AS minlng,
  #     b.latitude_down_left AS minlat,
  #     b.longitude_up_right AS maxlng,
  #     b.latitude_up_right AS maxlat
  #   FROM
  #     {} a,
  #     T_DICT_BLOCK_BASIC_INFO_{} b
  #   WHERE
  #     a.BLOCK_ID = b.BLOCK_ID
  #   AND a.TIME_TYPE = 24
  #   AND a.DELETE_FLAG = 0
  #   AND a.START_TIME > '{}'
  #   AND a.REGION_LEVEL = {};
  # '''
  # print(sql.count('{}'))
  provinceList = [{'PROVINCEID': 1}, {'PROVINCEID': 2}, {'PROVINCEID': 3}, {'PROVINCEID': 4}, {'PROVINCEID': 197}, {'PROVINCEID': 208}, {'PROVINCEID': 229}, {'PROVINCEID': 296}, {'PROVINCEID': 297}, {'PROVINCEID': 298}, {'PROVINCEID': 299}, {'PROVINCEID': 300}, {'PROVINCEID': 301}, {'PROVINCEID': 302}, {'PROVINCEID': 303}, {'PROVINCEID': 304}, {'PROVINCEID': 306}, {'PROVINCEID': 307}, {'PROVINCEID': 310}, {'PROVINCEID': 311}, {'PROVINCEID': 312}, {'PROVINCEID': 314}, {'PROVINCEID': 315}, {'PROVINCEID': 316}, {'PROVINCEID': 317}, {'PROVINCEID': 318}, {'PROVINCEID': 319}, {'PROVINCEID': 320}, {'PROVINCEID': 321}, {'PROVINCEID': 322}, {'PROVINCEID': 323}]
  sql = '''
  SELECT 
    a.LONGITUDE as lng,
    a.LATITUDE as lat,
    a.STAND_GRIDID as gridid,
    a.BLOCK_ID as blockid,
    a.PROVINCE_ID as provinceid,
    a.CITY_ID as cityid,
    a.COUNTY_ID as countyid,
    b.COUNTY_ID as countyid2,
    1 as type,
    a.LONGITUDE_DOWN_LEFT AS minlng,
    a.LATITUDE_DOWN_LEFT AS minlat,
    a.LONGITUDE_UP_RIGHT AS maxlng,
    a.LATITUDE_UP_RIGHT AS maxlat
  from 
    T_DICT_BLOCK_BASIC_INFO_{} a
  left join 
    T_GRID_CURRENT_HOT_GROUP_REGION b
  ON  a.STAND_GRIDID = b.STAND_GRIDID
  where a.STAND_GRIDID in (
    SELECT STAND_GRIDID FROM {} where PROVINCEID = {}
  );
  '''
  sqlList = []
  for row in provinceList:
    provinceId = row['PROVINCEID']
    a = sql.format(provinceId, 'T_GRID_CURRENT_HOT_GROUP', provinceId)
    sqlList.append(a)
  print(sqlList)

if __name__ == '__main__':
  main()