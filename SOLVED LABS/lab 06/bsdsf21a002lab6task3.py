class rationals:
    p = int(input("enter value of p= "))
    q = int(input("enter value of q= "))
def main():
    rational = rationals()
    if rational.q != 0:
        print("it is rationl no can written as:",rational.p,"/",rational.q)
    else:
        print("it is not rationl no cannot written as:",rational.p,"/",rational.q)
main()
