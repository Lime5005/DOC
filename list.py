friends = ['j', 'g', 's']  # a list is a kind of collection,用中括号，中间逗号隔开
print(['red', 24, 98.6, [5, 6]])  # 里面可以有任何object, even another list

friends = ['j', 'g', 's']
print(friends[1])
g   # 在list中选择第1个打印

zzz = [1, 12, 13, 14]
zzz[3] = 18    #改变list中的第3位，即14
print(zzz)
[1, 12, 13, 18]  #结果改变

#len 用来数数， 一个string或者一句话，数多少个字母包括空格
x = [1, 2, 3, 'j', 99]
print(len(x)) #这里的len是数有几个元素
5

# Concatenating list using + 并联list中的元素用+
a = [1,2]
b = [3,4]
c = a + b
print(c)
[1,2,3,4]
# Lists can be sliced using
m = [1,2,3,4,5,6]
t[1:3] #列出从1到3的元素,但不包含3
[2,3]

dir() # dir列出任何object的属性和方式

stuff = list() #建立一个空的list
stuff.append('book') # 在list里加上'book'这个元素
stuff.append(0) #在list里加上0这个元素
print(stuff)
['book', 0]

# "in" or "not in" a list
>>> some = [1, 9, 10, 11, 18]
>>> 1 in some   # 是否？
True
>>> 20 not in some
True

# sort methond  整理list, strings are not mutable, but list yes
friends = ['j', 'g', 's']
>>> friends.sort()
>>> print(friends)
['g', 'j', 's']
>>> print(friends[0])
g

#在list中有几个内置的functions，比如len, max, min, sum
>>> some = [1, 9, 10, 11, 18]
>>> print(sum(some))
49
>>> print(max(some))
18
print(sum(some)/len(some)) # 求平均值
9.8
