# coding:UTF-8

from pdftables.pdftables import *
from pdftables.display import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'VDTConstructor'


filepath = '1201163820.PDF'
fileobj = open(filepath, 'rb')

tables = get_tables(fileobj)
for table in tables:
    print to_string(table)
