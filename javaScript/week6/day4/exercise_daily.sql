-- 1. Create a table called orders and a table called items. 
-- You decide which fields should be in each table, 
-- although make sure the items table has a column called price.
-- 2. There should be a one to many relationship between the orders 
-- table and the items table. An order can have many items, 
-- but an item can belong to only one order.

-- CREATE TABLE items (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR
-- )

-- CREATE TABLE orders (
-- 	id SERIAL PRIMARY KEY,
-- 	customer_name VARCHAR,
-- 	table_num INT,
-- 	item_id INT REFERENCES items (id)
-- )

-- INSERT INTO items (name)
-- VALUES ('salmon')

-- INSERT INTO orders (customer_name, table_num, item_id)
-- VALUES ('zohar', 2, 1)

-- INSERT INTO orders (customer_name, table_num, item_id)
-- VALUES ('maor', 5, 2)

-- SELECT * FROM orders

-- UPDATE items
-- SET price = 19.99 WHERE name = 'salmon'

-- 3. Create a function that returns the total price for a given order.

CREATE FUNCTION total_price (orderCust_name VARCHAR)
RETURNS INTEGER
LANGUAGE plpgsql
AS
$func$
DECLARE
	total INTEGER;
BEGIN
	SELECT total = SUM(SELECT items.price FROM items 
   INNER JOIN orders ON orders.item_id = items.id
   WHERE orders.customer_name = orderCust_name)
-- 	RETURNING total INTO total;
	RETURN total;
END;
$func$

