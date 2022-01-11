-- 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE costumer_review SET language_id = 2 WHERE language_id = 3

-- 2. Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- we have a foreign key called store_id, when we insert into this table we need to choose a store_id which is viable and exists on the store table as a store id

-- 5. Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT film.title,film.replacement_cost,rental.return_date FROM film
INNER JOIN inventory ON inventory.film_id = film.film_id
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
WHERE rental.return_date IS NULL ORDER BY film.replacement_cost DESC LIMIT 30

-- 6.Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- 1.The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT film.title FROM film 
INNER JOIN film_actor ON film_actor.film_id = film.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE description LIKE '%Sumo%' 
AND actor.first_name = 'Penelope' AND actor.last_name = 'Monroe'

-- 2.he 2nd film : A short documentary (less than 1 hour long), rated “R”
SELECT film.title FROM film 
WHERE length < 60 
AND rating = 'R' 
AND description LIKE '%Documentary%'

-- 3.The 3rd film : A film that his friend Matthew Mahan rented. 
-- He paid over $4.00 for the rental, and he returned it 
-- between the 28th of July and the 1st of August, 2005.
SELECT film.title FROM film 
INNER JOIN inventory ON inventory.film_id = film.film_id
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
INNER JOIN customer ON customer.customer_id = rental.customer_id
WHERE rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'  
AND film.rental_rate > 4.00
AND customer.first_name = 'Matthew'

-- 4. The 4th film : His friend Matthew Mahan watched this film, 
-- as well. It had the word “boat” in the title or description, 
-- and it looked like it was a very expensive DVD to replace.
SELECT film.title, film.replacement_cost FROM film 
INNER JOIN inventory ON inventory.film_id = film.film_id
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
INNER JOIN customer ON customer.customer_id = rental.customer_id
WHERE film.title LIKE '%Boat%' OR film.description LIKE '%Boat%'
AND customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
ORDER BY film.replacement_cost DESC
