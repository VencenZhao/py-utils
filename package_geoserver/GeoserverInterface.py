# -*- coding: UTF-8 -*-

import os
import configparser

class GeoserverInterface(object):
  def __init__(self, server):
    root_dir = os.path.dirname(os.path.abspath('.'))
    cf = configparser.ConfigParser()
    serverOption = server
    cf.read(root_dir + '/config/geoserver.ini', encoding="utf-8")
    self.host = cf.get(serverOption, 'host')
    self.port = cf.get(serverOption, 'port')
    self.username = cf.get(serverOption, 'username')
    self.password = cf.get(serverOption, 'password')
    print(self)
    pass
