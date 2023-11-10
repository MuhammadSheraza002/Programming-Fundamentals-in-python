def main():
    string = ""
    triangle = createstring(string)
    i = 1
    tring = ""
    space = len(triangle) // 2
    while i < 10:
        print(space * " ",triangle[0:i],space * " ")
        space -= 1
        i += 2
def createstring(string):
    m = 107
    i = 0
    while i < 9:
        string += (chr(m))
        i = i + 1
        m += 1

    return string
main()
