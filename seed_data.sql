-- Customers
INSERT INTO Customer (Name, Email, Phone) VALUES
('Alice Kim', 'alice@example.com', '555-1234'),
('Jamal Peterson', 'jamal@example.com', '555-5678'),
('Maria Lopez', 'maria@example.com', '555-9012');

-- Employees
INSERT INTO Employee (Salary, Employment_Type, Job_Title) VALUES
(18.50, 'Part-Time', 'Server'),
(22.00, 'Full-Time', 'Cook'),
(15.00, 'Part-Time', 'Host');

-- Menu Items
INSERT INTO Menu_Item (Name, Category, Price) VALUES
('Iced Latte', 'Drink', 4.90),
('Cheeseburger', 'Food', 9.50),
('Chocolate Cake', 'Dessert', 6.75);

-- Inventory
INSERT INTO Inventory (Ingredient_name, Ingredient_quantity, Ingredient_status, Ingredient_supplier) VALUES
('Milk', 40, 'In Stock', 'DairyCo'),
('Beef Patty', 20, 'Low Stock', 'MeatSupply'),
('Cocoa Powder', 15, 'In Stock', 'SweetFoods');

-- Reservations
INSERT INTO Reservation_Queue (Customer_ID, Reserv_time, Reserv_size, Reserv_status) VALUES
(1, '2025-12-01 18:00', 2, 'Pending');
