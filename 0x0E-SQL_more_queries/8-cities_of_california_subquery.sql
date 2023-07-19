-- lists all the cities of california that can be found in the database
-- select the cities in California
SELECT cities.id, cities.name
FROM cities, states
WHERE states.name='California'
ORDER BY cities.id ASC;
