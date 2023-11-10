def main():
    n = 10
    ar = [0] * n
    k = 0
    sum = 0
    count = 0
    while k < n:
        ar[k] = int(input("enter values= "))
        sum += ar[k]
        k += 1
        count = count + 1
    print("array= ",ar)
    print("count of array=",count)
    print("sum of arrays indices is= ",sum)
    avrg = sum / n
    print("average of indices of arrays= ",avrg)
main()
