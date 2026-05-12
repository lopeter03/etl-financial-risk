DROP TABLE IF EXISTS Capital_Adequacy;

CREATE TABLE Capital_Adequacy (
    Account_ID VARCHAR(10),
    Currency VARCHAR(20),
    CET1_Ratio DECIMAL(5,2),
    LCR DECIMAL(5,2),
    Capital_Ratio DECIMAL(5,2),
    Bucket VARCHAR(20),
    Ledger_Value DECIMAL(5,2),
    Date DATE
);
