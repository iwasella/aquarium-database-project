CREATE TABLE IF NOT EXISTS Customer (
    Customer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Reservation_Queue (
    Reser_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_ID INTEGER NOT NULL,
    Reserv_time TEXT NOT NULL,
    Reserv_size INTEGER NOT NULL,
    Reserv_status TEXT NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
);

CREATE TABLE IF NOT EXISTS Employee (
    Employee_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Salary REAL NOT NULL,
    Employment_Type TEXT NOT NULL,
    Job_Title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Order_Table (
    Order_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_ID INTEGER NOT NULL,
    Employee_ID INTEGER NOT NULL,
    Order_Status TEXT NOT NULL,
    Order_Date TEXT NOT NULL,
    Total_Amount REAL NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);

CREATE TABLE IF NOT EXISTS Menu_Item (
    MenuItem_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Category TEXT CHECK (Category IN ('Drink','Food','Dessert')),
    Price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS Order_Item (
    Order_ID INTEGER NOT NULL,
    MenuItem_ID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    PRIMARY KEY (Order_ID, MenuItem_ID),
    FOREIGN KEY (Order_ID) REFERENCES Order_Table(Order_ID),
    FOREIGN KEY (MenuItem_ID) REFERENCES Menu_Item(MenuItem_ID)
);

CREATE TABLE IF NOT EXISTS Inventory (
    Ingredient_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Ingredient_name TEXT NOT NULL,
    Ingredient_quantity INTEGER NOT NULL,
    Ingredient_status TEXT NOT NULL,
    Ingredient_supplier TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Uses (
    MenuItem_ID INTEGER NOT NULL,
    Ingredient_ID INTEGER NOT NULL,
    PRIMARY KEY (MenuItem_ID, Ingredient_ID),
    FOREIGN KEY (MenuItem_ID) REFERENCES Menu_Item(MenuItem_ID),
    FOREIGN KEY (Ingredient_ID) REFERENCES Inventory(Ingredient_ID)
);

CREATE TABLE IF NOT EXISTS Maintains (
    Employee_ID INTEGER NOT NULL,
    Ingredient_ID INTEGER NOT NULL,
    PRIMARY KEY (Employee_ID, Ingredient_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID),
    FOREIGN KEY (Ingredient_ID) REFERENCES Inventory(Ingredient_ID)
);
