for i in range(5):
    print((str(i+1) +" ")*(i+1))
print("-------------------------------------")
print()
i = 1
k = 1
n = 4
while i< 5:
    j = 1
    print("  "* n,end=" ")
    while j <=k:
        print(j,end=" ")
        j+=2
    print()
    i+=1
    k+=2
    n-=1


