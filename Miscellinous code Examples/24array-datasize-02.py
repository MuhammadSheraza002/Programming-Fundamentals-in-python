def main():
    arraySize = 10000000
    a = [0] * arraySize

    print("Enter +ve numbers, a -ve number to end data entry")
    print("Maximum numbers you can enter are", arraySize)

    dataSize = getData(a, arraySize)
    sum = sumData(a, dataSize)
    displayData(a, dataSize, sum)


def getData(a, arraySize):
    dataSize = 0
    num = 1
    while dataSize <= arraySize and num > 0:
        num = int(input())
        if num > 0:
            a[dataSize] = num
            dataSize = dataSize + 1
    if dataSize <= arraySize:
        return dataSize
    else:
        raise RuntimeError("Crossing limits of maximum data entry")


def sumData(a, dataSize):
    sum = 0
    i = 0
    while i < dataSize:
        sum = sum + a[i]
        i = i + 1
    return sum


def displayData(a, dataSize, sum):
    print(sum, end=" is sum of ")

    i = 0
    while i < dataSize:
        print(a[i], end=" ")
        i = i + 1
    print()


main()
