class vector:
    x = 0
    y = 0
    z = 0
def createvector(v):
    v.x = int(input("enter caomponent x"))
    v.y = int(input("enter caomponent y"))
    v.z = int(input("enter caomponent z"))
    print("v = ",v.x,"x + ", v.y,"y + ", v.z,"z")
v = vector()
createvector(v)
def createvector(v):
    v.x = int(input("enter caomponent x"))
    v.y = int(input("enter caomponent y"))
    v.z = int(input("enter caomponent z"))
    print("v = ",v.x,"x + ", v.y,"y + ", v.z,"z")
v = vector()
def reversevector(v):
    v.x = int(input("enter caomponent x"))
    v.y = int(input("enter caomponent y"))
    v.z = int(input("enter caomponent z"))
    print("v = -",v.x,"vx -",v.y,"vy -",v.z,"vz")
v = vector()
reversevector(v)
def addvector(v1,v2):
    v1.x = int(input("enter caomponent x"))
    v1.y = int(input("enter caomponent y"))
    v1.z = int(input("enter caomponent z"))
    v2.x = int(input("enter caomponent x"))
    v2.y = int(input("enter caomponent y"))
    v2.z = int(input("enter caomponent z"))
    print("additionvector = v1 + v2= ",(v1.x + v2.x),"x + ",(v1.y + v2.y),"y + ",(v1.z + v2.z),"z")
v1 = vector()
v2 = vector()
addvector(v1,v2)
def dotproduct(v1,v2):
    v1.x = int(input("enter caomponent x"))
    v1.y = int(input("enter caomponent y"))
    v1.z = int(input("enter caomponent z"))
    v2.x = int(input("enter caomponent x"))
    v2.y = int(input("enter caomponent y"))
    v2.z = int(input("enter caomponent z"))
    dotproduct = (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z)
    return dotproduct
v1 = vector()
v2 = vector()
print("dotproduct of v1,v2=v1.v2= ",dotproduct(v1,v2))
def crossproduct(v1,v2):
    v1.x = int(input("enter caomponent x"))
    v1.y = int(input("enter caomponent y"))
    v1.z = int(input("enter caomponent z"))
    v2.x = int(input("enter caomponent x"))
    v2.y = int(input("enter caomponent y"))
    v2.z = int(input("enter caomponent z"))
    print("crossproduct v1 * v2",((v1.x - v2.y) + (v1.y * v1.x)),"z+", ((v1.x - v2.z) + (v1.z - v2.x)),"y +",((v1.x - v2.y) + (v1.y - v2.x)),"x")
v1 = vector()
v2 = vector()
crossproduct(v1,v2)
def magnitude(v):
    v.x = int(input("enter caomponent x"))
    v.y = int(input("enter caomponent y"))
    v.z = int(input("enter caomponent z"))
    mag = ((v.x **2) + (v.y **2) + (v.z **2)) ** (0.5)
    print("magnitude of vector= ",mag)
v = vector()
magnitude(v)



