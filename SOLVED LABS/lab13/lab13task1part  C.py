def index(Rollno,Array):
    i= 0
    while i < len(Array):
        if Rollno == Array[i]:
            return i+1
        else:
            pass
        i+=1
    raise Exception(f"{Rollno} is incorrect rollno,write correct roll no")
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
def namearray(file):
    f = file
    f.readline()
    f.readline()
    f.read(10)
    name=[""]*9
    rollNo = [""]*9
    blank=""
    for i in range(7):
        rollNo[i]+=f.read(10)
        name[i]+=f.read(32).strip()
        c = f.read(1)
        while c!="\n":
            blank+=c
            c = f.read(1)
        f.readline()
        f.readline()
    return rollNo
def main():
    f1 = open("result_data.txt","r+")
    r =input("Enter your roll no Completely")
    array = namearray(open("result_data.txt","r+"))
    name=""
    rollno=""
    sub1=""
    sub2=""
    sub3=""
    ict=[0 for i in range(3)]
    pf=[0 for i in range(3)]
    dld=[0 for i in range(3)]
    n = index(r,array)
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
    print(f"{name} Updated for roll no {rollno}")
    print()
    print(n,"-",rollno,"\t",name,":")
    print("Course Total Grade")
    print(sub1,"\t",ICT,"\t",ICTG)
    print(sub2,"\t",PF,"\t",PFG)
    print(sub3,"\t",DLD,"\t",DLDG)
    print("================")
    print("OPM","\t",avrg," ",cgpa(avrg))
main()

