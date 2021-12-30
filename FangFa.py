# -*- coding = utf-8 -*-
# @Time : 2021年12月17日 0017 14:44:10
# @Author:阳成
# @File:FangFa.py
# @Software:PyCharm

import random

import pandas as pd

tujian = pd.read_excel('F:\demo\shixun\MengHuanHeChong\ShuJu.xlsx', sheet_name="TuJian")


# ShuJuB = xlrd.open_workbook(r'F:\demo\shixun\MengHuanHeChong\ShuJu.xls')  # 获取数据表格
# tujian = ShuJuB.sheet_by_index(0)  # 获取第一个sheet

# 获取成长
def ChengZhang(a):
    y = tujian.loc[a-1, '成长']
    return y


# 获取资质
def ZiZhi(a):
    zz = {}
    zizhi=['攻资', '防资', '体资', '法资', '速资','成长']
    for z in zizhi:
        zz[z]=tujian.loc[a-1, z]
    return zz


# 获取名字
def Name(a):
    x = tujian.loc[a-1, '名称']
    return x


# 获取技能
def JiNeng(a):
    x = tujian.loc[a-1, '技能']
    y = x.split('/')  # 以/分割字符串至y列表
    return y


# 获取必带技能
def BiDaiJN(a):
    x = tujian.loc[a-1, '必带技能']
    y = x.split('/')  # 以/分割字符串至y列表
    return y


# 金柳露资质计算
def JingLiuLZZ(a, b):  # a为最高资质，b为百分比
    c = a * b
    c = int(c)
    y = random.randint(c, a)
    return y  # 返回c的值


# 金柳露成长随机
def JingLiuLCZ(a):
    i = 1
    x = []
    x.append(a)
    n = a
    while i <= 4:
        n = n - 12
        i += 1
        x.append(n)
    y = random.choice(x)
    czjg = '%.3f' % (y / 1000)
    return czjg


# 合宠资质计算
def HeChongZZJS(a, b):
    num = []
    x = 0.7
    c = (a + b) / 2
    while x < 1.11:
        y = int(c * x)
        x += 0.01
        num.append(y)
    sum = random.choice(num)
    return sum


# 合宠成长计算
def ChengZhangJS(a, b):
    x = 0
    c = (a + b) / 2
    cz = []
    mix = c - 48
    cz.append(mix)
    while x < 6:
        mix = mix + 12
        x += 1
        if mix < c:
            cz.append(mix)
    y = random.choice(cz)
    czjg = '%.3f' % (y / 1000)
    return czjg


# 最高资质计算,合成宠物不得超过最高资质
def ZuiGaoZZ(a, b):  # b为计算出来的资质，a为造型宠物的最高资质
    max = int(a * 1.05)
    if b > max:
        y = max
    else:
        y = b
    return y


# 获取基本宠物列表
def JiBenCWLB():
    hangshu = len(tujian)
    i = 0
    x = 0
    XuHao = []
    Name = []
    while i < hangshu:
        XuHao.append(tujian.loc[i, '序号'])  # 获取序号
        i += 1
    while x < hangshu:
        Name.append(tujian.loc[x, '名称'])  # 获取名字
        x += 1
    j = 0
    while j < hangshu:  # 代表减掉表头占去的一行
        print("%d %s" % (XuHao[j], Name[j]))
        j += 1
