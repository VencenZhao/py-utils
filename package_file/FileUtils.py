# -*- coding: UTF-8 -*-

import os

class FileUtils(object):
  def __init__(self):
    pass

  def createDir(self, path):
    if not os.path.isdir(path):
      os.makedirs(path)

  def createFile(self, filename):
    path = filename[0:filename.rfind(os.sep)]
    self.createDir(path)
    if not os.path.isfile(filename):
      #创建并打开一个新文件
      fd = open(filename, mode = 'w', encoding = 'utf-8')
      fd.close()