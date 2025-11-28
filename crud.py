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
    cur.execute("DELETE FROM Uses WHERE MenuItem_ID=?", (menu_id))
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

