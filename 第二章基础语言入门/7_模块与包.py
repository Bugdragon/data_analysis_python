# 将自己模块导入
import pandas
print(pandas.__file__)
# 选择自己模块的文件夹
import sys
sys.path.append('C:\\Users\\Bugdragon\\Desktop\\数据探索\\python数据分析师\\第二章基础语言入门\\')
import tmodel
print(tmodel.f1(10))
print(tmodel.f2([1, 2, 3, 4, 5, 6, 8], 3))
print(tmodel.f3(10, 2, 5))
import tmodel as tm
print(tm.f1(5))
from tmodel import f3
print(f3(1,2,3))
# random模块
import random
x = random.randint(0,20)
y = random.random()
lst = list(range(100))
s = random.choice(lst)
print(s)
sli = random.sample(lst,5)
print(sli)
random.shuffle(lst)
print(lst)
# time模块
import time
for i in range(5):
    print('hello')
    time.sleep(0.1) # 延迟
print(time.ctime()) # 当前时间
print(time.localtime()) # wday周几,yday第几天,isdst是否为夏令时
print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))