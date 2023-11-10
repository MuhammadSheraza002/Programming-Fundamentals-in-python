def main():
    size = 12
    array = [0] * size
    createdarray= createarray(array,size)
    print("created array = ",createdarray)
    garbagedata = countnegative(createdarray,size)
    print("no of index less than 0: ",garbagedata)
    usefuldata = countpositive(createdarray,size)
    print("positive no of indexes : ",usefuldata)
    p = size - garbagedata
    n = size - usefuldata
    positivearray = positive(createdarray,p)
    print("positive array",positivearray)
    negativearray = negative(createdarray,n)
    print("negative array",negativearray)
    append = len(positivearray) + len(negativearray)
    totalsize = append
    addition = add(positivearray,negativearray,totalsize)
    print("basedarry=",addition)
def createarray(array,size):
    i = 0
    while i < size:
        array[i] = int(input())
        i = i + 1
    return array
def countnegative(createdarray,size):
    i = 0
    count = 0
    while i < size:
        if createdarray[i] < 0:
            count += 1
        else:
            pass
        i += 1
    return count
def countpositive(createdarray,size):
    i = 0
    count = 0
    while i < size:
        if createdarray[i] >= 0:
            count += 1
        else:
            pass
        i += 1
    return count
def positive(array,size):
    i = 0
    m = 0
    arr = [0] * size
    while i < size:
        if array[i] >= 0:
            arr[m] += array[i]
            m += 1
        else:
            pass
        i = i + 1
    return arr
def negative(array,size):
    i = 0
    m = 0
    arr = [0] * size
    while i < size:
        if array[i] < 0:
            arr[m] += array[i]
            m += 1
        else:
            pass
        i = i + 1
    return arr
def add(positivearray,negativearray,totalsize):
    p = len(positivearray) - 1
    n = len(negativearray) - 1
    i = 0
    array = [0] * totalsize
    while i < totlesize:
        positivearray.append.negativearray[i]










