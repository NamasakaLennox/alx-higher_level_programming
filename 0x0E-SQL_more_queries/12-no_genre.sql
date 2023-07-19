-- lists all shows contained in table without a genre linked
-- list the shows
SELECT A.title, B.genre_id
FROM tv_shows A
LEFT JOIN tv_show_genres B
ON A.id = B.show_id
WHERE B.genre_id IS NULL
ORDER BY A.title ASC, B.genre_id ASC;
