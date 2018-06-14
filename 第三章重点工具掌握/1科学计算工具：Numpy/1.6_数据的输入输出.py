import numpy as np
# 存储数组数据.npy文件
import os
os.chdir('C:/Users/Bugdragon/Desktop/python数据分析师/第三章重点工具掌握/1科学计算工具：Numpy')
ar = np.random.rand(5,5)
np.save('test.npy',ar)
# 记事本分隔符存储
np.savetxt('test1.npy',ar,delimiter=',',fmt='%.2f')
print('finished!')
# 读取数组数据.npy文件
ar_read = np.load('test.npy')
print(ar_read)
ar_readtxt = np.loadtxt('test1.npy',delimiter=',')
print(ar_readtxt)
# 作业
a = np.random.randint(100,size=(10,10))
np.savetxt('zuoye.npy',a,delimiter=',',fmt='%i')
print('finished!')
ar_readzuoye = np.loadtxt('zuoye.npy',delimiter=',')
print(ar_readzuoye.astype(np.int))