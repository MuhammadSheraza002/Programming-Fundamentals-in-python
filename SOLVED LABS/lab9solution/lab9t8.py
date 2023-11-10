
def appending(ad,nd):
    i = 0
    while i < len(ad):
        if ad[i] == -1:
            j = 0
            while nd[j] != -1:
                ad[i] = nd[j]
                j += 1
                i += 1
            ad[i]=-1
            return ad

        i += 1
    return ad
def main():
    ad = [1,2,3,-1,10,22,33]
    nd = [4,5,-1,1,2]
    print(appending(ad,nd))
    print(ad)
main()
