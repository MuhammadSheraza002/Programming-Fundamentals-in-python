import random
list = [random.randint(1,10) for i in range(10)]

for index1,item in enumerate(list):
    print(index1,item)