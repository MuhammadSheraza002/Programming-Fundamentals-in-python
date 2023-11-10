def lcm(a,b):
    i = a * b
    cm = 0
    while i >= a or i >= b:
        if i % a == 0 and i % b == 0:
            cm = i
        else:
            pass
        i = i - 1
    return cm

print(lcm(5,10))
