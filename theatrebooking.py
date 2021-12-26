
from tkinter import *
from PIL import ImageTk,Image

import movieslist
import seating
import customersignup
import mysql.connector




mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='project')
k=mydb.cursor()




global x

x=(movieslist.getmname())

def gobackf():
    mybframe.destroy()
    print(frontpage())


def mybookings():
    global mybframe
    fnb=customersignup.findc()
    sqlm=("select * from customerbookings where Email_id=%s")
    mydb.commit()
    k.execute(sqlm,(str(fnb[0]),))
    dat=k.fetchall()
    bookclist=[]
    for i in dat:
        bookclist.append(i)
    print(bookclist)
    moviesframe.destroy()
    mybframe=LabelFrame(text="MY BOOKINGS",bg="black",fg="white")
    mybframe.grid(row=0,column=0,sticky="nesw")
    mybframe.grid_columnconfigure(0,weight=1)
    mybframe.grid_rowconfigure(0,weight=1)
    """mybframe.pack(fill=BOTH,expand="yes")"""
    
    myb=Text(mybframe,bg="black",fg="white",font="courier 12",bd=51,relief=SOLID)
    myb.grid(row=1,column=0)
    if len(bookclist)==0:
        goback=Button(mybframe,text="See what we got!",command=gobackf)
        goback.grid(row=0,column=0,columnspan=3,ipadx=4)
        myb.insert(INSERT,"YOU DID NOT BOOK ANY MOVIES\nHURRY UP! IT MAY AS WELL BE BOOKED QUICKLY!")
        myb.config(state=DISABLED)
    for i in range(len(bookclist)):
        goback=Button(mybframe,text="Wanna Look around for more?",command=gobackf)
        goback.grid(row=0,column=0,ipadx=10)
        myb.insert(INSERT,str(i+1)+"."+"EMAIL ID:"+bookclist[i][0]+"\n"+" "+"MOVIE:"+bookclist[i][1]+"\n"+" "+"Screen NO.:"+bookclist[i][2]+"\n"+" "+"Timings:"+bookclist[i][3]+",Day:"+str(bookclist[i][6])+"\n"+" Seats Booked:"+bookclist[i][4]+"\n"+" "+"total Amount:"+bookclist[i][5]+"\n\n")
    myb.config(state=DISABLED)


def logout():
    moviesframe.destroy()
    print(customersignup.front())



def back():
    theatresframe.destroy()
    
    return frontpage()
    

                  
def m0():
    global theatresframe
    
    moviesframe.destroy()

    

    
    
    theatresframe=LabelFrame(text="SCREENS AVAILABLE AND TIMINGS",bg="black",fg="white")
    theatresframe.grid(row=0,column=0,sticky="nesw")
    theatresframe.grid_columnconfigure(0,weight=1)
    theatresframe.grid_rowconfigure(0,weight=1)
    movie0=Button(theatresframe,text=x[0][1]+" screen no. "+str(x[0][2])+", timings:"+x[0][3]+", duration:"+x[0][4]+", "+"DAY:"+x[0][6]+","+x[0][5], command=lambda:seating.seatingsm01(s=0),font="aerial 10")
    movie0.grid(row=2,column=0,pady=5)
    back_button=Button(theatresframe,text="<<",command=back)
    back_button.grid(row=1,column=0)
    movie0x=Button(theatresframe,text= x[4][1]+" screen no. "+str(x[4][2])+", timings:"+x[4][3]+", duration:"+x[4][4]+", "+"DAY:"+x[4][6]+","+x[4][5],command=lambda:seating.seatingsm01(s=4),font="aerial 10")
    movie0x.grid(row=3,column=0)
    abt_movie0=Text(theatresframe,bg="black",fg="white",font="courier 12",bd=51,relief=SOLID)
    abt_movie0.grid(row=4,column=0)
    abt_movie0.insert(INSERT,"PLOT:\nVikram, a no-nonsense police officer, accompanied by \nSimon, his partner, is on the hunt to capture Vedha, a smuggler and a murderer. Vedha tries to change Vikram's life, which leads to a conflict")
    abt_movie0.insert(INSERT,"\n\n\nDirectors: Gayatri, Pushkar\nWriters: Manikandan (dialogue by), Gayatri\nStars: Madhavan, Vijay Sethupathi, Shraddha Srinath")
    abt_movie0.insert(INSERT,"\nVocals by Pradeep Kumar & Neha Venugopal\nLyrics by Sam C.S.\nMusic by Sam C.S.")

    
def m1():
    global theatresframe
    
    moviesframe.destroy()
    
    theatresframe=LabelFrame(text="SCREENS AVAILABLE AND TIMINGS",bg="black",fg="white")
    theatresframe.grid(row=0,column=0,sticky="nesw")
    theatresframe.grid_columnconfigure(0,weight=1)
    theatresframe.grid_rowconfigure(0,weight=1)
    movie1=Button(theatresframe,text=x[1][1]+" screen no. "+str(x[1][2])+", timings:"+x[1][3]+", duration:"+x[1][4]+", "+"DAY:"+x[1][6]+","+x[1][5],command=lambda:seating.seatingsm01(s=1),font="aerial 10")
    movie1.grid(row=2,column=0,pady=5)
    back_button=Button(theatresframe,text="<<",command=back)
    back_button.grid(row=1,column=0)
    movie1x=Button(theatresframe,text= x[5][1]+" screen no. "+str(x[5][2])+", timings:"+x[5][3]+", duration:"+x[5][4]+", "+"DAY:"+x[5][6]+","+x[5][5],command=lambda:seating.seatingsm01(s=5),font="aerial 10")
    movie1x.grid(row=3,column=0)
    abt_movie1=Text(theatresframe,bg="black",fg="white",font="courier 12",bd=51,relief=SOLID)
    abt_movie1.grid(row=4,column=0)
    abt_movie1.insert(INSERT,"")
    abt_movie1.insert(INSERT,"")
    abt_movie1.insert(INSERT,"")
def m2():
    global theatresframe
    
    moviesframe.destroy()
    
    theatresframe=LabelFrame(text="SCREENS AVAILABLE AND TIMINGS",bg="black",fg="white")
    theatresframe.grid(row=0,column=0,sticky="nesw")

    theatresframe.grid_columnconfigure(0,weight=1)
    theatresframe.grid_rowconfigure(0,weight=1)
    movie2=Button(theatresframe,text=x[2][1]+" screen no. "+str(x[2][2])+", timings:"+x[2][3]+", duration:"+x[2][4]+", "+"DAY:"+x[2][6]+","+x[2][5],command=lambda:seating.seatingsm01(s=2),font="aerial 10")
    movie2.grid(row=2,column=0,pady=5)
    back_button=Button(theatresframe,text="<<",command=back)
    back_button.grid(row=1,column=0)    
    movie2x=Button(theatresframe,text= x[6][1]+" screen no. "+str(x[6][2])+", timings:"+x[6][3]+", duration:"+x[6][4]+", "+"DAY:"+x[6][6]+","+x[6][5],command=lambda:seating.seatingsm01(s=6),font="aerial 10")
    movie2x.grid(row=3,column=0)
    abt_movie2=Text(theatresframe,bg="black",fg="white",font="courier 12",bd=51,relief=SOLID)
    abt_movie2.grid(row=4,column=0)
    abt_movie2.insert(INSERT,"")
    abt_movie2.insert(INSERT,"")
    abt_movie2.insert(INSERT,"")

def m3():
    global theatresframe
    
    moviesframe.destroy()
    
    theatresframe=LabelFrame(text="SCREENS AVAILABLE AND TIMINGS",bg="black",fg="white")
    theatresframe.grid(row=0,column=0,sticky="nesw")
    theatresframe.grid_columnconfigure(0,weight=1)
    theatresframe.grid_rowconfigure(0,weight=1)
    movie3=Button(theatresframe,text=x[3][1]+" screen no. "+str(x[3][2])+", timings:"+x[3][3]+", duration:"+x[3][4]+", "+"DAY:"+x[3][6]+","+x[3][5],command=lambda:seating.seatingsm01(s=3),font="aerial 10")
    movie3.grid(row=2,column=0,pady=5)
    back_button=Button(theatresframe,text="<<",command=back)
    back_button.grid(row=1,column=0)
    movie3x=Button(theatresframe,text= x[7][1]+" screen no. "+str(x[7][2])+", timings:"+x[7][3]+", duration:"+x[7][4]+", "+"DAY:"+x[7][6]+","+x[7][5],command=lambda:seating.seatingsm01(s=7),font="aerial 10")
    movie3x.grid(row=3,column=0)     
    abt_movie3=Text(theatresframe,bg="black",fg="white",font="courier 12",bd=51,relief=SOLID)
    abt_movie3.grid(row=4,column=0)
    abt_movie3.insert(INSERT,"")
    abt_movie3.insert(INSERT,"")
    abt_movie3.insert(INSERT,"")


def m4():
    global theatresframe
    
    moviesframe.destroy()
    
    theatresframe=LabelFrame(text="SCREENS AVAILABLE AND TIMINGS",bg="black",fg="white")
    theatresframe.grid(row=0,column=0,sticky="nesw")
    theatresframe.grid_columnconfigure(0,weight=1)
    theatresframe.grid_rowconfigure(0,weight=1)
    movie1=Button(theatresframe,text=x[8][1]+" screen no. "+str(x[8][2])+", timings:"+x[8][3]+", duration:"+x[8][4]+", "+"DAY:"+x[8][6]+","+x[8][5],command=lambda:seating.seatingsm01(s=8),font="aerial 10")
    movie1.grid(row=2,column=0,pady=5)
    back_button=Button(theatresframe,text="<<",command=back)
    back_button.grid(row=1,column=0)
    movie1x=Button(theatresframe,text= x[9][1]+" screen no. "+str(x[9][2])+", timings:"+x[9][3]+", duration:"+x[9][4]+", "+"DAY:"+x[9][6]+","+x[9][5],command=lambda:seating.seatingsm01(s=9),font="aerial 10")
    movie1x.grid(row=3,column=0)
    abt_movie1=Text(theatresframe,bg="black",fg="white",font="courier 12",bd=51,relief=SOLID)
    abt_movie1.grid(row=4,column=0)
    abt_movie1.insert(INSERT,"")
    abt_movie1.insert(INSERT,"")
    abt_movie1.insert(INSERT,"")

def m5():
    global theatresframe
    
    moviesframe.destroy()
    
    theatresframe=LabelFrame(text="SCREENS AVAILABLE AND TIMINGS",bg="black",fg="white")
    theatresframe.grid(row=0,column=0,sticky="nesw")
    theatresframe.grid_columnconfigure(0,weight=1)
    theatresframe.grid_rowconfigure(0,weight=1)
    movie1=Button(theatresframe,text=x[10][1]+" screen no. "+str(x[10][2])+", timings:"+x[10][3]+", duration:"+x[10][4]+", "+"DAY:"+x[10][6]+","+x[10][5],command=lambda:seating.seatingsm01(s=10),font="aerial 10")
    movie1.grid(row=2,column=0,pady=5)
    back_button=Button(theatresframe,text="<<",command=back)
    back_button.grid(row=1,column=0)
    movie1x=Button(theatresframe,text= x[13][1]+" screen no. "+str(x[13][2])+", timings:"+x[13][3]+", duration:"+x[13][4]+", "+"DAY:"+x[13][6]+","+x[13][5],command=lambda:seating.seatingsm01(s=13),font="aerial 10")
    movie1x.grid(row=3,column=0)
    abt_movie1=Text(theatresframe,bg="black",fg="white",font="courier 12",bd=51,relief=SOLID)
    abt_movie1.grid(row=4,column=0)
    abt_movie1.insert(INSERT,"")
    abt_movie1.insert(INSERT,"")
    abt_movie1.insert(INSERT,"")

def m6():
    global theatresframe
    
    moviesframe.destroy()
    
    theatresframe=LabelFrame(text="SCREENS AVAILABLE AND TIMINGS",bg="black",fg="white")
    theatresframe.grid(row=0,column=0,sticky="nesw")
    theatresframe.grid_columnconfigure(0,weight=1)
    theatresframe.grid_rowconfigure(0,weight=1)
    movie1=Button(theatresframe,text=x[11][1]+" screen no. "+str(x[11][2])+", timings:"+x[11][3]+", duration:"+x[11][4]+", "+"DAY:"+x[11][6]+","+x[11][5],command=lambda:seating.seatingsm01(s=11),font="aerial 10")
    movie1.grid(row=2,column=0,pady=5)
    back_button=Button(theatresframe,text="<<",command=back)
    back_button.grid(row=1,column=0)
    movie1x=Button(theatresframe,text= x[14][1]+" screen no. "+str(x[14][2])+", timings:"+x[14][3]+", duration:"+x[14][4]+", "+"DAY:"+x[14][6]+","+x[14][5],command=lambda:seating.seatingsm01(s=14),font="aerial 10")
    movie1x.grid(row=3,column=0)
    abt_movie1=Text(theatresframe,bg="black",fg="white",font="courier 12",bd=51,relief=SOLID)
    abt_movie1.grid(row=4,column=0)
    abt_movie1.insert(INSERT,"")
    abt_movie1.insert(INSERT,"")
    abt_movie1.insert(INSERT,"")

def m7():
    global theatresframe
    
    moviesframe.destroy()
    
    theatresframe=LabelFrame(text="SCREENS AVAILABLE AND TIMINGS",bg="black",fg="white")
    theatresframe.grid(row=0,column=0,sticky="nesw")
    theatresframe.grid_columnconfigure(0,weight=1)
    theatresframe.grid_rowconfigure(0,weight=1)
    movie1=Button(theatresframe,text=x[12][1]+" screen no. "+str(x[12][2])+", timings:"+x[12][3]+", duration:"+x[12][4]+", "+"DAY:"+x[12][6]+","+x[12][5],command=lambda:seating.seatingsm01(s=12),font="aerial 10")
    movie1.grid(row=2,column=0,pady=5)
    back_button=Button(theatresframe,text="<<",command=back)
    back_button.grid(row=1,column=0)
    movie1x=Button(theatresframe,text= x[15][1]+" screen no. "+str(x[15][2])+", timings:"+x[15][3]+", duration:"+x[15][4]+", "+"DAY:"+x[15][6]+","+x[15][5],command=lambda:seating.seatingsm01(s=15),font="aerial 10")
    movie1x.grid(row=3,column=0)
    abt_movie1=Text(theatresframe,bg="black",fg="white",font="courier 12",bd=51,relief=SOLID)
    abt_movie1.grid(row=4,column=0)
    abt_movie1.insert(INSERT,"")
    abt_movie1.insert(INSERT,"")
    abt_movie1.insert(INSERT,"")




#show movies with labels and images
def frontpage():
    
    
    global booknow1
    global booknow2
    global booknow3
    global booknow4
    global moviesframe
    global moviesimg1
    global moviesimg2
    global moviesimg3
    global moviesimg4
    global root
    global logoutf


    global img1
    global img2
    global img3
    global img4
    global img5
    global img6
    global img7
    global img8

    frame=Frame(bg="black")
    frame.grid(row=0,column=0,sticky="nesw")
    frame.grid_columnconfigure(1,weight=1)
    moviesframec=Canvas(frame,bg="black")
    moviesframec.grid(row=0,column=0,sticky="nesw")
    moviesframe=Frame(frame,bg="black")
    moviesframe.grid(row=0,column=0,sticky="nesw")
    """
    moviesframe.grid_columnconfigure(0,weight=1)
    moviesframe.grid_rowconfigure(0,weight=1)
    
    moviesframe=LabelFrame(text="MOVIES SCREENING THIS WEEK",bg="black",fg="white")
    moviesframe.pack(padx=10,pady=10,fill=BOTH,expand=1)"""
    Booknow1=Button(moviesframe,text="Vikram Vedha",command=m0)
    Booknow2=Button(moviesframe,text="Batman Vs Superman",command=m1)
    Booknow3=Button(moviesframe,text="Joker",command=m2)
    Booknow4=Button(moviesframe,text="Vivegam",command=m3)
    Booknow5=Button(moviesframe,text="The pursuit of\nHappyness",command=m4)
    Booknow6=Button(moviesframe,text="96",command=m5)
    Booknow7=Button(moviesframe,text="Oh My kadavule",command=m6)
    Booknow8=Button(moviesframe,text="WALL-E",command=m7)
    
    Book_list=[Booknow1,Booknow2,Booknow3,Booknow4,Booknow5,Booknow6,Booknow7,Booknow8]

    scroll_y = Scrollbar(frame, orient="vertical", command=moviesframec.yview)
    scroll_y.grid(row=0, column=4, sticky="ns",)

    moviesframec.config(yscrollcommand=scroll_y.set)
    """
    moviesframec.config(scrollregion=moviesframe.bbox("all"))"""
    moviesframec.bind('<Configure>',lambda e: moviesframec.configure(scrollregion=moviesframec.bbox("all")))

    moviesframec.create_window((0,0),window=moviesframe,anchor="nw")


    img1=ImageTk.PhotoImage(Image.open("images/Vikram Vedha.jpeg"))
    img2=ImageTk.PhotoImage(Image.open("images/BVS.jpeg"))
    img3=ImageTk.PhotoImage(Image.open("images/joker.jpeg"))
    img4=ImageTk.PhotoImage(Image.open("images/Vivegam.jpeg"))
    img5=ImageTk.PhotoImage(Image.open("images/poh.jpeg"))
    img6=ImageTk.PhotoImage(Image.open("images/96.jpeg"))
    img7=ImageTk.PhotoImage(Image.open("images/omk.jpeg"))
    img8=ImageTk.PhotoImage(Image.open("images/walle.jpeg"))


    moviesimg1=Button(moviesframe,image=img1,height=350,width=350,bd=2,bg="black")
    moviesimg2=Button(moviesframe,image=img2,height=350,width=350,bd=2,bg="black")
    moviesimg3=Button(moviesframe,image=img3,height=350,width=350,bd=2,bg="black")
    moviesimg4=Button(moviesframe,image=img4,height=350,width=350,bd=2,bg="black")
    moviesimg5=Button(moviesframe,image=img5,height=350,width=350,bd=2,bg="black")
    moviesimg6=Button(moviesframe,image=img6,height=350,width=350,bd=2,bg="black")
    moviesimg7=Button(moviesframe,image=img7,height=350,width=350,bd=2,bg="black")
    moviesimg8=Button(moviesframe,image=img8,height=350,width=350,bd=2,bg="black")
    moviesimg_list=[moviesimg1,moviesimg2,moviesimg3,moviesimg4,moviesimg5,moviesimg6,moviesimg7,moviesimg8]

    moviesimg1.grid(row=0,column=0,padx=10)
    moviesimg2.grid(row=0,column=1,padx=10)
    moviesimg3.grid(row=3,column=0,padx=10)
    moviesimg4.grid(row=3,column=1,padx=10)
    moviesimg5.grid(row=6,column=0,padx=10)
    moviesimg6.grid(row=6,column=1,padx=10)
    moviesimg7.grid(row=9,column=0,padx=10)
    moviesimg8.grid(row=9,column=1,padx=10)
    Booknow1.grid(row=1,column=0,padx=10,pady=(0,10))
    Booknow2.grid(row=1,column=1,padx=10,pady=(0,10))
    Booknow3.grid(row=4,column=0,padx=10,pady=(0,10))
    Booknow4.grid(row=4,column=1,padx=10,pady=(0,10))
    Booknow5.grid(row=7,column=0,padx=10,pady=(0,10))
    Booknow6.grid(row=7,column=1,padx=10,pady=(0,10))
    Booknow7.grid(row=10,column=0,padx=10,pady=(0,10))
    Booknow8.grid(row=10,column=1,padx=10,pady=(0,10))
    logoutf=Button(moviesframe,text="Log out",command=logout,bg="orange")
    logoutf.grid(row=11,column=0,pady=15,ipadx=100)
    showorders=Button(moviesframe,text="My Bookings",command=mybookings,bg="yellow")
    showorders.grid(row=11,column=1,pady=15,ipadx=100)
    















    
    

