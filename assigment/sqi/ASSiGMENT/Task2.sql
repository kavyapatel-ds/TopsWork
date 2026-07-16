CREATE TABLE customer12 (
cust_id INT PRIMARY KEY,
    cust_name VARCHAR(50),
    city VARCHAR(50),
    email VARCHAR(100),
    join_date DATE
);

CREATE TABLE products12(
    prod_id INT PRIMARY KEY,
    prod_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock INT
);

CREATE TABLE orders12 (
    order_id INT PRIMARY KEY,
    cust_id INT,
    order_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (cust_id) REFERENCES customer12(cust_id)
);


CREATE TABLE order_items12 (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    prod_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders12(order_id),
    FOREIGN KEY (prod_id) REFERENCES products12(prod_id)
);
-- Customers

INSERT INTO customer12 VALUES
(1, 'amit Sharma', 'Delhi', 'amit@gmail.com', '2022-01-15'),
(2, ' kavya patel', 'Mumbai', 'kavya@gmail.com', '2005-11-18'),
(3, 'riya panchal', 'Ahmedabad', 'riya@gmail.com', '2023-07-22'),
(4, 'hani patel', 'Mumbai', 'hani@gmail.com', '2024-01-05'),
(5, 'masum patel', 'Delhi', 'masum@gmail.com', '2023-08-19');

select * from customer12;
-- Products

INSERT INTO products12 VALUES
(101, 'Laptop', 'Electronics', 65000, 50),
(102, 'Headphones', 'Electronics', 2000, 100),
(103, 'Mobile', 'Electronics', 30000, 30),
(104, 'Chair', 'Furniture', 5000, 20),
(105, 'Table', 'Furniture', 8000, 15),
(106, 'Monitor', 'Electronics', 12000, 8);

select * from products12;

-- orders

INSERT INTO orders12 VALUES
(1001, 1, '2024-05-20', 'Delivered'),
(1002, 2, '2024-08-10', 'Delivered'),
(1003, 3, '2024-08-15', 'Cancelled'),
(1004, 1, '2024-09-01', 'Delivered'),
(1005, 4, '2024-07-21', 'Delivered'),
(1006, 5, '2024-08-05', 'Delivered');

select * from  orders12;

-- order_items

INSERT INTO order_items12 VALUES
(1, 1001, 101, 1),
(2, 1002, 102, 2),
(3, 1002, 103, 1),
(4, 1003, 104, 1),
(5, 1004, 101, 1),
(6, 1004, 102, 3),
(7, 1005, 105, 2),
(8, 1006, 106, 1);

select * from order_items12;

-- basic level
-- Show all customers who live in Mumbai.
select * from customer12 where city='Mumbai';

-- Display names of all products in the “Electronics” category.
select * from products12 where category='Electronics';

-- List all orders that were delivered
SELECT * FROM orders12 WHERE status = 'Delivered';

-- Find customers who joined after January 2023.
SELECT * FROM customer12 WHERE join_date > '2023-01-01';

-- Display products whose price is greater than ₹10,000.
select * from products12 where price > 10000;

-- Show the total number of customers.
select count(*) from customer12;

-- Display product names with their stock quantity.
 select prod_name, stock FROM products12;
 
 -- List orders placed August 2024 orders
select  * FROM orders12 where month(order_date) = 8 and year(order_date) = 2024;

-- Show customers whose  Name starts with S
select  * from customer12 where cust_name like 'S%';

--   Display Cheapest product
select * from products12 order by price asc limit 1;

-- 2.Intermediate Level
-- Count how many orders each customer has placed.
select cust_id, count(order_id) from orders12 group by cust_id;

-- Count how many orders each customer has placed
select  order_id, sum(quantity) from order_items12 group by order_id;
 
-- Show each customer’s name and the total value of their delivered orders.
SELECT c.cust_name, SUM(p.price * oi.quantity) AS total_value
FROM customer c
JOIN orders12 o ON c.cust_id = o.cust_id
JOIN order_items12 oi ON o.order_id = oi.order_id
JOIN products12 p ON oi.prod_id = p.prod_id
WHERE o.status = 'Delivered'
GROUP BY c.cust_name;

-- Display the most expensive product in each category.
select category, max(price) from products12 group by  category;

-- Find customers who have never placed an order.
select * from customer12 where  cust_id  not  in (select cust_id from orders);

-- Show total sales (price × quantity) of each product.
SELECT p.prod_name, SUM(p.price * oi.quantity)FROM products p
JOIN order_items11 oi ON p.prod_id = oi.prod_id GROUP BY p.prod_name;

-- List all products that have been ordered more than 2 times.
 select sum(quantity) from order_items12 group by prod_id having sum(quantity)>2;
 
 -- Find the total revenue generated in 2024.
 SELECT SUM(p.price * oi.quantity) FROM orders o
JOIN order_items12  oi  ON o.order_id = oi.order_id
JOIN products12 p ON oi.prod_id = p.prod_id
WHERE YEAR(o.order_date) = 2024;

-- Display all orders along with customer names and order status.
select o.order_id, c.cust_name, o.status from orders12 o join customer12 c on o.cust_id = c.cust_id;

--  Show the number of “Delivered” vs “Cancelled” orders.
select status, count(*) from orders12 group by status;

-- Advanced Level
-- Find the top 3 customers with the highest total spending
SELECT c.cust_id,c.cust_name,
SUM(oi.quantity * p.price) AS total_spending
FROM customer12 c
JOIN orders12 o ON c.cust_id = o.cust_id
JOIN order_items12 oi ON o.order_id = oi.order_id
JOIN product12 p ON oi.prod_id = p.prod_id
GROUP BY c.cust_id, c.cust_name
ORDER BY total_spending DESC
LIMIT 3;

-- Display the product categories ranked by total sales.
select p.category, SUM(p.price * oi.quantity) as total_sales
from products12 p
join order_items12 oi ON p.prod_id = oi.prod_id
group by p.category
order by total_sales desc;

-- Find customers who have purchased both “Laptop” and “Headphones”.
SELECT c.cust_name
FROM customer12 c
JOIN orders12 o ON c.cust_id = o.cust_id
JOIN order_items12 oi ON o.order_id = oi.order_id
JOIN products12 p ON oi.prod_id = p.prod_id
WHERE p.prod_name IN ('Laptop', 'Headphones')
GROUP BY c.cust_name
HAVING COUNT(DISTINCT p.prod_name) = 2;

-- Show products that were never ordered.
select* FROM products12  where  prod_id not in (SELECT prod_id FROM order_items);

-- Find orders with multiple products from different categories.
SELECT o.order_id
FROM orders12 o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products12 p ON oi.prod_id = p.prod_id
GROUP BY o.order_id
HAVING COUNT(DISTINCT p.category) > 1;

-- Calculate each month’s total revenue and show a running total
SELECT MONTH(o.order_date) AS month,
SUM(p.price * oi.quantity) AS revenue,
SUM(SUM(p.price * oi.quantity)) OVER (ORDER BY MONTH(o.order_date)) AS running_total
FROM orders12 o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products12 p ON oi.prod_id = p.prod_id
GROUP BY MONTH(o.order_date);

-- Display the average order value per customer.
SELECT c.cust_name, AVG(p.price * oi.quantity)
FROM customer12 c
JOIN orders12 o ON c.cust_id = o.cust_id
JOIN order_items12 oi ON o.order_id = oi.order_id
JOIN products12 p ON oi.prod_id = p.prod_id
GROUP BY c.cust_name;

-- Show the most frequently ordered product.
SELECT p.prod_name, SUM(oi.quantity) AS total_qty
FROM products12 p
JOIN order_items12 oi ON p.prod_id = oi.prod_id
GROUP BY p.prod_name
ORDER BY total_qty DESC
LIMIT 1;

-- List customers who placed orders in at least 3 different months.
SELECT c.cust_name
FROM customer12 c
JOIN orders12 o ON c.cust_id = o.cust_id
GROUP BY c.cust_name
HAVING COUNT(DISTINCT MONTH(o.order_date)) >= 3;

-- Find products that are out of stock or nearly out of stock (less than 10 units)
SELECT * FROM products12 WHERE stock < 10;