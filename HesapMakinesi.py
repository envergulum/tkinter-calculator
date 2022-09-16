from tkinter import *
from Islemler import process

Process=process

def tıklanan_button(sayi):
    entry1.config(state= "normal")
    entry1.insert(END,sayi)
    entry1.config(state= "disabled")

def toplama():
    global islem
    global sayi1
    islem="toplama"
    entry1.config(state= "normal")
    sayi1=int(entry1.get())
    entry1.delete(0,END)
    entry1.config(state= "disabled")

def çıkarma():
    global sayi1
    global islem
    islem="çıkarma"
    entry1.config(state= "normal")
    sayi1=int(entry1.get())
    entry1.delete(0,END)
    entry1.config(state= "disabled")

def çarpma():
    global sayi1
    global islem
    islem="çarpma"
    entry1.config(state= "normal")
    sayi1=int(entry1.get())
    entry1.delete(0,END)
    entry1.config(state= "disabled")

def bölme():
    global sayi1
    global islem
    islem="bölme"
    entry1.config(state= "normal")
    sayi1=int(entry1.get())
    entry1.delete(0,END)
    entry1.config(state= "disabled")

def esittir():
    entry1.config(state= "normal")
    sayi2=int(entry1.get())
    entry1.delete(0,END)
        
    if islem == "toplama":
        entry1.insert(0,Process.toplamaİslemi(sayi1,sayi2))
    elif islem =="çıkarma":
        entry1.insert(0,Process.cıkarmaİslemi(sayi1,sayi2))
    elif islem =="çarpma":
        entry1.insert(0,Process.carpmaİslemi(sayi1,sayi2))
    elif islem =="bölme":
        entry1.insert(0,Process.bölmeİslemi(sayi1,sayi2))
    else:
        print("gecersiz işlem")

    entry1.config(state= "disabled")

def temizle():
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



#işlemler------
topalama_butonu = Button(frame_alt, text='+',fg='black',bg='white',command=toplama,font=("",50))
topalama_butonu.place(x=0,y=0,width=100,height=100)

çıkarma_butonu = Button(frame_alt, text='-',fg='black',bg='white',command=çıkarma,font=("",50))
çıkarma_butonu.place(x=100,y=0,width=100,height=100)

çarpma_butonu = Button(frame_alt, text='x',fg='black',bg='white',command=çarpma,font=("",50))
çarpma_butonu.place(x=200,y=0,width=100,height=100)

bölme_butonu = Button(frame_alt, text='/',fg='black',bg='white',command=bölme,font=("",50))
bölme_butonu.place(x=300,y=0,width=100,height=100)

silme_butonu = Button(frame_alt, text='c',fg='black',bg='white',command=temizle,font=("",50))
silme_butonu.place(x=300,y=100,width=100,height=200)

sonuc_butonu = Button(frame_alt, text='=',fg='black',bg='white',command=esittir,font=("",50))
sonuc_butonu.place(x=300,y=300,width=100,height=200)


#--------
#sayilar üst------------
sayi7_butonu = Button(frame_alt, text='7',fg='black',bg='white',command=lambda:tıklanan_button(7),font=("",50))
sayi7_butonu.place(x=0,y=100,width=100,height=100)

sayi8_butonu = Button(frame_alt, text='8',fg='black',bg='white',command=lambda:tıklanan_button(8),font=("",50))
sayi8_butonu.place(x=100,y=100,width=100,height=100)

sayi9_butonu = Button(frame_alt, text='9',fg='black',bg='white',command=lambda:tıklanan_button(9),font=("",50))
sayi9_butonu.place(x=200,y=100,width=100,height=100)
#-------------
#sayilar orta------------
sayi4_butonu = Button(frame_alt, text='4',fg='black',bg='white',command=lambda:tıklanan_button(4),font=("",50))
sayi4_butonu.place(x=0,y=200,width=100,height=100)

sayi5_butonu = Button(frame_alt, text='5',fg='black',bg='white',command=lambda:tıklanan_button(5),font=("",50))
sayi5_butonu.place(x=100,y=200,width=100,height=100)

sayi6_butonu = Button(frame_alt, text='6',fg='black',bg='white',command=lambda:tıklanan_button(6),font=("",50))
sayi6_butonu.place(x=200,y=200,width=100,height=100)
#---------------
#sayilar alt
sayi1_butonu = Button(frame_alt, text='1',fg='black',bg='white',command=lambda:tıklanan_button(1),font=("",50))
sayi1_butonu.place(x=0,y=300,width=100,height=100)

sayi2_butonu = Button(frame_alt, text='2',fg='black',bg='white',command=lambda:tıklanan_button(2),font=("",50))
sayi2_butonu.place(x=100,y=300,width=100,height=100)

sayi3_butonu = Button(frame_alt, text='3',fg='black',bg='white',command=lambda:tıklanan_button(3),font=("",50))
sayi3_butonu.place(x=200,y=300,width=100,height=100)

sayi0_butonu = Button(frame_alt, text='0',fg='black',bg='white',command=lambda:tıklanan_button(0),font=("",50))
sayi0_butonu.place(x=000,y=400,width=300,height=100)
#--------



menu1.resizable(0,0)
menu1.mainloop()
