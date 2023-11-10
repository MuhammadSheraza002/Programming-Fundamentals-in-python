import collections

# Counter() Attribute

string = 'aaabbcccddddhhjjdjj'
my_counter = collections.Counter(string)
print('my_counter: ',my_counter)
#my_counter.elements() gives whole string
print('my_counter.elements(): ',list(my_counter.elements()))
print('my_counter.my_counter.items() : ',my_counter.items())
print('my_counter.my_counter.keys() : ',my_counter.keys())
print('my_counter.my_counter.values() : ',my_counter.values())

# MOST COMMON ATTRIBUTE
# it will return list with tuple in it
print('my_counter.most_common(1): ',my_counter.most_common(1)) # it gives 1 most comming chareacter
print('my_counter.most_common(2): ',my_counter.most_common(2)) # it gives 2 most comming chareacter
print('my_counter.most_common(4): ',my_counter.most_common(4)) # it gives 4 most comming chareacter

#                              Indexing of dictionaries
print('my_counter.most_common(4)[1][1]: ',my_counter.most_common(4)[1][1])

# using loop Indexing of dictionaries

# namedtuple() Attribute
Point1 = collections.namedtuple('Point1','x,y')
point = Point1(2,3)
print('Point1(2,3): ',point)
print(f'Point1.x\t=\t{point.x}\tand\tPoint1.y\t=\t{point.y}')

#collections.OrderedDict gives vsimple dictioary but in ordered
ordered_dictionary = collections.OrderedDict()
ordered_dictionary['b'] = 2
ordered_dictionary['c'] = 3
ordered_dictionary['d'] = 4
ordered_dictionary['e'] = 5
ordered_dictionary['a'] = 1
print('ordered_dictionary: ',ordered_dictionary)

#                               defaultdict give
#d = collections.defaultdict(datatype) data type can be int,float,list,tuple e.t.c
# this method gives default values iff that value does not acces
# this default value is different for different data typres
#0 for int, and also for string
#0.0 for float

#For int data type
d = collections.defaultdict(int)
d['a'] = 1
d['b'] = 2
print('d["a"]: ',d['a'])
print('default value: ',d['c'])

#For float data type
d = collections.defaultdict(float)
d['a'] = 1.1
d['b'] = 2
print('d["a"]: ',d['a'])
print('default value: ',d['c'])

#For float data type
d = collections.defaultdict(float)
d['a'] = 'a'
d['b'] = 'b'
print('d["a"]: ',d['a'])
print('default value: ',d['c'])

#Normal dictionary give error
'''
d = {}
d['a'] = 'a'
d['b'] = 'b'
print('d["a"]: ',d['a'])
print('default value: ',d['c'])
'''
# deque method
d = collections.deque()
d.append(1)
d.append(2)
print('d: ',d)

#d.leftappend(4) append on left side
d.appendleft(3)
print('d.appendleft(3): ',d)

#d.leftappend(4) append on left side
d.extendleft([51,65,78])
print('d.extendleft([51,65,78]): ',d)

#d.rotate(n) rotates n numbers from right
d.rotate(1) #rotate 1 element from right and placed at 0 index
print('d.rotate(1): ',d)
d.rotate(2)#rotate 2 element
print('d.rotate(2): ',d)
d.rotate(4)     # rotate 4 element
print('d.rotate(4): ',d)

# rotate(-1) rotate all elements
d.rotate(-1)
print('d.rotate(-1): ',d) #rotate all element

#d.pop() remove 1 index from right
d.pop()
print('d1.pop(): ',d)

#d.popleft() remove  index from left
d.popleft()
print('d1.pop(): ',d)

