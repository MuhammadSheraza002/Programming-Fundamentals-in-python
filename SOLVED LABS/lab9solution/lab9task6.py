def sumofstring(s,size):
    i = 0
    sum = 0
    while i < size:
        if ord(s[i]) >= ord("0") and ord(s[i]) <= ord("9"):
            sum += int(s[i])
        else:
            pass
        i += 1
    return sum
def main():
    string = "34"
    length = len(string)
    print("sum =",sumofstring(string,length))
    print("lewngth=",len(string))
main()




