def countvowel(a,n):
    i = 0
    count = 0
    while i < n:
        if a[i] == "a" or a[i] == "A":
            count += 1
        elif a[i] == "e" or a[i] == "E":
            count += 1
        elif a[i] == "i" or a[i] == "I":
            count += 1
        elif a[i] == "o" or a[i] == "O":
            count += 1
        elif a[i] == "u" or a[i] == "U":
            count += 1
        else:
            count += 0
        i = i + 1
    return count
def main():
    name = "SeuERAZ"
    count = countvowel(name,len(name))
    print("no of vowels in my name sheraz= ",count)
main()

