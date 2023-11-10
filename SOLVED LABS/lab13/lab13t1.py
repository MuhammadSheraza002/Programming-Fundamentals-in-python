def grade(a,b,c):
    sum = int(a) + int(b) + int(c)
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
def main():
    name=""
    rollno=""
    sub1=""
    sub2=""
    sub3=""
    blank=""
    ict=[0 for i in range(3)]
    pf=[0 for i in range(3)]
    dld=[0 for i in range(3)]
    f1 = open("result_data.txt","r")
    n = int(input("enter student n: "))
    if n <=0 or n>9:
        raise Exception("write student no between 1 and 9")
    f1.seek((((n-1)*3)*58)+116)
    print(f1.tell())
    rollno+=f1.read(10)
    print(rollno)
    c=c=f1.read(1)
    while c!="\t":
        name+=c
        c=f1.read(1)
    k = c
    while k=="\t" or k==" ":
        blank+=k
        k = f1.read(1)
    c = k
    sub1+=c + f1.read(6).strip()
    ict[0]=int(f1.read(3).strip())
    ict[1]=int(f1.read(3).strip())
    ict[2]=int(f1.read(2).strip())
    f1.read(1)
    c=f1.read(1)
    while c!="\t":
        blank+=c
        c=f1.read(1)
    k = c
    while k=="\t" or k==" ":
        blank+=k
        k = f1.read(1)
    c=k
    sub2+=c+f1.read(6).strip()
    pf[0]=int(f1.read(3).strip())
    pf[1]=int(f1.read(3).strip())
    pf[2]=int(f1.read(2).strip())
    f1.read(1)
    c=f1.read(1)
    while c!="\t":
        blank+=c
        c=f1.read(1)
    k = c
    while k=="\t" or k==" ":
        blank+=k
        k = f1.read(1)
    c=k
    sub3+=c+f1.read(6).strip()
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
    print("Course  Total  Grade")
    print(sub1,"\t",ICT,"\t",ICTG)
    print(sub2,"\t",PF,"\t",PFG)
    print(sub3,"\t",DLD,"\t",DLDG)
    print("---------------------")
    print("---------------------")
    print("OPM","\t",avrg,"\t",DLDG)



main()
