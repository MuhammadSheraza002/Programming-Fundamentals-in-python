def main():
    size = 12
    array = [0] * size
    createdarray = createarray(array,size)

    print(garbage(createdarray))
    print(data(createdarray))
def createarray(array,size):
    i = 0
    while i < size:
        array[i] = int(input())
        i = i + 1
    return array
def data(array):
    i = 0
    a = []
    while i < len(array):
        if array[i]==-1:
            return a
        else:
            a.append(array[i])
        i+=1
    return a
def garbage(array):
    i = 0
    a = []
    while i < len(array):
        if array[i]!=-1:
            pass
        else:
            m = i
            while m < len(array):
                a.append(array[m])
                m+=1
            return a
        i+=1
    return a
main()
