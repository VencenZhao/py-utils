# -*- coding: UTF-8 -*-

import datetime
import os
import sys
sys.path.append('..')
from package_log.LoggerUtils import LoggerUtils
from package_file.FileUtils import FileUtils

def main():
  # now = datetime.datetime.now()
  # et = now.replace(hour=0,minute=0,second=0)
  # targetDate = datetime.datetime.strftime(et, '%Y-%m-%d')
  # fileUtils = FileUtils()
  # log_filename = 'all_%s.log' % targetDate
  # err_filename = 'err_%s.log' % targetDate
  # root_dir = os.path.dirname(os.path.abspath('.'))
  # log_filename = '%s%slog%s%s' % (root_dir, os.sep, os.sep, log_filename)
  # err_filename = '%s%slog%s%s' % (root_dir, os.sep, os.sep, err_filename)
  # fileUtils.createFile(log_filename)
  # fileUtils.createFile(err_filename)
  log = LoggerUtils()
  log.logger.debug('debug')
  log.logger.info('info')
  log.logger.warning('警告')
  log.logger.error('报错')
  log.logger.critical('严重')
  # LoggerUtils(err_filename, level='error').logger.error('error')

if __name__ == '__main__':
  main()