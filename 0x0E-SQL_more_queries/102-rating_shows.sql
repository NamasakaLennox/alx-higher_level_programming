-- lists all shoes from a database by their ratings
-- list the shows
SELECT A.title, SUM(B.rate) AS rating
FROM tv_shows A
JOIN tv_show_ratings B
ON A.id = B.show_id
GROUP BY B.show_id
ORDER BY rating DESC;
