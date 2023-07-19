-- uses the database to list all genres of the show Dexter
-- list the names
SELECT A.name
FROM tv_genres A
JOIN tv_show_genres B
ON A.id = B.genre_id
JOIN tv_shows C
ON C.id = B.show_id
WHERE C.title = 'Dexter'
ORDER BY A.name ASC;
