def main():
    size = 12
    array = [0] * size
    createdarray = createarray(array,size)
    print("createdarray=",createdarray)
    bubble = bubblesort(createdarray,size)
    print("bubble=",bubble)
def createarray(array,size):
    i = 0
    while i < size:
        array[i] = int(input())
        i = i + 1
    return array
def bubblesort(array,size):
    m = 0
    while m <=size - 2:
        i = size - 2
        while i >=0:
            if array[i]>array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
            else:
                pass
            i-=1
        m+=1
    return array




main()
