# BMS-Python

This is a Python-based project for a **Billing Management System (BMS)**. It simulates a system where administrators can manage a menu and customer orders, and customers can view the menu, place orders, and track their purchases.

## Features

### Admin Features:
1. **Login**: Admin can log in using a username and password.
2. **Menu Management**:
   - Add new items to the menu.
   - Remove items from the menu.
   - Update item details such as price and quantity.
   - View the current menu.
   - Delete the entire menu.
3. **Customer Orders**: Admin can view a list of customer orders.

### Customer Features:
1. **View Menu**: Customers can view the menu with item names, prices, and available quantities.
2. **Buy Items**: Customers can select items to purchase, specify quantity, and place an order.
3. **View Orders**: Customers can view their past orders by providing their unique ID.

## Requirements

This project is written in Python and uses the following libraries:
- **csv**: For file handling and data storage.
- **os**: For file manipulation (like renaming and deleting files).
- **datetime**: For capturing and storing order timestamps.

### Installation

To use this project, you need to have Python installed on your system. If you don't have it already, you can download and install it from [here](https://www.python.org/downloads/).

1. Once Python is installed, clone this repository to your local machine:
   
    ```bash
    git clone https://github.com/ankit02yadav/BMS-Python.git
    cd BMS-Python
Usage
Admin Login: The admin must log in using a username and password, both of which are stored in AdminFile.csv.
Menu Management: The admin can add, remove, update, and view menu items. Menu data is stored in MenuFile.csv.
Customer Operations: Customers can view the menu, buy items, and track their orders. Customer details are saved in CostumerFile.csv.
Running the Program
2. To run the system, simply run the main Python script:

      python main.py
    
You will be presented with a menu where you can either log in as an admin or proceed as a customer.
Files
AdminFile.csv: Contains the admin login credentials (username, password).
MenuFile.csv: Stores the menu items (name, price, quantity).
CostumerFile.csv: Stores customer order information (ID, name, date, items, prices, quantities).
Example of CSV Files
AdminFile.csv:

    admin,admin123

MenuFile.csv:

    Burger,10,20
    Pizza,15,30

CostumerFile.csv:

    810,rao,2025-03-13 00:52:37.106115
    ITEMS,PRICE_1,QUANTITY
    CAKE,100,3
    EGG,10,5
    PIZZA,500,2
    TotalPrice,1350
    
Functions
AdminLogin: Handles the admin login process by checking credentials from the CSV file.
AdminMenu: Displays options for menu management and order viewing.
AddItems: Adds new items to the menu.
RemoveItem: Removes an item from the menu.
UpdateItem: Updates the details (price, quantity) of an existing item.
ViewMenu: Displays the list of menu items.
DeleteMenu: Deletes the menu (removes the MenuFile.csv).
CostumerMenu: Displays the options for customers (view menu, buy items, view orders).
BuyItems: Handles the process of customers buying items from the menu.
ViewOrder: Allows customers to view their past orders.
Notes
The program uses simple CSV files to store data. It is a basic version and doesn't include any security measures for login.
The program handles only basic functionalities for menu management and customer ordering.
Contributing
If you would like to contribute to this project, feel free to fork the repository and create a pull request. Please ensure that your contributions follow the project’s coding style and include appropriate comments.

License
This project is open-source and available under the MIT License.
