import sys
import os
import sqlite3
import pandas as pd

# =================== Add directory to path so we can import scripts.* ===================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # It is to use Scripts as a package, saved the ETL in memory

from scripts.data_etl import clean_data

file_path = './datasets/sample_datasets.xlsx'
customers, applications, stores, marketing = clean_data(file_path)

# =================== Create SQLite DB in memory ===================
conn = sqlite3.connect(':memory:')

customers.to_sql("customers", conn, index=False, if_exists="replace")
applications.to_sql("applications", conn, index=False, if_exists="replace")
stores.to_sql("stores", conn, index=False, if_exists="replace")
marketing.to_sql("marketing", conn, index=False, if_exists="replace")

# =================== Create unified dataset ===================
query = """
    SELECT 
        a.application_id,
        a.customer_id,
        a.store,
        a.submit_date,
        a.approved,
        a.approved_date,
        a.approved_amount,
        a.dollars_used,
        a.lease_grade,
        c.first_name,
        c.last_name,
        c.DOB AS date_of_birth,
        c.email,
        c.phone_number,
        c.language,
        c.income,
        c.title,
        c.campaign AS campaign_id,
        s.start_dt AS store_start_dt,
        s.state,
        s.size,
        s.industry,
        m.name AS marketing_name,
        m.spend AS marketing_spend,
        m.start_date AS marketing_start_dt,
        m.end_date AS marketing_end_dt,
        1 AS applications,
        CASE WHEN a.dollars_used IS NOT NULL THEN 1 ELSE 0 END AS used_apps
    FROM applications a
    LEFT JOIN customers c ON a.customer_id = c.customer_id
    LEFT JOIN marketing m ON c.campaign = m.id
    LEFT JOIN stores s ON a.store = s.store
"""

df_unified = pd.read_sql_query(query, conn)

date_cols = [
    'submit_date', 'approved_date', 'date_of_birth', 'store_start_dt', 'marketing_start_dt', 'marketing_end_dt'
]

for col in date_cols:
    if col in df_unified.columns:
        df_unified[col] = pd.to_datetime(df_unified[col], errors='coerce')

print('Unified dataset result')
df_unified.info()
df_unified.head()

# =================== Save Output dayaset ===================
output_path = "outputs/final_dataset_sqlite.xlsx"
os.makedirs("outputs", exist_ok=True)
df_unified.to_excel(output_path, index=False)
print(f"\nFinal dataset saved to: {output_path}")