import urllib
import urllib2
import json
import requests

__author__ = 'VDTConstructor'

# url = 'http://www.cninfo.com.cn/cninfo-new/disclosure/sse_latest'
url = 'http://www.cninfo.com.cn/cninfo-new/announcement/query'
values = {'stock': '',
          'searchkey': '2014%E5%B9%B4%E5%B9%B4%E5%BA%A6%E6%8A%A5%E5%91%8A%E6%91%98%E8%A6%81%3B',
          'plate': '',
          'category': '',
          'trade': '',
          'column': 'sse',
          'columnTitle': '%E5%8E%86%E5%8F%B2%E5%85%AC%E5%91%8A%E6%9F%A5%E8%AF%A2',
          'pageNum': '1',
          'pageSize': '30',
          'tabName': 'fulltext',
          'sortName': '',
          'sortType': '',
          'limit': '',
          'showTitle': '',
          'seDate': '%E8%AF%B7%E9%80%89%E6%8B%A9%E6%97%A5%E6%9C%9F'
          }
# data = urllib.urlencode(values)
# print data
# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# print response
# the_page = response.read()
# # print the_page
# the_page_json = json.loads(the_page)
# # print the_page_json
#
# print the_page_json['hasMore']
# file_object = open('thefile.txt', 'w')
# file_object.write(the_page)
# file_object.close()
# print 'finish'

headers = {'Host': 'www.cninfo.com.cn',
           'Connection': 'keep-alive',
           'Content-Length': '319',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Origin': 'http://www.cninfo.com.cn',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Referer': 'http://www.cninfo.com.cn/cninfo-new/announcement/show',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Cookie': 'JSESSIONID=70ECF0B5DB11281A9BF694DCC1265A90'
           }
r = requests.post(url, data=values, headers=headers)
print r.text
