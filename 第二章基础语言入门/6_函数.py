'''
abs(a)求绝对值
max,min,sum
sorted(list)返回排序后的list
len
divmod(a,b)获取商和余数
pow乘方
round(a,b)指定位数小数，a浮点数，b位数
range(a,b)a到b的数组，左闭右开
'''
print(eval('1+2+3')) # 执行字符串
exec("print('hello')") # 执行python语句
help(print) # 调用内置帮助

# 自定义函数
def f():
    print('hello')
f()
# 默认参数
def f(x, n=2):
    return (x**n)
print(f(10), f(10, 3))
# 可变参数,默认元组
def f(*x):
    return (x)
print(f(1,2,3,4,5,6))
# 作业
def f(st):
    for s in st:
        print(s)
st = input('输入字符串:')
f(st)
def f(a,b,c):
    y = ((a+b)*(a-b))*c
    return y
print(f(5,4,2))
def f(*m):
    s = 0
    lst = []
    for i in m:
        while str(i).isnumeric():
            s += i
            lst.append(i)
            break

        else:
            print('输入内容包含非数字!')
    return s/len(lst)
print(f(1,2,'a',4,5))
def area_jx(a,b):
    return a*b
def area_yx(r):
    return 2*r*3.14
print(area_jx(10,5), area_yx(10))
lst = eval(input('请输入一个列表：')) # 执行字符串语句
def f(lt):
    return dict.fromkeys(lt, 0)
print(f(lst))

# global局部变量变为全局变量
def f():
    global a
    a = '呵呵'
    print('函数内转换为全局变量：%s' %a)
a = input('请输入一个数字：')
print('输入变量值：%s' %a)
f()

# 匿名函数lambda
f = lambda a,b,c:a+b+c
print(f(2,3,4))
count = lambda lst:len(lst)
print(count([1,2,3,4]))
def f(*var):
    lst = list(var)
    return sorted(lst, reverse=True)
print(f(2,33,4,55))
def f(*scores):
    s = 0
    m = []
    for i in scores:
        if i > 90:
            m.append('A')
        elif i > 60 and i < 90:
            m.append('B')
        else:
            m.append('C')
        s += i
    mean = s / len(scores)
    return [m,mean]
result = f(89,96,20,45)
print(result[0])
print(result[1])
st = 'abcd rsd'
st.isalpha()
st.isspace()
st.isdigit()