from random import randint
def main():
    data = [[[[randint(60,95) for stu in range(50)] for sub in range(6)] for sem in range(8)] for pgm in range(4)]
    for p in range(4):
        print("programe",p)
        for stu in range(50):
            print("\tstudent",stu)
            print("\t\tsemestor no","\t","sub1","\t","sub2","sub3","\t","sub4","sub5","\t","sub6")
            for sem in range(8):
                print("\t\tsemester",sem,end="\t")
                for sub in range(6):
                    print(data[p][sem][sub][stu],end="\t")
                print()

main()
