"""Consider a 3D array named sales with first dimension as region of size
320, second
dimension as salesman of size 30, and third dimension as day shift of size
3 The array has sales of a day and salesmen can work in any region and at
any shift Write code or function for the following.
"""

#The statement or statements to create the array.
#Q-2: The statements to print salesman wise sales.
from random import randint
#The statements to print salesman wise sales.
def SalemanWiseSale(sale):
    for sm in range(30):
        print(f"Saleman No {sm+1}")
        for r in range(20):
            print(f"\tRegion No {r+1}")
            for d in range(3):
                print(f"\t\tday shift No {d+1} {sale[r][sm][d]}")
#total sales per shift
def total_sales_per_shift(sale):
    total = [0 for d in range(3)]
    for d in range(3):
        for r in range(20):
            for sm in range(30):
                total[d] += sale[r][sm][d]

    for d in range(3):
        print(f"Sale No {d} = {total[d]} sale")
def BestSaleMan(sale):
    saleman = [0]*30
    for sm in range(30):
        for r in range(20):
            for d in range(3):
                saleman[d] += sale[r][sm][d]
    max = saleman[0]
    bestsaleman = 0
    for i in range(30):
        if max < saleman[i]:
            max = saleman[i]
            bestsaleman = i
        else:
            pass

    print(f"Best Sale Man {bestsaleman}= {max}")
def main():
    sales = [[[randint(2,4) for d in range(3)]for sm in range(30)]for r in range(20)]
    SalemanWiseSale(sales)
    total_sales_per_shift(sales)
    BestSaleMan(sales)
main()

