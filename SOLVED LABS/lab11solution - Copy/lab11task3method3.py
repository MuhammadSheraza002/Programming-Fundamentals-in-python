from random import randint
def main():
    data = [[[[randint(60,95) for stu in range(50)] for sub in range(6)] for sem in range(8)] for pgm in range(4)]
    print("programe no\t","semester no",end="\t")
    for s in range(6):
        print("sub",s,end="\t")
    print()
    for p in range(4):
        for sem in range(8):
            for stu in range(50):
                print("programe",p,"semester",sem,"student",stu,end="\t")
                for sub in range(6):
                    print(data[p][sem][sub][stu],end="\t")
                print()


main()
