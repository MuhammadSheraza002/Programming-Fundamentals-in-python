def checknumber(s):
    i = 0
    while i < len(s):
        if ord(s[i]) >= ord("0") and ord(s[i]) <= ord("9") or ord(s[i])==ord("+") or ord(s[i])==ord("-"):
            i += 1
        else:
            return False
    return True
def main():
    numbers = "+6jj043"
    print("bolean value= ",checknumber(numbers))
main()
