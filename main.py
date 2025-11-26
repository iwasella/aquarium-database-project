from crud import *

def menu():
    print("\n==== RESTAURANT DATABASE ====")
    print("1. View Customers")
    print("2. Add Customer")
    print("3. View Reservations")
    print("4. Add Reservation")
    print("5. View Menu Items")
    print("6. Add Menu Item")
    print("7. View Inventory")
    print("8. Add Inventory Item")
    print("9. Exit")
    return input("Choose an option: ")


while True:
    choice = menu()

    # Customers
    if choice == "1":
        for row in read_customers():
            print(row)

    elif choice == "2":
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        create_customer(name, email, phone)
        print("Customer added!")

    # Reservations
    elif choice == "3":
        for row in read_reservations():
            print(row)

    elif choice == "4":
        cid = int(input("Customer_ID: "))
        time = input("Reservation Time: ")
        size = int(input("Party Size: "))
        status = input("Status: ")
        create_reservation(cid, time, size, status)
        print("Reservation added!")

    # Menu Items
    elif choice == "5":
        for row in read_menu_items():
            print(row)

    elif choice == "6":
        name = input("Item Name: ")
        category = input("Category (Drink/Food/Dessert): ")
        price = float(input("Price: "))
        create_menu_item(name, category, price)
        print("Menu Item added!")

    # Inventory
    elif choice == "7":
        for row in read_inventory():
            print(row)

    elif choice == "8":
        name = input("Ingredient Name: ")
        qty = int(input("Quantity: "))
        status = input("Status: ")
        supplier = input("Supplier: ")
        create_inventory_item(name, qty, status, supplier)
        print("Inventory item added!")

    # Exit
    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
