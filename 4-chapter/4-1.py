#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-04 16:54
# @Author  : zwz
# @Site    :  实现数据的标准化
# @File    : 4-1.py
# @Software: PyCharm


"""
    数据标准化是指: 将数据按照一定的比例进行缩放, 使其落入一个特定的小区间.
    其中, 最典型的就是数据的归一化处理, 即将数据统一映射到[0,1]之间
    数据标准化的好处: 加快模型的收敛速度, 提高模型的精度
"""
import numpy as np
import math

class DataNorm:
    def __init__(self):
        self.arr = [1,2,3,4,5,6,7,8,9]
        self.x_max = max(self.arr) # 最大值
        self.x_min = min(self.arr) # 最小值
        self.x_mean = sum(self.arr) / len(self.arr) # 平均值
        self.x_std = np.std(self.arr) # 标准差

    def Min_max(self):
        """
        Min-Max 标准差
        """
        arr_ = list()
        for x in self.arr:
            arr_.append(round((x-self.x_min)/(self.x_max-self.x_min), 4))
        print("经过Min_Max 标准化后的数据为:\n{}".format(arr_))
            # round(x,4) 对x保留4位小数


    def Z_Score(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round(((x - self.x_mean)/self.x_std), 4))
        print("经过Z_Score标准化后的数据为: \n{}".format(arr_))

    def DecimalScaling(self):
        """
        小数定标( Decimalscalin) 标准化
        :return:
        """
        arr_ = list()
        j = self.x_max // 10 if self.x_max % 10 == 0 else self.x_max // 10 + 1
        for x in self.arr:
            arr_.append(round(x / math.pow(10,j), 4))
        print("经过Decimal Scaling 标准化后的数据为: \n{}".format(arr_))

    def Mean(self):
        """
        均值归一化
        :return:
        """
        arr_ = list()
        for x in self.arr:
            arr_.append(round((x-self.x_mean)/(self.x_max-self.x_min), 4))
        print("经过均值标准化后的数据为:\n{}".format(arr_))

    def Vector(self):
        """
        向量归一化
        :return:
        """
        arr_ = list()
        for x in self.arr:
            arr_.append(round(x/sum(self.arr), 4))
        print("经过向量标准化后的数据为:\n{}".format(arr_))

    def exponential(self):
        arr_1 = list()
        for x in self.arr:
            arr_1.append(round(math.log10(x)/math.log10(self.x_max),4))
        print("经过支书转换法(log10) 标准化后的数据为:\n{}".format(arr_1))

        arr_2 = list()
        sum_e = sum([math.exp(one) for  one in self.arr])
        for x in self.arr:
            arr_2.append(round(math.exp(x)/sum_e,4))
        print("经过支书转换法(SoftMax) 标准化后的数据为:\n{}".format(arr_2))

        arr_3 = list()
        for x in self.arr:
            arr_3.append(round(1/(1+math.exp(-x)), 4))
        print("经过支书转换法(Sigmoid) 标准化后的数据为:\n{}".format(arr_3))


if __name__ == "__main__":
    dn = DataNorm()
    print("++++++++Min_Max 标准化++++++++")
    dn.Min_max()
    print("++++++++Z-Sore 标准化++++++++")
    dn.Z_Score()
    print("++++++++小数定标( Decimalscalin) 标准化++++++++")
    dn.DecimalScaling()
    print("++++++++均值归一化 标准化++++++++")
    dn.Mean()
    print("++++++++向量归一化 标准化++++++++")
    dn.Vector()
    print("++++++++指数转换++++++++")
    dn.exponential()

