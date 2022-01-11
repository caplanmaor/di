-- CREATE TABLE customer
-- (
-- id SERIAL PRIMARY KEY NOT NULL,
-- name VARCHAR,
-- email VARCHAR
-- )

-- CREATE TABLE customer_profile
-- (
-- id SERIAL PRIMARY KEY NOT NULL,
-- passport_number VARCHAR
-- )

-- INSERT INTO customer (name, email)
-- VALUES ('maor','caplanmaor@gmail.com'),('obama','obama@gmail.com')

-- INSERT INTO customer_profile (passport_number)
-- VALUES (31468), (67845)

-- ALTER TABLE customer
-- ADD passport_id int;

-- UPDATE customer SET passport_id=1 WHERE customer.name='obama'

SELECT customer.name,customer_profile.passport_number FROM customer
INNER JOIN customer_profile ON customer_Profile.id = customer.passport_id
WHERE name='maor'