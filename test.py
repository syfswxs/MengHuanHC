# -*- coding = utf-8 -*-
# @Time : 2021年12月15日 0015 17:22:12
# @Author:阳成
# @File:test.py
# @Software:PyCharm
import random, xlrd, xlsxwriter,xlwt,xlutils
from xlutils import copy


ShuJu = xlrd.open_workbook('F:\demo\shixun\Test\cwjbxx.xls',formatting_info=True)#读取数据表
CangKu = ShuJu.sheet_by_index(1)#获取表二
wb = xlutils.copy.copy(CangKu)#复制文件并保留格式
y = wb.get_sheet(1)
y.write(0,0,'bianghau')
wb.save('F:\demo\shixun\Test\cwjbxx.xls')