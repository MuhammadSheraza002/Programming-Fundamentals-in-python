from random import randint
a = [[[0 for x in range(7)] for y in range(9)] for z in range(4)]
"""
This upper loop will create a 3D array in which the smallest block
contains 7 elements and such 9 blocks(containing 7 elements) make
another larger block that are 4 in number.
"""

for z in range(4):
    for y in range(9):
        for x in range(7):
            a[z][y][x] = randint(11, 99)

for z in range(4):
    print(a[z])

