from tkinter import*

import math
#create window for calculator
root=Tk()
root.title("Simple Calculator")
#logo 
root.wm_iconbitmap("calc.ico")
photo=PhotoImage(r"logo2.png")
logo2=Label(root,image=photo)

#create function for operating button 
def buttonClick(number):
    global operator
    operator+=str(number)
    text_Input.set(operator) 
  
#create function getting result
def buttonEqual():
    global operator
    res=str(eval(operator))
    text_Input.set(res) 
    operator=" "

#create function getting clear
def buttonClear():
    global operator
    operator=" "
    text_Input.set(" ") 

#create function getting Square Root
def buttonRoot():
    global operator
    res=math.sqrt(float(operator))
    text_Input.set(res) 
    operator=" "
   
operator=" "
text_Input=StringVar()
text_Display=Entry(root,font=("arial,bold",20),textvariable=text_Input,bg="gray",
fg="black",justify="right",bd=20).grid(columnspan=4)

# >>----------------------------------Button Option---------------------------------------------------------------<<

#Button for Row 1
btn_Clear=Button(root,text="C",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=buttonClear).grid(row=1,column=3)
btn_sqroot=Button(root,text=chr (8730),font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=buttonRoot).grid(row=1,column=2)


# Button for Row 2
btn_7=Button(root,text="7",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(7)).grid(row=2,column=0)
btn_8=Button(root,text="8",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(8)).grid(row=2,column=1)
btn_9=Button(root,text="9",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(9)).grid(row=2,column=2)
btn__divition=Button(root,text="/",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick("/")).grid(row=2,column=3)

# Button for Row 3
btn_4=Button(root,text="4",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(4)).grid(row=3,column=0)
btn_5=Button(root,text="5",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(5)).grid(row=3,column=1)
btn_6=Button(root,text="6",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(6)).grid(row=3,column=2)
btn__multiplication=Button(root,text="*",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick("*")).grid(row=3,column=3)

# Button for Row 4
btn_1=Button(root,text="1",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(1)).grid(row=4,column=0)
btn_2=Button(root,text="2",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(2)).grid(row=4,column=1)
btn_3=Button(root,text="3",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(3)).grid(row=4,column=2)
btn_adition=Button(root,text="+",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick("+")).grid(row=4,column=3)

# Button for Row  5
btn_zero=Button(root,text="0",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(0)).grid(row=5,column=0)
btn_dot=Button(root,text=".",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick(".")).grid(row=5,column=1)
btn_equal=Button(root,text="=",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=buttonEqual).grid(row=5,column=2)
btn_subtraction=Button(root,text="-",font=("arial normal",15),bg="white",
fg="black",bd=8,padx=16,pady=16,command=lambda:buttonClick("-")).grid(row=5,column=3)

root.mainloop()

