# coding:UTF-8


"""
File: ticket_left_confirm
Author: Weitao Li
Email: weitaoli@gmail.com
Github:
Description: used to confirm how many ticket left on the 12306
"""

import json
import requests
from collections import OrderedDict

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'VDTConstructor'


if __name__ == '__main__':
    ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/queryT'

    page_values = OrderedDict()
    page_values['leftTicketDTO.train_date'] = '2016-10-01'
    page_values['leftTicketDTO.from_station'] = 'JNK'
    page_values['leftTicketDTO.to_station'] = 'JIK'
    page_values['purpose_codes'] = 'ADULT'

    ticket_queue_string_list = [key + '=' +
                                page_values[key] for key in page_values]
    ticket_queue_string = ticket_url + '?' + \
        ('&').join(ticket_queue_string_list)

    content = requests.get(ticket_queue_string, verify=False)
    # print content.text
    type(content.text)
    f = open('ticket.txt', 'w')
    f.write(content.text)
    f.close()

    # content_json = json.loads(content.text)
    # print content_json
