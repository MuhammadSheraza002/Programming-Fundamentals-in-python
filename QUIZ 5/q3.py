def main1(from_index,here_index):
    a = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17]
    n = int(input("No of  many swaps: "))
    for i in range(n):
        temp = a[from_index]
        a[from_index] = a[here_index]
        a[here_index] = temp
        from_index+=1
        here_index+=1
    return a
def main():

    print(main1(2,9))
main()
