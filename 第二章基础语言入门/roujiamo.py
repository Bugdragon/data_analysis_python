# 读取txt，转换成json即字典列表
import os

os.chdir('C:/Users/Bugdragon/Desktop/数据探索/python数据分析师/第二章基础语言入门/')
f = open('roujiamo.txt', 'r', encoding='utf8')
m = []
n = 0
f.seek(0)

for line in f.readlines():
    n += 1
    st1 = line.split(':')
    name = st1[0].strip() # 名称
    infor = st1[1]
    st2 = infor.split(',')
    lng = float(st2[0]) # 经度
    lat = float(st2[1]) # 纬度
    add = st2[2].strip() # 地址，去掉空格
    data = (('name',name),('lng',lng),('lat',lat),('address',add))
    m.append(dict(data))
    print(dict(data))
print(m[:10])
print('总共转换数据%i条' %n)
