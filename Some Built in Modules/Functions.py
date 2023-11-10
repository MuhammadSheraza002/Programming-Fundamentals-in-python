# default arguments
def myFun(x, y=50):
	print("x: ", x)
	print("y: ", y)

myFun(10)

# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
	print(firstname, lastname)

# Keyword arguments
# in Keyword arguments arguments variable must be same

student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')

#					Variable-length arguments
'''In Python, we can pass a variable number of arguments to a function 
using special symbols. There are two special symbols:

*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)
'''

# Python program to illustrate
# *args for variable number of arguments
# *argumentconverts argument into list
def keywordargument(*argument):
	for i in range(len(argument)):
		print(argument[i])

keywordargument('my','name','is','Muhammad','sheraz')
print()

#				Variable length keyword arguments
# Python program to illustrate
# *kwargs for variable number of keyword arguments

						#**kwargs
'''Python program to illustrate *kwargs for a variable number of keyword arguments.
Here **kwargs accept keyworded variable-length argument passed by the function
call. for first=’Geeks’ first is key and ‘Geeks’ is a value. in simple words, 
what we assign is value, and to whom we assign is key. '''

def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))

# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)

# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


def myFun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")


class car():  # defining car class
	def __init__(self, *args):  # args receives unlimited no. of arguments as an array
		self.speed = args[0]  # access args index like array does
		self.color = args[1]


# creating objects of car class

audi = car(200, 'red')
bmw = car(250, 'black')
mb = car(190, 'white')

print(audi.color)
print(bmw.speed)


class car():  # defining car class
	def __init__(self, **kwargs):  # args receives unlimited no. of arguments as an array
		self.speed = kwargs['s']  # access args index like array does
		self.color = kwargs['c']


# creating objects of car class

audi = car(s=200, c='red')
bmw = car(s=250, c='black')
mb = car(s=190, c='white')

print(audi.color)
print(bmw.speed)


# A simple Python function to check
# whether x is even or odd

def evenOdd(x):
	"""Function to check if the number is even or odd"""
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")

# Driver code to call the function
print('evenOdd(2); ',end='')
evenOdd(2)

# evenOdd.__doc__ is used to describe the functionality of the function.
# it is good practise
print('evenOdd.__doc__: ',evenOdd.__doc__)

def cube(x): return x*x*x
print('cube(2): ',cube(2))

