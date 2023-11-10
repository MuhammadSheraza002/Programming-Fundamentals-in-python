# A dictionary with integer keys, and string values, showing a symbol table
# generated by compiler
#Dictionary allows Duplicate Values, but not allows Duplicate keys
dict2 = {
    2580:'var1',
    2582:'var2',
    2586:'var3'
}
print('dict2: ',dict2)

# Creating an empty dictionary
dict5 = dict()
print('empty dict: ',dict5)

# A list of two object tuples can also be used to create dictionaries
dict7 = dict([('name', 'arif'), ('age',51), ('city', 'Lahore')])
print('dict7: ',dict7)

#               Dictionary allows Duplicate Values
# Duplicate values are allowed
d1 = {'name1' : 'kakamanna',
     'name2' : 'kakamanna'
     }
# Duplicate keys are not allowed
# This will not raise an error, but will overwrite the value corresponding to the key
d1 = {'name' : 'kakamanna',
     'name' : 'arif'
     }
print('d1: ',d1)

#           Keys inside Dictionaries Must be of Immutable data types
# Tuple being immutable can be used as a key
'''d1 = {'kakamanna':'name',
      (60, 78, 83): 'marks',
    [60, 78, 83]:'marks'
     }'''
#print(d1) it raises error due mutable data type as dictionary key

#       Values inside Dictionaies can be of mutable/immutable data type
# List being mutable can be used as a value
d1 = {'nam':'kakamanna',
      'marks':[60,78,83]
     }
#                                   Dictionaries are heterogeneous
#      The keys of a dictionary can be of integer, string, or tuple type
#      The values of a dictionary can be of any data type
dict3 = {
    'name': 'kakamanna',
    1: 10,
    'abc':25,
    33: 'xyz'
}
print('dict3: ',dict3)

#               Dictionaries can be nested to arbitrary depth
# Creating a Nested Dictionary
dict7 = {'name':'arif',
         'occupation':'teaching',
        'address':{'house#' : 131, 'area' : 'model town', 'city' : 'lahore'},
         'phone': '03214456454'
        }
'''
                    Dictionaries from Python 3.7 onward are ordered
From Python 3.7 onwards, dictionaries are guranteed to be in insertion ordered. i.e., every time you access dictionary elements they will show up in same sequence.
However, like string, list, and tuple, the elements of a dictionary are not associated by an index
Moreover, two dictionaries having same key-value pairs are two different objects
'''
d1 = {
    'arif':51,
    'rauf':52,
    'hadeed':20
}

d2 = {
    'arif':51,
    'rauf':52,
    'hadeed':20
}
d2
d3 = {
    'rauf':52,
    'hadeed':20,
    'arif':51
}
print('id(d1):',id(d1), '\nid(d2):',id(d2),'\nid(d3):',id(d3))

#                           Accessing Elements of a Dictionary
print('\t\t\t\t\t\tAccessing Elements of a Dictionary')

d1 = {
    'name':'kakamanna',
    'age':22,
    'address':'Johar Town',
    'marks':[60, 75, 80]
}
print("d1['address']: ",d1['address'])
print("d1.get('marks'): ",d1.get('marks'))

#                      To retrieve a value from a nested dictionary
print('\t\t\t\tTo retrieve a value from a nested dictionary')
d2 = {'name': 'arif',
      'occupation': 'teaching',
      'address': {'house#': 131,
                  'area': 'model town',
                  'city': 'lahore'}
      }
print("d2['address']: ",d2['address'])
print("d2['address']['city']: ",d2['address']['city'])
print("d2.get('address').get('city'): ",d2.get('address').get('city'))

#The dict.items() method returns all the key-value pairs of a dictionary as a two object tuple
print('The dict.items() method returns all the key-value pairs of a dictionary as a two object tuple')
print('d2.items(): ',d2.items())

#The dict.keys() method returns all the keys of a dictionary object
print('The dict.keys() method returns all the keys of a dictionary object')
print('d2.keys(): ',d2.keys())

#                   Adding/Modifying Elements using [] Operator
# Create a simple dictionary
d1 = {
    'name':'kakamanna',
    'age':22,
    'address':'Johar Town',
    'marks':[60, 75, 80]
}
print('d1 before modification',d1)

# Modify value corresponding to an existing key

d1['address'] = 'Model Town'
d1['name'] = 'Muhammad Sheraz'
print('d1 after modification',d1)

# Adding a new key:value pair
d1['key1'] = 'value1'
d1['class']='bs data science'
print('d1 after addition',d1)

#Modifying Elements using d1.update() method
#dict.update(key:value)
#If the key donot already exist, a new key:value is inserted in the dictionary
# Modify value corresponding to an existing key
d1.update({'name':'Arif Butt'})
print('d1 after updation using d1.update() method: ',d1)

#use the dict.update() method to merge two dictionaries
d1 = {
    'name':'kakamanna',
    'age':22,
}
print('d1: ',d1)
d2 = {
    'address':'Johar Town',
    'marks':[60, 75, 80]
}
print('d2: ',d2)
d1.update(d2)
print('merge two dictionaries',d1)

'''Removing Element using d1.popitem() Method
The d1.popitem() removes and returns a (key,value) pair as a 2-tuple
Pairs are returned in LIFO order, i.e., last inserted element is returned
Raises KeyError if the dict is empty'''

d1 = {
    'name':'kakamanna',
    'age':22,
    'address':'Johar Town',
    'marks':[60, 75, 80]
}
print('d1.popitem(): ',d1.popitem())
print('d1.popitem(): ',d1.popitem())
print('d1 after popitems() : ',d1.popitem())

#Removing Element using d1.pop(key) Method
print('Removing Element using d1.pop(key) Method')
d1 = {
    'name':'kakamanna',
    'age':22,
    'address':'Johar Town',
    'marks':[60, 75, 80]
}
print("d1.pop('name'): ",d1.pop('name'))
print("d1 after using d1.pop(key) Method,",d1)
#If key is not found a KeyError is raised
#d1.pop('nokey') #This will raise an error
#The d1.clear() removes all items from the dictionary and returns None
d1.clear()
print('d1 after d1.clear() Method',d1)

# The items() method, returns an object of dict_items containing two value tuples
rv = d1.items()
print('d1.items(): ',rv)
print("\n", type(rv))

# You can convert dictionary key-value pairs into a tuple containing two valued
# tuples
t1 = tuple(d1.items())
print('convert dictionary key-value pairs into a tuple: ',t1)
print("\n", type(t1))

#converting dictionary keys only into a tuple
t1 = tuple(d1.keys())
print('converting dictionary keys only into a tuple: ',t1)
print("\n", type(t1))
#dictionary keys cannot convert into a list
#converting dictionary values only into a list
mylist = list(d1.values())
print("\nconverting dictionary values only into a list", mylist)
print(type(mylist))

                        #Sorting a Dictionary by Values
print('\t\t\t\t\tSorting a Dictionary by Values')
#(1) We can use the built-in function sorted(iterable) to get a sorted copy
# of a dictionary (by value).
#(2) The sorted(iterable) returns a sorted version of the iterable,
# without making any change to the iterable
#(3) It's syntax is quite similar to list.sort() method, however, the iterator to be sorted needs to be passed as a required parameteras shown below:
  #sorted(iterable, key=None, reverse=False)
#(4) By default the reverse argument is False, you override the default behavior
# by passing a True value to this argument to perform a descending sort
#(5) A custom key function can also be supplied to customize the sort order.

dict1 = {'rauf': 81,
         'arif':90,
        'maaz':76,
        'hadeed':73,
         'mujahid':93,
        }
print('dict1 before sorted: ',dict1)
sorted(dict1, reverse=True)
print('dict1 after sorted in desending order: ',dict1)
d2 = sorted(dict1)
print('dict1 after sorted in ascending order: ',dict2)

#You can pass the keys only to the sorted() function, to do the above task
d2 = sorted(dict1.keys())
print('dict1 after sorted in ascending order: ',dict2)
#Similarly you can pass the values only to the sorted() function, and it will
# return the list of sorted values
d2 = sorted(dict1.values())
print('dict1 after sorted in ascending order: ',dict2)

# Function receives a key:value tuple (key, value) and returns the value
def func1(item):
    return item[1]

mylist = sorted(dict1.items(), key = func1, reverse=True)
print(mylist)
sorted_dict = dict(mylist)
print('sorted_dict: ',sorted_dict)

'''
Example 2: Suppose we have a JSON array containing name, age and grades of 
students. We want to sort it by the age of the students.
1) JSON stands for JavaScript Object Notation
2) JSON is a text format for storing and transporting data
3) A JSON string has comma separated key:value pairs
'''
# The following JSON array defines a student object with 3 properties: `name`, `age`, and `grade`
# It is actually a list containing dictionary objects each object containing three key:value pairs
students = [
         {"name": "Hashim", "age": 18, "grade": "B"},
         {"name": "Salman", "age": 11, "grade": "A"},
         {"name": "Mazhar", "age": 12, "grade": "C"},
         {"name": "Farhan", "age": 22, "grade": "D"},
         {"name": "Bilal", "age": 19, "grade": "A"},
         {"name": "Zalaid", "age": 17, "grade": "B"}
        ]
print("students: ",students)

# Function receives a dictionary object and returns the value corresponding to key age in that dictionary
def func2(item):
     return item.get('age') #return item['age']

sorted_students = sorted(students, key = func2)
print('sorted_students: ',sorted_students)

#Simple Assignment (aliasing) vs Shallow Copy vs Deep Copy
'''Aliasing: Making an Alias of a List object using simple Assignment = Operator
In Python, we use = operator to create a copy/alias of an object.
Remember it doesnot create a new object, rather creates a new variable that 
shares the reference of the original object'''

ict1 = {'rauf': 81,
         'arif':90,
        'maaz':76,
        'hadeed':73,
         'mujahid':93,
        }

dict2 = dict1

# Both references point to same memory object, so have the same ID
print('ID of dict1:', id(dict1))
print('ID of dict2:', id(dict2))
# If you modify an element of one object, the change will be visible in both
dict2["maaz"] = 100

print('\ndict1:', dict1)
print('dict2:', dict2)

#                               Shallow Copy
'''We have used the copy.copy() method of copy module to create a shallow copy of List objects in our previous session
To create a shallow copy of a list or dictionary, we can also use copy() method of List and Dictionary objects.'''

import copy
dict1 = {'rauf': 81,
         'arif':90,
        'maaz':76,
        'hadeed':73,
         'mujahid':93,
        }

#dict2 = copy.copy(dict1)
dict2 = dict1.copy()


# Both variables point to different memory objects, so have the different ID
print('ID of dict1:', id(dict1))
print('ID of dict2:', id(dict2))

# If you modify an element of one object, the change will NOT be visible in other
dict2["maaz"] = 100

print('\ndict1:', dict1)
print('dict2:', dict2)

#                               Limitation of Shallow Copy
'''
The word Shallow copy comes in picture when there is some object in dictionary
 like list or user define objects instead of primitive datatypes.
The limitation of shallow copy is that it does not create a copy of nested 
objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.
Let us understand this by an example
'''
import copy

dict1 = {'rauf': 81,
         'arif': 90,
         'maaz': [55, 66, 77],  # note we have a list of marks as a dictionary value
         'hadeed': 73,
         'mujahid': 93,
         }

# dict2 = copy.copy(dict1)
dict2 = dict1.copy()

# Both variables point to different memory objects, so have the different ID
print('ID of dict1:', id(dict1))
print('ID of dict2:', id(dict2))
# If you modify a nested element of one object, the change will be visible in both
# This is the limitation of shallow copy

dict2["maaz"][1] = 0

print('\ndict1:', dict1)
print('\ndict2:', dict2)

'''
Marks of student 'maaz' has been changed in both :(
So in case of a dictionary having primitive datatypes, the shallow copy works 
fine. However, when we have nested objects inside the dictionary the shallow copy does not work
Lets solve this using deep copy
'''
# Deep Copy: Making a Copy of an Object using copy.deepcopy() Method
#Deep copy creates a new object and recursively creates independent copy of original object and all its nested objects.
import copy

dict1 = {'rauf': 81,
         'arif': 90,
         'maaz': [55, 66, 77],
         'hadeed': 73,
         'mujahid': 93,
         }

dict2 = copy.deepcopy(dict1)

# Both variables point to different memory objects, so have the different ID
print('ID of dict1:', id(dict1))
print('ID of dict2:', id(dict2))
# If you modify a nested element of one object, the change will be visible in other
dict2["maaz"][1] = 0

print('\ndict1:', dict1)
print('\ndict2:', dict2)
