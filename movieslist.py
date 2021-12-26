
import mysql.connector
"""import theatrebooking"""
MOVIES=mysql.connector.connect(host="localhost",user="root",password="1234",database='project')
c=MOVIES.cursor()
"""c.execute("CREATE TABLE MOVIES(s_no varchar(3),moviename varchar(100),screen_no varchar(3),timings varchar(10),duration varchar(10),rating varchar(3),day varchar(5))")
"""


"""sqlFormula="insert into MOVIES(s_no,moviename,screen_no,timings,duration,rating,day)values(%s,%s,%s,%s,%s,%s,%s)"
movies=[("1","Vikram Vedha","1","2:45 PM","2h 27mins","U/A","1"),
        ("2","Batman VS Superman","1","11:45 AM","3h 3mins","U/A","1"),
        ("3","Joker","2","11:45 AM","2h 2mins","A","1"),
        ("4","Vivegam","2","10:00 PM","2h 28mins","U","1"),
        ("5","Vikram Vedha","2","6:30 PM","2h 27mins","U/A","2"),
        ("6","Batman VS Superman","2","2:45 PM","3h 3mins","U/A","2"),
        ("7","Joker","1","10.00 PM","2h 2mins","A","2"),
        ("8","Vivegam","1","6:30 PM","2h 28mins","U","2"),
        ("9","The pursuit of\nHappyness","1","6:30 PM","1h 57mins","U","1"),
        ("10","The pursuit of\nHappyness","1","2:45 PM","1h 57mins","U","2"),
        ("11","96","2","10.00 PM","2h 39mins","U/A","2"),
        ("12","Oh my kadavule","2","11:45 PM","2h 34mins","U/A","2"),
        ("13","Wall-E","1","11:45 AM","1h 43mins","U","2"),
        ("14","96","2","2:45 AM","2h 39mins","U/A","1"),
        ("15","Oh my kadavule","1","10.00 PM","2h 34mins","U/A","1"),
        ("16","Wall-E","2","6:30 PM","1h 43mins","U","1")]
c.executemany(sqlFormula,movies)
MOVIES.commit()"""


def getmname():
    global result1
    result1=[]
    c.execute("select * from movies")
    result=c.fetchall()
    for i in result:
        result1.append(i)
              
    return result1
print(getmname())
x=getmname()

            





































