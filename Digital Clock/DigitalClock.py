#Digital Clock 

from tkinter import *
from tkinter.ttk import*
#import time
from time import strftime
#To create window 
clock=Tk()
#set windows frame
clock.geometry("400x150")
#give a title
clock.title("Digital Clock")

#clock icon
clock.wm_iconbitmap("favico.ico")
photo=PhotoImage(r"logo.png")
logo=Label(clock,image=photo)

#call a function
def time():
    watchTime=strftime("%I:%M:%S %p")
    lbl.config(text=watchTime)
    lbl.after(1000,time)

lbl=Label(clock,font=("Arial Bold",35),background="black",foreground="aqua")
lbl.pack(side=TOP)

time()

clock.mainloop()
