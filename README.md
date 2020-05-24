g = dict()
>>> things = ['foie','liver','heart','paper','pencil','heart','liver']
>>> for thing in things:
    if thing not in bag:
       	     bag[thing] = 1
	     		else:
					bag[thing] += 1


>>> print(bag)
{'foie': 1, 'liver': 2, 'heart': 2, 'paper': 1, 'pencil': 1}

# The get() method for Dictionaries  去包里找某把钥匙，看是否在
>>> bag = dict()
>>> things = ['foie','liver','heart','paper','pencil','heart','liver']
>>> for thing in things:
    bag[thing] = bag.get(thing,0) + 1 # get()如果见过，thing=1,再+1
                                 #默认这样东西为0，现在才见到，自动+1

>>> print(bag)
{'foie': 1, 'liver': 2, 'heart': 2, 'paper': 1, 'pencil': 1}

# git







    