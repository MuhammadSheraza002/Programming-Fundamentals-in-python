def cgpa(avrg):
    if avrg <= 100 and avrg>=85:
        return "A+"
    elif avrg <= 84 and avrg>=80:
        return "A"
    elif avrg <= 79 and avrg>=75:
        return "B+"
    elif avrg <= 74 and avrg>=70:
        return "B"
    elif avrg <= 69 and avrg>=65:
        return "C+"
    elif avrg <= 64 and avrg>=60:
        return "C"
    elif avrg <= 59 and avrg>=55:
        return "C-"
    elif avrg <= 54 and avrg>=50:
        return "D"
    elif avrg <50:
        return "F"
def grade(a,b,c):
    sum = total(a,b,c)
    if sum <= 100 and sum>=85:
        return "A+"
    elif sum <= 84 and sum>=80:
        return "A"
    elif sum <= 79 and sum>=75:
        return "B+"
    elif sum <= 74 and sum>=70:
        return "B"
    elif sum <= 69 and sum>=65:
        return "C+"
    elif sum <= 64 and sum>=60:
        return "C"
    elif sum <= 59 and sum>=55:
        return "C-"
    elif sum <= 54 and sum>=50:
        return "D"
    elif sum <50:
        return "F"
def total(a,b,c):
    sum = int(a) + int(b) + int(c)
    return sum
def RESULT():
    name=""
    rollno=""
    sub1=""
    sub2=""
    sub3=""
    ict=[0 for i in range(3)]
    pf=[0 for i in range(3)]
    dld=[0 for i in range(3)]
    f1 = open("result_data.txt","r")
    print("<-----------------TASK 1(A)------------------>")
    n = int(input("Enter student number between 1 and 9: "))
    if n <=0 or n>9:
        raise Exception("write student no between 1 and 9")
    f1.seek((((n-1)*3)*59)+118)
    rollno+=f1.read(10)
    name+=f1.read(32).strip()
    sub1+=f1.read(7).strip()
    ict[0]=int(f1.read(3).strip())
    ict[1]=int(f1.read(3).strip())
    ict[2]=int(f1.read(2).strip())
    f1.read(1)
    f1.read(42)
    sub2+=f1.read(7).strip()
    pf[0]=int(f1.read(3).strip())
    pf[1]=int(f1.read(3).strip())
    pf[2]=int(f1.read(2).strip())
    f1.read(1)
    f1.read(42)
    sub3+=f1.read(7).strip()
    dld[0]=int(f1.read(3).strip())
    dld[1]=int(f1.read(3).strip())
    dld[2]=int(f1.read(2).strip())
    f1.read(1)
    ICT = total(ict[0],ict[1],ict[2])
    PF = total(pf[0],pf[1],pf[2])
    DLD = total(dld[0],dld[1],dld[2])
    ICTG = grade(ict[0],ict[1],ict[2])
    PFG = grade(pf[0],pf[1],pf[2])
    DLDG = grade(dld[0],dld[1],dld[2])
    avrg=(ICT+PF+DLD)/3
    print(n,"-",rollno,"\t",name,":")
    print("Course Total Grade")
    print(sub1,"\t",ICT,"\t",ICTG)
    print(sub2,"\t",PF,"\t",PFG)
    print(sub3,"\t",DLD,"\t",DLDG)
    print("================")
    print("OPM","\t",avrg," ",cgpa(avrg))

def PfAverage():
    f1 = open("result_data.txt","r")
    totalmarks=0
    for i in range(9):
        f1.seek((i*3*59)+118+48+59)
        totalmarks+=int(f1.read(3).rstrip())
        totalmarks+=int(f1.read(3).rstrip())
        totalmarks+=int(f1.read(2).rstrip())
        f1.read(1)
    print(f"Average result of pf is = {totalmarks}")




def main():
    RESULT()
    print()
    print("<--------------------TASK B----------------------------->")
    PfAverage()
    print()

    print("<--------------------TASK E----------------------------->")
    print("answer is in result_report.txt file")
    resultreport()

def resultreport():
    f1 = open("result.txt","r")
    f2 = open("result_report.txt","w")
    a = f1.readline()
    rollno = ["" for i in range(7)]
    name = ["" for st in range(7)]
    blank = " "
    sub1 = ["" for i in range(7)]
    sub2 = ["" for i in range(7)]
    sub3 = ["" for i in range(7)]
    ict = [["" for st in range(3)]for i in range(7)]
    pf = [["" for st in range(3)]for i in range(7)]
    dld = [["" for st in range(3)]for i in range(7)]
    for i in range(7):
        c = f1.read(1)
        while c !=",":
            rollno[i]+= c
            c = f1.read(1)
        k = f1.read(1)
        while k !=",":
            name[i] += k
            k = f1.read(1)
        c = f1.read(1)
        while c !=",":
            sub1[i] += c
            c = f1.read(1)
        c = f1.read(1)
        while c !=",":
            ict[i][0]+=c
            c = f1.read(1)
        c = f1.read(1)
        while c !=",":
            ict[i][1]+=c
            c=f1.read(1)
        c = f1.read(1)
        while c !="\n":
            ict[i][2]+=c
            c=f1.read(1)
        c=f1.read(1)
        while c !=",":
            blank+= c
            c = f1.read(1)
        k = f1.read(1)
        while k !=",":
            blank+= k
            k = f1.read(1)
        c = f1.read(1)
        while c !=",":
            sub2[i] += c
            c = f1.read(1)

        c = f1.read(1)
        while c !=",":
            pf[i][0]+=c
            c = f1.read(1)
        c = f1.read(1)
        while c !=",":
            pf[i][1]+=c
            c=f1.read(1)
        c = f1.read(1)
        while c !="\n":
            pf[i][2]+=c
            c=f1.read(1)
        c=f1.read(1)
        while c !=",":
            blank+= c
            c = f1.read(1)
        k = f1.read(1)
        while k !=",":
            blank+= k
            k = f1.read(1)
        c = f1.read(1)
        while c !=",":
            sub3[i] += c
            c = f1.read(1)
        c = f1.read(1)
        while c !=",":
            dld[i][0]+=c
            c = f1.read(1)
        c = f1.read(1)
        while c !=",":
            dld[i][1]+=c
            c=f1.read(1)


        dld[i][2]+=f1.read(2)
        f1.read(1)

    for i in range(7):
        f2.write(str(i+1)+". "+rollno[i]+" " + name[i]+"\n")
        f2.write("sub\t"+"Mid\t"+"Sessional\t"+"Final\t"+" "+"Total\t"+" "+"Grade"+"\n")
        f2.write(sub1[i]+"\t")
        f2.write(str(ict[i][0])+"\t "+str(ict[i][1])+"\t\t"+str(ict[i][2])+"\t ")
        f2.write(str(total(ict[i][0],ict[i][1],ict[i][2]))+"\t")
        f2.write(grade(ict[i][0],ict[i][1],ict[i][2])+"\n")
        f2.write(sub2[i]+"\t")
        f2.write(str(pf[i][0])+"\t "+str(pf[i][0])+"\t\t"+str(pf[i][0])+"\t ")
        f2.write(str(total(pf[i][0],pf[i][1],pf[i][2]))+"\t")
        f2.write(grade(pf[i][0],pf[i][1],pf[i][2])+"\n")
        f2.write(sub3[i]+"\t")
        f2.write(str(dld[i][0])+"\t "+str(dld[i][1])+"\t\t"+str(dld[i][2])+"\t ")
        f2.write(str(total(dld[i][0],dld[i][1],dld[i][2]))+"\t")
        f2.write(grade(dld[i][0],dld[i][1],dld[i][2])+"\n")
    f1.close()
    f2.close()
main()


