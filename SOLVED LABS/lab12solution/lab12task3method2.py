from math import *
def index(c,city):
    i= 0
    while i < len(city):
        if c == city[i]:
            return i
        else:
            pass
        i+=1
    raise Exception(f"{c}  is incorrect city,write correct name")
def main():
    c1= input("Enter name of first city: ")
    c2= input("Enter name of second city: ")
    f1 =open("pakcities.txt","r")
    blank =""
    cities = [""for j in range(74)]
    d1 = [0.0 for k in range(74)]
    d2 = [0.0 for m in range(74)]
    i = 0
    while i < 74:
        a=f1.read(1)
        while a !="\t":
            cities[i]+=a
            a=f1.read(1)
        a=a
        while a !="\t" or a !=" ":
            cities[i]+=a
            a=f1.read(1)
        d1[i]=float(a + f1.read(7).strip())

        d2[i]=float(f1.read(7))
        blank+=f1.read(1)
        i+=1



    """
    c1=φ1
    c2=φ2
    const1=Δφ
    const2=Δλ
    """
    R = 6371e3
    lat1 = d1[index(c1,cities)]
    lon1 = d2[index(c1,cities)]
    lat2 = d1[index(c2,cities)]
    lon2 = d2[index(c2,cities)]

    co1 = lat1 * (pi/180)
    co2 = lat2 * (pi/180)
    const1=(lat2-lat1) * (pi/180)
    const2=(lon2-lon1) * (pi/180)
    a = sin(const1/2) * sin(const1/2) +cos(co1) * cos(co2) * sin(const2/2) * sin(const2/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = R * c
    print(f"distance of {c1} and {c2}={d}")
main()
