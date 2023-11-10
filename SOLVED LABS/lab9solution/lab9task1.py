def main():
    string = ""
    triangle = createstring(string)
    i = 1
    while i < 10:
        print(triangle[0:i])
        i += 1
def createstring(string):
    m = 107
    i = 0
    while i < 9:
        string += (chr(m))
        i = i + 1
        m += 1

    return string
main()
