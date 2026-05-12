SELECT Account_ID, COUNT(*) AS Duplicate_Count
FROM Capital_Adequacy
GROUP BY Account_ID
HAVING COUNT(*) > 1;
