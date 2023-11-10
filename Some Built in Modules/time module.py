import time
a=time.time()
print(a)
A = 45
print(A)
print(time.time()-a)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

#time.sleep(second) sleeps and then start
for i in range(4):
    print("ASSALAM O ALAIKUM SHERAZ")
    time.sleep(2)
