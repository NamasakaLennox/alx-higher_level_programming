-- shows all shows without the genre comedy in  the database
-- select shows
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN
(
	SELECT C.title, C.id
	FROM tv_genres A
	JOIN tv_show_genres B
	     ON A.id = B.genre_id
	JOIN tv_shows C
	     ON C.id = B.show_id
	WHERE A.name = 'Comedy'
	ORDER BY C.title ASC
) comedy
ON comedy.id = tv_shows.id
WHERE comedy.id IS NULL
ORDER BY tv_shows.title ASC;
