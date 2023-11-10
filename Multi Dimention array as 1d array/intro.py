from random import randrange
def multiple_array(array,rows,cols,pages):
    for row in range(rows):
        for col in range(cols):
            for page in range(pages):
                print((row*cols*pages+page)*(col*pages+page))

def main():
    a = 3
    b=4
    print(f'a=%d b = %f'%(2,3))
    print(f"{{a={a}, b={b}}}")
    a = [randrange(50,100) for i in range(60)]
    print(a)
    multiple_array(a,3,4,5)
main()
