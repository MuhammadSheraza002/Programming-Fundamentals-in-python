class rational:
    pass
def createrational(p,q):
    r = rational()
    r.p = p
    r.q = q
    return r.p,r.q
def convert2pqform(p,q):
    r = rational()
    r.p = p
    r.q = q
    return r.p,r.q
def simplification(r1,r2):
    r = rational()
    r.p = r1
    r.q = r2
    i = 2
    d = r.p
    n = r.q
    while i <= r.p and i <= r.q:
        if r.p % i == 0 and r.q % i == 0:
            d = r.p / i
            n = r.q / i
            i += 1
        else:
            i = i + 1

    return int(d),int(n)
def Unary_minus_of_rational_number(p,q):
    r = rational()
    r.p = p
    r.q = q
    return int(-1 * p),int(q)
def reciprpocal_of_rational_number(p,q):
    r = rational()
    r.p = p
    r.q = q
    return int(q),int(p)
def binaryAddition(r1,r2):
    r1 = rational()
    r2 = rational()
    r1.p = 2
    r1.q = 4
    r2.p = 4
    r2.q = 3
    rp = r1.p + r2.p
    rq = r1.q + r2.q
    return rp,rq
def binarysubstraction(r1,r2):
    r1 = rational()
    r2 = rational()
    r1.p = 2
    r1.q = 4
    r2.p = 4
    r2.q = 3
    rp = r1.p - r2.p
    rq = r1.q - r2.q
    return rp,rq
def binarymultiplition(r1,r2):
    r1 = rational()
    r2 = rational()
    r1.p1 = 2
    r1.q1 = 8
    r2.p2 = 6
    r2.q2 = 4
    rp = r1.p1 * r2.p2
    rq = r1.q1 * r2.q2
    return rp,rq
def binarydivision(r1,r2):
    r1 = rational()
    r2 = rational()
    r1.p1 = 23
    r1.q1 = 2
    r2.p2 = 21
    r2.q2 = 3
    rp = (r1.p1) / (r2.p2)
    rq = (r1.q1) / (r2.q2)
    return rp,rq
def conditionaloperator(p,q):
    r = rational()
    r.p = p
    r.q = q
    if r.p > r.q:
        return r.p
    else:
        return r.q
def convert2complex(p,q):
    r = rational()
    r.p = p
    r.q = q
    return complex(r.p,r.q)
def convertfloat2int(p,q):
    r = rational()
    r.p = p
    r.q = q
    return round(r.p),round(r.q)
def main():
    print("creation_of_rationl numbers =",createrational(2,3))
    print("simplification of two rational nos (100,30)= ",simplification(100,30))
    print("Conversion to the string form => (p, q)= ",convert2pqform(3,7))
    print("Unary_minus_rational_number (100,30)=",Unary_minus_of_rational_number(100,30))
    print("reciprocal_of_rational_number (100,30)=",reciprpocal_of_rational_number(100,30))
    print("binaryaddition=",binaryAddition(1,7))
    print("binary substraction= ",binarysubstraction(1,32))
    print("binary multiplication= ",binarymultiplition(1,2))
    print("binarydivision= ",binarydivision(3,5))
    print("Binary conditional operations =",conditionaloperator(3,4),"is greater binary no")
    print("Conversions to other appropriate data type of rational no(2,4)=",convert2complex(2,4))
    print("Conversions to other appropriate data type of rational no= ",convertfloat2int(2.4,4.5))

main()



