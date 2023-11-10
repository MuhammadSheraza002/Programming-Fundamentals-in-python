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
    i = size - 1
    m = 0
    while i > 0:
        if array[i] < array[i - 1]:
            temp = array[i]
            array[i] = array[i - 1]
            array[i - 1]  = temp
        else:
            pass
        i = i - 1

    return array
main()
