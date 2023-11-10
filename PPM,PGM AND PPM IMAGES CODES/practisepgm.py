class PGM:
    pass
def ReadTextPGM(file):
    file = open(file)
    img = PGM()
    img.header= file.readline().rstrip()
    img.width,img.height=file.readline().rstrip().split(" ")
    img.shades= file.readline().rstrip()
    img.width = int(img.width)
    img.height = int(img.height)

    data = file.readlines()
    file.close()
    img.data = []
    for line in data:
        nums = line.rstrip().split(" ")
        for num in nums:
            img.data.append(int(num))
    img.datas =  [[0 for i in range(img.width)] for j in range(img.height)]
    i = 0
    for height in range(img.height):
        for width in range(img.width):
            img.datas[height][width] = img.data[i]
            i+=1
    return img
def main():
    img = ReadTextPGM("Lab03t1.pgm")
    print("header= ",img.header)
    print("width= ",img.width)
    print("height= ",img.height)
    print("shades= ",img.shades)
    print(img.datas)
main()

