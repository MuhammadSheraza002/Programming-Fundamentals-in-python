def createarray(a,s):
    i = 0
    while i < s:
        a[i]=int(input())
        i+=1
    return a
def counting(array,index):
    count=0
    for i in range(len(array)):
        if array[i]==index:
            count+=1
        else:
            pass
    return count
def printcount(a1,a2):
    j = 0
    while j < len(a2):
        if counting(a1,a2[j])>=4:
            print(f"{a2[j]} = {counting(a1,a2[j])} Counts")
        else:
            pass
        j+=1
def main():
    sx = int(input("Enter length of SX Array: "))
    sy = int(input("Enter length of SY Array: "))
    x = [0]*sx
    y = [0]*sy
    array1 = createarray(x,sx)
    print("SY starts")
    array2 = createarray(y,sy)
    printcount(array1,array2)

main()

