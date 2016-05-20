# -*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdocument import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

fp = open('1201163820.PDF', 'rb')
# 用文件对象来创建一个pdf文档分析器
parser = PDFParser(fp)
# 创建一个  PDF 文档
doc = PDFDocument(parser)
# 检测文档是否提供txt转换，不提供就忽略
if not doc.is_extractable:
    raise PDFTextExtractionNotAllowed
# 创建PDf 资源管理器 来管理共享资源
rsrcmgr = PDFResourceManager()
# 创建一个PDF设备对象
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
# 处理文档对象中每一页的内容
# doc.get_pages() 获取page列表
# 循环遍历列表，每次处理一个page的内容
# 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure,
# LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
for i, page in enumerate(PDFPage.create_pages(doc)):
    interpreter.process_page(page)
    layout = device.get_result()
    for x in layout:
        if(isinstance(x, LTTextBoxHorizontal)):
            # if(len(x.text) > 100):
            #     string = x.text.replace('/n', ' ')
            #     print string
            with open('a.txt', 'a') as f:
                f.write(x.get_text().encode('utf-8') + '\n')
            print '/n/n/n/n'
