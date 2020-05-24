# 都是string里自带的function
>>> x = 'zlp'
>>> y = len(x)  # len 表示有几个字母
>>> print(y)
3

>>> greet = 'Hello Bob'
>>> print(greet.lower())  #lower()表示全部字母都小写
hello bob

>>> greet = 'hello bob'
>>> yyy = greet.upper()  #upper()表示全部字母都大写
>>> print(yyy)
HELLO BOB

>>> nhm = greet.replace('bob','adam')
>>> print(nhm)
hello adam
>>> whh = greet.replace('o','p')
>>> print(whh)
hellp bpb

>>> s = 'lovely Python'
>>> print(s[:4])  # :表示从第一个字母到第四个但不含第四个
love
>>>

>>> fruit = 'pineapple'
>>> me = fruit.find('app') #找到'app'所在的位置，第一个字母是0
>>> print(me)
4

greet = ' hello li '
greet.lstrip()    #消除左空格
greet.rstrip()
greet.strip()      # 消除左右空格


>>> line = 'have a nice day'
>>> line.startswith('have')
True

>>> data = 'From zlp5005@gmail.com Prais France avril 9:14 2020'
>>> iwant = data.find('@')
>>> print(iwant)
12
>>> uwant = data.find(' ',iwant) # 注意‘’与‘ ’的区别，找到iwant前面的空格
>>> print(uwant)
22
>>> host = data[iwant+1:uwant] # 直到空格，但不包含空格
>>> print(host)
gmail.com

>>> total = 2012
>>> file = 3
>>> average = total / file
>>> print('the average size is:' + average)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print('the average size is:' + average)
TypeError: can only concatenate str (not "float") to str
>>> print('the average size is:' + str(average))
the average size is:670.6666666666666

>>> print(str("2+2= ")+str(int(2+2)))
2+2= 4
>>> print("2+2= " + str(int(2+2)))
2+2= 4

>>> def print_total(h, m, s):
	print(3600*h+60*m+1*s)

>>> print_total(1,2,3)
3723

def month_days(month, days):
	print(month + " has " + str(days) + " days.")
    # 注意month,days 不可加引号，要与上一行定义的一致

month_days("June", 30)  #在这里June 要加引号，否则NameError: name 'june' is not defined
month_days("July", 31)  #字母如果不是string，就没有output


>>> "cat" > "Cat"
True
