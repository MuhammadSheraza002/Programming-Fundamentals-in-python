from tkinter import *
top = Tk()
L1 = Label(top, text = "price")
L1.place(x = 10,y = 10)
E1 = Entry(top, bd = 3)
E1.place(x = 60,y = 10)
L2 = Label(top,text = "quantity")
L2.place(x = 10,y = 50)
E2 = Entry(top,bd = 3)
E2.place(x = 60,y = 50)
L3 = Label(top,text = "Amount")
L3.place(x = 10,y = 150)
E3 = Entry(top,bd = 3)
E3.place(x = 60,y = 150)
B = Button(top, text = "Calculate")
B.place(x = 100, y = 100)
top.geometry("250x200+10+10")
top.mainloop()