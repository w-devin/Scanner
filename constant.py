#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   constant.py
@Time    :   2020/03/28 23:46:27
@Author  :   w-devin
@Version :   1.0
@Contact :   Mr.wyw@foxmail.com
@License :   None
@Desc    :   None
'''

PORT_SCAN           = 'port_scan'
VUL_SPIDER          = 'vul_spider'
WEB_DIR_SCAN        = 'web_dir_scan'
SQL_VUL_SCAN        = 'sql_vul_scan'
XSS_VUL_SCAN        = 'xss_vul_scan'
GET_FINGER_PRINT    = 'get_finger_print'

OPERATE = [PORT_SCAN, WEB_DIR_SCAN, GET_FINGER_PRINT, SQL_VUL_SCAN, XSS_VUL_SCAN, VUL_SPIDER]

DEFAULT_URL         = 'localhost'
DEFAULT_HOST        = '127.0.0.1'
DEFAULT_THREAD_NUM  = 5
DEFAULT_REPORT_PATH = 'report.html'
DEFAULT_SCAN_PORT = [80,    8080,   3311,   3312,   3389,   4440,   5672,   5900,   6082,   7001,
                     8161,  8649,   9000,   9090,   9200,   9300,   9999,   10050,  11211,  27017,
                     28017, 3777,   50000,  50060,  50070,  21,     22,     23,     25,     53,
                     123,   161,    8161,   162,    389,    443,    512,    513,    873,    1433,
                     1080,  1521,   1900,   2049,   2601,   2604,   2082,   2083,   3128,   3312,
                     3306,  4899,   8834,   4848]
