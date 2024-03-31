import operationmenu as menu;

while True :
    print("==========================Main-Menu==========================");
    print("_____________________________________________________________");
    print("1. Data Operation : ");
    print("2. View Data Reports : ");
    print("3. Report Visualization  : ");
    print("0. Exit");
    print("_____________________________________________________________");
    
    ch=int(input("Enter Your Choice : "));
    if ch==0 :
        print("Exiting From Main Application....!");
        break;
    elif ch==1:
        menu.showop();       
    elif ch==2:
        menu.viewdata();
    elif ch==3:
        menu.viewgraphs()
        