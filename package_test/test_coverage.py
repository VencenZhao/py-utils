# -*- coding: UTF-8 -*-

import json
import sys
sys.path.append('..')

from package_geoserver.Coverage import Coverage

def read_json():
  with open('../data/store1.json','r') as f:
    load_dict = json.load(f)
    return load_dict

def main():
  # 高分卫星2
  # workspace = 'satellite'
  # work = Coverage('8076')
  # workspace = 'gaofen'
  # work = Coverage('8098')
  # for row in read_json():
  #   file_path = row['file_path']
  #   store = row['coverage']
  #   work.addCoveragestore(workspace, store, file_path)
  #   work.addCoverage(workspace, store, store)

  workspace = 'thermal'
  # store1.json
  work = Coverage('8076')
  for row in read_json():
    file_path = row['file_path']
    store = row['coverage']
    work.addCoveragestore(workspace, store, file_path)
    work.addCoverage(workspace, store, store)

if __name__ == '__main__':
  main()