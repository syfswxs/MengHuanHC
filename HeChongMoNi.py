# -*- coding = utf-8 -*-
# @Time : 2021年12月15日 0015 15:41:05
# @Author:阳成
# @File:HeChongMoNi.py
# @Software:PyCharm
import random

import FangFa  # 导入方法函数

ChongWuPZ = []  # 宠物胚子列表
PeiZiZZ1 = {}
PeiZiZZ1 = {}
# 列出可选择的胚子名字
i = 1  # i为胚子对应的编号，供用户选择
print("现有的胚子为：")
FangFa.JiBenCWLB()  # 调取方法显示现有宠物数据

# 用户选择胚子
print("-----------请输入两次胚子序号-----------")
x = 1  # 代表用户第几次选择胚子

KeyName2 = ["攻资", '防资', '体资', '法资', '速资']
while x <= 2:
    PeiZiXH = int(input("%d号胚子序号：" % x))
    ChongWuPZ.append(PeiZiXH)  # 把用户选择的胚子信息加入胚子列表
    print("胚子%d[" % x + FangFa.Name(PeiZiXH) + "]的资质为：")
    Num = 1
    for zz in KeyName2:  # 遍历基础资质
        DangQianZZ = FangFa.ZiZhi(PeiZiXH)  # 获取当前造型对应资质的最高资质数据
        jllzz = FangFa.JingLiuLZZ(DangQianZZ[zz], 0.9)  # 获取金柳露洗点后的资质
        print("|" + zz + ":%d" % jllzz, end="\t|")  # 输出资质和数据
        Num += 1
        if Num > 2:  # 如果输出了两个数据 换行
            print()
            Num = 1
    print("|成长:", end="")
    pzcz = FangFa.ChengZhang(PeiZiXH)
    jllcz = FangFa.JingLiuLCZ(pzcz)
    print(jllcz + " |")
    print("【技能】：", end="")
    print(FangFa.JiNeng(PeiZiXH))
    x += 1

# 生成一个随机数决定合成造型，50%概率
HeChengXB = random.randint(0, 1)  # 随机在0和1之间抽一个下标
if HeChengXB == 1:  # 如果合成宠下标为1
    DiuShiCXB = 0  # 丢失宠下标则为0
else:
    DiuShiCXB = 1  # 否则丢失宠下标为1
HeChengCXH = ChongWuPZ[HeChengXB]  # 合成宠下标
DiuShiCXH = ChongWuPZ[DiuShiCXB]  # 丢失宠下标
HeChengCBD = FangFa.BiDaiJN(HeChengCXH)  # 获取合成造型宠必带技能
HeChengCZX = FangFa.Name(HeChengCXH)  # 获取合成宠造型名称
DiuShiCBD = FangFa.BiDaiJN(DiuShiCXH)  # 丢失宠造型必带技能
ZhaoXingCJBJN = FangFa.JiNeng(HeChengCXH)  # 获取该造型胚子的基本技能
DiuShiCJBJN = FangFa.JiNeng(DiuShiCXH)  # 获取丢失胚子基本技能
KeNengCXJN = HeChengCBD + DiuShiCBD + ZhaoXingCJBJN + DiuShiCJBJN  # 获取可能出现的技能
QuChongYLJN = list(set(KeNengCXJN))  # 去重复技能

# 获取两个胚子名字
PeiZiMZ1 = FangFa.Name(ChongWuPZ[0])
PeiZiMZ2 = FangFa.Name(ChongWuPZ[1])

# 合成宠技能、造型、技能预览
print('--'*50)
print("<可能合成造型为[%s]或[%s]，合成技能预览>" % (PeiZiMZ1, PeiZiMZ2))
print(QuChongYLJN)
input("---按任意键继续合成---")
JieGuoZZ = {'攻资': 0, '防资': 0, '体资': 0, '法资': 0, '速资': 0}
# 计算生成资质
PeiZi1ZZ = FangFa.ZiZhi(ChongWuPZ[0])  # 获取胚子1的资质
PeiZi2ZZ = FangFa.ZiZhi(ChongWuPZ[1])  # 获取胚子2的资质
HeChengCZZ = FangFa.ZiZhi(ChongWuPZ[HeChengXB])
for jgzz in KeyName2:  # 遍历基础资质
    q = FangFa.HeChongZZJS(PeiZi1ZZ[jgzz], PeiZi2ZZ[jgzz])
    y = FangFa.ZuiGaoZZ(HeChengCZZ[jgzz], q)  # 计算最高资质
    JieGuoZZ[jgzz] = y  # 把数据保存入字典
cz = FangFa.ChengZhangJS(PeiZi1ZZ['成长'], PeiZi2ZZ['成长'])
JieGuoZZ["成长"] = cz  # 把数据保存入字典

# 检查胚子身上是否有必带技能，如果有则删除
for BiDaiJN in HeChengCBD:  # 把新合成宠的必带技能遍历出来
    if BiDaiJN in ZhaoXingCJBJN:  # 如果此技能存在胚子基础技能里
        ZhaoXingCJBJN.remove(BiDaiJN)  # 从基础技能列表里删除该技能

# 检查丢失胚子身上是否有必带技能，如果有则删除
for BiDaiJN2 in HeChengCBD:  # 把新合成宠的必带技能遍历出来
    if BiDaiJN2 in DiuShiCJBJN:  # 如果此技能存在丢失胚子基础技能里
        DiuShiCJBJN.remove(BiDaiJN)  # 从基础技能列表里删除该技能
# 把两个胚子的基础技能都添加到一个list中
QuanBuJN = ZhaoXingCJBJN + DiuShiCJBJN
QuChongJN = list(set(QuanBuJN))  # 去掉重复技能
# 最终保留的技能
ZuiZhongJN = HeChengCBD  # 先把必带技能塞入
for JiNeng in QuChongJN:  # 把去重技能都遍历
    i = random.randint(1, 100)  # i在1~100里随机
    if i < 45:  # 45%保留
        ZuiZhongJN.append(JiNeng)  # 把该技能添加入最终技能中

print("恭喜你合出了个%d技能[" % len(ZuiZhongJN) + HeChengCZX + "]技能为")
i = 1
for zzzj in KeyName2:
    print("|" + zzzj + ":%d" % JieGuoZZ[zzzj], end="\t|")
    i += 1
    if i > 2:
        print()
        i = 1
print("|成长:" + JieGuoZZ["成长"] + " |")
print(ZuiZhongJN)
