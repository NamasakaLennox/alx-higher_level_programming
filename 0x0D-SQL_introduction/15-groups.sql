-- Lists the number of records with the same score in the table
-- displays the score and the number of records with the score
SELECT score, COUNT(*) FROM second_table GROUP BY score;
