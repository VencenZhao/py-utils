# -*- coding: UTF-8 -*-
import sys
sys.path.append('..')

from package_geoserver.Workspace import Workspace

def main():
  workspace = 'hotgridtest'
  work = Workspace('2204')
  # print(work.delWorkspace(workspace))

if __name__ == '__main__':
  main()