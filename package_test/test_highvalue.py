# -*- coding: UTF-8 -*-

import _thread
import sys
sys.path.append('..')

from package_highvalue.HighValue import HighValue

def main():
  # highValue = HighValue(1, 'daily', 'BEIJING')
  # highValue = HighValue(1, 'daily', 'JINGWAIV1')
  # highValue = HighValue(1, 'weekly', 'BEIJING')
  # highValue = HighValue(1, 'weekly', 'JINGWAIV1')
  # highValue = HighValue(1, 'monthly', 'BEIJING')
  # highValue = HighValue(1, 'monthly', 'JINGWAIV1')
  highValue = HighValue(1, 'weekly', 'JINGWAIV1')
  highValue.createLayer()
  
if __name__ == '__main__':
  main()