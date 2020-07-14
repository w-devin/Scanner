#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   PortScan.py
@Time    :   2020/03/29 02:08:04
@Author  :   w-devin
@Version :   1.0
@Contact :   Mr.wyw@foxmail.com
@License :   None
@Desc    :   None
'''

import socket
import threading
from Queue import Queue

class PortScan(object):
    def __init__(self):
        self.queue = Queue()
        self.ret = list()

    def _scan(self, host): 
        while not self.queue.empty():
            port = self.queue.get()
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
            s.settimeout(1) 

            try:
                s.connect((host, port))

                self.ret.append({'host': host, 'port': port, 'open': True})
                print('[*] {}:{} OPEN'.format(host, port))
            except:
                self.ret.append({'host': host, 'port': port, 'open': False})
                print('[*] {}:{} CLOSE'.format(host, port))
            finally:
                s.close()

    def scan(self, host, ports, threadNum=5):
        self.ret = list()

        if not ports:
            return self.ret

        for port in ports:
            self.queue.put(port)

        threads = []
        for i in range(threadNum):
            t = threading.Thread(target=self._scan(host=host))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print('[!] The scan is complete!')
        return self.ret

def port_scan(hosts, ports, threadNum=5):
    scanner = PortScan()

    ret = list()

    for host in hosts:
        ret += scanner.scan(host, ports, threadNum=5)

    return ret


if __name__ == '__main__':
    ret = port_scan(['192.168.220.130'], [1, 2, 3, 4, 80])
    print ret