def solid_filled_rectangle(h,w):
    space = w -1
    i = 1
    w1 = 1
    while i <= h:
        print(" "*space+"C"*w1)
        w1+=2
        i+=2
        space-=1
solid_filled_rectangle(10,7)
print("<-------------------------------------->")
for i in range(10):
    print("*"*(i*i))
    i+=1
i = 8
while i >0:
    print("*"*(i*i))
    i-=1

