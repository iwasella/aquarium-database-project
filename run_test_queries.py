import sqlite3

conn = sqlite3.connect("restaurant.db")
cur = conn.cursor()

# --------------------------
# Test Query 1: Add Customer 
# View current customer list first, add a customer, and then recheck if a new customer is made
# --------------------------
print("=== Test Query 1: Add Customer ===")
cur.execute("SELECT * FROM Customer")
print("-- Before --".center(50))
for row in cur.fetchall():
    print(row)

# Add Customer
cur.execute("INSERT INTO Customer (Name, Email, Phone) VALUES ('Test Customer','testcustomer@example.com','555-0101')")
conn.commit()

cur.execute("SELECT * FROM Customer")
print("-- After --".center(50))
for row in cur.fetchall():
    print(row)

# --------------------------
# Test Query 2: View Reservations
# Select all reservation in the system
# --------------------------
print("\n=== Test Query 2: View Reservations ===")
cur.execute("SELECT * FROM Reservation_Queue")
for row in cur.fetchall():
    print(row)

# --------------------------
# Test Query 3: Cancel Order
# View all current orders,delete the order along with its items, and then view all orders in the system to ensure its gone
# (In the CLI, you can only delete queued order to mock a real establishment, here as an example we also delete the queued order)
# --------------------------
print("\n=== Test Query 3: Cancel Order (Order_ID=3) ===")
cur.execute("""
SELECT o.Order_ID, c.Name AS Customer, e.Name AS Employee, o.Order_Status, o.Order_Date, o.Total_Amount
FROM Order_Table o
INNER JOIN Customer c ON o.Customer_ID = c.Customer_ID
INNER JOIN Employee e ON o.Employee_ID = e.Employee_ID
ORDER BY o.Order_Date ASC
""")
print("-- Before --".center(50))
for row in cur.fetchall():
    print(row)

# Delete order items and order
cur.execute("DELETE FROM Order_Item WHERE Order_ID = 3")
cur.execute("DELETE FROM Order_Table WHERE Order_ID = 3")
conn.commit()

cur.execute("""
SELECT o.Order_ID, c.Name AS Customer, e.Name AS Employee, o.Order_Status, o.Order_Date, o.Total_Amount
FROM Order_Table o
INNER JOIN Customer c ON o.Customer_ID = c.Customer_ID
INNER JOIN Employee e ON o.Employee_ID = e.Employee_ID
ORDER BY o.Order_Date ASC
""")
print("-- After --".center(50))
for row in cur.fetchall():
    print(row)

# --------------------------
# Test Query 4: Update Inventory (restocking)
#  View all items in the inventory, update one, then recheck if the item is updated
# --------------------------
print("\n=== Test Query 4: Update Inventory ===")
cur.execute("SELECT * FROM Inventory")
print("-- Before --".center(50))
for row in cur.fetchall():
    print(row)

# Update Cocoa Powder
cur.execute("""
UPDATE Inventory
SET Ingredient_name='Cocoa Powder', Ingredient_quantity=30, Ingredient_status='In Stock', Ingredient_supplier='SweetFoods'
WHERE Ingredient_ID=3
""")
conn.commit()

cur.execute("SELECT * FROM Inventory")
print("-- After --".center(50))
for row in cur.fetchall():
    print(row)

# --------------------------
# Test Query 5: Delete Employee
# View all employee in the system, delete one, recheck to see if the employee is removed
# --------------------------
print("\n=== Test Query 5: Delete Employee (Employee_ID=3) ===")
cur.execute("SELECT * FROM Employee")
print("-- Before --".center(50))
for row in cur.fetchall():
    print(row)

# Delete Employee from the system
cur.execute("DELETE FROM Employee WHERE Employee_ID=3")
conn.commit()

cur.execute("SELECT * FROM Employee")
print("-- After --".center(50))
for row in cur.fetchall():
    print(row)

conn.close()
