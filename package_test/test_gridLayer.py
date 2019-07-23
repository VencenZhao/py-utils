# -*- coding: UTF-8 -*-

import sys
sys.path.append('..')

from package_grid.GridLayer import GridLayer

def main(args):
  # (0, 1, False) 部级WGS84坐标 
  # (0, 1, True) 部级gcj坐标 
  # (1, 1, False) 省级WGS84坐标 
  # (1, 1, True) 省级gcj坐标 
  # (2, 1, False) 市级WGS84坐标 
  # (2, 1, True) 市级gcj坐标 
  # (3, 1, False) 区县级WGS84坐标 
  # (3, 1, True) 区县级gcj坐标 
  gl = GridLayer(int(args[0]), 1, bool(int(args[1])))
  gl.createLayer()
  pass

if __name__ == '__main__':
  # print(sys.argv[1:])
  main(sys.argv[1:])