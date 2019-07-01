#基于随机矩阵分解Random matrix decomposition
import pandas as pd
from numpy import *
import numpy
import matplotlib.pyplot as plt
import datetime,time

s1 = datetime.datetime.now()   #start time

#读取文件
def load_data(path):
    f = open(path)
    data = []
    for line in f.readlines():
        arr = []
        lines = line.strip().split(" ")
        for x in lines:
            if x != "-":
                arr.append(float(x))
            else:
                arr.append(float(0))
        data.append(arr)
    print('数据加载完毕'+str(datetime.datetime.now()-s1))
    return data

#数据矩阵化，并写入文件
# data =load_data('./ml-100k/data') 
# rating = numpy.zeros((944,1683),dtype=int)   
# for i in range(100000):
#     rating[int(data[i][0]),int(data[i][1])]=int(data[i][2])

# rf=open('rating','a')
# ff=open('record','a')
# for i in range(1,944):
#     for j in range(1,1683):
#         rf.write(str(rating[i][j])+' ')
#         if rating[i,j] != 0 :
#             ff.write('1 ')
#         else:
#             ff.write('0 ')
#     rf.write('\n')
#     ff.write('\n')

loss_arr=[]
#基于传统随机矩阵分解
def gradAscent(data, K):
    dataMat = mat(data)
    print( dataMat)
    m, n = shape(dataMat)
    p = mat(random.random((m, K)))
    q = mat(random.random((K, n)))
    # p = mat(load_data('./data/p2'))
    # q = mat(load_data('./data/q2'))

    alpha = 0.0002
    beta = 0.02
    maxCycles = 10000

    for step in  range(maxCycles):
        loop_start=datetime.datetime.now()
        for i in  range(m):
            for j in  range(n):
                if dataMat[i,j] > 0:
                    error = dataMat[i,j]
                    for k in  range(K):
                        error = error - p[i,k]*q[k,j]
                    for k in  range(K):
                        p[i,k] = p[i,k] + alpha * (2 * error * q[k,j] - beta * p[i,k])
                        q[k,j] = q[k,j] + alpha * (2 * error * p[i,k] - beta * q[k,j])

        loss = 0.0
        for i in  range(m):
            for j in  range(n):
                if dataMat[i,j] > 0:
                    error = 0.0
                    for k in  range(K):
                        error = error + p[i,k]*q[k,j]
                    loss = (dataMat[i,j] - error) * (dataMat[i,j] - error)
                    for k in  range(K):
                        loss = loss + beta * (p[i,k] * p[i,k] + q[k,j] * q[k,j]) / 2

        if loss < 0.001:
            break
        #print step
        loss_arr.append(loss)
        if step % 1000 == 0:
            print('step ' +str(step)+',loss:'+str(loss)+',loop_time:'+str(datetime.datetime.now()-loop_start))

    return p, q

if __name__ == "__main__":
    dataMatrix = load_data("./data/data0.8")

    p, q = gradAscent(dataMatrix, 5)

    result = p * q
    # doc=open('./data/rmd','a')
    # fp=open('./data/p3','a')
    # fq=open('./data/q3','a')
    # a,b=shape(result)
    # pa,pb=shape(p)
    # qa,qb=shape(q)
    # for i in range(a):
    #     for j in range(b):
    #         doc.write(str('{:f}'.format(result[i,j]))+' ')
    #     doc.write('\n')
    # for i in range(pa):
    #     for j in range(pb):
    #         fp.write(str('{:f}'.format(p[i,j]))+' ')
    #     fp.write('\n')
    # for i in range(qa):
    #     for j in range(qb):
    #         fq.write(str('{:f}'.format(q[i,j]))+' ')
    #     fq.write('\n')
    
    print(result)
    
    n=len(loss_arr)
    x=range(n)
    plt.plot(x,loss_arr,color='r',linewidth=3)
    plt.title("Convergence curve")
    plt.xlabel("generation")
    plt.ylabel("loss")
    plt.show()

#https://blog.csdn.net/google19890102/article/details/51124556
#http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/
#1000 0.16509452722557558
#2000 0.08491509778876713