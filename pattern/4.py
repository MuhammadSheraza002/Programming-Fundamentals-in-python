i = 1
j = 1
n = 4
m = 1
while i <=5:
    print(" "*n,end="")
    j = 1
    while j <=m:
        print(j,end="")
        j+=1
    print()
    m+=2
    n-=1
    i+=1
print("-------------------------------------")
print()
i = 1
n = 4
m = 1
while i <=5:
    print(" "*n+str(i)*m)
    n-=1
    m+=2
    i+=1
print("-------------------------------------")
print()
