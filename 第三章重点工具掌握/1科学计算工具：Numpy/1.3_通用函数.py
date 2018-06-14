import numpy as np

ar1 = np.arange(16)
ar2 = np.zeros((2,5))
print(ar1,ar1.T) # 转置
print(ar2,ar2.T)
print(ar2.reshape(5,2))
print(ar1.reshape(8,2))
print(np.reshape(np.arange(16),(2,8)))
print(np.resize(np.arange(5),(3,4))) # 少重复，多选择
print(np.zeros((2,5)).reshape(10))
# 数组复制
ar1 = np.arange(10)
ar2 = ar1
ar1[2] = 100 # 同时更改
print(ar1,ar2)
ar3 = ar1.copy()
ar1[3] = 1000
print(ar1,ar3)
s = np.arange(10)
print(np.resize(s,(2,6))) # 生成新数组
print(s.resize(2,6)) # 改变数组本身
print(s)
# 改变数组类型
ar1 = np.arange(10,dtype=float)
ar2 = ar1.astype(np.int64)
print(ar1,ar2)
# 数组堆叠
a = np.arange(5)
b = np.arange(5,9)
print(a,b,np.hstack((a,b))) # 横向连接
a = np.array([[1],[2],[3]])
b = np.array([['a'],['b'],['c']])
print(a,b,np.vstack((a,b))) # 纵向连接
a = np.arange(5)
b = np.arange(5,10)
print(a,b,np.stack((a,b),axis=1)) # 按列横向连接
print(a,b,np.stack((a,b))) # 按行纵向连接
# 数据拆分
ar = np.arange(16).reshape(4,4)
print(np.split(ar,2))
print(np.hsplit(ar,4)) # 横向拆分
print(np.vsplit(ar,4)) # 纵向拆分
# 作业
ar = np.arange(20)
print(np.reshape(ar,(4,5)),np.resize(ar,(5,6))) # 生成新数组
ar = np.arange(16).reshape(4,4)
print(ar.astype(np.str))
ar = np.arange(16).reshape(4,4)
print('创建数组为：\n',ar)
result = ar * 10 + 100
print('计算后的数组为：\n',result)
print('result的均值为：\n',np.mean(result))
print('result的求和为：\n',np.sum(result))