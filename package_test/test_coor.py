# -*- coding: UTF-8 -*-

import sys
sys.path.append('..')

from package_coor.CoorUtils import CoorUtils

def main():
  coor = CoorUtils()
  # 39.9078433959,116.3976144791
  lng = 116.395645
  lat = 40.229986
  print(coor.wgs84_to_gcj02(lng, lat))
  # output [116.40192936929614, 40.231413793979364]

if __name__ == '__main__':
  main()
