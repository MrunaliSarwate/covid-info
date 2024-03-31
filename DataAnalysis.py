import mysql.connector as sqlcon;
import pandas as pd;


def showallcases():
    con=sqlcon.connect(host="localhost", user="root", password="root", database="ipproject", charset="utf8")
    df=pd.read_sql("select * from covidinfo order by year,state",con);
    print("Total Covid Cases In Various States .....");
    print("___________________________________________________________________________________________________________________________");
    print(df);
    print("___________________________________________________________________________________________________________________________");
    input("Press Enter To Continue....");
    con.close();        
    
def showtoptotal():
    print("Maximum Covid Cases In Various States .....");
    print("___________________________________________________________________________________________________________________________");
    year=int(input("Enter Year  : "));
    n=int(input("Enter Total Top No : "));
    con=sqlcon.connect(host="localhost", user="root", password="root", database="ipproject", charset="utf8")
    df=pd.read_sql("select state, year, totalcases from covidinfo where year=%s order by totalcases desc limit %s"%(year,n),con);
    print(df);
    print("___________________________________________________________________________________________________________________________");
    input("Press Enter To Continue....");
    con.close();       
    
def showlowesttotal():
    print("Minimum Covid Cases In Various States .....");
    print("___________________________________________________________________________________________________________________________");
    year=int(input("Enter Year  : "));
    n=int(input("Enter Total lowest No : "));
    con=sqlcon.connect(host="localhost", user="root", password="root", database="ipproject", charset="utf8")
    df=pd.read_sql("select state, year, totalcases from covidinfo where year=%s order by totalcases limit  %s"%(year,n), con);
    print(df);
    print("___________________________________________________________________________________________________________________________");
    input("Press Enter To Continue....");
    con.close(); 

def showstatewise():
    print("Total Covid Cases In Various States .....");
    print("___________________________________________________________________________________________________________________________");
    state=input("Enter State name : ");
    con=sqlcon.connect(host="localhost", user="root", password="root", database="ipproject", charset="utf8")
    df=pd.read_sql("select * from covidinfo where state='%s'"%(state),con);
    print(df);
    print("___________________________________________________________________________________________________________________________");
    input("Press Enter To Contiune....");
    con.close();
   
    
def showyearwise():
    print("Total Covid Cases For Individual Year .....");
    print("___________________________________________________________________________________________________________________________");
    print("Yearwise Covid data");
    #state=input("Enter State name : ");
    year=int(input("Enter Year : "));
    con=sqlcon.connect(host="localhost", user="root", password="root", database="ipproject", charset="utf8")
    df=pd.read_sql("select * from covidinfo where Year=%s"%(year),con);
    print(df);
    print("___________________________________________________________________________________________________________________________");
    print("Press Enter To Continue....");
    con.close();
    
#showyearwise()

def showsummary():
    print("Total Covid data Summary");
    con=sqlcon.connect(host="localhost", user="root", password="root", database="ipproject", charset="utf8");
    df=pd.read_sql("select sum(totalcases) as 'TOTAL CASES',sum(recovered) as 'TOTAL RECOVERED',sum(deaths) as 'TOTAL DEATHS'  from covidinfo",con);
    print("___________________________________________________________________________________________________________________________");
    print(df);
    print("___________________________________________________________________________________________________________________________");
    con.close();

#showsummary();
#showyearwise();
#showstatewise();
#showyearwise();
#showtotalcases();    
#showallcases();
#showtoptotal();
#showlowesttotal();
#showstatewise();