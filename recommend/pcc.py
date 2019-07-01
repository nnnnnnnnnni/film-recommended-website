#计算皮尔逊距离
import pandas as pd
from math import sqrt
import numpy as np

f=open('./data/data0.6')
doc=open('./data/pcc.6','a')
data =[]
for line in f.readlines():
    arr=[]
    ls=line.strip().split(' ')
    for x in ls:
        arr.append(int(x))
    data.append(arr)

def multipl(a,b):
    sumofab=0.0
    for i in range(len(a)):
        temp=a[i]*b[i]
        sumofab+=temp
    return sumofab
 
def corrcoef(x,y):
    n=len(x)
    #求和
    sum1=sum(x)
    sum2=sum(y)
    #求乘积之和
    sumofxy=multipl(x,y)
    #求平方和
    sumofx2 = sum([pow(i,2) for i in x])
    sumofy2 = sum([pow(j,2) for j in y])
    num=sumofxy-(float(sum1)*float(sum2)/n)
    #计算皮尔逊相关系数
    den=sqrt((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n))
    return num/den

pc=[]
n=0
for i in data:
    x=[]
    for j in data:
        num=round(corrcoef(i,j)*0.5+0.5,8)
        doc.write(str('{:f}'.format(num))+' ')
        n+=1
        print(str(n)+'/'+str(1586126))
    doc.write('\n')
