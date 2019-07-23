# -*- coding: UTF-8 -*-

import sys
sys.path.append('..')

from package_block.BlockLayer import BlockLayer

def main():
  # (0, 1, False) 部级WGS84坐标 
  # (0, 1, True) 部级gcj坐标 
  # (1, 1, False) 省级WGS84坐标 
  # (1, 1, True) 省级gcj坐标 
  # (2, 1, False) 市级WGS84坐标 
  # (2, 1, True) 市级gcj坐标 
  # (3, 1, False) 区县级WGS84坐标 
  # (3, 1, True) 区县级gcj坐标 
  bl = BlockLayer(0, 1, False)
  # print(bl.provinceList)
  bl.createLayer()
  bl = BlockLayer(0, 1, True)
  # print(bl.provinceList)
  bl.createLayer()
  bl = BlockLayer(2, 1, False)
  # print(bl.provinceList)
  bl.createLayer()
  bl = BlockLayer(2, 1, True)
  # print(bl.provinceList)
  bl.createLayer()
  pass

if __name__ == '__main__':
  # print(sys.argv[1:])
  main()