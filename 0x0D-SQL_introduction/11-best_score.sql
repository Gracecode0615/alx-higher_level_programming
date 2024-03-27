-- lists all records with a score >= 10 in table
--  second_table of the database hbtn
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
