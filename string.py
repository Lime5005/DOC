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
