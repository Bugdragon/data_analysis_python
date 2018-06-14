dic = {'a':1, 'a':2}
print(dic) # 记住后一个值
# key必须是字符串，value可以是任意对象
dic = {'小明':18, '小红':17, '小王':19}
lst = list(range(10))
print(lst)
print(dic)
dic['小张'] = 16
del dic['小明']
print(dic)
dic.clear()
print(dic)
del dic # 删除词典

# 字典的声明
dic = {'a':'hello', 'b':100}
dic1 = dict(jack=20, marry=19, jone=25)
print(dic1)
# 复合序列
lst = (('a',1), ('b',2))
dic2 = dict(lst)
print(dic2)
keys = ['a','b','c']
dics = dict.fromkeys(keys, 0)
print(dics)
keys = ['语文', '数学', '外语', '物理']
grade = dict.fromkeys(keys, 60)
print(grade)

# 字典的常用操作
dic1 = {'a':1, 'b':2}
dic2 = {'c':3, 'd':4}
dic1.update(dic2) # 字典更新
print(dic1, dic2)
dic3 = dic2.copy() # copy方法，改变dic2不改变dic3
dic2.update({'f':100})
print('原字典', dic2, '复制后字典', dic3)
print(len(dic1))
print('a' in dic1) # 用key判断是否在字典中
print(1 in dic1)
data = [{'name':'Jack1', 'age':18},
        {'name':'Jack2', 'age':19},
        {'name':'Jack3', 'age':20}]
for i in data:
    print(i['age'])

# 字典元素的访问
dic = {'a':1, 'b':2}
print(dic['a'])
print(dic)
poi = [{'a':1, 'b':2, 'information':{'c':100, 'd':4}},
        {'a':1, 'b':2, 'information':{'c':3, 'd':4}}]
print(poi[0]['information']['c'])
print(dic.get('a')) # 查看key的value
print(dic.get('type', print('nothing')))
print(dic.keys(), type(dic.keys())) # keys()方法输出所有key
print(list(dic.keys())) # 内容格式是视图
print(dic.values()) # 输出所有value
print(list(dic.items())) # 输出所有元素
poi = {'a':1, 'b':2, 'information':{'c':100, 'd':4}}
for keys in poi:
    print(keys)
print('--------')
for values in poi.values():
    print(values)
print('--------')
for keys in poi:
    print(poi[keys])
print('--------')
for (k,v) in poi.items():
    print('key为%s, value为%s' %(k,v))
print(1 in poi.values())