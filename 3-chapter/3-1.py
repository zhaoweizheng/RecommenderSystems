#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-04 10:03
# @Author  : zwz
# @Site    : 代码3-1  数据集介绍之MovieLens数据集
# @File    : 3-1.py
# @Software: PyCharm

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# 用来正常显示中文标签
#plt.rcParams["font.sans-serif"] = ["SimHei"]
# 用来正常显示负号
plt.rcParams["axes.unicode_minus"] = False

def getRatings(file_path):
    rates = pd.read_table(
        file_path,
        header=None,
        sep="::",
        names=["userID", "movieID", "rate", "timestamp"],
        engine='python'
    )
    #print(rates.describe())

    print("userID的范围为: <{},{}>"
          .format(min(rates["userID"]), max(rates["userID"])))
    print("movieID的范围为: <{},{}>"
          .format(min(rates["movieID"]), max(rates["movieID"])))
    print("评分值的范围为: <{},{}>"
          .format(min(rates["rate"]), max(rates["rate"])))
    print("数据总条数为:\n{}".format(rates.count()))
    print("数据前5条记录为:\n{}".format(rates.head(5)))
    df = rates["userID"].groupby(rates["userID"])
    print("用户评分记录最少条数为：{}".format(df.count().min()))

    scores = rates["rate"].groupby(rates["rate"]).count()
    # 图上添加数字
    for x, y in zip(scores.keys(), scores.values):
        plt.text(x, y + 2, "%.0f" % y, ha="center", va="bottom", fontsize=12)
    plt.bar(scores.keys(), scores.values, fc="r", tick_label=scores.keys())
    plt.xlabel("评分分数")
    plt.ylabel("对应的人数")
    plt.title("评分分数对应人数统计")
    plt.show()


def getMovies(file_path):

    movies = pd.read_table(

        file_path,
        header=None,
        sep="::",
        names=["movieID","title","genres"],
        engine="python"
     )

    print("movieID的范围为: <{},{}>".format(min(movies["movieID"]),max(movies["movieID"])))
    print("数据总条数为:\n{}".format(movies.count()))
    moviesDict = dict()

    for line in movies["genres"].values:
        for one in line.split("|"):
            moviesDict.setdefault(one,0)
            moviesDict[one] += 1

    print("电影类型总数为: {}".format(len(moviesDict)))
    print("电影类型分别为: {}".format(moviesDict.keys()))
    print(moviesDict)


    newMD = sorted(moviesDict.items(),key=lambda x:x[1], reverse=True)
    # g = lambda x, y, z : (x + y) * z  单行函数   g(1,2,3)  输出: 9
    # 设置标签
    labels = [newMD[i][0] for i in range(len(newMD))]
    values = [newMD[i][1] for i in range(len(newMD))]
    # 与labels对应, 数值越大离中心区越远
    explode = [x * 0.01 for x in range(len(newMD))]
    # 设置X轴Y轴比例
    plt.axes(aspect = 1)
    # labeldistance 表示标签离中心距离, pctdistance 表示百分百数据离中心区距离
    # autopct 表示百分比的格式, shadow 表示阴影
    plt.pie(
        x =values,
        labels = labels,
        explode = explode,
        autopct="%3.1f %%",
        shadow=False,
        labeldistance=1.1,
        startangle=0,
        pctdistance=0.8,
        center=(-1,0),
    )

    #控制位置: 在bbox_to_anchor 数组中, 前者控制左右移动, 后者控制上下移动
    # ncol 控制图例所列的列数, 默认为1
    plt.legend(loc=7, bbox_to_anchor=(1.3, 1.0), ncol=3, fancybox=True, shadow=True, fontsize=6)
    plt.show()


if __name__ == "__main__":
    #getRatings("ml-1m/ratings.dat")
    getMovies("ml-1m/movies.dat")
