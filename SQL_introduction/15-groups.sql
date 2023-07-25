-- a script that lists the number of records with the same score in second_table
-- should display score, num of records for this score, with label 'number'
-- list should be sorted by number, descending
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;
