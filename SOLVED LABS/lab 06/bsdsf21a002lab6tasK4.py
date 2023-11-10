class matrix:
    a11 = 0
    a12 = 0
    a21 = 0
    a22 = 0
def main():
    a = matrix()
    a.a11 = int(input("enter a1= "))
    a.a12 = int(input("enter a2= "))
    a.a21 = int(input("enter a3= "))
    a.a22 = int(input("enter a4= "))
    print(a.a11,"  ",a.a12)
    print(a.a21,"  ",a.a22)
    determinant = (a.a11 * a.a12) - (a.a21 * a.a22)
    print("determinant of matrix is= ",determinant)
main()





