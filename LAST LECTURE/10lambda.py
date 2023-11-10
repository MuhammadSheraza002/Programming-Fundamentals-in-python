# lambda functions
def power(n):
	return lambda a: a ** n

# base = lambda a : a**2 get
# returned to base
base = power(2)

print("Now power is set to 2")

# when calling base it gets
# executed with already set with 2
print("8 powerof 2 = ", base(8))

# base = lambda a : a**5 get
# returned to base
base = power(5)
print("Now power is set to 5")

# when calling base it gets executed
# with already set with newly 2
print("8 powerof 5 = ", base(8))

print()

# Program to filter out only the even items from a list
#filter(functiuon,sequnce) sequence can be list or other type
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)
print()

s = 2
x = lambda s: s+5*2
print(x(2))
print()

#map(functiuon,sequnce) sequence can be list or other type
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)
print()

#reduce(functiuon,sequnce) sequence can be list or other type
import functools
list1 = [1,2,3,4,5]
product_of_list1 = functools.reduce(lambda x,y:x*y ,list1)
print('product_of_list1: ',product_of_list1)
print()

'''
            (1) sort  w.r.t x-axis is with this sorted(list_name,list[index=0])
             index=0 is optional
            if we don't write by default it sort tu[ple  w.r.t x-axis
            (2) sort  w.r.t y-axis is with this sorted(list_name,list[index=1])
             index=1 is compulsory for sorted w.r.t y - axis
            if we don't write by default it sort tu[ple  w.r.t x-axis
'''

l1 = [(1,2),(45,67),(4,6),(8,4)]
#sort tuple in list by lambda function
print('sort tuple in list w.r.t x-axis by lambda function: ',end='')
print(sorted(l1,key=lambda l: l))
print()

#sort tuple in list by lambda function
print('sort tuple in list w.r.t y-axis by lambda function: ',end='')
print(sorted(l1,key=lambda l: l[1]))
print()

#sort w.r.t x-axis witout lambda function
print('sort w.r.t x-axis witout lambda function: ',end='')
print(sorted(l1))
print()

#Another method for sort w.r.t x-axis witout lambda function
'''def get_index(list):
   return list[0]
print(sorted(l1,key=get_index))'''
print('sort w.r.t y-axis witout lambda function: ',end='')

def get_index(list):
   return list[1]
print(sorted(l1,key=get_index))
print()

'''
We use lambda functions when we require a nameless function
for a short period of time. In Python, we generally use
it as an argument to a higher-order function (a function
that takes in other functions as arguments). Lambda 
functions are used along with built-in functions like 
filter() , map() etc.
'''