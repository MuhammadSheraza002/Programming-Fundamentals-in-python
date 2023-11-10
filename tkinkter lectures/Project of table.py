import tkinter as tkt
def multiply():
    print('sdfgh')

page =  tkt.Tk()

page.title('Multiply Table')
page.geometry('400x300')
tkt.Label(text='write number ').pack()
number = tkt.Entry(page)
number.grid(row=2,column=5)

tkt.Button(text='click',command=multiply)
page.mainloop()