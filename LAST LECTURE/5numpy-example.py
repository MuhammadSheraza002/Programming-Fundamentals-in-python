import numpy as np
x = np.array([(1,2,3),(3,4,5)])
y = np.array([(1,2,3),(3,4,5)])
print('\n')
print(x-y)
print()
print('\n')
print(x*y)
print()
print('\n')
print(x/y)

"""
np.array(seq, dtype)
The only required argument is a sequence like object like a list from which to create an array
The optional dtype argument specifies the data type of the array objects.
For integer values it is normally int64
For float values it is normally float64.
You can mention dtype if you want to limit memory usage

{'int': [numpy.int8, numpy.int16, numpy.int32, numpy.int64],
 'uint': [numpy.uint8, numpy.uint16, numpy.uint32, numpy.uint64],
 'float': [numpy.float16, numpy.float32, numpy.float64, numpy.float128],
 'complex': [numpy.complex64, numpy.complex128, numpy.complex256],
 'others': [bool, object, bytes, str, numpy.void]}

"""

