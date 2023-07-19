-- lists all genres from table and displays number of shows linked to each
-- list the genres
SELECT A.name AS genre,
COUNT(B.genre_id) AS number_of_shows
FROM tv_genres A
JOIN tv_show_genres B
ON A.id = genre_id
GROUP BY genre_id
ORDER BY number_of_shows DESC;
