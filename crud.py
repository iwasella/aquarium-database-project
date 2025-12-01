import sqlite3

DB_NAME = "restaurant.db"


# ---------------------------
# Helper DB connection
# ---------------------------
def get_connection():
    return sqlite3.connect(DB_NAME)


# ---------------------------
# CUSTOMER CRUD
# ---------------------------
def create_customer(name, email, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Customer (Name, Email, Phone)
        VALUES (?, ?, ?)
    """, (name, email, phone))
    conn.commit()
    conn.close()


def read_customers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Customer")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_customer(customer_id, name, email, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Customer
        SET Name=?, Email=?, Phone=?
        WHERE Customer_ID=?
    """, (name, email, phone, customer_id))
    conn.commit()
    conn.close()


def delete_customer(customer_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Customer WHERE Customer_ID=?", (customer_id,))
    conn.commit()
    conn.close()


# ---------------------------
# RESERVATION QUEUE CRUD
# ---------------------------
def create_reservation(customer_id, time, size, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Reservation_Queue (Customer_ID, Reserv_time, Reserv_size, Reserv_status)
        VALUES (?, ?, ?, ?)
    """, (customer_id, time, size, status))
    conn.commit()
    conn.close()


def read_reservations():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Reservation_Queue")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_reservation(reser_id, time, size, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Reservation_Queue
        SET Reserv_time=?, Reserv_size=?, Reserv_status=?
        WHERE Reser_ID=?
    """, (time, size, status, reser_id))
    conn.commit()
    conn.close()


def delete_reservation(reser_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Reservation_Queue WHERE Reser_ID=?", (reser_id,))
    conn.commit()
    conn.close()


# ---------------------------
# EMPLOYEE CRUD
# ---------------------------
def create_employee(salary, employment_type, job_title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Employee (Salary, Employment_Type, Job_Title)
        VALUES (?, ?, ?)
    """, (salary, employment_type, job_title))
    conn.commit()
    conn.close()


def read_employees():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Employee")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_employee(employee_id, salary, employment_type, job_title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Employee
        SET Salary=?, Employment_Type=?, Job_Title=?
        WHERE Employee_ID=?
    """, (salary, employment_type, job_title, employee_id))
    conn.commit()
    conn.close()


def delete_employee(employee_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Employee WHERE Employee_ID=?", (employee_id,))
    conn.commit()
    conn.close()


# ---------------------------
# MENU ITEM CRUD
# ---------------------------
def create_menu_item(name, category, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Menu_Item (Name, Category, Price)
        VALUES (?, ?, ?)
    """, (name, category, price))
    conn.commit()
    conn.close()


def read_menu_items():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Menu_Item")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_menu_item(menu_id, name, category, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Menu_Item
        SET Name=?, Category=?, Price=?
        WHERE MenuItem_ID=?
    """, (name, category, price, menu_id))
    conn.commit()
    conn.close()


def delete_menu_item(menu_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Menu_Item WHERE MenuItem_ID=?", (menu_id,))
    cur.execute("DELETE FROM Uses WHERE MenuItem_ID=?", (menu_id,))
    conn.commit()
    conn.close()
    
    
def read_menu_item_ingredients():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT Uses.MenuItem_ID, Menu_Item.Name, Uses.Ingredient_ID, Inventory.Ingredient_name
        FROM Uses
        INNER JOIN Menu_Item
        ON Uses.MenuItem_ID = Menu_Item.MenuItem_ID
        INNER JOIN Inventory
        ON Uses.Ingredient_ID = Inventory.Ingredient_ID
    """)
    rows = cur.fetchall()
    conn.close()
    return rows
    
    
def add_menu_item_ingredient(menu_id, ingredient_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Uses (MenuItem_ID, Ingredient_ID)
        VALUES (?, ?)
    """, (menu_id, ingredient_id))
    conn.commit()
    conn.close()
   
    
def delete_menu_item_ingredient(menu_id, ingredient_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Uses WHERE MenuItem_ID=? AND Ingredient_ID=?", (menu_id, ingredient_id))
    conn.commit()
    conn.close()


# ---------------------------
# INVENTORY CRUD
# ---------------------------
def create_inventory_item(name, quantity, status, supplier):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Inventory (Ingredient_name, Ingredient_quantity, Ingredient_status, Ingredient_supplier)
        VALUES (?, ?, ?, ?)
    """, (name, quantity, status, supplier))
    conn.commit()
    conn.close()


def read_inventory():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Inventory")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_inventory(ingredient_id, name, quantity, status, supplier):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Inventory
        SET Ingredient_name=?, Ingredient_quantity=?, Ingredient_status=?, Ingredient_supplier=?
        WHERE Ingredient_ID=?
    """, (name, quantity, status, supplier, ingredient_id))
    conn.commit()
    conn.close()


def delete_inventory(ingredient_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Inventory WHERE Ingredient_ID=?", (ingredient_id,))
    cur.execute("DELETE FROM Uses WHERE Ingredient_ID=?", (ingredient_id))
    conn.commit()
    conn.close()


# ---------------------------
# ORDER CRUD
# ---------------------------

def get_orders():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT o.Order_ID, 
               c.Name AS Customer,
               e.Name AS Employee,
               o.Order_Status, o.Order_Date,  o.Total_Amount
        FROM Order_Table o
        INNER JOIN Customer c ON o.Customer_ID = c.Customer_ID
        INNER JOIN Employee e ON o.Employee_ID = e.Employee_ID
        ORDER BY o.Order_Date ASC;
    """)
    orders = cur.fetchall()
    conn.close()

    print("🌊🌊 ALL ORDERS 🌊🌊".center(50))
    for order in orders:
        print(f"""Order #{order[0]}
        Customer: {order[1]}
        Employee: {order[2]}
        Status: {order[3]}
        Date: {order[4]}
        Total: ${order[5]:.2f}
        {'-' * 30}""") 


def add_order():
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT Customer_ID, Name FROM Customer")
    customer_list = cur.fetchall()
    print("🌊🌊 Customers 🌊🌊".center(50))
    for c in customer_list:
        print(f"{c[0]}: {c[1]}")
    customer_id = int(input("Enter Customer ID: "))

    cur.execute("SELECT Employee_ID, Name FROM Employee WHERE Job_Title = 'Server'")
    server = cur.fetchall()
    print("🌊🌊 Available Server 🌊🌊".center(50))
    for e in server:
        print(f"{e[0]}: {e[1]}")
    server_id = int(input("Enter Server ID: "))

    cur.execute("SELECT MenuItem_ID, Name, Price FROM Menu_Item")
    menu = cur.fetchall()
    print("🌊🌊 Menu Items 🌊🌊".center(50))
    for i in menu:
        print(f"{i[0]}: {i[1]}    ${i[2]:.2f}")
    
    order = []
    while True:
        add_item = input ("Enter Menu Item ID (or 'done' when finished): ")
        if add_item.lower() == 'done':
            break
        item_id = int(add_item)
        quantity = int(input("Quantity: "))
        order.append((item_id, quantity))

    total = sum(
        cur.execute("SELECT Price FROM Menu_Item WHERE MenuItem_ID = ?", (item_id,)).fetchone()[0] * quantity for item_id, quantity in order
    )

    cur.execute("""
        INSERT INTO Order_Table (Customer_ID, Employee_ID, Order_Status, Order_Date, Total_Amount)
        VALUES (?, ?, 'Queue', datetime('now'), ?)
    """, (customer_id, server_id, total))
    order_id = cur.lastrowid

    for item_id, quantity in order:
        cur.execute("""
        INSERT INTO Order_Item (Order_ID, MenuItem_ID, Quantity)
        VALUES (?, ?, ?)
    """, (order_id, item_id, quantity))
        
    conn.commit()
    conn.close()

    print(f"Order #{order_id} successfully added!")

def cancel_order():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT o.Order_ID, 
               c.Name AS Customer,
               o.Order_Date
        FROM Order_Table o
        INNER JOIN Customer c ON o.Customer_ID = c.Customer_ID
        WHERE o.Order_Status = 'Queue'
        ORDER BY o.Order_Date ASC;
    """)
    orders = cur.fetchall()
    print("🌊🌊 QUEUED ORDERS 🌊🌊".center(50))
    for order in orders:
        print(f"Order #{order[0]}  Customer: {order[1]}  Date: {order[2]}")

    order_id = int(input("Enter Order ID to cancel: "))
    cur.execute("SELECT Order_Status FROM Order_Table WHERE Order_ID = ?", (order_id,))
    result = cur.fetchone()

    if result is None:
        print(f"Order #{order_id} does not exist.")
    elif result[0] != 'Queue':
        print(f"Order #{order_id} cannot be cancelled (not queued).")
    else:
        cur.execute("DELETE FROM Order_Item WHERE Order_ID = ?", (order_id,))
        cur.execute("DELETE FROM Order_Table WHERE Order_ID = ?", (order_id,))
        conn.commit()
        print(f"Order #{order_id} has been successfully cancelled!")

    conn.close()

def receipt():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT o.Order_ID, 
               c.Name AS Customer,
               o.Order_Date
        FROM Order_Table o
        INNER JOIN Customer c ON o.Customer_ID = c.Customer_ID
        WHERE o.Order_Status = 'Finished'
        ORDER BY o.Order_Date ASC;
    """)
    orders = cur.fetchall()
    print("🌊🌊 FINISHED ORDERS 🌊🌊".center(50))
    for order in orders:
        print(f"Order #{order[0]}  Customer: {order[1]}  Date: {order[2]}")
    order_id = int(input("Enter order ID for receipt: "))
    cur.execute("""
        SELECT c.Name AS Customer, e.Name as Employee, o.Order_date, o. Total_Amount
        FROM Order_Table o
        INNER JOIN Customer c ON o.Customer_ID = c.Customer_ID
        INNER JOIN Employee e ON o.Employee_ID = e.Employee_ID
        WHERE o.Order_ID = ? AND o.Order_Status = 'Finished' 
    """, (order_id,))
    receipt = cur.fetchone()
    if not receipt:
        print("Failed to grab receipt! (Did not exist or not a Finished order)")
        conn.close()
        return
    
    print(f"""Order #{order_id}
    Customer: {receipt[0]}
    Employee: {receipt[1]}
    Date: {receipt[2]}
    {'-' * 30}""") 

    cur.execute("""
        SELECT m.Name, i.Quantity, m.Price, (i.Quantity * m.Price) AS Subtotal
        FROM Order_Item i
        INNER JOIN Menu_ITem m ON i.MenuItem_ID = m.MenuItem_ID
        WHERE i.Order_ID = ?
    """, (order_id,))
    items = cur.fetchall()
    for item in items:
        print(f"{item[0]} x{item[1]}  ${item[2]:.2f} each   Subtotal: ${item[3]:.2f}")
    print("-" * 30)
    print(f"Total: ${receipt[3]:.2f}")

    conn.close()

def update_order_status():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(""" 
        SELECT o.Order_ID, c.Name AS Customer, o.Order_Status
        FROM Order_Table o
        INNER JOIN Customer c ON o.Customer_ID = c.Customer_ID
        WHERE o.Order_Status != 'Finished'
        ORDER BY o.Order_Date ASC
    """)
    orders = cur.fetchall()
    
    print("🌊🌊 AVAILABLE ORDERS FOR UPDATE 🌊🌊".center(50))
    for order in orders:
        print(f"Order #{order[0]}  Customer: {order[1]}  Status: {order[2]}")
    order_id = int(input("Enter Order ID to update: "))
    status_change = input("Enter new status (Preparing/Finished): ")
    cur.execute("SELECT Order_Status FROM Order_Table WHERE Order_ID = ?", (order_id,))
    cur_status = cur.fetchone()[0]

    if(cur_status == 'Queue' and status_change in ['Preparing', 'Finished']) or (cur_status == 'Preparing' and status_change == 'Finished'): 
        cur.execute("UPDATE Order_Table SET Order_Status = ? WHERE Order_ID = ?", (status_change, order_id))
        conn.commit()
        print(f"Order #{order_id} status is updated from {cur_status} to {status_change}!")
    else: 
        print(f"Cannot change Order #{order_id} status from {cur_status} to {status_change}!")
    conn.close()
