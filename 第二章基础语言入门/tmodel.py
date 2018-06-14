def f1(n):
    y = 1
    for i in range(1,n+1):
        y = y * i
    return y

def f2(lst,x):
    while x in lst:
        lst.remove(x)
    return lst

def f3(a,d,n):
    an = a
    s = 0
    for i in range(n):
        s = s + an
        an = an + d
    return s
