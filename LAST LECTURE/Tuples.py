#TUPLES ARE Hetrogenous,ordered,immutable,can have duplicate elements,
# creating empty tuple
t5 = ()
print("t5: ", type(t5))

# creating single tuple
t5 = (2,)
print("t5: ", type(t5))

# Wrong method to creating single tuple
t5 = (1)
print("t5: ", type(t5))

#Although tuple is immutable
# A List within a tuple is still mutable
t1 = (1, "Hello", [8, 'OK', 6], (1, 2, 'BYE'), 5.5)
t1[2][1] = 'Not OK'         # will work fine
print(t1)

# Like Lists, Tuples allow duplicate elements
names = ('Arif', 'Rauf', 'Hadeed', 'Arif', 'Mujahid')
print(names)

# A tuple having two sub-tuples within it
a = (1,2,3,(4,5),(6,7,8,9),10,11)
# A tuple having a sub-tuple, which is further having a sub-tuple and that again having a subtuple
b = (1,2,3,(4,5,(6,7,8,(9,10,11))))
print(a, b)

# you can unpack tuple elements
print('\t\t\tPacking and Unpacking Tuples')
t1 = ('learning', 'is', 'fun', 'with', 'Arif')
a, b, c, d, e = t1 # the number of variables on the left must match the length of tuple
print (a, c, e)
print(type(a))

# you can pack individual elements to a tuple
t1 = a,b,c,d,e
print(t1)
print(type(t1))
'''
                    Different ways to access Elements of a Tuple
Since Tuple like List is of type Sequence, and any component within a sequence
can be accessed by entrying an index within square brackets. So naturally this
must work for Tuple as well
Similarly, if we want to find out the index of a specific item/character, we 
can use the index() method of Tuple class
'''

#You can access elements of tuple using indexing which starts from zero
t1 = ("Arif", 30, 5.5, (10,'rauf'))

print(t1[2])       #accessing element of tuple at index2
print(t1[3])       #accessing element of tuple at index3, which is again a tuple

#accessing Nested tuple element
print(t1[0][2])              #accessing third character of a tuple element at index 0
print(t1[3][1])              #accessing second element of Nested tuple at index 3
print("t1.index(3): ", t1.index('Arif'))
'''
                        Slicing Tuples
            mytuple[start:end:step]
start is the index from where we want the subtuple to start.If start is not 
provided, slicing starts from the beginning.
end is the index where we want our subtuple to end (not inclusive in the 
subtuple). If end is not provided, slicing goes till the last element of the tuple.
step is the step through which we want to skip elements in the tuple. The 
default step is 1, so we iterate through every element of the tuple.


'''
print('\t\t\tSlicing Tuples')
# Slicing by using strides
print('Slicing by using strides\n')

print('t1: ',t1)
print('t1[::]: ',t1[::])  # A default step of 1
print('t1[::1]: ',t1[::1])  # A step of 1
print('t1[::2]: ',t1[::2])  # A step of 2
print('t1[::3]: ',t1[::3])  # A step of 3

#                       Reverse slicing
print('\t\t\tReverse slicing')
print('t1[::-1]: ' ,t1[::-1]) # Take 1 step back each time
#for negative step start should be greater than end otherwise give empty tuple
print('t1[5:1:-1]: ',t1[10:1:-1]) # Take 1 step back each time
#if start is less than end in case of a negative step, it will return empty string
print('t1[2:10:-1]: ' ,t1[2:10:-1])
print('t1[::-2]: ',t1[::-2]) # Take 2 steps back

# You CANNOT use slice operator on the left side of assignment as tuple is immutable
t1 = (1, 2, 3, 4, 5, 6, 7)
#t1[2:4] = ['a', 'b', 'c']  # will generate an error as 'tuple' object does not support item assignment

# use + operator to concatenate two tuples
food_items1 = ('fruits', 'bread', 'veggies')
print('food_items1: ',food_items1)
food_items2 = ('meat', 'spices', 'burger')
print('food_items2: ',food_items2)
print('food_items1 + food_items2: ',food_items1 + food_items2)

t1 = (5, 3.4, 'hello')
t2 = (31, 9.7, 'bye')
t3 = t1 + t2
print(t3)

#tuple of 100 A's
buf = ('A',)
newbuf = buf * 100
print("newbuf: ",newbuf)

#Being immutable, you cannot add elements to a tuple (in list this is possible
# using append, extend, and insert)
'''
myfamily = ("Farooq", 'Rauf', 'Hadeed')
print("\n myfamily tuple: ", myfamily)
myfamily.insert(2,'Arif') # will generate an error as tuple object has no attribute 'insert'

'''
tuple1 = ('learning', 'is', 'fun', 'with', 'arif', 'butt')

#You cannot delete items from a tuple using del keyword
#del tuple1[3]    # will generate an error as tuple object doesn't support item deletion

# However, you can assign a new tuple object to the reference tuple1
tuple1 = (1, 2, 3, 'arif')
# However, you can delete an entire tuple object using del keyword
#del tuple1
#print(tuple1)

# convert a string into tuple using tuple()
str1 = 'Learning is fun'    #this is a string
print("Original string: ", str1, "and its type is:  ", type(str1))
t1 = tuple(str1)
print("t1: ", t1, "and its type is:  ", type(t1))

#   Use str.split() to Split a Tuple into Strings
print('Use str.split() to Split a Tuple into Strings')
str1 = 'Learning is fun'    #this is a string
t1 = tuple(str1.split(' ')) # The split() method returns a list, which you can typecast to a tuple
print(t1)
print(type(t1))

'''
Use str.join() to Join Strings into a Tuple
The str.join() is the reverse of split() method, and is used to joing multiple
strings by inserting the string in between on which this method is called
Remember, you can pass any iterable as argument to str.join() method
'''
t1 = ('This', 'is', 'getting', 'more', 'and', 'more', 'interesting')
print('t1: ',t1)
delimiter = " # "
str3 = delimiter.join(t1)
print('str3:',str3)
print(type(str3))

t1 = (3, 8, 1, 6, 0, 8, 4)
rv = t1.index(6)
print(rv)

t1 = (3, 8, 1, 6, 8, 0, 8, 4)
rv = t1.count(8)
print(rv)

t1 = (3, 8, 1, 6, 0, 8, 4)
print("length of list: ", len(t1))
print("max element in list: ", max(t1))
print("min element in list: ",min(t1))
print("Sum of element in list: ",sum(t1))

t1 = (3, 8, 1, 6, 0, 8, 4)
rv1 = 9 in t1
print(rv1)

rv2 = 9 not in t1
print(rv2)


t2 = ("XYZ", "ABC", "MNO", "ARIF")
rv3 = "ARIF" in t2
print(rv3)

#In case of strings, both variables str1 and str2 refers to the same memory location containing string object 'hello'
str1 = 'hello'
str2 = 'hello'
print(id(str1), id(str2))

print (str1 is str2)  # is operator is checking the memory address (ID) of two strings
print (str1 == str2)  # == operator is checking the contents of two strings

#In case of tuples, both t1 and t2 refers to two different objects in the memory having same values
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(id(t1), id(t2))

print (t1 is t2)   # is operator is checking the memory address (ID) of two tuples
print (t1 == t2)   # == operator is checking the contents of two tuples element by element

# Sorting a Dictionary by it values with numeric values

t1 = (3, 8, 1, 6, 0, 8, 4)

print("Original Tuple = ", t1)

list1 = sorted(t1)
list2 = sorted(t1, reverse=True)

print("Ascending Sort: ", list1)
print("Descending Sort: ", list2)
