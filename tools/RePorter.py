#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   outputer.py
@Time    :   2020/03/29 03:04:21
@Author  :   w-devin
@Version :   1.0
@Contact :   Mr.wyw@foxmail.com
@License :   None
@Desc    :   None
'''

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

html_head = '''
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="gbk">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Scan Report</title>
<link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
<div class="container container-fluid">
	<div class="row-fluid">
		<div class="span12">
			<h3 class="text-center">
				Scan Report
			</h3>
			</BR>
			<table class="table table-bordered">
				<thead>
                    {report_head}
					
				</thead>
				<tbody>
					{report_tab}
				</tbody>
			</table>
		</div>
	</div>
</div>  </body>
</html>
'''

def _build_table(data):
    th = '' 
    td = ''
    for line in data:
        if not th:
            for x in line:
                th = ''.join([th, '<th>{}</th>'.format(x)])

            th = '<tr>{}</tr>\n'.format(th)

        _td = ''
        for x in line:
            _td = ''.join([_td, '<th>{}</th>'.format(line[x])])

        td = ''.join([td, '<tr>{}</tr>\n'.format(_td)])

    return th, td


def write_html(filename='report.html', data=dict()):
    global html_head

    if not data:
        data = dict()
        
    head, body = _build_table(data)
    html_head = html_head.format(report_head=head, report_tab=body)

    if not filename.endswith('.html'):
        filename = ''.join([filename, '.html'])

    file_object = open(filename, 'w')
    file_object.write(html_head)
    file_object.close()

if __name__ == '__main__':
    data = [
        {'a':1, 'b':5, 'c':3},
        {'a':2, 'b':4, 'c':3},
        {'a':3, 'b':3, 'c':3},
        {'a':4, 'b':2, 'c':3},
        {'a':5, 'b':1, 'c':3},
    ]

    write_html('test', data)
