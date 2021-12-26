from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

import movieslist
import theatrebooking
import customersignup
import qrcode
import numpy
import pickle
from functools import partial
import mysql.connector


mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='project')
k=mydb.cursor()
movs=movieslist.getmname()

def lback():
    billframe.destroy()
    paymentframe.destroy()
    print(theatrebooking.frontpage())

def backshow(s):
    seatingframe.destroy()
    if s==0 or s==4:
         print(theatrebooking.m0())
    elif s==1 or s==5:
         print(theatrebooking.m1())
    elif s==2 or s==6:
         print(theatrebooking.m2())
    elif s==3 or s==7:
         print(theatrebooking.m3())
    elif s==8 or s==9:
         print(theatrebooking.m4())
    elif s==10 or s==13:
         print(theatrebooking.m5())
    elif s==11 or s==14:
         print(theatrebooking.m6())
    elif s==12 or s==15:
         print(theatrebooking.m7())



def seatingsm01(s):
    
    global read
    f=open("seattaken.txt","rb")
    read=pickle.load(f)
    
    
    
        
    
    global lo
    lo=[] 
    global seatingframe
    seatingframe=LabelFrame(text="select your seats",bg="black",fg="white")
    seatingframe.grid(row=0,column=0,sticky="nesw")
    seatingframe.grid_columnconfigure(0,weight=1)
    seatingframe.grid_rowconfigure(0,weight=1)
    seatingframe.grid_columnconfigure(16,weight=1)
    seatingframe.grid_rowconfigure(11,weight=1)
    
    global seats
    global e
    global t
    global books
    global i
    global j
    theatrebooking.theatresframe.destroy()

    
    
    
    for i in range(10):
        for j in range(15):
            e=((i)*15)+(j)
            t=1
            if read[s][e]=="0":
                if j==5 or j==10:
                    
                    seats=Button(seatingframe,text=chr(97+i)+str(j+1),bg='green',fg='white')
                    seats.grid(row=i+1,column=j+1,padx=(50,3),pady=5)
                    seats.config(command=lambda seats=seats:changecolour(seats))
                else:    
                    seats=Button(seatingframe,text=chr(97+i)+str(j+1),bg='green',fg='white')
                    seats.grid(row=i+1,column=j+1,padx=3,pady=5)
                    seats.config(command=lambda seats=seats:changecolour(seats))
            if read[s][e]=="1":
                if j==5 or j==10:
                    seats=Button(seatingframe,text=chr(97+i)+str(j+1),bg='grey',state=DISABLED,fg='white')
                    seats.grid(row=i+1,column=j+1,padx=(50,3),pady=5)
                    
                else:    
                    seats=Button(seatingframe,text=chr(97+i)+str(j+1),bg='grey',state=DISABLED,fg='white')
                    seats.grid(row=i+1,column=j+1,padx=3,pady=5)
            
            
    
    f.close()                
    screen=Button(seatingframe,text="SCREEN")
    screen.grid(ipadx=200,row=0,column=0,columnspan=100,sticky=N)        
            
    back_buttonshow=Button(seatingframe,text="<",command=lambda:backshow(s))

    back_buttonshow.grid(row=10,column=0)

    books=Button(seatingframe,text="Book the selected seats",command=lambda:showbill(s),state=DISABLED)
    books.grid(row=15,column=4,columnspan=200)
            


        
    
def againcolour(seats):
    lo.remove(seats.cget('text'))
    print("removed",lo)
    if len(lo)==0:
        books.config(state=DISABLED)   
    seats.configure(bg="green",command=lambda e=seats:changecolour(e))
        
def changecolour(seats):
    rowcol=seats.cget('text')
    lo.append(rowcol)
    print("added",lo)   
    rowcol=seats.cget('text')
    seats.config(bg="red",command=lambda e=seats:againcolour(e))
    books.config(state=NORMAL)
    

def bookseats(s):
    print(s)
    really=messagebox.askyesno("Confirm Booking","Proceed to Pay.")
    if really==1:
        f=open("seattaken.txt","wb")
        
        for i in range(len(lo)):
            letter=lo[i][0]
            number=lo[i][1:]
            index=(((int(ord(letter))-97)*15))+((int(number)-1))
            read[s][index]="1"

        pickle.dump(read,f)
        f.close()       
        sqlb=("insert into CUSTOMERBOOKINGS(Email_ID,bookedmovie,screen_no,timings,seats_booked,tot_amt,day)values(%s,%s,%s,%s,%s,%s,%s)")
        datadumpb=[(fnv[0],movs[s][1],movs[s][2],movs[s][3],ss,str(200*len(lo)),str(movs[s][6]))]
        k.executemany(sqlb,datadumpb)
        mydb.commit()

        billframe.destroy()
        paymentframe.destroy()

        print(theatrebooking.frontpage())
        
def showbill(s):
    
    global paymentframe
    global billframe
    global rowscols
    global ss
    global fnv
    global x
    global visa
    global master
    global paypal
    global visaimg
    global mastercardimg
    global paypalimg
    global qrcodeimg
    global qrcodelabel

    ss=""
    show=""
    ssdict={'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[]}
    for i in lo:
        letter=i[0]
        number=i[1:]
        ssdict[letter].append(number)
        ss=ss+i+" "

    for i in ssdict:
        if len(ssdict[i])!=0:
            show=show+i+"-"           
            for j in range(len(ssdict[i])):              
                show=show+str(ssdict[i][j])+" "

        
    fnv=customersignup.findc()
        
        
    seatingframe.destroy()
        
    billframe=LabelFrame(text="BILL",bg="black",fg="white",relief=GROOVE)
    billframe.grid(row=0,column=0,sticky="nesw")
    billframe.columnconfigure(0,weight=10)
    billframe.rowconfigure(0,weight=10)
    billframe.propagate(FALSE)
    
         
    bille=Label(billframe,text="Email ID:"+fnv[0],font="calibri 10")
    bille.grid(row=4,column=4)
    
    billm=Label(billframe,text="MOVIE:"+movs[s][1]+" "+movs[s][5],font="calibri 10")
    billm.grid(row=5,column=4)
    
    billsc=Label(billframe,text="Screen No:"+movs[s][2],font="calibri 10")
    billsc.grid(row=6,column=4)
    
    billt=Label(billframe,text="Timings:"+movs[s][3]+",Day: "+str(movs[s][6]),font="calibri 10")
    billt.grid(row=7,column=4)
    
    bills=Label(billframe,text="Seats booked:"+ show,font="calibri 10")
    bills.grid(row=8,column=4)
    
    billam=Label(billframe,text="Total Amount(GST included): Rs "+str(200*len(lo)),font="calibri 15",height=3)
    billam.grid(row=9,column=4)
    
    qrdata=[fnv[0]+" " +movs[s][1]+" "+movs[s][5] +" " +movs[s][2] +" " +movs[s][3]+" "+" "+str(200*len(lo))]
    qr=qrcode.QRCode(version=1)
    qr.add_data(qrdata[0])
    qr.make(fit=True)
    img=qr.make_image(fill="black")
    img.save("images/qrcodeimg.png")
    qrcodeimg=ImageTk.PhotoImage(Image.open("images/qrcodeimg.png"))
    qrcodelabel=Label(billframe,image=qrcodeimg)
    qrcodelabel.grid(row=4,column=5,padx=7,pady=5,rowspan=6)
    
    paymentframe=LabelFrame(text="PAYMENT GATEWAY",bg="black",fg="white",height=10)
    paymentframe.grid(row=1,column=0,sticky="nesw")

    cardtype=Label(paymentframe,text="Type of Card",width=20)
    cardtype.grid(row=0,column=0,padx=5,pady=5)

    visaimg=ImageTk.PhotoImage(Image.open("images/visa.png"))
    mastercardimg=ImageTk.PhotoImage(Image.open("images/mastercard.png"))
    paypalimg=ImageTk.PhotoImage(Image.open("images/paypal.png"))
    
    d=IntVar()
    visa=Radiobutton(paymentframe,image=visaimg,variable=d,value="visa")
    visa.grid(row=0,column=1,padx=5,pady=5)
    master=Radiobutton(paymentframe,image=mastercardimg,variable=d,value="mastercard")
    master.grid(row=0,column=2,padx=5,pady=5)
    paypal=Radiobutton(paymentframe,image=paypalimg,variable=d,value="paypal")
    paypal.grid(row=0,column=3,padx=20,pady=5)
    list_pay=[visa,master,paypal]

    cardno=Label(paymentframe,text="Card Number",width=20)
    cardno.grid(row=1,column=0,padx=5,pady=5)
    cardentry=Entry(paymentframe,width=25)
    cardentry.grid(row=1,column=1,padx=5,pady=5)
    cardexpire=Label(paymentframe,text="expiry date(MM/YYYY)",width=20)
    cardexpire.grid(row=2,column=0,pady=5,padx=5)
    click=StringVar(paymentframe)
    click1=StringVar(paymentframe)
    dropmonth=OptionMenu(paymentframe,click,"01","02","03","04","05","06","07","08","09","10","11","12")
    dropmonth.grid(row=2,column=1,pady=5,padx=5)
    dropyear=OptionMenu(paymentframe,click1,"2020","2021","2022","2023","2024","2025","2026")
    dropyear.grid(row=2,column=2,pady=5,padx=5)
    card=Label(paymentframe,text="CVV2",width=20)
    card.grid(row=3,column=0,pady=5,padx=5)
    cvv2entry=Entry(paymentframe)
    cvv2entry.grid(row=3,column=1,pady=5,padx=5)
    
    chooseag=Button(paymentframe,text="CANCEL",bg="red",fg="white",command=lambda:backtoseats(s),height=1,relief=SUNKEN)
    chooseag.grid(row=4,column=0,padx=5,pady=10,columnspan=3)    
    
    confirm=Button(paymentframe,text="CONFIRM BOOKING",bg="blue",fg="white",command=lambda:bookseats(s),height=1,relief=SUNKEN)
    confirm.grid(row=4,column=3,padx=5,pady=10,columnspan=3)
    
          
def backtoseats(s):
    billframe.destroy()
    paymentframe.destroy()
    print(seatingsm01(s))


        
        

    
        
    
        
    
    

            
    
            
            
            
            
        
            
            
            
                   

        
    
    
            
        
        
        
    
    



