def main():
    f = open("Lab03t1.pgm","r")
    f2 = open("Lab03t2.pgm","w")
    f2.write(f.readline())
    m = f.read(4)
    k = f.read(4)
    f2.write(k.strip()+" ")
    f2.write(m.strip()+"\n")
    f2.write(f.readline())
    data1 = [[0for j in range(274)] for i in range(302)]
    data2 = [[0for j in range(302)] for i in range(274)]
    for i in range(302):
        for j in range(274):
            a = f.read(4)
            data1[i][j] = a.strip()
    for i in range(302):
        for j in range(274):
            data2[j][i] = data1[i][j]
            f2.write(str(data2[j][i])+" ")
        f2.write("\n")
    f.close()
    f2.close()
main()
