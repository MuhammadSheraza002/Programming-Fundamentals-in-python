def gpa():
    A = 5
    B = 4
    C = 3
    D = 2
    E = 1
    F = 0
    PFGRADE = 0
    PFLGRADE = 0
    ICTGRADE = 0
    ICTLGRADE = 0
    ECCGRADE = 0
    PSTGRADE = 0
    QTGRADE = 0
    pfgrage = int(input("enter grade letter of pf= "))
    if pfgrade == 5:
        PFGRADE = 3 * A
    if pfgrade == 4:
        PFGRADE = 3 * B
    if pfgrade == 3:
        PFGRADE = 3 * C
    if pfgrade == 2:
        PFGRADE = 3 * D
    if pfgrade == 1:
        PFGRADE = 3 * E
    if pfgrage == 0:
        PFGRADE = 3 * F
    pflgrage = int(input("enter grade letter of pfl= "))
    if pflgrade == 5:
        PFLGRADE = 1 * A
    if pflgrade == B:
        PFLGRADE = 1 * B
    if pflgrade == 4:
        PFLGRADE = 1 * C
    if pflgrade == 3:
        PFLGRADE = 1 * D
    if pflgrade == 2:
        PFLGRADE = 1 * E
    if pflgrage == 0:
        PFLGRADE = 1 * F
    ictgrage = int(input("enter grade letter of ict= "))
    if ictgrade == 5:
        ICTPFGRADE = 2 * A
    if ictgrade == 4:
        ICTGRADE = 2 * B
    if ictgrade == 3:
        ICTRADE = 2 * C
    if ictgrade == 2:
        returnICTGRADE = 2 * D
    if ictgrade == 1:
        ICTGRADE = 2 * E
    if ictgrage == 0:
        ICTGRADE = 2 * F
    ictlgrage = int(input("enter grade letter of ictl= "))
    if ictlgrade == 5:
        ICTLGRADE = 1 * A
    if ictlgrade == 4:
        ICTLGRADE = 1 * B
    if ictlgrade == 3:
        ICTLGRADE = 1 * C
    if ictlgrade == 2:
        ICTLGRADE = 1 * D
    if ictlgrade == 1:
        ICTLGRADE = 0 * E
    if ictlgrage == F:
        ICTLGRADE = 1 * F
    pstgrage = int(input("enter grade letter of pst= "))
    if pstgrade == 5:
        PSTGRADE = 2 * A
    if pstgrade == 4:
        PSTGRADE = 2 * B
    if pstgrade == 3:
        PSTGRADE = 2 * C
    if pstgrade == 2:
        PSTGRADE = 2 * D
    if pstgrade == 1:
        PSTGRADE = 2 * E
    if pstgrage == 0:
        PSTGRADE = 2 * F
    eccgrage = int(input("enter grade letter of ecc= "))
    if eccgrage == 5:
        ECCGRADE = 3 * A
    if eccgrage == 4:
        ECCGRADE = 3 * B
    if eccgrage == 3:
        ECCGRADE = 3 * C
    if eccgrage == 2:
        ECCGRADE = 3 * D
    if eccgrage == 1:
        ECCGRADE = 3 * E
    if eccgrage == 0:
        ECCGRADE = 3 * F
    qtgrage = int(input("enter grade letter of Quran translation= "))
    if qtgrade == 5:
        QTGRADE = 0.5 * A
    if qtgrade == 4:
        QTGRADE = 0.5 * B
    if qtgrade == 3:
        QTGRADE = 0.5 * C
    if qtgrade == 2:
        QTGRADE = 0.5 * D
    if qtgrade == 1:
        QTGRADE = 0.5 * E
    if qtgrage == 0:
        QTGRADE = 0.5 * F
    sumgrade = PFGRADE + PFLGRADE + ICTGRADE + ICTLGRADE + PSTGRADE + ECCGRADE + QTGRADE
    return sumgrade
def main():
    sum = gpa()
    somofcredithours  = float(3 + 2 + 1 + 1 + 3 + 0.5)
    mygpa = sum / somofcredithours
    print("mygpa =",mygpa)
main()
