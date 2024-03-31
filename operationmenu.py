import DBOperations as db;
import DataAnalysis as da;
import Graphs as gp;
def showop():
    while(True):
        print("_____________________________________________________________");
        print("1. Add Covid Info : ");
        print("2. Update Covid Info : ");
        print("3. Delete Covid Info : ");
        print("0. Exit");
        print("_____________________________________________________________");
        opch=int(input("Enter Your Choice : "));
        if opch==0:
            print("Exiting From DB Operations....!");
            break;
        elif opch==1:
            db.addrecord();
        elif opch==2:
            db.updaterecord();
        elif opch==3:
            db.deleterecord();

def viewdata():
    while(True):
        print("_____________________________________________________________");
        print("1. View All States Data : ");
        print("2. View States With Maximum Cases  : ");
        print("3. View States With Minimum Cases  : ");
        print("4. View Report For Individual State : ");
        print("5. View Report For Individual Year  : ");
        print("6. View Summary : ");
        print("0. Exit");
        print("_____________________________________________________________");
        opch=int(input("Enter Your Choice : "));
        if opch==0:
            print("Exiting From Data Reports....!");
            break;
        elif opch==1:
            da.showallcases();
        elif opch==2:
            da.showtoptotal();
        elif opch==3:
            da.showlowesttotal();
        elif opch==4:
            da.showstatewise();
        elif opch==5:
            da.showyearwise();
        elif opch==6:
            da.showsummary();

def viewgraphs():
    while(True):
        print("_____________________________________________________________");
        print("1. View Graphical Report For Total Cases  : ");
        print("2. View Graphical Report For Total Deaths  : ");
        print("3. View Comparative Report For Any Two States  : ");
        print("0. Exit");
        print("_____________________________________________________________");
        opch=int(input("Enter Your Choice : "));
        if opch==0:
            print("Exiting From Report Visualization....!");
            break;
        elif opch==1:
            gp.graphallstatestotal();
        elif opch==2:
            gp.graphallstatesdeaths();
        elif opch==3:
            gp.graphcompare();
        