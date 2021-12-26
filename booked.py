from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox





import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database='project')
k=mydb.cursor()








k.execute("create table CUSTOMERBOOKINGS(Email_ID varchar(100),bookedmovie varchar(51),screen_no varchar(19),timings varchar(21),seats_booked varchar(199),tot_amt varchar(19),day varchar(5))")

