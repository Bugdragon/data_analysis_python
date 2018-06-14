# coding=utf-8
# Number数字分为：int,float
x1 = 10
x2 = 10.0
print(x1, x2)
print(type(x1), type(x2))

# 字符串string
x3 = 'hello world'
x4 = "hehe"
x5 = '''a
b
c
'''
print(x3, x4)
print(x5)

# bool布尔型，用作判断
a = True
b = False
print(a == 1)
print(b == 0)
print(2 > 3)

# 列表list
lst = [1, 2, 3, 4, 5]
print(lst, type(lst))
lst2 = [1, 2.5, 'hello', [1, 2, 3]]
print(lst2[0], type(lst2[0]))

# 元组tuple，不可变
tup = (1, 2, 3, 4, 5)
lst = [1, 2, 3, 4, 5]
lst[0] = 100
print(lst)

# 字典dict，key/value
dic = {'a':100, 'b':'hello'}
print(dic['a'])

# 数据类型转换方法，int，float，str三者
var1 = 10
var2 = float(var1)
print(var2)
print(var2+1)
var3 = str(var1)
print(var3)
var4 = 10.456
print(int(var4))

a = 1
b = 10.0
name = 'jack'
a = b = c = 1
a, b, c = 1, 2, 'hello'
print(a, b, c)

# 算术运算符
a, b, c = 30, 7, 0
c = a % b # 取模，余数
print('a取b的模为', c)
c = a**b
print('a的b次方为', c)
c = a//b #取整
print('a关于c取整为', c)
print(1 >= 0)

# 逻辑运算符
print(True and False)
print(2==9 or 2<9)
print(not 2==9)
print(True == 1)
a, b, c, d = 10.0, 0 , 'hello', []
print(bool(a), bool(b), bool(c), bool(d)) #0和空为False

# 成员运算符：in/not in
lst = [1, 2, 3, 4, 5]
st = 'abcdef'
dic = {'a':1, 'b':2, 'c':3}
print(1 in lst)
print('h' in st)
print('d' not in dic)

m = []
for i in range(10):
    m.append('h'*i)
    #print(m)
print(m)