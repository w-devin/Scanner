#!/usr/bin/env python
# __author__= 'w8ay'
import os
import sys

class spiderplus(object):
    def __init__(self,plugin,disallow=[]):
        self.dir_exploit = []
        self.disallow = ['__init__']
        self.disallow.extend(disallow)
        self.plugin = os.getcwd()+'/' +plugin
        sys.path.append(plugin)

        print 'plugin init succeed'

    def list_plusg(self):
        def filter_func(file):
            if not file.endswith(".py"):
                return False
            for disfile in self.disallow:
                if disfile in file:
                    return False
            return True
        dir_exploit = filter(filter_func, os.listdir(self.plugin))
        print 'plugin find:{}'.format(dir_exploit)
        return list(dir_exploit)

    def work(self,url):
        ret = list()
        if not '?' in url:
            return ret

        for _plugin in self.list_plusg():
            try:
                print 'plugin: {}'.format(_plugin)
                m = __import__(_plugin.split('.')[0])
                scanner = getattr(m, 'scanner')
                s = scanner.run(url)

                if s:
                    ret.append({'url':url, 'vul': _plugin[:3]})
            except Exception,e:
                print Exception,":",e 

        return ret