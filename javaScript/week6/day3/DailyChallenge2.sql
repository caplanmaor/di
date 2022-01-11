

-- CREATE TABLE product (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR
-- )

-- INSERT INTO product (name)
-- VALUES ('Donut'), ('Bagel')

-- CREATE TABLE order_junction (
-- 	customer_id INT NOT NULL REFERENCES customer(id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	product_id INT NOT NULL REFERENCES product(id) ON DELETE CASCADE ON UPDATE CASCADE
-- )

-- INSERT INTO order_junction (product_id, customer_id)
-- VALUES ((SELECT product.id FROM product WHERE name='Donut'),(SELECT customer.id FROM customer WHERE name='maor'))


-- SELECT * FROM product

SELECT product.name,customer.name FROM product
INNER JOIN order_junction ON order_junction.product_id = product.id
INNER JOIN customer ON customer.id = order_junction.customer_id
WHERE customer.name = 'maor'