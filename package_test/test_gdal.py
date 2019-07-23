# -*- coding: UTF-8 -*-

import sys
sys.path.append('..') # 添加自己指定的搜索路径

from package_gdal.GDALUtils import GDALUtils

# print(GDALUtils)

def main():
  gd = GDALUtils(['city', 'region'], 0, './', 'testLayer')
  print(gd.oLayer)
  print(gd.oDS)

if __name__ == '__main__':
  main()