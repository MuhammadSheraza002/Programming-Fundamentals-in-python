#Sets are heterogeneous,unordered,mutable,CANNOT have duplicate elements,
#Mutable data types cannot be elements of the set.
# You cannot have a list, set or dictionary inside a set (being mutable)
#s1 = {"Arif", 30, 5.5, {'key':'value'}}
#Elements of a Set Cannot be Sorted
s1 = {1,1,2,3,3,4}
print(len(s1))#ans =
s1 = {1,2,3,4,5}   #set of integers
s1 = set([1, 2, 3, 4, 5])
print(s1, type(s1))

# creating an empty set
#emptyset = {}  # this is not correct way
# to create empty set, we can use set()
s5 = set()
print(s5)
print(type(s5))

# So when we want to remove duplication from list, we typecast it to a set
mylist = [2, 4, 5, 6, 8, 7, 3, 3, 2]
print("\nList: ", mylist)
myset = set(mylist)
print("List converted to set: ", myset)

# You cannot have a list, set or dictionary inside a set (being mutable)
#s1 = {"Arif", 30, 5.5, {'key':'value'}}

'''
You can have tuple inside a set
However, you CANNOT have a list, set, and dictionary objects inside a set, because sets cannot contain mutable values
This is one situation where you may wish to use a frozenset, which is very similar to a set except that a frozenset is immutable.
'''
# Nested sets: sets can have another tuple as an item due to immutable
s1 = {"Arif", 30, 5.5, (10,'rauf')}
print(s1)

# However, you cannot have a list inside a set, , because sets cannot contain mutable values (lists are mutable)
#s1 = {"Arif", 30, 5.5, [10,'rauf']} # Error unhashable type list

#Similarly, you cannot have a set within a set, because sets cannot contain mutable values (sets are mutable)
#s1 = {"Arif", 30, 5.5, {10,'rauf'}} # Error unhashable type set

#                   Packing and Unpacking Sets
print('\n\t\t\tPacking and Unpacking Sets')
# you can unpack set elements
myset = set(['learning', 'is', 'fun', 'with', 'Arif'])
print('myset: ',myset)
a, b, c, d, e = myset # the number of variables on the left must match the length of set
print (a, b, c, d, e)

# you can pack individual elements to a set
t1 = a, b, c, d, e  # By default they are packed into a tuple
set2 = set(t1)      # So you have to type cast it to set
print (set2)
print(type(set2))

# Set items cannot be accessed by referring to an index, since sets are unorder
# the items has no index.
# But you can loop through the set items using a for loop
myset = set(['learning', 'is', 'fun', 'with', 'Arif'])
for i in myset:
    print(i, end=' ')
print()
# To check if a specific element is there in the set, use the in keyword
print("'fun' in myset: ",'fun' in myset)

#cannot perform Slicing and  perform Set Concatenation and Repetition on Sets
#Cannot Modify/Add elements to a set using [ ] operator
#create an empty set
set1 = set()
set1.add(25)
set1.add(73)
print(set1)

# Adding a tuple
set1.add((19,25))
print("Set after adding three elements: ", set1)

'''
    Adding elements to a set using set.add(val) or set.update(val) method
    (1) The set.add(val) method is used to add a single element to a set
    (2) The set.update(val) method is used to add two or more elements to a set
    (3) if the value already exist no change occur
    (4) Lists and sets cannot be added to a set as elements because they are
    not hashable
    (5) Tuples can be added because tuples are immutable and hence Hashable.
'''

# update() method is used to add one two or more elements, passed as a list
set3 = set([4, 9, 12])
set3.update(['arif', 'rauf', 45])
print(set3)

#       Removing element from a set using set.pop(index) method
s1 = {'learning', 'is', 'fun', 'with', 'arif', 'butt'}
print("Original set: ", s1)

x  = s1.pop()
print("Element popped is: ", x)
print("Set now is: ", s1)

#Removing element from a set using set.remove(val) method
s2 = set(['Welcome', 'to', 'department', 'of', 'Data', 'Science'])
print("\nOriginal set: ", s2)
x = s2.remove('department')
print("After remove('department'): ", s2)
print("Return value of remove() is: ", x)

# If the element to be removed does not exist in the set remove() method will
# flag an error
#y = s2.remove('arif')  # Error: Element doesn’t exist in the set.

#Removing element from a set using set.discard(val) method
#The set.discard(val) like set.remove(val) method is used to remove a specific element by value from a set without returning it
#The advantage of using set.discard(val) method is that, if the element doesn’t exist in the set, no error is raised and the set remains unchanged.
s2 = set(['Welcome', 'to', 'department', 'of', 'Data', 'Science'])
y = s2.discard('arif')
print(s2)

#use the clear() method to clear all elements of a set
s2 = set(['Welcome', 'to', 'department', 'of', 'Data', 'Science'])
print('s2 before clear method: ',s2)
s2.clear()
print('s2 after clear method: ',s2)

#Using del Keyword to delete the set entirely from memory
# use del keyword to delete entire set, (you cannot delete a specific element as it is non-indexed)
s2 = set(['Welcome', 'to', 'department', 'of', 'Data', 'Science'])
del s2

# convert a string into set using set()
str1 = 'Learning is fun'    #this is a string
print("Original string: ", str1)

s1 = set(str1)
print("s1: ", s1, "\nand its type is:  ", type(s1))

#str1.split(' ') method
str1 = 'Learning is fun'    #this is a string
set1 = set(str1.split(' '))
print(set1)
print(type(set1))

#Use str.join() to Join Strings into a Lis
delimiter = " # "
str3 = delimiter.join(str1)
print('delimiter.join(str1): ',str3)
print(type(str3))   #str.join(set) generates string

#Elements of a Set Cannot be Sorted
#you can apply max(), min(), and sum() functions on Sets with numeric elements
s1 = set([3, 8, 1, 6, 0, 8, 4])
print("length of set: ", len(s1))
print("max element in set: ", max(s1))
print("min element in list: ",min(s1))
print("Sum of element in list: ",sum(s1))

#you can apply in and not in membership operators on Sets
s1 = set([3, 8, 1, 6, 0, 8, 4])

rv1 = 9 in s1
print('9 in s1: ',rv1)

rv2 = 9 not in s1
print('9 not in s1:',rv2)


s2 = set(["XYZ", "ABC", "MNO", "ARIF"])
rv3 = "ARIF" in s2
print('"ARIF" in s2: ',rv3)

#                   Comparing Objects and Values
print('\t\t\t\t\tComparing Objects and Values')
#In case of strings, both variables str1 and str2 refers to the same memory location containing string object 'hello'
str1 = 'hello'
str2 = 'hello'
print(id(str1), id(str2))

print (str1 is str2)  # is operator is checking the memory address (ID) of two strings
print (str1 == str2)  # == operator is checking the contents of two strings

#In case of sets, both t1 and t2 refers to two different objects in the memory having same values
s1 = set([1, 2, 3])
s2 = set([1, 2, 3])
print(id(s1), id(s2))

print (s1 is s2)   # is operator is checking the memory address (ID) of two sets
print (s1 == s2)   # == operator is checking the contents of two sets element by element

#                                Union of sets
#A s1.union(s2) method or s1 | s2, returns a new set containing all values that are in s1, or s2, or both
print('\t\t\t\t\tUnion of sets')
set1 = {'arif', 'rauf'}
set2 = {'maaz', 'hadeed', 'arif'}

set3 = set1 | set2
set3 = set1.union(set2)

print("set1: ", set1)
print("set2: ", set2)
print("set1 | set2: ", set3)

#                       Intersection of sets
#s1.intersection(s2) method or s1 & s2, returns a new set containing all values that are common in in s1 and s2
print('\t\t\t\t\tIntersection of sets')
set1 = {'arif', 'rauf'}
set2 = {'maaz', 'hadeed', 'arif'}

set3 = set1 & set2
set4 = set1.intersection(set2)

print("set1: ", set1)
print("set2: ", set2)
print("set1 & set2: ", set4)
#                           Difference of sets
#A s1.difference(s2) method or s1 - s2, returns a new set containing all values of s1 that are not there in s2
Set1 = {'arif', 'rauf'}
set2 = {'maaz', 'hadeed', 'arif'}
set3 = set1 - set2
set4 = set1.difference(set2)

print("set1: ", set1)
print("set2: ", set2)
print("set1 - set2: ", set4)

#                           symmetric_difference OF SETS
#A s1.symmetric_difference(s2) method or s1 ^ s2, returns a new set containing all elements that are in exactly one of the sets, equivalent to (s1 | s2) - (s1 & s2)
print('symmetric_difference OF SET')
set1 = {'arif', 'rauf'}
set2 = {'maaz', 'hadeed', 'arif'}

set3 = set1 ^ set2
set4 = set1.symmetric_difference(set2)

print("set1: ", set1)
print("set2: ", set2)
print("set1 ^ set2: ", set4)

#                   Checking Subset
#The s1.issubset(s2) method or s1 <= s2, returns True if s1 is a subset of s2
print('\t\t\t\tChecking Subset')
s1 = {1,2,3,4,5,6,7}
s2 = {1,2,3,4}

print(s1.issubset(s2))     # is s2 a subset of s1
print(s1 <= s2)            # is s2 a subset of s1

#                       Checking Superset
#The s1.issuperset(s2) method or s1 >= s2, returns True if s1 is a superset of s2
print('\t\t\t\tChecking Superset')
s1 = {1,2,3,4,5,6,7}
s2 = {1,2,3,4}

print(s1.issuperset(s2)) # is s1 a superset of s2
print(s1 >= s2)          # is s1 a superset of s2

#Checking Disjoint
#The s1.isdisjoint(s2) method, returns True if two sets have a null intersection
print('\t\t\tChecking Disjoint')
s1 = {1,2,3,4,5,6,7}
s2 = {1,2,3,4}
print(s1.isdisjoint(s2))

# Another example
s3 = {1,2,3,4}
s4 = {5,6,7,8}
print(s3.isdisjoint(s4))
