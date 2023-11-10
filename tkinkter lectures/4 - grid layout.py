'''import tkinter as tkt

page =  tkt.Tk()

page.title('first tkinkter')

page.geometry('100x200')

#sticky=E ALIGNS IT INTO DIRECTIION(e.g,E,N,W,S means EAST,NORTH,WEST,SOUTH RESPECTIVELY)

name = tkt.Label(page,text='name').grid(row=0,sticky=tkt.E) #tkt.Label(page,text='name').grid(row=0) can also use
password = tkt.Label(text='password').grid(row=1,sticky=tkt.E) #tkt.Label(page,text='name').grid(row=0) can also use
email = tkt.Label(text='email' ).grid(row=2,sticky=tkt.E) #tkt.Label(page,text='name').grid(row=0) can also use
tkt.Entry(page).grid(row=0,column=2) #Entry(page) can also use

tkt.Entry(bd=10).grid(row=1,column=2,padx=30) #Entry(page) can also use
tkt.Entry().grid(row=2,column=2) #Entry(page) can also use

"""
name = tkt.Label(page,text='name').grid(row=0) #tkt.Label(page,text='name').grid(row=0) can also use
password = tkt.Label(text='password').grid(row=1) #tkt.Label(page,text='name').grid(row=0) can also use
email = tkt.Label(text='email' ).grid(row=2) #tkt.Label(page,text='name').grid(row=0) can also use
tkt.Entry(page).grid(row=0,column=2) #Entry(page) can also use
tkt.Entry().grid(row=1,column=2) #Entry(page) can also use
tkt.Entry().grid(row=2,column=2) #Entry(page) can also use

"""
page.mainloop()
'''

import tkinter as tk

screen = tk.Tk()
l1 = tk.Label(screen,text ='PRICE' )
l2 = tk.Label(screen,text ='QUANTITY' )
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
tk.Entry(screen).grid(row=0,column=1)
tk.Entry(screen).grid(row=1,column=1)
tk.mainloop()