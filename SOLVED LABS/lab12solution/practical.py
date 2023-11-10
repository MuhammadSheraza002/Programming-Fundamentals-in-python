"""
Roll NoName                     Crs Md Ss Fn
======================================== ====== == ==
BSEF09M001Hammad Khan			ITC 22 21 31
BSEF09M001Hammad Khan			PF  14 15 25
BSEF09M001Hammad Khan			DLD 20 18 22
BSEF09M003Younas Ahmad			ITC 30 00 29
BSEF09M003Younas Ahmad			PF  34 25 30
BSEF09M003Younas Ahmad			DLD 10 15 10
BSEF09M005Riffat Kaleem			ITC 33 20 33
BSEF09M005Riffat Kaleem			PF  26 11 35
BSEF09M005Riffat Kaleem			DLD 30 24 38
BSEF09M012Barkat Jan			ITC 25 18 34
BSEF09M012Barkat Jan			PF  19 20 28
BSEF09M012Barkat Jan			DLD 28 21 34
BITF09M002Khawer Hayat			ITC 11 18 37
BITF09M002Khawer Hayat			PF  19 17 27
BITF09M002Khawer Hayat			DLD 31 22 34
BITF09M003Kishwar Hameed		ITC 24 20 33
BITF09M003Kishwar Hameed		PF  28 24 37
BITF09M003Kishwar Hameed		DLD 19 15 26
BITF09M010Yasir Ubaid			ITC 18 20 31
BITF09M010Yasir Ubaid			PF  25 21 34
BITF09M010Yasir Ubaid			DLD 29 22 33
BSEF09M011MUHAMMAD sheraz		ICT 32 18 45
BSEF09M011MUHAMMAD sheraz		PF  34 22 39
BSEF09M011MUHAMMAD sheraz		DLD 24 23 33
BSEF09M012Hassan fareed			ICT 32 18 45
BSEF09M012Hassan fareed			PF  34 22 39
BSEF09M012Hassan fared			DLD 24 23 33"""
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
    f1 = open("result_data.txt","r")
    f2 = open("result_report.txt","w")
    a = f1.readline()
    b = f1.readline()
    rollno = ["" for i in range(9)]
    name = ["" for st in range(9)]
    blank = " "
    sub1 = ["" for i in range(9)]
    sub2 = ["" for i in range(9)]
    sub3 = ["" for i in range(9)]
    ict = [[0 for st in range(3)]for i in range(9)]
    pf = [[0 for st in range(3)]for i in range(9)]
    dld = [[0 for st in range(3)]for i in range(9)]
    for i in range(9):
        rollno[i]+=f1.read(10)
        c = f1.read(1)
        while c !="\t":
            name[i] += c
            c = f1.read(1)
        k = c
        while k =="\t" or k ==" ":
            blank +=k
            k = f1.read(1)
        c = k
        sub1[i]+= c + f1.read(3).strip()
        ict[i][0] =int(f1.read(3).strip())
        ict[i][1] =int(f1.read(3).strip())
        ict[i][2] =int(f1.read(2))
        f1.read(1)
        f1.read(10)
        c = f1.read(1)
        while c !="\t":
            blank += c
            c = f1.read(1)
        k = c
        while k =="\t" or k ==" ":
            blank +=k
            k = f1.read(1)
        c = k
        sub2[i]+= c + f1.read(3).strip()
        pf[i][0] = int(f1.read(3).strip())
        pf[i][1] =int(f1.read(3).strip())
        pf[i][2] =int(f1.read(2))
        f1.read(1)
        f1.read(10)
        c = f1.read(1)
        while c !="\t":
            blank += c
            c = f1.read(1)
        k = c
        while k =="\t" or k ==" ":
            blank +=k
            k = f1.read(1)
        c = k
        sub3[i]+= c + f1.read(3).strip()
        dld[i][0] = int(f1.read(3).strip())
        dld[i][1] =int(f1.read(3).strip())
        dld[i][2] =int(f1.read(2))
        f1.read(1)
    for i in range(9):
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
# Write your code here :-)
