from random import randint
def main():
    n = int(input("enter no of files: "))
    for i in range(n):
        fname=input("write name of files: ")
        f=createNlists(fname)
def createNlists(fname):
    no_of_lists = randint(3,9)
    file =open(fname,"w")
    file.write(str(no_of_lists)+"\n")
    for j in range(no_of_lists):
        size = randint(3,6)
        a =[randint(1,99) for s in range(size)]
        file.write(str(size)+" ")
        for t in range(size):
            file.write(str(a[t])+" ")
        file.write("\n")
main()



