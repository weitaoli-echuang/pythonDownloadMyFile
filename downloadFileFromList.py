# coding:utf-8
import urllib
import urllib2
import json
import requests

__author__ = 'VDTConstructor'

# url = 'http://www.cninfo.com.cn/cninfo-new/disclosure/sse_latest'
url = 'http://www.cninfo.com.cn/cninfo-new/announcement/query'
values = {'stock': '',
          'searchkey': '2014年年度报告摘要',
          'plate': '',
          'category': '',
          'trade': '',
          'column': 'sse',
          'columnTitle': '历史公告查询',
          'pageNum': '1',
          'pageSize': '30',
          'tabName': 'fulltext',
          'sortName': '',
          'sortType': '',
          'limit': '',
          'showTitle': '',
          'seDate': '请选择日期'
          }

r = requests.post(url, data=values)
# print r.text

the_page_json = json.loads(r.text)
print the_page_json

print the_page_json['hasMore']
file_object = open('thefile.txt', 'w')
file_object.write(r.text)
file_object.close()
print 'finish'
