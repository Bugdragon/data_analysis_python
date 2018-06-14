path1 = 'C:\\Users\\Bugdragon\\Desktop\\数据探索\\python数据分析师\\第二章基础语言入门\\text.txt'
path2 = 'C:/Users/Bugdragon/Desktop/数据探索/python数据分析师/第二章基础语言入/text.txt'
path3 = r'C:\Users\Bugdragon\Desktop\数据探索\python数据分析师\第二章基础语言入门\text.txt'
print(path1,path2,path3)
# 读取文件：open
f = open(path1, 'r', encoding='utf8')
print(f)
print(f.read()) # 读取后光标在末尾
print('读取完毕')
print('二次读取')
print(f.read())
print('读取完毕')
f.seek(0) # 重置光标位置
print('三次读取')
print(f.read())
print('读取完毕')
f.close()
# os模块
import os
print(os.name) # 输出系统工作平台名字
print(os.getcwd()) # 当前工作目录
print(os.listdir()) # 目录下文件
os.chdir('C:/Users') # 改变工作路径
print(os.getcwd())
#os.remove('') # 删除文件
flst = os.path.split('C:/Users/Text.txt')
print(flst) # 分离成路径和文件名
print(os.path.exists('C:/Users/Text.txt')) # 判断路径或文件是否存在
# 文件读取-read
os.chdir('C:/Users/Bugdragon/Desktop/数据探索/python数据分析师/第二章基础语言入门/')
f = open('text.txt', 'r', encoding='utf8')
print(f.read(10))
print(f.read(10))
f.seek(0)
print(f.readline()) # 读取一行
f.seek(0)
for line in f.readlines(): # 遍历文件
    print(line)
# 文件写入-write
os.chdir('C:/Users/Bugdragon/Desktop/数据探索/python数据分析师/第二章基础语言入门/')
f_w = open('text_w.txt', 'w', encoding='utf8')
f_w.write('hello world!')
lst = ['1','2','3','4','5','6']
for i in range(len(lst)):
    lst[i] = lst[i] + '\n'
f_w.writelines(lst)
f_w.close()
print('finished!')
# 作业
lst1 = list(range(1,7))
lst2 = ['a','b','c','d','e','f']
f = open('text_zy.txt', 'w')
m = []
for i in range(len(lst1)):
    #lst = [str(lst1[i]),',',lst2[i]+'\n']
    lst = [str(lst1[i])+','+lst2[i]+'\n']
    m.append(lst)
    f.writelines(lst)
f.close()
print(m)
print('finished!')
# 存储：pickle(不改变数据结构)，模块序列化，反序列化
import pickle
data = {'a':[1,2,3], 'b':('string','abc'), 'c':'hello'}
pic = open('C:/Users/Bugdragon/Desktop/数据探索/python数据分析师/第二章基础语言入门/data.pkl','wb')
pickle.dump(data,pic)
pic.close()
print('finished!')
pic2 = open('C:/Users/Bugdragon/Desktop/数据探索/python数据分析师/第二章基础语言入门/data.pkl','rb') # 读取
data = pickle.load(pic2)
print(data)