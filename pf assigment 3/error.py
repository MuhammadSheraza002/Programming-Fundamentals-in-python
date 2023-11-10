
def max(arr,n):
    m = 0
    i = 0
    while i < n:
        if arr[i] > m:
            m = arr[i]
        i = i + 1
    return m
def main():
    ar = [3,5,7,9976,99,34,790]
    ark = max(ar,len(ar))
    print(ark)

main()


