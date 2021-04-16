
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql as sq

def Login_to_Home():
    nextsc.destroy()
    main_page()


def Home_to_Login(user):
    mainsc.destroy()
    Login_Screen(user)
    
def Home_to_Home():
    mainsc.destroy()
    main_page()

def state(user):
    
    mydb = sq.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="project")

    mycursor = mydb.cursor()

    

    mycursor.execute("select * from accountmembers")

    data=mycursor.fetchall()
    for i in data:
        if i[0]==user:
            print(i)
            STATEME=messagebox.showinfo('Balance','YOU HAVE RS %s '%i[2])

def width(user,amount):
    
    
    mydb = sq.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="project")

    mycursor = mydb.cursor()

    

    mycursor.execute("select * from accountmembers")
    

    data=mycursor.fetchall()
    for i in data:
        if i[0]==user:
            if amount>i[2]:
                messagebox.showerror('Error..!','Insufficient Funds..')
            else:
                mycursor.execute("UPDATE accountmembers set amount={} where Name='{}'".format(i[2]-amount,i[0]))
                mydb.commit()
                mycursor.execute("select * from accountmembers")
                data=mycursor.fetchall()
                for j in data:
                    if j[0]==user:
                        statement=messagebox.showinfo('Balance','Balance amount is'+str(j[2]))


def wid(user):
    global nextsc
    amountdraw=Entry(nextsc,text="Enter the amount",font=("arial",25))
    amountdraw.place(x=500,y=300)
    
    amountbutton=Button(nextsc,text="Widthdraw money",command=lambda:width(user,int(amountdraw.get().strip())))
    amountbutton.place(x=500,y=350)

def Change_Pin(user,new_pin):
    
    mydb = sq.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="project")

    mycursor = mydb.cursor()

    

    mycursor.execute("select * from accountmembers")
    

    data=mycursor.fetchall()
    for i in data:
        if i[0]==user:
            mycursor.execute("update accountmembers set pin={} where name='{}'".format(new_pin,user))
            mydb.commit()
            messagebox.showinfo('Pin','your pin is changed succeesfully')
    





def change(user):
    
    new_pin=Entry(nextsc,font=("arial",25))
    new_pin.place(x=500,y=400)
    
    Submit=Button(nextsc,text='Submit',command=lambda:Change_Pin(user,int(new_pin.get().strip())))
    Submit.place(x=500,y=440)


def taker(user,amount):
    
    
    mydb = sq.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="project")

    mycursor = mydb.cursor()

    

    mycursor.execute("select * from accountmembers")
    

    data=mycursor.fetchall()
    for i in data:
        if i[0]==user:
            if amount>i[2]:
                messagebox.showerror('Error..!','Insufficient Funds..')
            else:
                mycursor.execute("UPDATE accountmembers set amount={} where Name='{}'".format(i[2]-amount,i[0]))
                mydb.commit()
                mycursor.execute("select * from accountmembers")
                data=mycursor.fetchall()
                for j in data:
                    if j[0]==user:
                        statement=messagebox.showinfo('Balance','Balance amount is'+str(j[2]))

def reciever(user,Amount,Name):
    
    
    mydb = sq.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="project")

    mycursor = mydb.cursor()

    mycursor.execute("select * from accountmembers")
    

    data=mycursor.fetchall()
    for i in data:
        if user==i[0]:
            
            mycursor.execute("update accountmembers set amount={} where Name='{}'".format(i[2]-Amount,i[0]))
            mydb.commit()

    mycursor.execute("select * from accountmembers")
    

    data=mycursor.fetchall()
    for i in data:
        if Name==i[0]:
            
            mycursor.execute("update accountmembers set amount={} where Name='{}'".format(i[2]+Amount,i[0]))
            mydb.commit()
            messagebox.showinfo('Info','Successfully Transferred')
   
                        

def send(user):
    global nextsc
    global amountgives
    amountgives=Entry(nextsc,text="Enter the value",font=("arial",20))
    amountgives.place(x=500,y=550)
    
    recieve=Entry(nextsc,text="Enter",font=("arial",20))
    recieve.place(x=850,y=550)
    
    amountbutton=Button(nextsc,text="Transfer To:",command=lambda:reciever(user,int(amountgives.get().strip()),recieve.get().strip()))
    amountbutton.place(x=500,y=610)
            


def create(user,amount):
    
    
    mydb = sq.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="project")

    mycursor = mydb.cursor()

    

    mycursor.execute("select * from accountmembers")
    

    data=mycursor.fetchall()
    for i in data:
        if i[0]==user:
            if amount>i[2]:
                messagebox.showerror('Error..!','Insufficient Funds..')
            else:
                mycursor.execute("UPDATE accountmembers set amount={} where Name='{}'".format(i[2]+amount,i[0]))
                mydb.commit()
                mycursor.execute("select * from accountmembers")
                data=mycursor.fetchall()
                for j in data:
                    if j[0]==user:
                        statement=messagebox.showinfo('Balance','Balance amount is'+str(j[2]))


def created(user):
    global nextsc
    amountdraw=Entry(nextsc,text="Money",font=("arial",25))
    amountdraw.place(x=500,y=490)
    
    amountbutton=Button(nextsc,text="Credit money",command=lambda:create(user,int(amountdraw.get().strip())))
    amountbutton.place(x=500,y=530) 
    

       
def Login_Screen(user):
    global nextsc
    nextsc=Tk()
    nextsc.geometry("1500x1000")
    
    logo2=Image.open(r"C:\Users\acer\Desktop\project python\logo.jpg")
    resized=logo2.resize((175,270))
    
    mainbackground10=ImageTk.PhotoImage(resized)
    mylabel1=Label(nextsc,image=mainbackground10,bd=0,width=100,height=230)
    mylabel1.place(x=900,y=40)
    
    background1=Image.open(r"C:\Users\acer\Desktop\project python\exa.jpg")
    resized1=background1.resize((2000,1000))
    
    
    button_img=ImageTk.PhotoImage(Image.open(r"C:\Users\acer\Desktop\project python\bal.jpg").resize((230,50),Image.ANTIALIAS))
    
    
    mainbackground1=ImageTk.PhotoImage(resized1)
    my_label1=Label(nextsc,image=mainbackground1)
    my_label1.place(x=0,y=0)    

    
    background=Image.open(r"C:\Users\acer\Desktop\project python\ss.jpg").resize((1000,500),Image.ANTIALIAS)
    resized=background.resize((1200,100))
    
    mainbackground=ImageTk.PhotoImage(resized)
    my_label=Label(nextsc,image=mainbackground)
    my_label.place(x=50,y=70)
    

        
    statement=Button(nextsc,image= button_img,bd=0,command=lambda:state(user))
    statement.place(x=225,y=220)
    
    withdraw_img=ImageTk.PhotoImage(Image.open(r"C:\Users\acer\Desktop\project python\withdraw.jpg").resize((230,50),Image.ANTIALIAS))
    
    widthdraw=Button(nextsc,image=withdraw_img,bd=0,font=("arial",25),command=lambda:wid(user))
    widthdraw.place(x=225,y=300)
    
    changepin_img=ImageTk.PhotoImage(Image.open(r"C:\Users\acer\Desktop\project python\pin change.jpg").resize((230,50),Image.ANTIALIAS))
    
    changepin=Button(nextsc,image=changepin_img,bd=0,font=("arial",25),command=lambda:change(user))
    changepin.place(x=225,y=390)
    
    deposit_img=ImageTk.PhotoImage(Image.open(r"C:\Users\acer\Desktop\project python\deposit.jpg").resize((230,50),Image.ANTIALIAS))
    
    deposit=Button(nextsc,image=deposit_img,bd=0,font=("arial",25),command=lambda:created(user))
    deposit.place(x=225,y=470)
    
   
    
    transfer_img=ImageTk.PhotoImage(Image.open(r"C:\Users\acer\Desktop\project python\transfar.jpg").resize((230,50),Image.ANTIALIAS)) 
    transfer=Button(nextsc,image=transfer_img,bd=0,font=("arial",25),command=lambda:send(user))
    transfer.place(x=225,y=550)
    
    home_img=ImageTk.PhotoImage(Image.open(r"C:\Users\acer\Desktop\project python\home.jpg").resize((230,50),Image.ANTIALIAS)) 
    home=Button(nextsc,image=home_img,bd=0,font=("arial",25),command=Login_to_Home)
    home.place(x=225,y=610)
    
     
    nextsc.mainloop()
    
def us():
    mainsc.destroy()
    about_us()

    
def Home_to_Home():
    mainsc.destroy()
    main_page()

               
def about_us():
    global new
    new=Tk()
    new.configure(bg="black")
    new.geometry("1500x1000")

    
    
    background5=Image.open(r"C:\Users\acer\Desktop\project python\logo.jpg")
    resized=background5.resize((175,270))
    
    mainbackground10=ImageTk.PhotoImage(resized)
    my_label1=Label(new,image=mainbackground10,bd=0,width=100,height=230)
    my_label1.place(x=1250,y=10)
    
    
    ch=Image.open(r"C:\Users\acer\Desktop\project python\image3.png")
    resized=ch.resize((200,400))
    
    ch1=ImageTk.PhotoImage(resized)
    my_label1=Label(new,image=ch1,bd=0,width=100,height=170)
    my_label1.place(x=40,y=20)
    
    background1=Image.open(r"C:\Users\acer\Desktop\project python\samba.jpg")
    resized=background1.resize((200,250))
    
    mainbackground=ImageTk.PhotoImage(resized)
    my_label=Label(new,image=mainbackground)
    my_label.place(x=900,y=220)
    
    a=Label(new,text="P.SAMBA",font=("arial",25),bg="white",fg="Blue")
    a.place(x=900,y=510)
    
    a1=Label(new,text="CLASS XII",font=("arial",25),bg="white",fg="Blue")
    a1.place(x=900,y=570)
    
    background2=Image.open(r"C:\Users\acer\Desktop\project python\salman.jpg")
    resized=background2.resize((200,250))
    
    mainbackground1=ImageTk.PhotoImage(resized)
    my_label1=Label(new,image=mainbackground1)
    my_label1.place(x=300,y=220)
    
    
    b=Label(new,text="SK.SALMAN",font=("arial",25),bg="white",fg="Blue")
    b.place(x=300,y=510)
    
    B1=Label(new,text="CLASS XII",font=("arial",25),bg="white",fg="Blue")
    B1.place(x=300,y=570)
    
    
    background3=Image.open(r"C:\Users\acer\Desktop\project python\rajug.jpg")
    resized=background3.resize((200,250))
    
    mainbackground3=ImageTk.PhotoImage(resized)
    my_label2=Label(new,image=mainbackground3)
    my_label2.place(x=600,y=220)
    
    c=Label(new,text="G.RAJU KUMAR",font=("arial",25),bg="white",fg="Blue")
    c.place(x=600,y=510)
    
    C1=Label(new,text="CLASS XII",font=("arial",25),bg="white",fg="Blue")
    C1.place(x=600,y=570)
    
    h1=Label(new,text="GVK CHINMAYA VIDYALAYA",font=("ARIAL",45,"bold"),bg="black",fg="orange")
    h1.place(x=290,y=20)
    
    h2=Label(new,text="SENIOR SECONDARY SCHOOL",font=("ARIAL",35),bg="black",fg="orange")
    h2.place(x=330,y=90)
    
    h3=Label(new,text="Affiliated to CBSE, Affl No:130434 ",font=("ARIAL",35),bg="black",fg="orange")
    h3.place(x=330,y=150)
    
    new.mainloop()
    

def entrybutton():
    mydb = sq.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="project")

    mycursor = mydb.cursor()

    

    mycursor.execute("select * from accountmembers")
    

    data=mycursor.fetchall()
    for i in data:
        print(i)
        if i[0]==entry1.get().strip() and i[1]==int(entry2.get().strip()):
            c=messagebox.showinfo('Account','Login Successful!')
            if c=='ok':
                Home_to_Login(i[0])
    
def main_page():
    global mainsc
    mainsc=Tk()
    
    mainsc.geometry("1500x1000")
    
    
    background=Image.open(r"C:\Users\acer\Desktop\project python\wall2.jpg")
    resized=background.resize((2000,1000))
    
    mainbackground=ImageTk.PhotoImage(resized)
    my_label=Label(mainsc,image=mainbackground)
    my_label.place(x=0,y=0)
    
    mainheading=Label(mainsc,text="WELCOME TO ATM",font=("Arial",75),bg="black",fg="orange")
    
    mainheading.place(x=220,y=250)
    
    
    background2=Image.open(r"C:\Users\acer\Desktop\project python\logo.jpg")
    resized=background2.resize((175,270))
    
    mainbackground1=ImageTk.PhotoImage(resized)
    my_label1=Label(mainsc,image=mainbackground1,bd=0,width=170,height=270)
    my_label1.place(x=20,y=10)
    
    
    nameheading=Label(mainsc,text="Enter User Name",font=("arial",25))
    
    nameheading.place(x=120,y=450)
    global entry1
    entry1=Entry(mainsc,text='welcome',font=("arial",35))

    entry1.place(x=400,y=450)
    
    pinheading=Label(mainsc,text="Enter the PIN",font=("arial",25))
    pinheading.place(x=120,y=520)
    
    
    global entry2
    entry2=Entry(mainsc,text='hlo',show='*',font=("arial",35))
    
    entry2.place(x=400,y=520)
    
    login_img=ImageTk.PhotoImage(Image.open(r"C:\Users\acer\Desktop\project python\login3.jpg").resize((230,100),Image.ANTIALIAS))
    
    button1=Button(mainsc,image=login_img,bd=0,command=entrybutton,width=210,height=80)
    
    button1.place(x=425,y=580)
    
    about=Button(mainsc,text="About US",bg="orange",fg="black",font=("arial",20),command=us)
    about.place(x=1200,y=600)
    
    h1=Label(mainsc,text="GVK CHINMAYA VIDYALAYA",font=("ARIAL",45,"bold"),bg="black",fg="orange")
    h1.place(x=290,y=20)
    
    h2=Label(mainsc,text="SENIOR SECONDARY SCHOOL",font=("ARIAL",35),bg="black",fg="orange")
    h2.place(x=330,y=90)
    
    h3=Label(mainsc,text="Affiliated to CBSE, Affl No:130434 ",font=("ARIAL",35),bg="black",fg="orange")
    h3.place(x=330,y=150)
    
    
    mainsc.mainloop()

     

        
main_page()       