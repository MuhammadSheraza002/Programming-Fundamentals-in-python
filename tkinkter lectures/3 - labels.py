"""
                        LABELS
        text = adds text
        fg = foreground
        font = set font like font("calibary","red","")
        padx = padx gives length of box
        pady = pady gives height of box
        relief = border style like SUNKEN,RAISED,GROOVE,RIDGE
        bd	=   border size of the text box. Default is 2 pixels.
        show	 set show = "*" to convert text box into a password field.

"""
import tkinter as tkt

page =  tkt.Tk()
# page.title('first tkinkter') create title of tkinkter

page.title('first tkinkter')

#geometry('widthxheight') gives area

page.geometry('100x200')

tkt.Label(text='Red' ,bg='red' ,fg = 'white').pack(fill=tkt.X) #tkt.Label(page,text='name').grid(row=0) can also use
tkt.Label(text='Blue' ,bg='blue', fg = 'white').pack(side='right',fill=tkt.Y) #tkt.Label(page,text='name').grid(row=0) can also use
tkt.Label(text='green', bg='green', fg = 'white').pack() #tkt.Label(page,text='name').grid(row=0) can also use

'''
tkt.Label(text='Red' ,bg='red' ,fg = 'white').pack()
tkt.Label(text='Blue' ,bg='blue', fg = 'white').pack()
tkt.Label(text='green', bg='green', fg = 'white').pack()
'''

page.mainloop()
