-- lists all the cities of california that can be found in the database
-- select the cities in California
SELECT id, name
FROM cities
WHERE state_id = ( -- get the id of California
      SELECT id
      FROM states
      WHERE name = 'California')
ORDER BY id ASC;
