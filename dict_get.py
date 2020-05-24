# Dictionaries 像是一个无秩序的大袋子，每件物品都由一把钥匙掌管
# 有python最强大的数据收集，让数据快速操作，跟c++的property bag是一样的
bag = dict() #建立一个词典
bag['pencil'] = 0 #词典里的0用index‘pencil’可以打开看到
bag['erasal'] = 1
bag['paper'] = 99
print(bag)
{'pencil': 0, 'erasal': 1, 'paper': 99} #大括号，冒号，逗号
print(bag['paper'])  #打开‘paper’看看里面是什么
99
bag['paper'] = bag['paper'] + 1  #在paper里加上1, this key keep adding itself with 1
print(bag)
{'pencil': 0, 'erasal': 1, 'paper': 100}
print(bag['paper'] + bag['pencil']) # 也可以对里面的钥匙进行换算
100
print(bag['paper'] * bag['pencil']) # the keys can be calculated between them
0
# lists与dictionaries不同之处：list用顺序0开始.dictionarie用index
# 比如要看一份文件内的某个名字出现多少次，每出现一次+1
# 在dictionarie里查找某样东西在不在里面
'erasal' in bag
True
# 计算一个袋子里每样东西有几件
bag = dict()
things = ['foie','liver','heart','paper','pencil','heart','liver']
for thing in things:
	if thing not in bag:
		bag[thing] = 1
	else:
		bag[thing] += 1


print(bag)
{'foie': 1, 'liver': 2, 'heart': 2, 'paper': 1, 'pencil': 1}

# The get() method for Dictionaries  去包里找某把钥匙，看是否在
bag = dict()
things = ['foie','liver','heart','paper','pencil','heart','liver']
for thing in things:
	bag[thing] = bag.get(thing,0) + 1 # get()如果见过，thing=1,再+1
                             #默认这样东西为0，现在才见到，自动+1

print(bag)
{'foie': 1, 'liver': 2, 'heart': 2, 'paper': 1, 'pencil': 1}

# 输入一段文字，计算文字里每个单词出现几次
counts = dict() #counts是一个袋子
line = input('Enter a line of text: ')
words = line.split()  #把一个string变成list
print('Words: ',words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word,0) + 1  #袋子里装了word,每见一个word，就+1
     #已经命名为word的袋子 要去袋子里找every word
print('Counts', counts) #袋子里每个word列出来，每个出现几次
