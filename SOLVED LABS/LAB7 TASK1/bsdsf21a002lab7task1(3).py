def notabs(s):
    i = 0
    r = ""
    while i < len(s):
        if s[i] == "\t":
            r += "   "
        else:
            r = r + s[i]
        i += 1
    return r
def main():
    p = "d\tjdvbsa"
    a = notabs(p)
    print(a)
main()

