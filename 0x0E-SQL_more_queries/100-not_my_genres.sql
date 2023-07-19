-- lists all genres not linked to the show Dexter
-- list shows
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN
(
	SELECT A.name, A.id
	FROM tv_genres A
	JOIN tv_show_genres B
	     ON A.id = B.genre_id
	JOIN tv_shows C
	     ON C.id = B.show_id
	WHERE C.title = 'Dexter'
	ORDER BY A.name ASC
) dexter_genre
ON dexter_genre.id = tv_genres.id
WHERE dexter_genre.id IS NULL
ORDER BY tv_genres.name;
