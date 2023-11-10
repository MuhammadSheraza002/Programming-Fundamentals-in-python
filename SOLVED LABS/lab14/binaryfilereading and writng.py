def main():
    f1 = open("result_data.txt","r")
    f = open("result_cv.b","wb+")
    for i in f1:
        a = i.encode()
        print(type(a))
        print(i)


    f2 = open("result_cvwrite.txt","w")
    for i in f:
        a = i.decode()
        f2.write(a)
        print(type(a))
    f1.close()
    f2.close()
    f.close()
main()

