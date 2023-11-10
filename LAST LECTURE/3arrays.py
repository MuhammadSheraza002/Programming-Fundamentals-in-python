'''
Python Arrays
A simple Python array is a sequence of objects of similar data dype. Python array module requires all array elements to be of the same type. Moreover, to create an array, you'll need to specify a value type.
array(typecode [, initializer])
Return a new array whose items are restricted by typecode, and initialized from the optional initializer value, which must be a list, string or iterable over elements of the appropriate type.

Arrays represent basic values and behave very much like lists, except the type of objects stored in them is constrained. The type is specified at object creation time by using a type code, which is a single character.

The following type codes are defined:
Type code   C Type             Minimum size in bytes
'b'         signed integer     1
'B'         unsigned integer   1
'u'         Unicode character  2 (see note)
'h'         signed integer     2
'H'         unsigned integer   2
'i'         signed integer     2
'I'         unsigned integer   2
'l'         signed integer     4
'L'         unsigned integer   4
'q'         signed integer     8 (see note)
'Q'         unsigned integer   8 (see note)
'f'         floating point     4
'd'         floating point     8
'''


import array as arr

a = arr.array('f', [1.1, 3.5, 4.5])
print(a)
a = arr.array('f', [1.1, 3.5, 4])
print(a)
a = arr.array('f', [1.1, 3.5, 4.0])
print(a)




'''
When to use arrays?
Lists are much more flexible than arrays.
They can store elements of different data types
including strings. And, if you need to do
mathematical computation on arrays and matrices,
you are much better off using something like NumPy.

So, what are the uses of arrays created from
the Python array module?
The array.array type is just a thin wrapper on
C arrays which provides space-efficient storage
of basic C-style data types. If you need to
allocate an array that you know will not change,
then arrays can be faster and use less memory
than lists.

Unless you don't really need arrays (array module
may be needed to interface with C code), the use
of the array module is not recommended.
'''
