import csv,os,datetime

class Constants:
    ADMIN_FILE = "AdminFile.csv"
    MENU_FILE = "MenuFile.csv"
    COSTUMER_FILE = "CostumerFile.csv"
    INITIAL_ID = 800
    
def main():
    while True:
        print("############################");
        print("1. Admin Login");
        print("2. Costumer");
        print("3. Exit");
        choice = int(input("Enter Your Choice : "))
        if choice ==1:
            AdminLogin();
        elif choice==2:
            CostumerMenu();
        else:
            exit();
def CheckFile(filename):
    try:
        file = open(filename, "r") 
        file.close()  
        return 1  
    except:
        file = open(filename, "w")
        file.close()
        return 1    
def AdminLogin():
    username = input("Enter Your Username : ");
    Password = input("Enter Your Pasword : ");
    if(CheckFile(Constants.ADMIN_FILE)):
        file = open(Constants.ADMIN_FILE,"r");
        csv_reader = csv.reader(file)
        for data in csv_reader:
            FileUsername = data[0];
            FilePassword = data[1];
            if(FileUsername == username and FilePassword == Password):
                print("Login Successful ");
                AdminMenu();
def AdminMenu():
    CheckFile(Constants.MENU_FILE);
    while True:
        print("############################");
        print("1. Add Items ");
        print("2. View Menu ");
        print("3. Remove Item ");
        print("4. Update Item");
        print("5. Delete Menu ");
        print("6. All Costumer Order");
        print("7. Exit");
        choice = int(input("Enter Your Choice : "));
        if choice == 1:
            AddItems();
        elif choice == 2:
            ViewMenu();
        elif choice == 3:
            RemoveItem();
        elif choice == 4:
            UpdateItem();
        elif choice == 5:
            DeleteMenu();
        elif choice == 6:
            CostumerList();
        else:
            return 0;
def AddItems():
    No = int(input("Enter No. of Items You Want To Add : "));
    file = open(Constants.MENU_FILE,"a",newline='')
    for i in range(1,No+1):
        ItemName = input(f"Enter Item{i} Name : ");
        ItemName = ItemName.upper();
        ItemPrice = input(f"Enter Item{i} Price : ");
        ItemQuantity = input(f"Enter Item{i} Quantity : ");
        ItemData = [ItemName,ItemPrice,ItemQuantity];
        csv_writer = csv.writer(file)
        csv_writer.writerow(ItemData);
        print("Intem Added Succesfully ");
    file.close();
def RemoveItem():
    ItemName = input("Enter Item Name To Remove : ");
    ItemName = ItemName.upper();
    CheckFile(Constants.MENU_FILE);
    file = open(Constants.MENU_FILE,"r");
    file2 = open("tempfile.csv","w",newline='');
    read = csv.reader(file);
    for data in read:
        if data[0] == ItemName:
            print("Item Removed......");
            found = 1;
            continue;
        write = csv.writer(file2);
        write.writerow(data);
    file.close();
    file2.close();
    if found == 1:
        os.remove(Constants.MENU_FILE)
        os.rename("tempfile.csv",Constants.MENU_FILE)
        return 0;
    else:
        print("Item Not Found ");
        return 0;
def UpdateItem():
    ItemName = input("Enter Item Name To Update : ");
    ItemName = ItemName.upper();
    CheckFile(Constants.MENU_FILE);
    file = open(Constants.MENU_FILE,"r");
    file2 = open("tempfile.csv","w",newline='');
    read = csv.reader(file);
    for data in read:
        if data[0] == ItemName:
            print("Item Updating......");
            found = 1;
            itemNewQuantity = int(input("Enter New Quantity : "))
            itemNewPrice = int(input("Enter New Price : "))
            newdata = [data[0],itemNewPrice,itemNewQuantity]
            write = csv.writer(file2);
            write.writerow(newdata);
            continue;
        write = csv.writer(file2);
        write.writerow(data);
    file.close();
    file2.close();
    if found == 1:
        os.remove(Constants.MENU_FILE)
        os.rename("tempfile.csv",Constants.MENU_FILE)
        return 0;
    else:
        print("Item Not Found ");
        return 0;
def ViewMenu():
    file = open(Constants.MENU_FILE,"r");
    csv_reader = csv.reader(file)
        
    print(f"{'Item Name':<20} {'Price':<10} {'Quantity':<10}")
    print("-" * 35)

    for data in csv_reader:
        ItemName, ItemPrice, ItemQuantity = data
        print(f"{ItemName:<20} {ItemPrice:<10} {ItemQuantity:<10}")   
def DeleteMenu():
    os.remove(Constants.MENU_FILE); 
def CostumerList():
    CheckFile(Constants.COSTUMER_FILE);
    file = open(Constants.COSTUMER_FILE,"r");
    csv_reader = csv.reader(file);
    print("###########################");
    for lines in csv_reader:
        for word in lines:
            print(f"{word:<9}",end="");
        print("");
    file.close();

# ADMIN COMPLETE

def CostumerMenu():
    while True:
        print("\n###########################");
        print("1. View Menu");
        print("2. Buy Items");
        print("3. View Order");
        print("4. Exit ");
        choice = int(input("Enter Your Choice : "));
        if choice == 1:
            ViewMenu();
        elif choice == 2:
            BuyItems();
        elif choice == 3:
            ViewOrder();
        else:
            return 0;     
def IdChecker():
    CheckFile(Constants.COSTUMER_FILE);
    file = open(Constants.COSTUMER_FILE,"r");
    csv_reader = csv.reader(file);
    id = 0
    for data in csv_reader:
        try:
            id = int(data[0])
        except:
            continue;

    if id>Constants.INITIAL_ID:
        return (id + 1);
    else:
        return Constants.INITIAL_ID;  
def DateAndTime():
    CurrentTime = datetime.datetime.now()
    return CurrentTime;
def BuyItems():
    price = 0;
    CheckFile(Constants.COSTUMER_FILE);
    CheckFile(Constants.MENU_FILE);
    file = open(Constants.COSTUMER_FILE,"a",newline='');
    file2 = open(Constants.MENU_FILE,"r");
    name = input("Enter Your Name : ");
    csv_writer = csv.writer(file);
    csv_reader = csv.reader(file2);
    data = [IdChecker(),name,DateAndTime()]
    csv_writer.writerow(data);
    csv_writer.writerow(["ITEMS","PRICE_1","QUANTITY"])
    NOItemsUBuy = int(input("Enter No. Of Items You Want To Buy : "));
    for i in range(1,NOItemsUBuy+1):
        file2.seek(0)
        ItemName = input("Enter Item Name : ");
        ItemName = ItemName.upper();
        ItemQuantity = int(input("Enter No Of Quantity : "));
        for data in csv_reader:
            if data[0] == ItemName:
                userdata = [ItemName,data[1],ItemQuantity]
                csv_writer.writerow(userdata);
                price = price + (int(data[1])*ItemQuantity);
            else:
                continue;
                
    csv_writer.writerow([f"TotalPrice",price]);
    file.close();
def ViewOrder():
    Id = int(input("Enter Your Id : "));
    CheckFile(Constants.COSTUMER_FILE);
    file = open(Constants.COSTUMER_FILE,"r");
    csv_reader = csv.reader(file);
    id = 0
    for data in csv_reader:
        try:
            id = int(data[0]);
            if id == Id:
                for word in data:
                    print(f"{word:<12}",end="");
                print("")
                
        except:
            if Id == id:
                for word in data:
                    print(f"{word:<12}",end="");
                print("")
            continue;

# COSTUMER COMPLETE

main();