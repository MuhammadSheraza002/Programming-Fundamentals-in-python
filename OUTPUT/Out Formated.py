# % method
#      %s for string data type
#      %d for int data type
#      %f for float data type
a = f'a=%d b = %f'
print('a=%d b = %f: ',a %(2,3))
name = 'sheraz'
rollno = 2
marks = 55.3

print('my name is: %s rollno: %d and marks in pf : %f' %(name,rollno,marks))
print('my name is: %s rollno: %.5d and marks in pf : %.2f' %(name,rollno,marks))


print("Geeks : %d, Portal : %5.2f" % (1, 05.333))
print("Total students : %3d, Boys : %2d" % (240, 120))
print("%7.3o" % (25))
print("%10.3E" % (356.08977))

# use of format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))
print('{1} and {2}'.format('Geeks', 'Portal','helo'))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

#f-string
print(f"I love {'Geeks'} for \"{'Geeks'}!\"")

