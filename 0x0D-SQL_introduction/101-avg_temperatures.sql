-- display average temperatures ordered by temperature
-- diplay averages
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
