#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("650x250")

#Define a function to clear the Entry Widget Content
def clear_text():
   text.delete(0, END)

#Create a entry widget
text= Entry(win, width=40)
text.pack()

#Create a button to clear the Entry Widget
Button(win,text="Clear", command=clear_text, font=('Helvetica bold',10)).pack(pady=5)

win.mainloop()