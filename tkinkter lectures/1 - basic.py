'''from tkinter import *
# create root window
root = Tk()
# frame inside root window
frame = Frame(root)
# geometry method
frame.pack()
# button inside frame which is
# inside root
button = Button(frame, text ='Geek')
button.pack()

# Tkinter event loop
root.mainloop()		'''

# Import Module
from tkinter import *
# create root window
root = Tk()
# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('350x200')
# adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()
# function to display text when
# button is clicked

def clicked():
	lbl.configure(text="I just got clicked")

# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)
# Execute Tkinter
root.mainloop()
