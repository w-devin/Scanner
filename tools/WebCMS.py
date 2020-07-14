#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   WebCMS.py
@Time    :   2020/03/29 14:25:25
@Author  :   w-devin
@Version :   1.0
@Contact :   Mr.wyw@foxmail.com
@License :   None
@Desc    :   None
'''

import json
import os
import sys
import hashlib
import requests
import threading
from Queue import Queue

class WebCMS(object):
    workQueue = Queue()
    URL = ""
    threadNum = 0
    NotFound = True
    result = ""

    def __init__(self,url,threadNum = 10):
        self.URL = url
        self.threadNum = threadNum
        filename = os.path.join("config", "data.json")
        fp = open(filename)
        webdata = json.load(fp,encoding="utf-8")
        for i in webdata:
            self.workQueue.put(i)
        fp.close()
    
    def getmd5(self, body):
        m2 = hashlib.md5()
        m2.update(body)
        return m2.hexdigest()

    def th_whatweb(self):
        if(self.workQueue.empty()):
            self.NotFound = False
            return False

        if(self.NotFound is False):
            return False
        cms = self.workQueue.get()
        _url = self.URL + cms["url"]

        try:
            r = requests.get(_url, timeout=10)
            if r.status_code != 200:
                html = None
            else:
                html = r.text
        except Exception:
            html = None

        print('[*] checking {}'.format(_url))
        if(html is None):
            return False
        if cms["re"]:
            if(html.find(cms["re"])!=-1):
                self.result = cms["name"]
                self.NotFound = False
                return True
        else: 
            md5 = self.getmd5(html)
            if(md5==cms["md5"]):
                self.result = cms["name"]
                self.NotFound = False
                return True
    
    def run(self):
        while(self.NotFound):
            th = []
            for i in range(self.threadNum):
                t = threading.Thread(target=self.th_whatweb)
                t.start()
                th.append(t)
            for t in th:
                t.join()
        if(self.result):
            print('[!]: {} cms is {}'.format(self.URL, self.result))
            return self.result
        else:
            print('[!]: {} cms NOTFound!'.format(self.URL))
            return None


def get_finger_print(url, threadNum=5):
    if url.endswith('/'):
        url = url[:-1]
        
    scanner = WebCMS(url, threadNum=5)
    ret = scanner.run()

    return [{'url':url, 'cms': ret}]
        
if __name__ == '__main__':
    # url = 'http://192.168.220.130'
    url = 'https://www.freebuf.com'
    scanner = WebCMS(url, threadNum=5)

    scanner.run()