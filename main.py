#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/03/29 00:00:33
@Author  :   w-devin
@Version :   1.0
@Contact :   Mr.wyw@foxmail.com
@License :   None
@Desc    :   None
'''

import sys
import click

from constant import OPERATE, DEFAULT_THREAD_NUM, DEFAULT_REPORT_PATH
from constant import DEFAULT_HOST, DEFAULT_URL, DEFAULT_SCAN_PORT
from constant import PORT_SCAN, WEB_DIR_SCAN, SQL_VUL_SCAN, XSS_VUL_SCAN, GET_FINGER_PRINT, VUL_SPIDER

from tools.RePorter import write_html
from tools.PortScan import port_scan
from tools.WebDirScan import web_dir_scan
from tools.WebCMS import get_finger_print
from tools.SQLScan import sql_vul_scan
from tools.XSSScan import xss_vul_scan
from tools.Spider import spider


def get_ports(ports):
    if isinstance(ports, (unicode, str)):
        if '-' in ports:
            ports = ports.split('-')

            if len(ports) != 2:
                print('[!] not sport this ports format, use 80 or 80-1080')
                return None

            try:
                ports = range(int(ports[0]), int(ports[1]) + 1)
            except Exception:
                print('[!] not sport this ports format, use 80 or 80-1080')
                return None
        else:
            try:
                ports = [int(ports)]
            except Exception:
                print('[!] not sport this ports format, use 80 or 80-1080')
                return None

    if not isinstance(ports, list):
        print('[!] not sport this ports format, use 80 or 80-1080')
        return None

    return ports

def get_hosts(host):
    hosts = list()
    if isinstance(host, (unicode, str)):
        host = host.split('.')

        if len(host) != 4:
            print('[!] not sport this ports format, use 192.168.0.1 or 192.168.0.1-255')
            return list()

        try:
            for x in range(3): int(host[x])
        except Exception:
            print('[!] not sport this ports format, use 192.168.0.1 or 192.168.0.1-255')
            return list()

        _range = list()
        if '-' in host[3]:
            _range = host[3].split('-')

            if len(_range) != 2:
                print('[!] not sport this ports format, use 192.168.0.1 or 192.168.0.1-255')
                return list()

            try:
                _range = range(int(_range[0]), int(_range[1]))
            except Exception:
                print('[!] not sport this ports format, use 192.168.0.1 or 192.168.0.1-255')
                return list()
        elif host[3].isdigit():
            _range = [int(host[3])]

        hosts = ['.'.join(host[:3] + [str(x)]) for x in _range]

    return hosts


@click.command()
@click.option('-o', '--operate', type=click.Choice(OPERATE))
@click.option('-h', '--host', type=click.STRING, default=DEFAULT_HOST)
@click.option('-u', '--url', type=click.STRING, default=DEFAULT_URL)
@click.option('-p', '--ports', type=click.STRING, default=DEFAULT_SCAN_PORT)
@click.option('-t', '--threadNum', type=click.IntRange(0, 50), default=DEFAULT_THREAD_NUM)
@click.option('-f', '--filename', type=click.STRING, default=DEFAULT_REPORT_PATH)
def run(operate, host, url, ports, threadnum, filename):
    ret = dict()
    if operate == PORT_SCAN:
        ret = port_scan(hosts=get_hosts(host), ports=get_ports(ports), threadNum=threadnum)
    elif operate == WEB_DIR_SCAN:
        ret = web_dir_scan(root=url, threadNum=threadnum)
    elif operate == GET_FINGER_PRINT:
        ret = get_finger_print(url=url, threadNum=threadnum)
    elif operate == XSS_VUL_SCAN:
        ret = xss_vul_scan(url=url)
    elif operate == SQL_VUL_SCAN:
        ret = sql_vul_scan(url=url)
    elif operate == VUL_SPIDER:
        ret = spider.craw(url=url, threadNum=threadnum)

    write_html(filename, ret)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('[!] --help to get help message')
        exit(0)

    run()