class Box:
    pass
def main():
    b = Box()
    b.h = 80
    b.w = 150
    b.l = 320
    tmp = (b.h - b.w) / b.l
    print( b.h+b.w+b.l )
    print( 'tmp',tmp )
    return
main()
