-- List number of records with same score in second_table of hbtn_0c_0
SELECT score, count(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
