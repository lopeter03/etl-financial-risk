-- File: schema_completeness.sql
-- Completeness check for Capital_Ratio

SELECT Account_ID, Currency, CET1_Ratio, LCR, Bucket, Date
FROM Capital_Adequacy
WHERE Capital_Ratio IS NULL OR Capital_Ratio = '';
