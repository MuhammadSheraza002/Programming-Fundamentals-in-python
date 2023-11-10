from random import randint
def main():
    budjet = [[randint(5000,10000) for i in range(6)] for j in range(12)]
    heads = ["traveling","eating","books","stationary","charity","mobile package"]
    totalbudgut(budjet,heads)
    print("<-------------------------------------------------->")
    totalcharity(budjet,heads)
    print("<-------------------------------------------------->")
    MonthWithmaxtraveling(budjet,heads)
    print("<-------------------------------------------------->")
    monthwisebudjet(budjet,heads)
    print("<-------------------------------------------->")
def totalbudgut(budjet,heads):
    total = 0
    for month in range(12):
        for head in range(6):
            total += budjet[month][head]
    print("total bugjet of year= ",total)
def totalcharity(budjet,heads):
    total = 0
    for month in range(12):
            total += budjet[month][4]
    print("totalcharity of year= ",total)
def MonthWithmaxtraveling(budjet,heads):
    maxmonth = 0
    maximum = budjet[0][0]
    for month in range(12):
        if maximum < budjet[month][0]:
            maximum = budjet[month][0]
            maxmonth = month + 1
        else:
            pass
    print("month no",maxmonth,"has max traveling with ",maximum,"rupee")
def monthwisebudjet(budjet,heads):
    monthwisebudjet=[0] * 12
    for month in range(12):
        for head in range(6):
            monthwisebudjet[month] +=budjet[month][head]
    print("month wise budjet")
    print("month no","\t","bugjet")
    for month in range(12):
        print("month",month + 1,monthwisebudjet[month],end="\t")
        for head in range(6):
            print(budjet[month][head],end="\t")
        print()
main()

