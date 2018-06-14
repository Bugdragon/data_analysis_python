import numpy as np
# 随机数生成
print(np.random.normal(size=(4,4)))
# 生成一个[0,1)之间的随即浮点数或N维浮点数组,均匀分布
a = np.random.rand(4)
print(a)
print(np.random.rand(2,4))
data1 = np.random.rand(500)
data2 = np.random.rand(500)
import matplotlib.pyplot as plt
plt.scatter(data1,data2)
plt.show()
# 正态分布
data3 = np.random.randn(500)
data4 = np.random.randn(500)
plt.scatter(data3,data4)
plt.show()
# 0~100
print(np.random.rand(2,4)*100)
# 随机整数[)
print(np.random.randint(2)) # [0,2)
print(np.random.randint(2,10)) # [2,10)
print(np.random.randint(2,size=10))
print(np.random.randint(10,50,size=(2,5)))
# 作业
a = np.random.randint(100,size=(10,10))
print(a)