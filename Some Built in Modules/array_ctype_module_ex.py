import ctypes
import random

ArrayType = ctypes.c_int * 5
slots = ArrayType()

for i in range( 5 ) :
	slots[i] = i*i

for i in range( 5 ) :
	print(slots[i])

