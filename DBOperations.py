import pandas as pd;
import mysql.connector as sql;

def addrecord():
    print("Covid Data Addition : ");
    state=input("Enter State : ");
    year=int(input("Enter Year : "));
    total=int(input("Enter Total Cases : "));
    rec=int(input("Enter Recovered Cases : "));
    death=int(input("Enter Deaths : "));
    con=sql.connect(host="localhost",user="root",password="root",database="ipproject",charset="utf8");
    cursor=con.cursor();
    cursor.execute("insert into covidinfo values('%s',%s,%s,%s,%s)"%(state,year,total,rec,death));
    con.commit();
    con.close();
    print("Record Successfully Added....");

def updaterecord():
    print("Covid Data Modification : ");
    state=input("Enter State To Be Updated : ");
    year=int(input("Enter Year To Be Updated : "));
    total=int(input("Enter New Total Cases : "));
    rec=int(input("Enter New Recovered Cases : "));
    death=int(input("Enter New Deaths : "));
    con=sql.connect(host="localhost",user="root",password="root",database="ipproject",charset="utf8");
    cursor=con.cursor();
    cursor.execute("update covidinfo set totalcases=%s, recovered=%s, deaths=%s where state='%s' and year=%s"%(total,rec,death,state,year));
    con.commit();
    con.close();
    print("Record Successfully Modified....");

def deleterecord():
    print("Covid Data Deletion : ");
    state=input("Enter State To Be Deleted : ");
    year=int(input("Enter Year To Be Deleted : "));
    con=sql.connect(host="localhost",user="root",password="root",database="ipproject",charset="utf8");
    cursor=con.cursor();
    cursor.execute("delete from covidinfo where state='%s' and year=%s"%(state,year));
    con.commit();
    con.close();
    print("Record Successfully Removed....");

#deleterecord();
#addrecord();
    
