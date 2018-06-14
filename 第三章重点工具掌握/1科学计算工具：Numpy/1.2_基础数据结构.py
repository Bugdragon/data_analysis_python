import numpy as np

ar = np.array([[1,2,3,3,4,5],[1,2,3,4,5,6]])
print(ar)
print(ar.ndim) # 轴,维度
print(ar.shape) # n行m列
print(ar.size) # 元素总数
print(ar.dtype) # 数值数据类型
print(ar.itemsize) # 元素的字节大小
print(ar.data) # 位置
# 创建数组,列表,元组,数组,生成器
ar1 = np.array(range(10))
ar2 = np.arange(10)
ar3 = np.array([1,2,3,4,5])
ar4 = np.array([[1,2,3,4,5,6],['a','b','c''d']])
print(ar1,ar2,ar3,ar4.ndim)
print(np.random.rand(10).reshape(2,5))
# linspace():[开始,停止]计算num个均匀间隔的样本
print(np.linspace(10,20,num=21,endpoint=False))
print(np.linspace(10,20,num=21,retstep=True))
print(np.zeros((2,5),dtype=np.int)) # 创建数值为0的数组
ar = np.array([list(range(10)),list(range(10,20))])
print(np.zeros_like(ar))
print(np.ones(9))
print(np.ones_like(ar))
print(np.eye(5))
# 作业
ar00 = np.array([1,2,'a','hello',[1,2,3],{'two':200,'one':100}])
print(ar00,ar00.shape)
ar01 = np.array([['0','1','2'],['a','b','c'],['True','False','True']])
print(ar01,ar01.shape)
print(np.linspace(5,15,num=10,endpoint=False,dtype=int))
print(np.zeros((4,4)))
print(np.ones((2,3)))
print(np.eye(3,dtype=int))