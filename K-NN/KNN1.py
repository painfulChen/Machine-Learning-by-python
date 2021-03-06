# -*- coding: UTF-8 -*-

import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


""" 产生高斯随机数据作为样本数据集
    
    Parameters
    ----------
    mean :  高斯均值
    sigma :  高斯函数方差
    count: 要产生的数据个数
    ----------
    return : 产生的数据列表
"""
def GaussNum(mean,sigma,count):
    res = [0] * count
    for i in range(count):
        res[i] = random.gauss(mean,sigma) 
    return res

""" 计算点与点之间的距离，这里里二维数据为例
    
    Parameters
    ----------
    inX :  测试样本，数组
    x :  x
    y: y
    ----------
    return : 测试样本与（x，y）的距离
"""
def Distance_for_dot(inX,x,y):
    size = len(inX)
    sum = 0
    for i in range(size):
        sum += ((inX[0] - x) ** 2 + (inX[1] - y) ** 2)
    return sum ** 0.5

""" knn分类
    
    Parameters
    ----------
    inX :  测试样本，数组
    x :  x
    y: y
    labels: 数据样本标签
    k: knn中k值，为选取最近点的数量
    ----------
    return : inX被判定的划分类
"""
def knn_Classify(inX,x,y,labels,k):
    
    # 计算样本数据的个数
    dataSetSize = len(x)
    # 建立数组，用来存放测试数据与每个样本数据的距离
    distances_for_eachSample = np.tile([0],dataSetSize) 
    # print(type(distances_for_eachSample))
    # 数据与标签dict，key值为距离，value值为该样本数据的类别，这里假设所有距离都不相等
    data_and_label = {}
    # 对于样本数据集，一次求距离，并且与自己的类别合并，存入data_and_label
    for i in range(dataSetSize):
        distances_for_eachSample[i] = Distance_for_dot(inX,x[i],y[i])
    # 此处，排序得到的是索引index，按照此index可以将array进行排序
    sort_Index = distances_for_eachSample.argsort()

    vote = {}
    for i in range(k):
        ith_label = labels[sort_Index[i]]
        #get(ith_label,0) : if dictionary 'vote' exist key 'ith_label', return vote[ith_label]; else return 0  
        vote[ith_label] = vote.get(ith_label,0)+1 
    sortedvote = sorted(vote.items(),key = lambda x:x[1], reverse = True)  
    
    print(sortedvote)
    draw_point(inX,sortedvote[0][0])
    print("the result is : %s" %sortedvote[0][0])

# 画单点
def draw_point(inX,color):
    plt.scatter(inX[0],inX[1],c=color,marker='*',s=400,alpha=0.8)
    

# 产生训练数据集，在数据集中自动分为三类，并且画出图
def data_generate():
    x1 = GaussNum(15,7,200)
    y1 = GaussNum(20,7,200)

    x2 = GaussNum(30,7,200)
    y2 = GaussNum(50,8,200)

    x3 = GaussNum(5,7,200)
    y3 = GaussNum(40,7,200)

    plt.scatter(x1,y1,c='b',marker='s',s=50,alpha=0.8)
    plt.scatter(x2,y2,c='k',marker='^',s=50,alpha=0.8)
    plt.scatter(x3,y3,c='r',marker='o',s=50,alpha=0.8)
    # 这里list可以直接用 + 合并
    x = x1 + x2 + x3
    y = y1 + y2 + y3
    labels = ["blue"]*200+["black"]*200+["red"]*200

    return x,y,labels


if __name__ == '__main__':
    x,y,labels = data_generate()
    for i in range(3):
        knn_Classify([20 - (i-1) * 10,40 - (i-1) * 10 ],x,y,labels,20)
    
    plt.show()


