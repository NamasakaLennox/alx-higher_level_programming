-- displays maximum temperature of each state
-- list the maximum temperatures
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
