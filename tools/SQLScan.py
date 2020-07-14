#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SQLScan.py
@Time    :   2020/04/05 12:18:32
@Author  :   w-devin
@Version :   1.0
@Contact :   Mr.wyw@foxmail.com
@License :   None
@Desc    :   None
'''

from scripts.sqlcheck import scanner

def sql_vul_scan(url):
    pritn(scanner.run(url))
