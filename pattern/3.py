"""i = 1
n = 10
j=1
while j <= 5:
    print(" "*(n-1)+"* "*i)
    i+=2
    n-=2
    j+=1
print("-------------------------------------")
print()"""
i = 1
n = 4
while i < 10:
    print("  "* n+"* "*i)
    i+=2
    n-=1

print("-------------------------------------")
print()
i = 1
n = 4
while i<= 5:
    print("  "*n,end=" ")
    j = 1
    k = 1
    while j <= k:
        print((str(j)+" "),end="")
        j+=2
        k+=1
    i+=1
    n-=1



