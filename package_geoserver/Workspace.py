# -*- coding: UTF-8 -*-

import requests
import json
import sys
sys.path.append('..')

from package_geoserver.GeoserverInterface import GeoserverInterface
'''
工作区工具类
extends GeoserverInterface
'''
class Workspace(GeoserverInterface):
  def __init__(self, server):
    super().__init__(server)
    self.url_prefix = 'http://{}:{}/geoserver/rest/'.format(self.host, self.port)
    print(self.url_prefix)
    pass

  def getWorkspaces(self):
    myurl = '{}workspaces'.format(self.url_prefix)
    headers = {'Content-type': 'application/json','Accept': 'application/json'}
    resp = requests.get(myurl, auth=(self.username, self.password), headers = headers)
    code = resp.status_code
    print('Result ==========> %d' % code)
    workspaces = resp.json()['workspaces']['workspace']
    return workspaces

  def hasWorkspace(self, workspace):
    myurl = '{}workspaces/{}'.format(self.url_prefix, workspace)
    # headers = {'Content-type': 'application/json','Accept': 'application/json'}
    headers = {'Content-type': 'text/xml','Accept': 'text/xml'}
    resp = requests.get(myurl, auth=(self.username, self.password), headers = headers)
    code = resp.status_code
    print('Result ==========> %d' % code)
    print(resp.text)
    if code == 200:
      return True
    else:
      return False

  def addWorkspace(self, workspace):
    myurl = '{}workspaces'.format(self.url_prefix)
    headers = {'Content-type': 'text/xml','Accept': 'text/xml'}
    payload = '''
      <workspace>
        <name>{}</name>
      </workspace>
    '''.format(workspace)
    print(payload)
    resp = requests.post(myurl, auth=(self.username, self.password), data = payload, headers = headers)
    code = resp.status_code
    print(resp)
    if code == 201:
      return True
    else:
      return False

  def delWorkspace(self, workspace):
    myurl = '{}workspaces/{}'.format(self.url_prefix, workspace)
    headers = {'Content-type': 'application/json','Accept': 'application/json'}
    resp = requests.delete(myurl, auth=(self.username, self.password), headers = headers)
    code = resp.status_code
    if code == 200:
      return True
    else:
      return False
