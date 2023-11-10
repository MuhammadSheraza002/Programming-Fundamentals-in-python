class matrix:
    pass
def create(rows,cols):
    m = matrix()
    m.rows = rows
    m.cols = cols
    m.data = [[ 0  for i in range(cols)] for i in range(rows)]
    return m
def inp(m):
    i = 0
    while i < m.rows:
        j = 0
        while j < m.cols:
            m.data[i][j] = int(input())
            j += 1
        i += 1
    return m
def printmatrix(m):
    i = 0
    while i < m.rows:
        j = 0
        while j < m.cols:
            print(m.data[i][j],end=" ")
            j += 1
        print()
        i += 1
def transpose(m):
    t = create(m.rows,m.cols)
    i = 0
    while i < m.rows:
        j = 0
        while j < m.cols:
            t.data[i][j] = m.data[j][i]
            j += 1
        i += 1
    return t
def add(m1,m2):
    if m1.rows != m2.rows or m1.cols != m2.cols:
        raise Exception ("for addition rows and colums both should be equal")
    t = create(m1.rows,m1.cols)
    i = 0
    while i < m1.rows:
        j = 0
        while j < m1.cols:
            t.data[i][j] = m1.data[i][j] + m2.data[i][j]
            j += 1
        i += 1
    return t
def issymetric(m):
    i = 0
    while i < m.rows:
        j = 0
        while j < m.cols:
            if m.data[i][j] != m.data[j][i]:
                return False
            else:
                j += 1
        i += 1
    return True
def main():
    matrix1 = create(2,2)
    matrix2 = create(2,2)
    print("null matrix=")
    printmatrix(matrix1)
    print("type elements of matrix 1")
    inpm1= inp(matrix1)
    print("type elements of matrix 2")
    inpm2  = inp(matrix2)
    print("matrix 1=")
    printmatrix(inpm1)
    print("matrix 2=")
    printmatrix(inpm2)
    addition = add(inpm1,inpm2)
    print("addition of matrixes=")
    printmatrix(addition)
    transpose_of_m1 = transpose(inpm1)
    transpose_of_m2 = transpose(inpm2)
    print("transpose of matrix 1 =")
    printmatrix(transpose_of_m1)
    print("transpose of matrix 2 =")
    printmatrix(transpose_of_m2)
    print("matrix 1 symmetric =",issymetric(inpm1))
    print("matrix 2 symmetric =",issymetric(inpm2))
main()
