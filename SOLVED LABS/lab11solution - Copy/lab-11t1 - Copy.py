from random import randint
def main():
    budjet = [[randint(5000,10000) for i in range(6)] for j in range(12)]
    heads = ["traveling","eating","books","stationary","charity","mobile package"]
    months = ["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
    print("total bujet of year")
    totalbudgut(budjet,heads)
    print("<------------------------------------------------------------------------------>")
    print("total charity of year")
    totalcharity(budjet,heads)
    print("<------------------------------------------------------------------------------>")

    print("month with maximum traveling ")
    MonthWithmaxtraveling(budjet,heads,months)
    print("<------------------------------------------------------------------------------>")

    monthplusHeadbudjet(budjet,heads,months)

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
def MonthWithmaxtraveling(budjet,heads,months):
    maxmonth = 0
    maximum = budjet[0][0]
    for month in range(12):
        if maximum < budjet[month][0]:
            maximum = budjet[month][0]
            maxmonth = month + 1
        else:
            pass
    print(months[maxmonth],"has max traveling with ",maximum,"rupee")
def monthplusHeadbudjet(budjet,heads,months):
    monthwisebudjet=[0] * 12
    for month in range(12):
        for head in range(6):
            monthwisebudjet[month] +=budjet[month][head]
    print("month wise budjet")
    print("month name",end="\t")
    for head in range(6):
        print(heads[head],end="\t")
    print("totalbudgut")
    for month in range(12):
        print(months[month],end="\t")
        for head in range(6):
            print(budjet[month][head],end="\t")
        print()
main()

