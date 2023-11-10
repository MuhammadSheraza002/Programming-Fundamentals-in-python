from random import randint
def main():
    data = [[[[randint(60,95) for stu in range(50)] for sub in range(6)] for sem in range(8)] for pgm in range(4)]
    p=0
    while p < 4:
        print("programe",p)
        sem=0
        while sem <8:
            print("\tsemester",sem)
            stu = 0
            print("\t\tstudent no","\t","sub1","\t","sub2","sub3","\t","sub4","sub5","\t","sub6")
            while stu <50:
                print("\t\tstudent",stu,end="\t")
                sub=0
                while sub <6:
                    print(data[p][sem][sub][stu],end="\t")
                    sub+=1
                print()
                stu+=1
            sem+=1
        p+= 1

main()
