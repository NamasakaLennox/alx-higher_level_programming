-- lists all genres by their ratings
-- list genres
SELECT A.name, SUM(D.rate) as rating
FROM tv_genres A
JOIN tv_show_genres B
     ON B.genre_id = A.id
JOIN tv_shows C
     ON C.id = B.show_id
JOIN tv_show_ratings D
     ON C.id = D.show_id
GROUP BY A.name
ORDER BY rating DESC;
