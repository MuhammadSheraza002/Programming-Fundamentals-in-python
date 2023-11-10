class BMP:
    pass


def ReadtextBMP(filename):
    img = BMP()
    file=open(filename,"r")
    img.header=file.readline().rstrip()
    img.width,img.height=file.readline().rstrip().rsplit(" ")
    img.shades=file.readline().rstrip()
    img.width=int(img.width)
    img.height=int(img.height)
    img.shades=int(img.shades)
    lines = file.readlines()
    img.data=[]
    file.close()
    for i in lines:
        nums = i.rstrip().split(" ")
    for num in nums:
        img.data.append(int(num))
    return img
def main():
    fname=input("Enter file name : ")
    img = ReadtextBMP(fname)
    print("Image properties")
    print("================")
    print("Signature",img.header)
    print("Width", img.width)
    print("Height", img.height)
    print("Shades", img.shades)
    print("Data Size from different ways")
    print(len(img.data))
    print(img.width*img.height)



main()
