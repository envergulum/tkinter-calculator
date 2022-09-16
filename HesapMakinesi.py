from tkinter import *
from operating import processes

Process=processes

def clicked_button(number):
    entry1.config(state= "normal")
    entry1.insert(END,number)
    entry1.config(state= "disabled")

def addtion():
    global operation
    global number_one
    operation="addtion"
    entry1.config(state= "normal")
    number_one=int(entry1.get())
    entry1.delete(0,END)
    entry1.config(state= "disabled")

def subtraction():
    global number_one
    global operation
    operation="subtraction"
    entry1.config(state= "normal")
    number_one=int(entry1.get())
    entry1.delete(0,END)
    entry1.config(state= "disabled")

def multiplication():
    global number_one
    global operation
    operation="multiplication"
    entry1.config(state= "normal")
    number_one=int(entry1.get())
    entry1.delete(0,END)
    entry1.config(state= "disabled")

def division():
    global number_one
    global operation
    operation="division"
    entry1.config(state= "normal")
    number_one=int(entry1.get())
    entry1.delete(0,END)
    entry1.config(state= "disabled")

def equal():
    entry1.config(state= "normal")
    number_two=int(entry1.get())
    entry1.delete(0,END)
        
    if operation == "addtion":
        entry1.insert(0,Process.addtion_process(number_one,number_two))
    elif operation =="subtraction":
        entry1.insert(0,Process.subtraction_process(number_one,number_two))
    elif operation =="multiplication":
        entry1.insert(0,Process.multiplication_process(number_one,number_two))
    elif operation =="division":
        entry1.insert(0,Process.division_process(number_one,number_two))
    else:
        print("gecersiz işlem")

    entry1.config(state= "disabled")

def clear():
    entry1.config(state= "normal")
    entry1.delete(0,END)
    entry1.config(state= "disabled")



menu1 = Tk()
menu1.title("hesap makinesi")

canvas = Canvas(menu1, bg="DarkGray" ,height=600, width=418)
canvas.pack()

frame_üst = Frame(canvas,bg="white")
frame_üst.place(relx=0.025, rely=0.03, relwidth=0.95, relheight=0.1)

frame_alt = Frame(canvas,bg="grey")
frame_alt.place(relx=0.025, rely=0.14, relwidth=0.95, relheight=0.83)

entry1 = Entry(frame_üst,bd=1,font=("",35),justify=RIGHT)
entry1.config(state= "disabled")
entry1.pack()
#-------------------------



#operating------
addtion_button = Button(frame_alt, text='+',fg='black',bg='white',command=addtion,font=("",50))
addtion_button.place(x=0,y=0,width=100,height=100)

subtraction_button = Button(frame_alt, text='-',fg='black',bg='white',command=subtraction,font=("",50))
subtraction_button.place(x=100,y=0,width=100,height=100)

multiplication_button = Button(frame_alt, text='x',fg='black',bg='white',command=multiplication,font=("",50))
multiplication_button.place(x=200,y=0,width=100,height=100)

division_button = Button(frame_alt, text='/',fg='black',bg='white',command=division,font=("",50))
division_button.place(x=300,y=0,width=100,height=100)

clear_button = Button(frame_alt, text='c',fg='black',bg='white',command=clear,font=("",50))
clear_button.place(x=300,y=100,width=100,height=200)

equal_button = Button(frame_alt, text='=',fg='black',bg='white',command=equal,font=("",50))
equal_button.place(x=300,y=300,width=100,height=200)


#--------
#numbers at the top------------
number_seven_button = Button(frame_alt, text='7',fg='black',bg='white',command=lambda:clicked_button(7),font=("",50))
number_seven_button.place(x=0,y=100,width=100,height=100)

number_eight_button = Button(frame_alt, text='8',fg='black',bg='white',command=lambda:clicked_button(8),font=("",50))
number_eight_button.place(x=100,y=100,width=100,height=100)

number_nine_button = Button(frame_alt, text='9',fg='black',bg='white',command=lambda:clicked_button(9),font=("",50))
number_nine_button.place(x=200,y=100,width=100,height=100)
#-------------
#numbers in the middle------------
number_four_button = Button(frame_alt, text='4',fg='black',bg='white',command=lambda:clicked_button(4),font=("",50))
number_four_button.place(x=0,y=200,width=100,height=100)

number_five_button = Button(frame_alt, text='5',fg='black',bg='white',command=lambda:clicked_button(5),font=("",50))
number_five_button.place(x=100,y=200,width=100,height=100)

number_six_button = Button(frame_alt, text='6',fg='black',bg='white',command=lambda:clicked_button(6),font=("",50))
number_six_button.place(x=200,y=200,width=100,height=100)
#---------------
#numbers in the down
number_one_button = Button(frame_alt, text='1',fg='black',bg='white',command=lambda:clicked_button(1),font=("",50))
number_one_button.place(x=0,y=300,width=100,height=100)

number_two_button = Button(frame_alt, text='2',fg='black',bg='white',command=lambda:clicked_button(2),font=("",50))
number_two_button.place(x=100,y=300,width=100,height=100)

number_theree_button = Button(frame_alt, text='3',fg='black',bg='white',command=lambda:clicked_button(3),font=("",50))
number_theree_button.place(x=200,y=300,width=100,height=100)

number_zero_button = Button(frame_alt, text='0',fg='black',bg='white',command=lambda:clicked_button(0),font=("",50))
number_zero_button.place(x=000,y=400,width=300,height=100)
#--------



menu1.resizable(0,0)
menu1.mainloop()
