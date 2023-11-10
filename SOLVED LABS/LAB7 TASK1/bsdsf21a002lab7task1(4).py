def propercase(s,n):
    i = 1
    r = ""
    if ord(s[0]) <= ord("z") and ord(s[0]) >= ord("a"):
        r = r + chr(ord(s[0]) - ord("a") + ord("A"))
    else:
        r = r + s[0]
    while i < n:
        if s[i] == "." or s[i] == " ":
            r = r + s[i]
            i += 1
            if ord(s[i]) <= ord("z") and ord(s[i]) >= ord("a"):
                r = r + chr(ord(s[i]) - ord("a") + ord("A"))
            else:
                r = r + s[i]
        elif ord(s[i]) <= ord("Z") and ord(s[i]) >= ord("A"):
            r = r + chr(ord(s[i]) - ord("A") + ord("a"))
        else:
            r = r + s[i]
        i = i + 1
    return r

def main():
    p = "HELLO!.my nAme is MUHAMMAD Sheraz"
    name = propercase(p,len(p))
    print(name)
main()

