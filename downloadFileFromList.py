# coding:utf-8
import json
import requests
import os

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'VDTConstructor'


def announcement(url, values):
	announcement_list = []
	content = requests.post(url, data=values)
	content_json = json.loads(content.text)
	announcement_list.append(content_json['announcements'])
	while content_json['hasMore'] and len(announcement_list) < 3:
		values['pageNum'] = str(int(values['pageNum']) + 1)
		content = requests.post(url, data=values)
		content_json = json.loads(content.text)
		announcement_list.append(content_json['announcements'])

	return announcement_list


if __name__ == '__main__':
	pdf_download_url = 'http://www.cninfo.com.cn/'
	page_url = 'http://www.cninfo.com.cn/cninfo-new/announcement/query'
	page_values = {'stock': '',
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

	page_content = announcement(page_url, page_values)
	print len(page_content[0])

	for page in page_content:
		for item in page:
			# print item['announcementId'], item['secName'], item['adjunctUrl']
			download_path = pdf_download_url + item['adjunctUrl']
			announcement_time = item['adjunctUrl'].split('/')[2]
			# print download_path
			command_str = 'wget ' + download_path + ' -O ' + item['secName'] + '_' + announcement_time
			# print command_str
			os.system(command_str)
