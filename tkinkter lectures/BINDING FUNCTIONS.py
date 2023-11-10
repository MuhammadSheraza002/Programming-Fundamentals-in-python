'''
There are 2 methods
(1) command = function                   without brackets
(2) bind()
'''
#                           1st method

'''import tkinter as tkt

def fun():
    print("Welcome to knowlege shelf")


page =  tkt.Tk()
# page.title('first tkinkter') create title of tkinkter

page.title('BINDING FUNCTIONS')

#geometry('widthxheight') gives area

page.geometry('400x300')

button=tkt.Button(page,text='click me',command=fun)
button.pack()

page.mainloop()'''

#                           2nd method


import tkinter as tkt

def fun(event):
    print("Welcome to knowlege shelf")


page =  tkt.Tk()

page.title('BINDING FUNCTIONS')
page.geometry('400x300')

button=tkt.Button(page,text='click me')
button.bind('Button-1',fun)
button.pack()


page.mainloop()
