#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   xss_check.py
@Time    :   2020/04/05 12:28:41
@Author  :   w-devin
@Version :   1.0
@Contact :   Mr.wyw@foxmail.com
@License :   None
@Desc    :   None
'''

import sys,os
from tools.craw import Download, common

class spider():
    def __init__(self):
        self.download = Download.Downloader()
        self.payload = []

        filename = os.path.join("config", "xss.txt")

        with open(filename) as f:
            for i in f:
                self.payload.append(i.strip())

    def run(self,url):
        urls = common.urlsplit(url)

        if urls is None:
            return False

        for _urlp in urls:
            for _payload in self.payload:
                _url = _urlp.replace("my_Payload", _payload)
                #我们需要对URL每个参数进行拆分,测试
                _str = self.download.get(_url)
                if _str is None:
                    print '_str is None`'
                    return False

                if(_str.find(_payload) != -1):
                    print "xss found:%s" % url
                    return True
        return False

scanner = spider()

