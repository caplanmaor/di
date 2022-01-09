<!-- INSTRUCTIONS -- Questions -->

-- 1. Select everything from the table. (every row and columns) - How many records does the table have?
SELECT * FROM city_info;

-- 2. What was Bostons temperature on the 01/03/2015 at 11am ?
SELECT * FROM city_info WHERE city = 'Boston' AND event_datetime LIKE '2015-03-01T11%';

-- 3. When (ie. days and hours) was the temperature between 28 and 30 degrees in San Francisco ? 
SELECT * FROM city_info WHERE city='San Francisco' AND temperature > '28' AND temperature < '30';

-- 4. Which city was the most noisy (show the name of the city, the date and the noise index)? - Don't use the MAX function
SELECT city, event_datetime, sound FROM city_info ORDER BY sound DESC LIMIT 1;

-- 5. Which city was the least noisy (show the name of the city, the date and the noise index)? - Don't use the MIN function
SELECT city, event_datetime, sound FROM city_info ORDER BY sound ASC LIMIT 1;

-- 6. Show the dust index of San Francisco on the 26/03/2015 after 20:00.
SELECT dust FROM city_info WHERE city = 'San Francisco' AND event_datetime LIKE '2015-03-26T2%';

-- 7. When (ie. days and hours) is the humidity index less that 40 or more than 60 in Geneva?
SELECT event_datetime FROM city_info WHERE city = 'Geneva' AND humidity < 60 AND humidity > 40;

-- 8. Where and when (Find the day (Sunday-Saturday)) is the light index the highest? - Use an alias for the day of the week.

-- 9. Select only the info of the cities that start with an "S" (uppercase or lowercase). - Look at the DISTINCT constraint.

-- 10. Add to the table, todays information in Israel - of this very hour. 
(timestamp,city,temperature,light,airquality_raw,sound,humidity,dust)
-- - Use the return statement to see what you just inserted: 

https://www.postgresqltutorial.com/postgresql-insert/