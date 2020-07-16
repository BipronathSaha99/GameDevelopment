# >>----------------------------Calculator---------------------------------------------<<

#import tkinter
from tkinter import *

#create main window for calculator
cal=Tk()
#calculator title
cal.title("Calculator")
#logo
cal.wm_iconbitmap("favicon.ico")
photo=PhotoImage(r"logo1.png")
logo1=Label(cal,image=photo)

# call a function to click buttons
def buttonClick(number):
    global operator
    operator+=str(number)
    text_Input.set(operator)

# button clear function
def buttonClear():
    global operator
    operator=" "
    text_Input.set(" ")

#function for equal button
def buttonEqual():
    global operator
    res=str(eval(operator))
    text_Input.set(res)
    operator=""

operator=""
text_Input=StringVar()

textDisplay=Entry(cal,font=("arial bold",20),textvariable=text_Input,bd=30,bg="gray",fg="black",insertwidth=4,
justify="right").grid(columnspan=4)

# >>----------------------------------Clear Button--------------------------------------------------------<<
btn_clr=Button(cal,text="AC",font=("arial bold",15),fg="black",bd=9,padx=10,pady=10,
command=buttonClear).grid(row=1,column=3)

# >>--------------------------------Button-------------------------------------------------------------<<
btn7=Button(cal,text="7",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(7)).grid(row=2,column=0)
btn8=Button(cal,text="8",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(8)).grid(row=2,column=1)
btn9=Button(cal,text="9",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(9)).grid(row=2,column=2)
btnDiv=Button(cal,text="/",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick("/")).grid(row=2,column=3)

# >>--------------------------------Button---------------------------------------------------------------<<
btn4=Button(cal,text="4",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(4)).grid(row=3,column=0)
btn5=Button(cal,text="5",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(5)).grid(row=3,column=1)
btn6=Button(cal,text="6",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(6)).grid(row=3,column=2)
btnMul=Button(cal,text="*",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick("*")).grid(row=3,column=3)

# >>--------------------------------Button---------------------------------------------------------------<<
btn1=Button(cal,text="1",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(1)).grid(row=4,column=0)
btn2=Button(cal,text="2",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(2)).grid(row=4,column=1)
btn3=Button(cal,text="3",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(3)).grid(row=4,column=2)
btn_Add=Button(cal,text="+",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick("+")).grid(row=4,column=3)

# >>----------------------------Button-------------------------------------------------------------------<<
btn0=Button(cal,text="0",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(0)).grid(row=5,column=0)
btn_dot=Button(cal,text=".",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick(".")).grid(row=5,column=1)
btn_equal=Button(cal,text="=",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=buttonEqual).grid(row=5,column=2)
btn_persent=Button(cal,text="-",font=("arial bold",15),fg="black",bd=9,padx=16,pady=16,
command=lambda:buttonClick("-")).grid(row=5,column=3)


cal.mainloop()
