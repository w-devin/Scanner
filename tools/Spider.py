#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tools.craw import Download,UrlManager,plugin,common
import threading
from urlparse import urljoin
from bs4 import BeautifulSoup
from scripts import sqlcheck
import sys

class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager.UrlManager()
        self.download = Download.Downloader()
        self.root = ''
      
    def _judge(self, domain, url):
        if (url.find(domain) != -1):
            return True
        else:
            return False

    def _parse(self,page_url,content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser')
        _news = self._get_new_urls(page_url,soup)
        return _news

    def _get_new_urls(self, page_url,soup):
        new_urls = set()
        links = soup.find_all('a')
        for link in links:
            new_url = link.get('href')
            new_full_url = urljoin(page_url, new_url)
            if(self._judge(self.root,new_full_url)):
                new_urls.add(new_full_url)
        return new_urls

    def craw(self, url, threadNum):
        ret = list()
        print 'start craw'
        self.root = url
        self.urls.add_new_url(self.root)
        while self.urls.has_new_url():
            _content = []
            th = []
            for i in list(range(threadNum)):
                if self.urls.has_new_url() is False:
                    break
                new_url = self.urls.get_new_url()
                print("craw:" + new_url)
                t = threading.Thread(target=self.download.download, args=(new_url, _content))
                t.start()
                th.append(t)
            for t in th:
                t.join()

            for _str in _content:
                if _str is None:
                    continue
                new_urls = self._parse(new_url, _str["html"])
                _plugin = plugin.spiderplus("tools/scripts")
                _ret = _plugin.work(_str["url"])
                ret += _ret
                self.urls.add_new_urls(new_urls)

        return ret

spider = SpiderMain()



if __name__ == '__main__':
    url = 'http://192.168.220.130'
    spider = SpiderMain(url, 3)

    spider.craw()
