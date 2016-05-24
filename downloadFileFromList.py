# coding:UTF-8


"""
File: downloadFileFromList.py
Author: Weitao Li
Email: weitaoli@gmail.com
Github:
Description: use to download pdf file from cninfo.com
"""

import json
import requests
import os
import subprocess

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'VDTConstructor'


def announcement(url, values):
    """
    try to get file's download address from the url
    """
    announcement_list = []
    content = requests.post(url, data=values)
    content_json = json.loads(content.text)
    announcement_list.append(content_json['announcements'])
    while content_json['hasMore'] and len(announcement_list) < 2:
        # while content_json['hasMore']:
        values['pageNum'] = str(int(values['pageNum']) + 1)
        content = requests.post(url, data=values)
        content_json = json.loads(content.text)
        announcement_list.append(content_json['announcements'])
        print 'now download the infomation in page ', values['pageNum']

    return announcement_list


def write_urls_in_pages(pages, file_name):
    print 'writing down the commands'
    download_urls = open(file_name, 'w')
    download_urls_list = []
    for page in pages:
        for item in page:
            download_path = pdf_download_url + item['adjunctUrl']
            announcement_time = item['adjunctUrl'].split('/')[2]
            command_str = 'wget -T 120 ' + download_path + ' -O ' + \
                          item['secCode'] + '_' + announcement_time
            download_urls_list.append(command_str)
    download_urls.write('\n'.join(download_urls_list))
    download_urls.close()


def read_commands_run(commands_file_name, reDownload_file_name):
    print 'running commands'
    commands = open(commands_file_name, 'r').read()
    commands_list = commands.split('\n')
    for command in commands_list:
        print command
        # subprocess.check_output(command)
        p = subprocess.Popen(command, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        if err is not None:
            print 'error happen, add this file to undownload'

            # os.system(command)


def download_page(pages):
    for page in pages:
        for item in page:
            # print item['announcementId'], item['secName'], item['adjunctUrl']
            download_path = pdf_download_url + item['adjunctUrl']
            announcement_time = item['adjunctUrl'].split('/')[2]
            # print download_path
            # command_str = 'wget ' + download_path + ' -O ' + \
            #     item['secName'] + '_' + announcement_time
            command_str = 'wget ' + download_path + ' -O ' + \
                          item['secCode'] + '_' + announcement_time
            # command_str = 'wget ' + download_path
            # print command_str
            os.system(command_str)


if __name__ == '__main__':
    # need_download = False
    need_download = True
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

    command_file_name = 'downloadUrls.txt'
    undownload_file_name = 'undownload.txt'
    if need_download:
        page_content = announcement(page_url, page_values)
        print len(page_content)
        write_urls_in_pages(page_content, command_file_name)

    read_commands_run(command_file_name)
