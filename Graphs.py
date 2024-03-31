import mysql.connector as sqlcon;
import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;

def graphcompare():
   year=int(input("Enter Year : "));
   state1=input("Enter First State : ");
   state2=input("Enter Second State : ");
   con=sqlcon.connect(host="localhost", user="root", password="root", database="ipproject", charset="utf8")
   df=pd.read_sql("select state,totalcases,recovered,deaths from covidinfo where Year=%s and state='%s' or state='%s'"%(year,state1,state2),con);
   con.close();
   x=np.arange(len(df.state));
   plt.figure(figsize = (8,6));
   plt.bar(df.state,df.totalcases,color='blue',width=.25);
   plt.bar(x+.35,df.recovered,color='green',width=.25);
   plt.bar(x+.70,df.deaths,color='red',width=.25);
   plt.xlabel("States"); 
   plt.ylabel("Total Cases / Recovered / Deaths");   
   plt.title("Total Covid Cases Comparison For States "+state1 + " and "+state2+" For The Year : "+str(year)); 
   plt.show();
   input("Press Enter To Continue....");

def graphallstatestotal():
   year=int(input("Enter Year : "));
   con=sqlcon.connect(host="localhost", user="root", password="root", database="ipproject", charset="utf8")
   df=pd.read_sql("select state,totalcases from covidinfo where Year=%s"%(year),con);
   con.close();
   plt.figure(figsize = (12,6));
   plt.bar(df.state,df.totalcases,color='red');
   plt.xlabel("States"); 
   plt.ylabel("Total Cases");   
   plt.title("Total Covid Cases Comparison For States For The Year : "+str(year)); 
   plt.show();
   input("Press Enter To Continue....");
   
def graphallstatesdeaths():
   year=int(input("Enter Year : "));
   con=sqlcon.connect(host="localhost", user="root", password="root", database="ipproject", charset="utf8")
   df=pd.read_sql("select state,deaths from covidinfo where Year=%s"%(year),con);
   con.close();
   plt.figure(figsize = (12,6));
   plt.bar(df.state,df.deaths,color='red');
   plt.xlabel("States"); 
   plt.ylabel("Total Deaths");   
   plt.title("Total Covid Deaths Comparison For States For The Year : "+str(year)); 
   plt.grid(True);
   plt.show();
   input("Press Enter To Continue....");
#graphcompare();
#graphallstatesrecovered();
   
   

