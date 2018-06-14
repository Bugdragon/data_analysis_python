x = 1
print(type(x))
x = 1.0
print(type(x))
x = 'hello'
print(type(x))

# 可变序列：列表list
# 不可变序列：元组tuple，字符串str
# *生成器：range

# 判断值是否属于序列
lst = [1,2,3,4,5,6,7,8]
a,b,c = 1,2.0,'hello'
print(a in lst)
print(b in lst) # 值相同
print(c not in lst)

# 序列连接与重复
lst1 = [1,2,3]
lst2 = ['a', 'b']
print(lst2 + lst1) # 序列有顺序
lst1.append(lst2)
print(lst1)
print(lst1*3)

# 下表索引
print(lst)
print(lst[0], lst[2], lst[7])
print(lst[-1], lst[-3]) # 倒数的值
lst[4] = 'hello'
print(lst)

# 切片
print(lst[0:2]) # 左闭右开区间，[0,2)
print(lst[2:5])
print(lst[:5])
print(lst[1:-1])

# 步长
lst = 'abcdefght'
print(lst)
print(lst[2:7:2]) # 最后一个数，步长为2
print(lst[:6:3])
print(lst[1::2])
print(lst[::2])

# 序列的基本内置全局函数
lst = [1,2,3,4,5,6,7,8,9,0]
print(len(lst))
print(max(lst), min(lst), sum(lst)) # 函数
print(lst.index(0)) # 查找索引编号(返回第一个匹配项)，0的索引是9
lst = [1,1,2,3,3,4,6,6,6,6,6]
print(lst.count(6)) # 方法

lst = [1,2,3,'abc',[1,2,3]]
print(lst[-1][2])

lst = list(range(4,10,2)) # 步长2
print(lst)
m = range(10)
print(m)
print(m[2], m[-1])

lst = list(range(10))
print(lst + [1,2,3]) # lst不变
print(lst)
lst.append('a') # lst改变
print(lst)

a = [1,2,3]
b = [4,5,6]
a.append(b)
print(a)
a.extend(b) # 用新列表扩展原来的列表
print(a)

lst = ['Jack', 'Jack', 'Tom', 'Tracy', 'Alex', 'White']
lst.remove('Jack')
print(lst) # 移除第一个匹配项
lst.pop(2)
print(lst)
del lst[3:5]
print(lst) # 删除相应索引值
lst.clear()
print(lst) # 移除所有值

lst = [1,2,3]
lst.insert(2,'h') #索引i处插入m
print(lst)

x = list(range(10))
m = x # 同一引用
m = x.copy() # 复制，不同引用
print(x,m)
x[2] = 101
print(x,m)

lst1 = list(range(10,20))
lst2 = ['abc', 'sdfg', 'ssw']
lst1.sort(reverse=True) # 逆序
lst2.sort()
print(lst1, lst2)
lst1 = [1,22,3,4,66,5]
lst3 = sorted(lst1) # 排序并复制，原列表不变
print(lst1,lst3)

tup1 = 'a', 'b', 'c'
tup2 = (1,) # 元组只包含一个元素，需要在后面添加逗号
tup = (1,2,3,4,5)
del tup # 直接删除元组
print(tup1+tup2)
print(len(tup1))
print(tup2*3)
tup = (1,2,3,4,5)
print(max(tup))

lst = list(range(10))
tup = tuple(lst)
print(tup)
lst = list(range(10))
lst.extend('abc')
print(lst)

# 转义字符
print('\'')
print('a\nb')
print(r'c:\\Users\\Bugdragon')
st = 'adasdaww'
print('st长度为' + str(len(st)))

# 字符串常用功能
st = 'I am handsome'
st2 = st.replace('handsome', 'ugly') # 生成新字符串
print(st, st2)
st = 'hahaha'
st2 = st.replace('ha', 'he', 2) # 更改2个
print(st2)

st = 'poi01 116 44634 39.001'
lst = st.split(' ') # 字符串拆分为列表
print(lst)
m = '-'
st2 = m.join((lst)) # 列表连接成字符串
print(st2)

st = 'abDsha Lkd'
print(st.startswith('a'), st.endswith('k'))
print(st.upper()) # 全部大写
print(st.lower()) # 全部小写
print(st.swapcase()) # 大小写互换
print(st.capitalize()) # 仅首字母大写
st = '1223123'
print(st.isnumeric()) # 是否全是数字
st = 'DSADA'
print(st.isalpha()) # 至少有一个字符，并且所有字符都是字母
st = 'avd '
print(st.rstrip()) # 删除末尾空格

# 格式化字符：在字符串中插入变量
name = 'hehehe'
truth = '%s is 好人' %name
print(truth)
x = 4
y = 'hehe'
z = 4.2
print('this is %i' %x) # 整型
print('this is %s' %y) # 字符型
print('this is %f' %z) # 浮点型
print('小明的成绩为%i，小红的成绩为%i' %(70,90)) # 序列
m = 3.5455
print('pi is %f' %m)
print('pi is %.2f' %m) # 两位小数，四舍五入
print('pi is %.0f' %m)
m = -100
print('have fun %i' %m)
print('have fun %.2f' %-0.01)
m = 123123123.123123123
print('have fun %.2e' %m)
print('have fun %.4E' %m) # 科学计数法
print('have fun %.2g' %m) # 两位有效位数
m1 = 1.2
print('have fun %g' %m1) # 位数少用浮点，数据复杂自动识别用科学记数法

# 格式化：format
print('今天天气怎么样{}'.format('，非常好'))
st = '您好！{}'
print(st.format('谢谢！'))
print('{}{}{}'.format('a', 'b', 'c'),'\t',
      '{0}{1}{2}{0}'.format('a', 'b', 'c'),'\n') # 指定顺序
print('User ID:{0}'.format('root'))
print('{}呵呵{}'.format('a', 'b'))
print(('我的工作是{work}'.format(work = '设计'))) # 用变量来指示
a = st.format('谢谢！')
print(a, st)
print('{:f}'.format(4.123), '\n',
      '{:.2f}'.format(4.123), '\n',
      '{:e}'.format(4.123), '\n',
      '{:.0f}'.format(99.9), '\n', # 四舍五入
      '{:%}'.format(4.123), '\n', # 百分比
      '{:d}'.format(10), '\n', ) # 整型
print('今年产值增长了%.2f%%' %12.345)

# 作业
a = '''
a
b
c
'''
print(a)
str1 = 'c:\\a\\a'
print(str1)
print(33+int('22'))
print('22'+str(55))
m = 'a,b,c'
print(m.split())
n = '.'
print(n.join(m.split(',')))
print('abc%s' %'aa')
str2 = '我的工作是{0}，我喜欢{1}'
print(str2.format('编程', '打羽毛球'))