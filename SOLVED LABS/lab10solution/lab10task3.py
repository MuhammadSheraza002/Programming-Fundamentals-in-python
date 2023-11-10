from random import randint
def create(x,y,z):
    a = [[[0  for i in range(z)] for i in range(y)] for i in range(x)]
    return a
def inputmatrix(m):
    # array = [[[randint(11,99)for i in range(z)] for i in range(y)] for i in range(x)]
    i = 0
    while i < 4:
        j = 0
        while j < 9:
            k = 0
            while k < 7:
                m[i][j][k] = randint(11,99)
                k += 1

            j += 1

        i += 1
    return m

def input2Dmatrix(m):
    t = [[0 for c in range(7)] for r in range(9)]
    i = 0
    while i < 4:
        j = 0
        while j < 9:
            k = 0
            while k < 7:
                t[j][k] = m[i][j][k]
                k += 1

            j += 1

        i += 1
    return t

def main():
    m1 = create(4,9,7)
    inpm1 = inputmatrix(m1)
    print("3D array of size 4 X 9 X 7=")
    print()
    print(inputmatrix(inpm1))
    print()
    print("2D arrays of size 9 X 7.")
    print()
    print(input2Dmatrix(inpm1))
    print()
    print("4 stacked 2D arrays of size 9 X 7.")
    print()
    print(input2Dmatrix(inpm1) * 4)

main()
