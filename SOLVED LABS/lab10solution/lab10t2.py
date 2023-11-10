class matrix:
    pass
def create(rows,cols):
    m = matrix()
    m.rows = rows
    m.cols = cols
    m.data = [[ 0  for i in range(cols)] for i in range(rows)]
    return m


def identitymatrix(rows,cols):
    a = create(rows,cols)
    a.rows = rows
    a.cols= cols
    a.data = [[ 0  for i in range(cols)] for i in range(rows)]
    if a.rows != a.cols:
        raise Exception ("for identity matrix rows == cols")

    j = 0
    i = 0
    while j < cols or j < rows:
        a.data[i][j] = 1
        j += 1
        i += 1
    return a
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
def subt(m1,m2):
    if m1.rows != m2.rows or m1.cols != m2.cols:
        raise Exception ("for subtractio rows and colums both should be equal ")
    t = create(m1.rows,m1.cols)
    i = 0
    while i < m1.rows:
        j = 0
        while j < m1.cols:
            t.data[i][j] = m1.data[i][j] - m2.data[i][j]
            j += 1
        i += 1
    return t
def mul(m1,m2):
    if m1.cols != m2.rows:
        raise Exception ("for multiolicatio m1.cols = m2.rows")
    t = create(m1.cols,m2.rows)
    i = 0
    while i < m1.cols:
        j = 0
        while j < m2.rows:
            m = 0
            while m < m2.cols:
                t.data[i][j] = m1.data[i][j] * m2.data[j][m]
                m += 1
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

def issquare(m):
    if m.rows == m.cols:
        return True
    else:
        return False

def main():
    matrix1 = create(2,2)
    matrix2 = create(2,2)
    print("type elements of matrix 1")
    inpm1= inp(matrix1)
    print("type elements of matrix 2")
    inpm2  = inp(matrix2)
    identity= identitymatrix(2,2)
    print("identity matrix=")
    printmatrix(identity)
    print("matrix 1=")
    printmatrix(inpm1)
    print("matrix 2=")
    printmatrix(inpm2)
    subtraction = subt(inpm1,inpm2)
    print("subtraction of matrixes=")
    printmatrix(subtraction)
    print("matrix1 is square=",issquare(inpm1))
    print("matrix2 is square=",issquare(inpm2))
    multiplication = mul(inpm1,inpm2)
    print("multiplication of matrixes=")
    printmatrix(multiplication)
main()
