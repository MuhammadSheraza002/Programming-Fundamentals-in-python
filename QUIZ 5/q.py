def main1(arr,sz):
    for i in range(sz-1):
        if arr[i]==-1:
            if arr[i+1]!=-1:
                arr.insert(i,arr[i+1])
            else:
                pass
        else:
            arr[i]==arr[i]
    return arr
def main():
    size= 9
    array = [-1]*size
    i = 0
    while i < size:
        array[i] = int(input())
        i+=1
    print(array)
    array.insert(1,2)
    print(array)
    print(main1(array,size))
main()
