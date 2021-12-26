from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

import movieslist
import theatrebooking
import seating
import random
import math
import mysql.connector

import smtplib

global mydb

mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='project')
log=mydb.cursor()
"""
log.execute("create table CUSTOMERS(First_Name varchar(50),Last_Name varchar(50),phone_no char(10),Email_ID varchar(100),Password varchar(40))")
"""



    


global cdata
cdata=[]
def backfront2():
    loginframe.destroy()
    print(front())
def backfront1():
    signupframe.destroy()
    print(front())


global root
root=Tk()
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)
root.geometry("750x650" ) 

root.resizable(False,False)

v=0


def findc():
    return cdata
   
    

def front():
    
    global frontframe
    global logoimg
    global logolabel
    frontframe=LabelFrame(root,text="WELCOME",bg="black",fg="white")
    frontframe.grid(row=0,column=0,sticky="nesw")
    
    frontframe.grid_columnconfigure(0,weight=1)
    frontframe.grid_rowconfigure(0,weight=1)
    logoimg=ImageTk.PhotoImage(Image.open("images/logo.jpeg"))
    


    
    
    logolabel=Label(frontframe,image=logoimg,bg="black")
    logolabel.place(x=0, y=0, relwidth=1, relheight=1)
    
    signbutton=Button(frontframe,text="SIGN UP",bg="black",fg="white",width=18,relief=SUNKEN,command=lambda:signup(1))
    signbutton.grid(row=0,column=1,sticky="e")

    alog=Button(frontframe,text="Alredy have an account?",bg="black",fg="white",relief=SUNKEN,command=lambda:login(2))
    alog.grid(row=0,column=0,sticky="w")

def resendotp():
    otpentry.destroy()
    otplabel.destroy()
    subbutton.destroy()
    try:
        otpbutton.config(text="Resend OTP",state=NORMAL)
    except:
        return
    
    
    
    
def sendotp():
    global otpentry
    global otp
    global emailgo
    global email
    global otp
    global otpuser
    global emailgo
    global emailentry
    global otpbutton
    global otplabel
    global subbutton
   
    emailgo=emailentry.get()
    var=("select Email_id from CUSTOMERS where Email_id=%s")
    
    log.execute(var,(emailgo,))
    finde=log.fetchall()
    print(finde)
    
    if len(finde)==0:
        messagebox.showerror("Oops!","No Email such as this have signed up here.")
    else:
        root.after(120000,resendotp)
        otpbutton.config(state=DISABLED)
        otplabel=Label(loginframe,text="Enter your OTP",padx=10,pady=10)
        otplabel.grid(row=9,column=2)
        otpentry=Entry(loginframe,font="courier 12")
        otpentry.grid(row=9,column=3)
        
        subbutton=Button(loginframe,text="SUBMIT",command=verify,padx=10,pady=10)
        subbutton.grid(row=10,column=3)
        
    
        otp=""
        stringrange="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        for i in range(6):
            otp=otp+stringrange[math.floor(random.random()*36)]
            fileotp=open("otpget.txt",'w')
            fileotp.write(otp)
        fileotp.close()

        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("xxxx@gmail.com","yyyyy")  
        server.sendmail("xxxx@gmail.com",emailgo,"BOOKING SIMULATION\nThe Verification code to change your password is "+otp+"\nNOTE:\nThis is Valid only for two minutes from when you clicked 'Send OTP'")
        server.quit()
def otpgen():
    global otpentry
    global otp
    global emailgo
    global email
    global otp
    global otpuser
    global emailgo
    global emailentry
    global otpbutton
    global otpbutton
    global otplabel
    global subbutton
    
    forgotp.config(state=DISABLED)
    email=Label(loginframe,text="Enter the EMAIL ID ",padx=10,pady=10)
    email.grid(row=8,column=2)
    emailentry=Entry(loginframe,font="courier 12")
    emailentry.grid(row=8,column=3)
    
    otpbutton=Button(loginframe,text="Send OTP",command=sendotp,padx=10,pady=10)
    otpbutton.grid(row=8,column=4)

    
    
    



    
def verify():
    otpuser=otpentry.get()
    global newpentry
    global confpentry
    global confirm
    global confp
    global newp
    
    if otp==otpuser:
        email.destroy()
        emailentry.destroy()
        otpbutton.destroy()
        
        otplabel.destroy()
        otpentry.destroy()
        subbutton.destroy()
        newp=Button(loginframe,text="Enter new Password",padx=10,pady=10)
        newp.grid(row=11,column=2)
        newpentry=Entry(loginframe,font="courier 12",show="*")
        newpentry.grid(row=11,column=3)
        confp=Label(loginframe,text="Confirm Password",padx=10,pady=10)
        confp.grid(row=12,column=2)
        confpentry=Entry(loginframe,font="courier 12",show="*")
        confpentry.grid(row=12,column=3)
        confirm=Button(loginframe,text="Change password",command=change,padx=10,pady=10)
        confirm.grid(row=12,column=4)
    else:
        messagebox.showerror("Not what we sent you","OTP is wrong,try again")
        
def change():
    if len(newpentry.get())<8:
        messagebox.showerror("Alert!","Password should be atleast 8 characters")
    elif newpentry.get()!=confpentry.get():
        messagebox.showerror("Oops!","Password is Wrong at second attempt")
    
    else :
        info="update customers set password=%s where email_id=%s"
        infovar=(newpentry.get(),emailgo)
        log.execute(info,infovar)
        mydb.commit()
        confp.destroy()
        newp.destroy()
        confpentry.destroy()
        newpentry.destroy()
        confirm.destroy()
        messagebox.showinfo("successfully changed","your password is Brand New")
        forgotp.config(state=NORMAL)
    
            
            
        
    
        
    

    






def signup(b):
    


    frontframe.destroy()
    
    global firstnamew
    global lastnamew
    global passwordw
    global emailw
    global phnow
    global signupframe
    
    
   
    

    signupframe=LabelFrame(text="CREATE AN ACCOUNT",bg="grey",fg="black")
    signupframe.grid(row=0,column=0,sticky="nesw")

    backtof1=Button(signupframe,text="<<",command=backfront1)
    backtof1.grid(row=2,column=1)

    

    firstname=Label(signupframe,text="Enter your Firstname:",fg="white",bg="dark blue")
    firstname.grid(row=2,column=2,padx=10,pady=10)

    lastname=Label(signupframe,text="Enter your Lastname:",fg="white",bg="dark blue")
    lastname.grid(row=3,column=2,padx=10,pady=10)

    phno=Label(signupframe,text="Enter your Phone No.: +91-",fg="white",bg="dark blue")
    phno.grid(row=4,column=2,padx=10,pady=10)

    email=Label(signupframe,text="Enter your Email ID:",fg="white",bg="dark blue")
    email.grid(row=5,column=2,padx=10,pady=10)

    password=Label(signupframe,text="Enter your Password:",fg="white",bg="dark blue")
    password.grid(row=6,column=2,padx=10,pady=10)

    acc=Button(signupframe,text="Sign in",command=signin)
    acc.grid(row=7,column=3,padx=10,pady=10)


    firstnamew=Entry(signupframe,font="courier 12")
    firstnamew.grid(row=2,column=3,padx=10,pady=10)

    lastnamew=Entry(signupframe,font="courier 12")
    lastnamew.grid(row=3,column=3,padx=10,pady=10)

    phnow=Entry(signupframe,font="courier 12")
    phnow.grid(row=4,column=3,padx=10,pady=10)

    emailw=Entry(signupframe,font="courier 12")
    emailw.grid(row=5,column=3,padx=10,pady=10)

    passwordw=Entry(signupframe,font="courier 12",show="*")
    passwordw.grid(row=6,column=3,padx=10,pady=10)


def signin():
    v=1
    global cdata
    
    cdata=[]
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='project')
    log=mydb.cursor()
    firstnameg=str(firstnamew.get())
    lastnameg=str(lastnamew.get())
    phnog=str(phnow.get())
    emailg=str(emailw.get())
    passwordg=str(passwordw.get())
    
    customerdata=(str(firstnamew.get()),str(lastnamew.get()),str(phnow.get()),str(emailw.get()),str(passwordw.get()))
    
    for i in range(5):
        print(customerdata[i])
        if customerdata[i]=="":
            blankerror=messagebox.showerror("Message","No entry should be left blank")
            break
    if len(customerdata[4])<8:
        perror=messagebox.showerror("Message","Password should contain atleast 8 characters")
    elif len(str(customerdata[2]))!=10:
        pherror=messagebox.showerror("Message","phone number should contain 10 nummbers")
    else:
        sqls=("select Email_id from CUSTOMERS where Email_id=%s")
        
        log.execute(sqls,(emailg,))
        
       
        searchs=[]
        resultcs=log.fetchall()
        for c in resultcs:
            searchs.append(c)
        if len(searchs)!=0:
            serror=messagebox.showerror("Message","Email already exists")
    
        else:
        
                                            
            
            sql=("insert into CUSTOMERS(First_Name,Last_Name,phone_no,Email_ID,Password)values(%s,%s,%s,%s,%s)")
            datadump=[(firstnameg,lastnameg,phnog,emailg,passwordg)]
            log.executemany(sql,datadump)
            mydb.commit()
            cdata=[datadump[0][3],datadump[0][4]]
            signupframe.destroy()
            print(cdata)
     
            print(findc())
        
        
        
    
            print(theatrebooking.frontpage())
        
    

          
    

    


    


def login(b):
    
    
    frontframe.destroy()
    global passwordw
    global emailw
    global passwordwl
    global emailwl
    global loginframe
    global forgotp

    loginframe=LabelFrame(text="LOGIN PAGE",bg="grey",fg="black")
    loginframe.grid(row=0,column=0,sticky="nesw")

    backtof=Button(loginframe,text="<<",command=backfront2)
    backtof.grid(row=5,column=1)


    emaillog=Label(loginframe,text="Enter your Email ID:",fg="white",bg="dark blue")
    emaillog.grid(row=5,column=2,padx=10,pady=10)

    passwordlog=Label(loginframe,text="Enter your Password:",fg="white",bg="dark blue")
    passwordlog.grid(row=6,column=2,padx=10,pady=10)

    acclog=Button(loginframe,text="Log in",command=Log)
    acclog.grid(row=7,column=3,padx=10,pady=10)

    forgotp=Button(loginframe,text="forgotten password?",command=otpgen)
    forgotp.grid(row=7,column=2,padx=10,pady=10)

    
    emailwl=Entry(loginframe,font="courier 12")
    emailwl.grid(row=5,column=3,padx=10,pady=10)

    passwordwl=Entry(loginframe,font="courier 12",show="*")
    passwordwl.grid(row=6,column=3,padx=10,pady=10)
    
    


def Log():
    v=2
    
    global cdata
    cdata=[]
    
    emailgl=str(emailwl.get())
    passwordgl=str(passwordwl.get())


    customerdatal=(str(emailwl.get()),str(passwordwl.get()))
    
    for i in range(2):
        print(customerdatal[i])
        if customerdatal[i]=="":
            blankerror=messagebox.showerror("Message","No entry should be left blank")
            break
    if len(customerdatal[1])<8:
        perror=messagebox.showerror("Message","Password should contain atleast 8 characters")
    else:
        sqll=("select Email_id,Password from CUSTOMERS where Email_id=%s and Password=%s")
        
        log.execute(sqll,(emailgl,passwordgl))
       
        search=[]
        resultc=log.fetchall()
        for c in resultc:
            search.append(c)
        if len(search)==0:
            lerror=messagebox.showerror("Message","Wrong Email or Password")
        else:
            
            loginframe.destroy()
            cdata=[search[0][0],search[0][1]]
            print(findc())    
          
        
            
            
    
            print(theatrebooking.frontpage())
print(front())
            
            

        
        

        
            


            
    
    
    
    

    
    
    
    


    

    



    

    
                           


                           








