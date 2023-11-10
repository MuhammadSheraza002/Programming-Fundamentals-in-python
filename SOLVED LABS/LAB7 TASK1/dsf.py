class rational:
    pass
def convertfloat2int(f):
    i = 0
    count = 0
    while i < 7:
        if f[i] == ".":
            i = i + 1
            while ord(f[i]) <= ord("9") and ord(f[i]) >= ord("0"):
                count += 1
                i = i + 1
        else:
            count += 0
            i = i + 1
    return count
def main():
    print(convertfloat2int(0.4565))
main()
