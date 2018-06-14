import numpy as np
# 基本索引及切片
ar = np.arange(20)
print(ar)
print(ar[4])
print(ar[:3])
print(ar[::2])
ar = np.arange(16).reshape(4,4)
print(ar)
print(ar[2])
print(ar[2][2])
print(ar[2,2]) # [行索引,列索引]
print(ar[1:3])
print(ar[:1,2:]) # 左闭右开
ar = np.arange(12).reshape(3,2,2) # 3个2x2
print(ar)
print(ar[2][1][0])
print(ar[2,1,0])
print(ar[:2,:,1:])
# 布尔型索引及切片
ar = np.arange(12).reshape(3,4)
print(ar)
i = np.array([True,False,True])
j = np.array([True,True,False,False])
print(i,j)
print(ar[i]) # 保留True行
print(ar[:,j])
print(ar>5) # 布尔矩阵
print(ar[ar>5])
# 索引及切片的值更改、复制
ar = np.arange(10)
print(ar)
ar[5] = 100
ar[7:9] = 200
print(ar)
ar = np.arange(10)
b = ar.copy()
b[7:9] = 200
print(ar)
print(b)
# 作业
ar = np.arange(25).reshape(5,5)
print(ar)
print(ar[4])
print(ar[:2,3:])
print(ar[3][2])
ar = np.arange(10).reshape(2,5)
b = ar[ar>5]
print(b)