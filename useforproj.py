def some():
    for i in range(1,21):
        print("    "+"s"+str(i+150)+"=Button(seatingframe,text='k"+str(i)+"'"+",bg='green',fg='white',command=lambda:changecolour("+str(i+150)+"))")
        print("    "+"s"+str(i+150)+".grid(row=11,column="+str(i)+",padx=3,pady=(10,5))\n")
        
def some2():
    for i in range(1,150):
        print("s"+str(i),end=",")
print(some())
              
