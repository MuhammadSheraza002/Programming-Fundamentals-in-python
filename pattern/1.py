i = 1
while i<= 5:
    j = 1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1
print("-------------------------------------")
print()
n = 5
i = 1
while i<=5:
    j = 1
    print("  "*(n-1),end="")
    while j <=i:
        print(str(j),end=" ")
        j+=1
    print()
    n-=1
    i+=1
print("-------------------------------------")
print()
i = 1
n = 5
while i <=5:
    print("  "*(n-1)+"* "*i)
    n-=1
    i+=1
