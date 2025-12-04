-- Customers
INSERT INTO Customer (Name, Email, Phone) VALUES
('Alice Kim', 'alice@example.com', '555-1234'),
('Jamal Peterson', 'jamal@example.com', '555-5678'),
('Maria Lopez', 'maria@example.com', '555-9012');

-- Employees
INSERT INTO Employee (Name, Salary, Employment_Type, Job_Title) VALUES
('Alexander Farell', 18.50, 'Part-Time', 'Server'),
('Isabella Martinez', 22.00, 'Full-Time', 'Cook'),
('Lucas Henderson', 15.00, 'Part-Time', 'Host');

-- Menu Items
INSERT INTO Menu_Item (Name, Category, Price) VALUES
('Iced Latte', 'Drink', 4.90),
('Cheeseburger', 'Food', 9.50),
('Chocolate Cake', 'Dessert', 6.75);

-- Orders
INSERT INTO Order_Table (Customer_ID, Employee_ID, Order_Status, Order_Date, Total_Amount) VALUES
(1, 1, 'Finished', datetime('now', '-1 hour'), 19.30),        
(2, 1, 'Preparing', datetime('now', '-40 minutes'), 11.65), 
(3, 1, 'Queue', datetime('now', '-20 minutes'), 15.40);

-- Order Items
INSERT INTO Order_Item (Order_ID, MenuItem_ID, Quantity) VALUES
(1, 1, 2), (1, 2, 1),  
(2, 3, 1), (2, 1, 1), 
(3, 2, 1), (3, 3, 1);  

-- Inventory
INSERT INTO Inventory (Ingredient_name, Ingredient_quantity, Ingredient_status, Ingredient_supplier) VALUES
('Milk', 40, 'In Stock', 'DairyCo'),
('Beef Patty', 20, 'Low Stock', 'MeatSupply'),
('Cocoa Powder', 15, 'In Stock', 'SweetFoods');

-- Reservations
INSERT INTO Reservation_Queue (Customer_ID, Reserv_time, Reserv_size, Reserv_status) VALUES
(1, '2025-12-01 18:00', 2, 'Pending');

-- Uses
INSERT INTO Uses (MenuItem_ID, Ingredient_ID) VALUES
(2, 2),
(1, 1),
(1, 3),
(3, 1),
(3, 3);
