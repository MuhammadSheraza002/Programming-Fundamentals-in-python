#  Consider a four dimensional array contains the percentage marks for students
#  first dimension  is for program no (0,1,2 and 3)
#  second dimension is for semester no (0,1,2,3,4,5,6 and 7)
#  third  dimension is for subject no (0,1,2,3,4 and 5)
#  fourth dimension is for student no (0,1,2,3,4,...,49)

#  Write a function to compute and display the program wise average
#  Write a function to compute and display the semester wise average
#  Write a function to compute and display the subject wise average
#  Write a function to compute and display the program (passed as parameter) + semester wise average
#  Write a function to compute and display the result of , both passed as parameter
#  Following is code to populate the array with suitable random values and display them.

from random import randint
def main():
    marks = [[[[randint(10,99) for st in range(50)] for sub in range(6)] for sem in range(8)]for p in range(4)]
    programewiseaverage(marks)
    print("<-------------------------------------------------->")
    semesterwiseaverage(marks)
    print("<-------------------------------------------------->")
    subjectwiseaverage(marks)
    print("<-------------------------------------------------->")
    print("the array with suitable random values")
    properform(marks)
    print("<-------------------------------------------------->")
    print("Sem Wise  Avg 4  Prog")
    programe = int(input("enter program no less than 4= "))
    print("Sem Wise  Avg 4  Prog")
    SemWiseAvg4Prog(marks,programe)
    print("<-------------------------------------------------->")
    print("Sem Wise  Avg 4  Prog+student")
    program = int(input("enter program no less than 4= "))
    stu = int(input("enter student roll no less 50= "))
    print("Sem Wise  Avg 4  Prog+student")
    semWiseAvg4Progandstudent(program,marks,stu)
def properform(marks):
    for p in range(4):
        print("programe",p)
        for sem in range(8):
            print("\tsemester",sem)
            for sub in range(6):
                print("\t\tsubect",sub)
                for stu in range(50):
                    print("\t\t\tstudent",stu,"marks",marks[p][sem][sub][stu])

def programewiseaverage(marks):
    add = [0] * 4
    for p in range(4):
        for sem in range(8):
            for sub in range(6):
                for stu in range(50):
                    add[p] += marks[p][sem][sub][stu]
    print("programe  wise average")
    print("programe no","\t","average marks")
    for p in range(4):
        print("programe",p,"\t",add[p]/8/6/50)
def semesterwiseaverage(marks):
    add = [0] * 8
    for sem in range(8):
        for p in range(4):
            for sub in range(6):
                for stu in range(50):
                    add[sem] += marks[p][sem][sub][stu]
    print("semester  wise average")
    print("semester no","\t","average marks")
    for sem in range(8):
        print("semester",sem,"\t",add[sem]/4/6/50)
def subjectwiseaverage(marks):
    add = [0] * 6
    for sub in range(6):
        for p in range(4):
            for sem in range(8):
                for stu in range(50):
                    add[sub] += marks[p][sem][sub][stu]
    print("subject  wise average")
    print("subject no","\t","average marks")
    for sub in range(6):
        print("subject",sub,"\t",add[sub]/4/8/50)
def SemWiseAvg4Prog(marks,prgm):
    if prgm > 3:
        raise Exception("programe should be less than 4")
    print("semester wise average for program")
    print("semester no","\t","average marks")
    for sub in range(6):
        for stu in range(50):
            print("student",stu)
            for sem in range(8):
                print("\tsemester",sem,"\t",marks[prgm][sem][sub][stu]/6/50)

def semWiseAvg4Progandstudent(programe,marks,stu):
    if programe > 3:
        raise Exception("programe should be less than 4")
    if stu > 50:
        raise Exception("student roll no should be be less than 50")
    print("result of student of roll no",stu)
    avrg=[0] * 8
    print("semester no\t","average")
    for sem in range(8):
        for sub in range(6):
            avrg[sem] += marks[programe][sem][sub][stu]
    for sem in range(8):
        print("sem ",sem,"\t",avrg[sem]/6)
main()
