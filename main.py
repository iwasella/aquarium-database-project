from crud import *

def main_options():
    print("\n==== RESTAURANT DATABASE ====")
    print("1. Customers")
    print("2. Reservations")
    print("3. Menu")
    print("4. Inventory")
    print("5. Employees")
    print("6. Order")
    print("7. Exit")
    return input("Choose an option: ")

def customer_options():
    print("1. View Customers")
    print("2. Add Customer")
    print("3. Delete Customer")
    print("4. Update Customer")
    return input("Choose an option: ")

def do_customer_operation(choice):
    match choice:
        case "1":
            for row in read_customers():
                print(row)
        case "2":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            create_customer(name, email, phone)
            print("Customer added!")
        case "3":
            print("Not implemented.")
        case "4":
            print("Not implemented.")
        case _:
            return False
    return True
    
def reservation_options():
    print("1. View Reservations")
    print("2. Add Reservation")
    print("3. Delete Reservation")
    print("4. Update Reservation")
    return input("Choose an option: ")

def do_reservation_operation(choice):
    match choice:
        case "1":
            for row in read_reservations():
                print(row)
        case "2":
            cid = int(input("Customer_ID: "))
            time = input("Reservation Time: ")
            size = int(input("Party Size: "))
            status = input("Status: ")
            create_reservation(cid, time, size, status)
            print("Reservation added!")
        case "3":
            print("Not implemented.")
        case "4":
            print("Not implemented.")
        case _:
            return False
    return True
    
def menu_options():
    print("1. View Menu Items")
    print("2. Add Menu Item")
    print("3. Delete Menu Item")
    print("4. Update Menu Item")
    
    print("5. View Menu Item Ingredients")
    print("6. Add Menu Item Ingredient")
    print("7. Delete Menu Item Ingredient")
    
    return input("Choose an option: ")

def do_menu_operation(choice):
    match choice:
        case "1":
            for row in read_menu_items():
                print(row)
        case "2":
            name = input("Item Name: ")
            category = input("Category (Drink/Food/Dessert): ")
            price = float(input("Price: "))
            create_menu_item(name, category, price)
            print("Menu Item added!")
        case "3":
            id = input("Item ID: ")
            delete_menu_item(id)
            print("Menu Item deleted!")
        case "4":
            id = input("Item ID: ")
            name = input("Item Name: ")
            category = input("Category (Drink/Food/Dessert): ")
            price = float(input("Price: "))
            update_menu_item(id, name, category, price)
            print("Menu Item updated!")
        case "5":
            for row in read_menu_item_ingredients():
                print(row)
        case "6":
            menu_id = input("Item ID: ")
            ingredient_id = input("Ingredient ID: ")
            add_menu_item_ingredient(menu_id, ingredient_id)
            print("Menu Item Ingredient added!")
        case "7":
            menu_id = input("Item ID: ")
            ingredient_id = input("Ingredient ID: ")
            delete_menu_item_ingredient(menu_id, ingredient_id)
            print("Menu Item Ingredient deleted!")
        case _:
            return False
    return True
    
def inventory_options():
    print("1. View Inventory")
    print("2. Add Inventory Item")
    print("3. Delete Inventory Item")
    print("4. Update Inventory Item")
    return input("Choose an option: ")

def do_inventory_operation(choice):
    match choice:
        case "1":
            for row in read_inventory():
                print(row)
        case "2":
            name = input("Ingredient Name: ")
            qty = int(input("Quantity: "))
            status = input("Status: ")
            supplier = input("Supplier: ")
            create_inventory_item(name, qty, status, supplier)
            print("Inventory item added!")
        case "3":
            ingredient_id = input("Ingredient ID: ")
            delete_inventory(ingredient_id)
            print("Inventory item deleted!") 
        case "4":
            ingredient_id = input("Ingredient ID: ") 
            name = input("Name: ") 
            qty = input("Quantity: ")
            status = input("Status: ") 
            supplier = input("Supplier: ") 
            update_inventory(ingredient_id, name, qty, status, supplier) 
            print("Inventory Updated!") 
        case _:
            return False
    return True
    
def employee_options():
    print("1. View Employees")
    print("2. Add Employee")
    print("3. Delete Employee")
    print("4. Update Employee")
    return input("Choose an option: ")

def do_employee_operation(choice):
    match choice:
        case "1":
            for row in read_employees():
                print(row) 
        case "2":
            name = input("Name: ")
            salary = float(input("Salary: ")) 
            employment_type = input("Employment Type: ")
            job_title = input("Job Title: ")
            create_employee(name, salary, employment_type, job_title) 
            print("Employee Added!") 
        case "3":
            employee_id = input("Employee ID: ")
            delete_employee(name, employee_id) 
            print("Employee Deleted!")
        case "4":
            employee_id = input("Employee ID: ")
            salary = float(input("Salary: "))
            employment_type  = input("Employment Type: ")
            job_title = input("Job Title: ")
            update_employee(name, employee_id, salary, employment_type, job_title)
            print("Employee Updated: ")
        case _:
            return False
    return True

def order_options():
    print("1. Get All Orders")
    print("2. Add Order")
    print("3. Cancel Order")
    print("4. View Receipt")
    print("5. Update Order Status")
    return input("Choose an option: ")

def do_order_operation(choice):
    match choice:
        case "1":
            get_orders()
        case "2":
            add_order()
        case "3":
            cancel_order()
        case "4":
            receipt()
        case "5":
            update_order_status()
        case _: 
            return False
    return True


while True:
    main_option = main_options()
    valid = True
    
    match main_option:
        case "1":
            choice = customer_options()
            valid = do_customer_operation(choice)
        case "2":
            choice = reservation_options()
            valid = do_reservation_operation(choice)
        case "3":
            choice = menu_options()
            valid = do_menu_operation(choice)
        case "4":
            choice = inventory_options()
            valid = do_inventory_operation(choice)
        case "5":
            choice = employee_options()
            valid = do_employee_operation(choice)
        case "6":
            choice = order_options()
            valid = do_order_operation(choice)
        case "7":
            print("Goodbye!")
            break
        case _:
            valid = False
            
    if not valid:
        print("Invalid choice. Try again.")
