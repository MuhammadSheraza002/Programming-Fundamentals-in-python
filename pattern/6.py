i = 1

w = 5
space = 4
while i <= 5:
    j =1
    print(" "*space,end="")
    while j<=i:
        print(str(j),end="")
        j+=1
    k = j-2
    while k>0:
        print(str(k),end="")
        k-=1
    print()
    i+=1
    space -=1


