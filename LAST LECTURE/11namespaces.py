# This function uses global variable s
'''If a variable is assigned a value anywhere within the function’s body, it’s
 assumed to be a local unless explicitly declared as global.
Variables that are only referenced inside a function are implicitly global.
We Use a global keyword to use a global variable inside a function.
There is no need to use global keywords outside a function.
Use of global keyword in Python: To access a global variable inside a function
 there is no need to use a global keyword'''
# Python program showing a use of
# global in nested function

def add():
	x = 15
	def change():
		global x
		x = 20
	print("Before making changing: ", x)
	print("Making change")
	change()
	print("After making change: ", x)

add()
print("value of x", x)

def f():
	print("Inside Function", s)

# Global scope
s = "I love Geeksforgeeks"
f()
print("Outside Function", s)

print('<---------------------------------------------------->')

# This function has a variable with
# name same as s.

# This function modifies the global variable 's'
def f():
	global s
	s += ' GFG'
	print(s)
	s = "Look for Geeksforgeeks Python Section"
	print(s)

# Global Scope
s = "Python is great!"
f()
print(s)

print('<---------------------------------------------------->')

a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)


def outer_function():
    #global a
    a = 20

    def inner_function():
        nonlocal a  # nonlocal
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)
