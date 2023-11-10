# Python program to change the
# current working directory


import os


# Function to Get the current
# working directory
def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()

current_path()
# Changing the CWD
os.chdir('../')
current_path()

'''
                            Using os.mkdir()
os.mkdir() method in Python is used to create a directory named path with the 
specified numeric mode. This method raises FileExistsError if the directory to
 be created already exists.
'''

#It will return maximum number of list
def maximum_number_of_list(list):
    maximum_number=list[0]
    for index in range(len(list)):
        if maximum_number<list[index]:
            maximum_number=list[index]
    return maximum_number

#It will return minimum number of list
def minimum_number_of_list(list):
    minimum_number=list[0]
    for index in range(len(list)):
        if minimum_number>list[index]:
            minimum_number=list[index]
    return minimum_number

def centered_average(list):
    sum_of_list = 0
    for index in range(len(list)):
        sum_of_list += list[index]
    sum_of_list -= (maximum_number_of_list(list) + minimum_number_of_list(list))
    return sum_of_list / (len(list)-2)
array1 = [1, 2, 3, 4, 100]
print('centered_average([1, 2, 3, 4, 100]): ',centered_average(array1))

array2 = [1, 1, 5, 5, 10, 8, 7]
print('centered_average([1, 1, 5, 5, 10, 8, 7]): ',centered_average(array2))

array3 = [-10, -4, -2, -4, -2, 0]
print('centered_average([-10, -4, -2, -4, -2, 0]): ',centered_average(array3))

