# -*- coding: UTF-8 -*-

import requests
import json
import sys
sys.path.append('..')

from package_geoserver.GeoserverInterface import GeoserverInterface
'''
GeoTIFF图层发布工具类
extends GeoserverInterface
'''
class Coverage(GeoserverInterface):
  '''
  @params host geoserver服务器ip
  @params port geoserver服务器端口
  @params username 用户名 default admin
  @params password 密码 default geoserver
  '''
  def __init__(self, server):
    super().__init__(server)
    self.url_prefix = 'http://{}:{}/geoserver/rest/'.format(self.host, self.port)
    pass

  '''
  获取工作空间下的 coverages 列表
  @params workspace 工作空间
  '''
  def getCoverages(self, workspace):
    myurl = '{}workspaces/{}/coverages'.format(self.url_prefix, workspace)
    headers = {'Content-type': 'application/json','Accept': 'application/json'}
    resp = requests.get(myurl, auth=(self.username, self.password), headers = headers)
    code = resp.status_code
    print('Result ==========> %d' % code)
    coverages = resp.json()['coverages']['coverage']
    return coverages

  def getCoveragestore(self, workspace, store):
    myurl = '{}workspaces/{}/coveragestores/{}/coverages'.format(self.url_prefix, workspace, store)
    headers = {'Content-type': 'application/json','Accept': 'application/json'}
    resp = requests.get(myurl, auth=(self.username, self.password), headers = headers)
    code = resp.status_code
    print('Result ==========> %d' % code)
    coverages = resp.json()
    return coverages
  '''
  判断是否store是否已存在
  @param workspace
  @param store
  @returns Boolean 
  '''
  def __hasCoveragestore__(self, workspace, store):
    myurl = '{}workspaces/{}/coveragestores/{}/coverages'.format(self.url_prefix, workspace, store)
    headers = {'Content-type': 'application/json','Accept': 'application/json'}
    resp = requests.get(myurl, auth=(self.username, self.password), headers = headers)
    code = resp.status_code
    if code == 200:
      return True
    else:
      return False
  '''
  @params workspace 工作区名称
  @params store store名称
  @params file_path tiff文件路径
  '''
  def addCoveragestore(self, workspace, store, file_path):
    if self.__hasCoveragestore__(workspace, store):
      print('======================> workspace: {}, store: {} has already exist!'.format(workspace, store))
      return
    myurl = '{}workspaces/{}/coveragestores'.format(self.url_prefix, workspace)
    headers = {'Content-type': 'text/xml','Accept': 'text/xml'}
    payload = '''
      <coverageStore>
        <name>%s</name>
        <type>GeoTIFF</type>
        <enabled>true</enabled>
        <workspace>
            <name>%s</name>
        </workspace>
        <__default>false</__default>
        <url>file:%s</url>
      </coverageStore>
    ''' % (store, workspace, file_path)
    print(payload)
    resp = requests.post(myurl, auth=(self.username, self.password), data = payload, headers = headers)
    print(resp.status_code)
  
  def addCoverage(self, workspace, store, coverage):
    myurl = '{}workspaces/{}/coveragestores/{}/coverages'.format(self.url_prefix, workspace, store)
    headers = {'Content-type': 'text/xml','Accept': 'text/xml'}
    payload = '''
      <coverage>
        <name>%s</name>
        <namespace>
          <name>%s</name>
        </namespace>
        <title>%s</title>
        <description>%s</description>
        <keywords>
          <string>WCS</string>
          <string>WorldImage</string>
          <string>%s</string>
        </keywords>
        <srs>EPSG:4326</srs>
        <store class="coverageStore">
          <name>%s</name>
        </store>
        <requestSRS>
          <string>EPSG:4326</string>
        </requestSRS>
        <responseSRS>
          <string>EPSG:4326</string>
        </responseSRS>
      </coverage>
    ''' % (coverage, workspace, coverage, coverage, coverage, store)
    
    resp = requests.post(myurl, auth=(self.username, self.password), data = payload, headers = headers)
    print('Result: %s' % resp.text)
    print(resp.status_code)

