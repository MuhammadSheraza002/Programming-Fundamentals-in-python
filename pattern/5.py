i = 9
n = 1
while i>0:
    print(" "*n+"*"*i)
    i-=2
    n+=1
print("-------------------------------------")
print()
d = 1
w = 9
s = 0
l = 1
while l <=5:
    print(" "*s+str(d)*w)
    w-=2
    l+=1
    d+=1
    s+=1
print("-------------------------------------")
print()
i = 1
s = 0
m = 9
while i <= 5:
    print(" "*s,end="")
    j = 1
    while j<=m:
        print(j,end="")
        j+=1
    print()
    i+=1
    s+=1
    m-=2

