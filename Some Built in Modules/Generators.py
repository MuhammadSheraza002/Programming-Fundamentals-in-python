'''                             Generator-Function
Generator-Function : A generator-function is defined like a normal function, but
whenever it needs to generate a value, it does so with the yield keyword rather
than return. If the body of a def contains yield, the function automatically
becomes a generator function.
'''

# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3
print(simpleGeneratorFun()) #return generator object
# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)

#               why use yield instead of return
'''
The yield statement suspends a function’s execution and sends a value back to 
the caller, but retains enough state to enable the function to resume where it
left off. When the function resumes, it continues execution immediately after 
the last yield run. This allows its code to produce a series of values over 
time, rather than computing them at once and sending them back like a list.
'''


#next() method for generator

# x is a generator object
'''x = simpleGeneratorFun()
# Iterating over the generator object using next
print(x.next()) # In Python 3, __next__()
print(x.next())
print(x.next())
'''


# A simple generator for Fibonacci Numbers
'''def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
        
        


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(x.next())  # In Python 3, __next__()
print(x.next())
print(x.next())
print(x.next())
print(x.next())

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)'''
