# BI Engineer Take-Home Assessment
This repository contains the files used for the BI Engineer I - Take Home Assessment

This project demonstrates my ability to work with raw data, apply SQL and Python-based ETL logic, generate insights, and present them using Tableau dashboards.

### Project Overview
The goal of this assessment is to process a set of business-related data tables and derive insights through analytics, code, and visualization. I focused on writing clean, efficient, and reproducible code, as well as creating a stakeholder-friendly dashboard.

### Tools and Technologies used
- **Visual Studio Code** - 
    - **Python (Pandas, SQLite)** – Data loading, transformation, and merging.
    - **SQL** – Joins and logic simulation via SQLite.
    - **Excel/CSV** – Final data format for Tableau
- **Tableau** – Final storytelling and data visualization.

### Project Folders and Files
    datasets/
        sample_datasets.xlsx
    outputs/
        final_dataset_python.xlsx
        final_dataset_sqlite.xlsx
    scripts/
        data_etl.py
        generate_unified_pandas.py
        generate_unified_sqlite.py
    BI Engineer Assessment Analysis.twbx
    README.md
    requirements.txt

### Project Structure

1. Data Extraction and Cleaning (data_etl.py)
- Loaded the original dataset from excel, saving each data sheet into a dataframe.
- Converted date fields to use the right data type.
2. Generate Unified datasets (Python and SQLite)
- Created two versions of joining the data into one single dataset for the final usage, using Pandas and SQL inside SQLite.
- Added binary columns to count applications, approvals and used applications for the Tableau analysis, as it helps to create complex calculations in Tableau, or for future blending data sources.
3. Tableau Dashboard
- Built visualizations aligned with the assessment tasks for the presentation to Stakeholders.
- Include trends over time, store-level insights, marketing impact and custom insights.

### Notes for Reviewers
- The dataset was created in a Python function to allow flexible and multiple usage in both Python and SQL pipelines.
- The Tableau workbook is conected to the unified output final_dataset_sqlite.xlsx
- I used SQLite for the SQL version to simulate joins similar to what we do in a production BI pipeline.

### How to Run
1. Install / import dependencies:
    pandas
    sys
    os
    sqlite3
