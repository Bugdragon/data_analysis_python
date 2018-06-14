def f():
    print('hello world')
f()
# if语句
age = 20
if age < 18:
    print('18岁以下不能')
    print('haha')
print('finished!')
score = float(input('请输入成绩:\n'))
print('该学生成绩为%s' %score)
age = int(input('年龄为:'))
if age < 18:
    print('18岁以下不能')
else:
    print('可以')
print('finished!')
score = int(input('请输入成绩:'))
if score < 0 or score > 100:
    print('error')
elif score >= 60:
    print('及格')
elif score < 60:
    print('不及格')
# for循环
st = input('输入字符串:')
for s in st:
    print(s)
lst1 = ['a', 'b', 'c']
lst2 = [1,2,3]
m = []
for i in range(3):
    lsti = (lst1[i], lst2[i])
    print(lsti)
    m.append(lsti)
print(dict(m))
# while循环
count = 0
while count < 9:
    print('the count is', count)
    count += 1
else:
    print('bye bye')
# break终止循环
# continue跳出该次循环
# pass空语句，保持程序结构的完整性
