#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   XSSScan.py
@Time    :   2020/04/05 12:19:56
@Author  :   w-devin
@Version :   1.0
@Contact :   Mr.wyw@foxmail.com
@License :   None
@Desc    :   None
'''

from scripts.xss_check import scanner

def xss_vul_scan(url):
    print(scanner.run(url))


