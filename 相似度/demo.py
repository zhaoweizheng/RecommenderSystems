#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-21 10:24
# @Author  : zwz
# @Site    : 
# @File    : demo.py
# @Software: PyCharm

'''
    相似度计算
        相似度计算在数据挖掘和推荐算法系统中有着广泛的应用场景. 如:
        @ 在协同过滤算法中, 可以利用相似度计算用户之间或者物品之间的相似度
        @ 在利用k-means 进行聚类时, 利用相似度计算公式计算个体到簇类中心的距离, 进而判断个体所属的类别
        @ 利用KNN进行分类时, 利用相似度计算个体与已知类别之间的相似性, 从而判断个体所属的类别等,
'''


'''
    1. 欧式距离: 指在m维空间中两个点的真实距离
'''

from numpy import *

def EuclideanDistance(a,b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
print('a,b 二维欧式距离为:', EuclideanDistance((1,1),(2,2)))

'''
    2. 哈曼顿距离
    注:abs 是取绝对值
'''

def ManhattanDistance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

print('a,b 二维哈曼顿距离为:', ManhattanDistance((1,1),(2,2)))

'''
    3. 切比雪夫距离
'''

def ChebyshevDistance(a,b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))
print('a, b二维切比雪夫距离: ', ChebyshevDistance((1,2),(3,4)))

'''
    4. 马氏距离: 指数据的协方差距离
'''