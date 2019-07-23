# -*- coding: UTF-8 -*-
'''
  Create on 2019-06-15
  @about Log functions
  @author zhao
'''

import datetime
import os
import logging
from logging import handlers, config
import sys 
sys.path.append('..')
from package_file.FileUtils import FileUtils

class LoggerUtils(object):
  # 定义三种日志输出格式 开始
  standard_format = '[%(asctime) -s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                    '[%(levelname)s][%(message)s]'

  simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

  id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

  # 定义日志输出格式 结束

  now = datetime.datetime.now()
  et = now.replace(hour=0,minute=0,second=0)
  targetDate = datetime.datetime.strftime(et, '%Y-%m-%d')
  fileUtils = FileUtils()
  log_filename = 'log_%s.log' % targetDate
  root_dir = os.path.dirname(os.path.abspath('.'))
  log_filename = '%s%slog%s%s' % (root_dir, os.sep, os.sep, log_filename)
  fileUtils.createFile(log_filename)

  # log配置字典
  LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
      'standard': {
        'format': standard_format,
        'datefmt': '%Y-%m-%d %H:%M:%S',
      },
      'simple': {
        'format': simple_format
      },
    },
    'filters': {},
    'handlers': {
      'console': {
        'level': 'DEBUG',
        'class': 'logging.StreamHandler',  # 打印到屏幕
        'formatter': 'simple'
      },
      'default': {
        'level': 'DEBUG',
        'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
        'filename': log_filename,  # 日志文件
        'maxBytes': 1024*1024*5,  # 日志大小 5M
        'backupCount': 5,
        'formatter': 'standard',
        'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
      },
    },
    'loggers': {
      '': {
        'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
        'level': 'DEBUG',
        'propagate': True,  # 向上（更高level的logger）传递
      },
    },
  }
  
  # 日志级别关系映射
  # level_relations = {
  #   'debug':logging.DEBUG,
  #   'info':logging.INFO,
  #   'warning':logging.WARNING,
  #   'error':logging.ERROR,
  #   'crit':logging.CRITICAL
  # } 

  # def __init__(self, filename, level='info', when='D', backCount=3, fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
  #   self.logger = logging.getLogger(filename)
    # format_str = logging.Formatter(fmt)#设置日志格式
    # self.logger.setLevel(self.level_relations.get(level))#设置日志级别
    # sh = logging.StreamHandler()#往屏幕上输出
    # sh.setFormatter(format_str) #设置屏幕上显示的格式
    # th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
    # #实例化TimedRotatingFileHandler
    # #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
    # # S 秒
    # # M 分
    # # H 小时、
    # # D 天、
    # # W 每星期（interval==0时代表星期一）
    # # midnight 每天凌晨
    # th.setFormatter(format_str)#设置文件里写入的格式
    # self.logger.addHandler(sh) #把对象加到logger里
    # self.logger.addHandler(th)
  def __init__(self):
    config.dictConfig(self.LOGGING_DIC)  # 导入上面定义的配置
    self.logger = logging.getLogger(self.log_filename)

if __name__ == '__main__':
  log = LoggerUtils()
  log.logger.debug('debug')
  log.logger.info('info')
  log.logger.warning('警告')
  log.logger.error('报错')
  log.logger.critical('严重')
  LoggerUtils().logger.error('error')
