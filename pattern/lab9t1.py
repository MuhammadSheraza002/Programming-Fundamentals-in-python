def printTriange(k,s):
    i = ord(k)
    l = ord(s)
    while i <=l:
        w = ord(k)
        while w <=i:
            print(chr(w),end="")
            w+=1
        print()
        i+=1




printTriange( "k","s")
print("<---------------------------------->")
def printPyramid(m,u ):
    i = ord(m)
    l = ord(u)
    S = 4
    while i <= l:
        w = ord(m)
        print(" "*S,end="")
        while w <= i:
            print(chr(w),end="")
            w+=1
        print()
        i+=2
        S -=1
printPyramid("m","u")







