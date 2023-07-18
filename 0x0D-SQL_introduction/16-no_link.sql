-- Lists all records of the table second_table except rows without a name value
-- display score and name in that order in descending score
SELECT score, name FROM second_table WHERE name != "NULL" ORDER BY score DESC;
