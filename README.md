ETL Pipeline with Data Quality Implementation on Finance

Overview
This project demonstrates an end-to-end ETL pipeline for Basel III financial risk reporting,
with integrated Data Quality functions mapped across ETL stages. It covers:
- Business Requirements (BRS)
- Functional Specification (FS)
- Installation Guideline
- Schema Guideline
- Automation Guideline
- Dashboard Guideline

Deliverables include ETL scripts, SQL schema, sample data, visualization layer, and documentation.

Project Structure
etl-financial-risk/
│  basel_demo.db
│  requirements.txt
│  README.md
│
├─dashboard/
│      app.py
│      main_dashboard.py
│
├─docs/
│      ETL Pipeline for Financial Risk Data (BRS).docx
│      ETL Pipeline for Financial Risk Data (FS).docx
│      ETL Pipeline for Financial Risk Data (Installation Guideline).docx
│      ETL Pipeline for Financial Risk Data (Schema Guideline).docx
│      ETL Pipeline for Financial Risk Data (Automation Guideline).docx
│      ETL Pipeline for Financial Risk Data (Dashboard Guideline).docx
│
├─etl_scripts/
│      run_pipeline.py
│      stress_test.py
│      basel_ratios.csv
│      Basel_Test_Dataset.csv
│      validation_report.txt
│      (supporting ETL + DQ scripts)
│
└─sql_schema/
       init_db.py
       load_sample_data.py
       capital_adequacy_schema.sql
       schema_completeness.sql

Deliverables
- ETL scripts with logging and validation
- Basel III ratio automation modules
- Schema definitions and test cases
- Visualization Layer (Static + Streamlit)
  - main_dashboard.py → static matplotlib visualization of Basel III ratios from CSV
  - app.py → simple Streamlit app for browser-based viewing (non-interactive)
- Documentation in /docs (BRS, FS, Installation, Schema, Automation, Dashboard)

Key Reference
The most detailed documentation is in the Schema Guideline Document:

docs/ETL Pipeline for Financial Risk Data (Schema Guideline).docx

This file includes the mapping:

ETL Stages → ETL Functions → DQ Functions → DQ Dimensions → Case Mapping → FS Items

It provides the structured link between ETL processes and data quality checks.
For anyone interested in the technical design and test plan, please refer to this document.
