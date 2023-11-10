def printTriange(k,s):
    n = ord(k)
    i = n+1
    while n <= ord(s):
        j = n
        while j < i:
            print(chr(j),end=" ")
            i+=1
            j+=1
        print()
printTriange("k","s")
