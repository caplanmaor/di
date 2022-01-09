-- creating the tables

CREATE TABLE items (
	name varchar,
	price float
)

CREATE TABLE customers (
	name varchar
)

INSERT INTO items 
VALUES ('Small Desk', 100)
VALUES ('Large Desk', 300)
VALUES ('Fan', 80)

INSERT INTO customers
VALUES ('Greg Jones')
VALUES ('Sandra Jones')
VALUES ('Scott Scott')
VALUES ('Trevor Green')
VALUES ('Melanie Johnson')

-- all the items
SELECT * FROM customers, items

-- All the items with a price above 80 (80 not included).
SELECT * FROM items WHERE price > 80;

-- All the items with a price below 300. (300 included)
SELECT * FROM items WHERE price <= 300;

-- All smith customers (the outcome is none)
SELECT * FROM customers WHERE name = 'Smith'

-- names that end with jones
SELECT * FROM customers WHERE name LIKE '%Jones'

-- not scott
SELECT * FROM customers WHERE name NOT LIKE 'Scott%'