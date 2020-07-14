#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sqlcheck.py
@Time    :   2020/04/05 15:47:18
@Author  :   w-devin
@Version :   1.0
@Contact :   Mr.wyw@foxmail.com
@License :   None
@Desc    :   None
'''

import re, random

from tools.craw import Download

BOOLEAN_TESTS = (" AND %d=%d", " OR NOT (%d=%d)")
DBMS_ERRORS = {# regular expressions used for DBMS recognition based on error message response
    "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
    "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
    "Microsoft SQL Server": (r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*", r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.", r"(?s)Exception.*\WRoadhouse\.Cms\."),
    "Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
    "Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
    "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
    "SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*", r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
    "Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
}
 
class spider():
    def __init__(self):
        self.Downloader = Download.Downloader()

    def run(self, url):
        if(not url.find("?")):
            return False

        _url = url + "%29%28%22%27"
        _content = self.Downloader.get(_url)

        for (dbms, regex) in ((dbms, regex) for dbms in DBMS_ERRORS for regex in DBMS_ERRORS[dbms]):
            if(re.search(regex,_content)):
                print "sql fonud: {}".format(url)
                return True

            # 不同的网站有SQL漏洞时表现不同, 针对pentesterlab的判断
            if(re.search('PentesterLab', _content)):
                if(not re.search('table-striped">', _content)):
                    print "sql fonud: {}".format(url)
                    return True

        content = {}
        content["origin"] = self.Downloader.get(_url)
        for test_payload in BOOLEAN_TESTS:
            RANDINT = random.randint(1, 255)
            _url = url + test_payload%(RANDINT,RANDINT)
            content["true"] = self.Downloader.get(_url)
            _url = url + test_payload%(RANDINT,RANDINT+1)
            content["false"] = self.Downloader.get(_url)
            if content["origin"]==content["true"]!=content["false"]:
                print "sql fonud: %"%url
                return True

        return False

scanner = spider()