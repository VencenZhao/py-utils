# -*- coding: UTF-8 -*-
'''
  Create on 2019-06-14
  @about GDAL functions
  @author zhao
'''

from osgeo import gdal, gdalnumeric
from osgeo import ogr, osr
import os
import sys
sys.path.append('..')

from package_coor.CoorUtils import CoorUtils
from package_log.LoggerUtils import LoggerUtils

'''
utils for gdal
@params properties shapefile中属性 default ['lng', 'lat']
@params fileType shapefile元素类型  0 多边形， 1 点  default 0
@params filePath 生成shapefile位置 default ./ 当前文件夹
@params layerName 生成shapefile名称 default LayerName
@params needDelta 是否需要通过偏移来得到四角经纬度 fileType为0时生效 defalut False
@params isGCJ 是否为gcj02 坐标系  default False
'''
class GDALUtils():
  def __init__(self, properties = ['lng', 'lat'], fileType = 0, filePath = './', layerName = 'layerName', needDelta = False, isGCJ = False):
    self.properties = properties
    self.fileType = fileType
    self.filePath = filePath
    self.layerName = layerName
    self.wekType = self.__wkbType__()
    self.delta = 0.006265664160405/2
    self.needDelta = needDelta
    self.isGCJ = isGCJ
    self.log = LoggerUtils()
    if self.isGCJ:
      self.coor = CoorUtils()
      self.layerName = layerName + '_gcj'
    # self.initShapeFile(self.properties, self.filePath, self.layerName)
    # coor = CoorUtils()
    # 39.9078433959,116.3976144791
    # lng = 116.395645
    # lat = 40.229986
    # print(coor.wgs84_to_gcj02(lng, lat))
    pass

  '''
  @params fileType shapefile元素类型 0:多边形 1:点
  @return webType 
  '''
  def __wkbType__(self):
    wkbType = ogr.wkbPolygon
    if self.fileType == 0:
      wkbType = ogr.wkbPolygon
    elif self.fileType == 1:
      wkbType = ogr.wkbPoint
    return wkbType

  def initShapeFileProperties(self, result):
    for row in result:
      # self.log.logger.info(row)
      oFeatureRectangle = ogr.Feature(self.oDefn)
      ring = ogr.Geometry(ogr.wkbLinearRing)
      if self.fileType == 0:
        self.__polygon__(row, ring, oFeatureRectangle)
      elif self.fileType == 1:
        self.__point__(row, ring, oFeatureRectangle)

  def __point__(self, row, ring, oFeatureRectangle):
    for i in range(len(self.properties)):
      value = row[self.properties[i]]
      oFeatureRectangle.SetField(i, value)

    lng = float(row[self.properties[0]])
    lat = float(row[self.properties[1]])
    if self.isGCJ:
      tmpLonAndLat = self.coor.wgs84_to_gcj02(lng, lat)
      lng = tmpLonAndLat[0]
      lat = tmpLonAndLat[1]
    poly = ogr.Geometry(self.wekType)
    poly.AddPoint(lng, lat)
    oFeatureRectangle.SetGeometry(poly)
    self.oLayer.CreateFeature(oFeatureRectangle)

  def __polygon__(self, row, ring, oFeatureRectangle):
    for i in range(len(self.properties)):
      value = row[self.properties[i]]
      oFeatureRectangle.SetField(i, str(value))
    
    ring = self.__getMinMaxLngLat__(row, ring)
    poly = ogr.Geometry(self.wekType)
    poly.AddGeometry(ring)
    oFeatureRectangle.SetGeometry(poly)
    self.oLayer.CreateFeature(oFeatureRectangle)

  def __getMinMaxLngLat__(self, row, ring):
    delta = self.delta
    lng = float(row[self.properties[0]])
    lat = float(row[self.properties[1]])
    if self.needDelta:
      minlng = lng - delta
      minlat = lat - delta
      maxlng = lng + delta
      maxlat = lat + delta
    else:
      minlng = float(row['minlng'])
      minlat = float(row['minlat'])
      maxlng = float(row['maxlng'])
      maxlat = float(row['maxlat'])
    if self.isGCJ:
      tmpLonAndLat1 = self.coor.wgs84_to_gcj02(minlng, minlat)
      minlng = tmpLonAndLat1[0]
      minlat = tmpLonAndLat1[1]
      tmpLonAndLat2 = self.coor.wgs84_to_gcj02(maxlng, maxlat)
      maxlng = tmpLonAndLat2[0]
      maxlat = tmpLonAndLat2[1]
    ring.AddPoint(minlng, minlat)
    ring.AddPoint(maxlng, minlat)
    ring.AddPoint(maxlng, maxlat)
    ring.AddPoint(minlng, maxlat)
    return ring

  def initShapeFile(self):
    properties = self.properties
    filePath = self.filePath
    layerName = self.layerName
    # 为了支持中文路径，请添加下面这句代码
    gdal.SetConfigOption('GDAL_FILENAME_IS_UTF8', 'NO')
    # 为了使属性表字段支持中文，请添加下面这句
    gdal.SetConfigOption('SHAPE_ENCODING', '')
    strVectorFile = filePath
    # 注册所有的驱动
    ogr.RegisterAll()
    # 创建数据，这里以创建ESRI的shp文件为例
    strDriverName = 'ESRI Shapefile'    
    # 创建驱动
    oDriver = ogr.GetDriverByName(strDriverName)
    # 创建数据源
    oDS = oDriver.CreateDataSource(strVectorFile)
    # 创建图层，创建一个多边形图层，这里没有指定空间参考，如果需要的话，需要在这里进行指定
    papszLCO = ['EPSG:4326']
    srsRef = osr.SpatialReference()
    srsRef.ImportFromEPSG(4326)
    oLayer = oDS.GetLayerByName(layerName)
    if oLayer != None:
      oDS.DeleteLayer(layerName)
    oLayer = oDS.CreateLayer(layerName, srsRef, self.wekType, papszLCO)
    oDefn = oLayer.GetLayerDefn()
    if oLayer == None:
      print("图层创建失败！\n")
      return
    # 下面创建属性表
    for p in properties:
      oFieldID = ogr.FieldDefn(p, ogr.OFTString)
      oLayer.CreateField(oFieldID, 1)
      pass
    self.oLayer = oLayer
    self.oDS = oDS
    self.oDefn = oDefn
