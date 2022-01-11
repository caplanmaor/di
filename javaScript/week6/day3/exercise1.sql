-- 1. Get a list of all film languages.
SELECT language.name FROM language
INNER JOIN film ON film.language_id = language.language_id
GROUP BY language.name

-- 2. Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
Get all films, even if they don’t have languages.
Get all languages, even if there are no films in those languages.
SELECT film.title,film.description,language.name FROM language
RIGHT JOIN film ON film.language_id = language.language_id
-- this is for all languages even if no films
SELECT film.title,film.description,language.name FROM language
LEFT JOIN film ON film.language_id = language.language_id

-- 3.Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film (
	id SERIAL PRIMARY KEY,
	name VARCHAR
)
INSERT INTO new_film (name)
VALUES ('Star Wars'), ('The Matrix'), ('Kong Fu Panda');

-- 4.Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted.
-- It should have the following columns:
-- 1. review_id – a primary key, non null, auto-increment.
-- 2. film_id – references the new_film table. The film that is being reviewed.
-- 3. language_id – references the language table. What language the review is in.
-- 4. title – the title of the review.
-- 5. score – the rating of the review (1-10).
-- 6. review_text – the text of the review. No limit on the length.
-- 7. last_update – when the review was last updated.

CREATE TABLE costumer_review (
	review_id SERIAL PRIMARY KEY NOT NULL,
	film_id INT REFERENCES new_film (id) ON DELETE CASCADE ON UPDATE CASCADE,
	language_id INT REFERENCES language (language_id) ON DELETE CASCADE ON UPDATE CASCADE,
	title VARCHAR,
	score INT,
	review_text VARCHAR,
	last_update date
)

-- 5. Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO costumer_review (film_id,language_id,title,score,review_text,last_update)
VALUES(1,3,'a good family movie',7,'the effects were awesome but i could not understand the characters', NOW())
VALUES(2,1,'i didnt like it',3,'this new movie is not as good as the old ones in the franchise', NOW())

-- 6.Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE id=2
-- the review was deleted because of CASCADE