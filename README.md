# Web Scanner

## 使用说明

![help](media/help.png)

- `-o, --operate` 指定扫描操作
    - port_scan 端口扫描
    - web_dir_scan 目录扫描
    - get_finger_print 获取web指纹
    - sql_vul_scan SQL注入扫描
    - xss_vul_scan XSS漏洞扫描

- `-h, --host` 指定要扫描的主机, 支持两种写法, 默认值为 `127.0.0.1`
    - 192.168.0.1
    - 192.168.0.1-120

- `-u, --url` 指定扫描的url(用于目录扫描和xss, sql漏洞扫描), 默认为 `localhost`

- `-p, --port` 指定要扫描的端口, 支持两种写法, 默认值为常见端口
    - 80
    - 80-100

- `-t, --threadNum` 指定扫描的线程数, 未必每个扫描都支持

- `f, --filename` 指定扫描结果导出的文件名, 默认为 `report.html`

- `--help` 查看关于参数的帮助信息

## 端口扫描

```bash
python main.py -o port_scan -h 192.168.220.120-135 -p 80-100
```

![port_scan](media/port_scan.png)

![port_scan_report](media/port_scan_report.png)


## 目录扫描

```bash
python main.py -o web_dir_scan -u 'http://192.168.220.130'
```

![web_dir_scan](media/web_dir_scan.png)

![web_dir_scan_report](media/web_dir_scan_report.png)

## web 指纹获取

```bash
 python main.py -o get_finger_print -u 'https://www.freebuf.com/'
```

![cms_scan](media/cms_scan.png)

![cms_scan_report](media/cms_scan_report.png)

## XSS 漏洞扫描

```bash
 python main.py -o xss_vul_scan -u https://www.baidu.com/s?wd=test
```

![xss_scan](media/xss_scan.png)


## SQL 漏洞扫描

```bash
python main.py -o sql_vul_scan -u http://192.168.220.144/sqli/example1.php?name=root
```

![sql_vul_scan](media/sql_vul_scan.png)

## Spider

```bash
python main.py -o vul_spider -u http://192.168.220.144
```

![vul_spider](media/vul_spider.png)
![vul_spider_report](media/vul_spider_report.png)