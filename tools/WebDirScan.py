#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   WebDirScan.py
@Time    :   2020/03/29 12:58:41
@Author  :   w-devin
@Version :   1.0
@Contact :   Mr.wyw@foxmail.com
@License :   None
@Desc    :   None
'''

import os
import sys
import requests
import threading

from Queue import Queue

class WebDirScan:
    def __init__(self):
        self.headers = {
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
             'Referer': 'http:idevin.cn',
             'Cookie': 'whoami=jarvis',
             }

        self.dirfile = os.path.join('config', "dir.txt")
        self.ret = list()
    
    def checkdir(self, url):
        status_code = 0
        try:
            r = requests.head(url,headers=self.headers)
            status_code = r.status_code
        except Exception as e:
            print e
            status_code = 0
        return status_code

    def test_url(self):
        while not self.task.empty():
            url = self.task.get()
            status_code = self.checkdir(url)
            if status_code != 404:
                self.ret.append({'url': url, 'status_code': status_code})

            print '[*] Testing: {} status: {}'.format(url, status_code)
    
    def scan(self, root, threadNum=5):
        self.ret = list()

        if not isinstance(root, (str, unicode)):
            return self.ret

        if root.endswith('/'):
            root = root[:-1]

        self.task = Queue()

        if isinstance(root, unicode):
            root = root.encode('utf8')

        for line in open(self.dirfile):  
            self.task.put(''.join([root,-
             line.strip()]))

        threads = []
        for i in range(threadNum):
            t = threading.Thread(target=self.test_url())
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        print('[*] The DirScan is complete!')

        return self.ret

def web_dir_scan(root, threadNum=5):
    scanner = WebDirScan()

    ret = scanner.scan(root, threadNum)

    return ret

if __name__ == '__main__':
    ret = web_dir_scan('http://192.168.220.130')
    print ret
