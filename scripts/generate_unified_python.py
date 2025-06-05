import sys
import os
import pandas as pd

# =================== Add directory to path so we can import scripts.* ===================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # It is to use Scripts as a package, saved the ETL in memory

from scripts.data_etl import clean_data

file_path = './datasets/sample_datasets.xlsx'
customers, applications, stores, marketing = clean_data(file_path)

# =================== Create unified dataset ===================
for df in [customers, applications, stores, marketing]:
        unnamed_cols = [col for col in df.columns if 'Unnamed' in col]
        df.drop(columns=unnamed_cols, inplace=True)

df_unified = applications.merge(customers, on='customer_id', how='left')
df_unified = df_unified.merge(stores, on='store', how='left', suffixes=('', '_store'))
df_unified = df_unified.merge(marketing, left_on='campaign', right_on='id', how='left', suffixes=('', '_marketing'))

df_unified["applications"] = 1
df_unified["approvals"] = df_unified["approved"].apply(lambda x: 1 if x == 1 else 0)
df_unified["used_apps"] = df_unified["dollars_used"].notnull().astype(int)

print('Unified dataset result')
df_unified.info()
df_unified.head()

find_duplicate_app_id = df_unified[df_unified.duplicated(subset='application_id', keep=False)]
print(f"\nDuplicate application_id rows: {len(find_duplicate_app_id)}")
if not find_duplicate_app_id.empty:
    print(find_duplicate_app_id[['application_id', 'customer_id', 'submit_date']].head())

# =================== Save Output dayaset ===================
output_path = "outputs/final_dataset_python.xlsx"
os.makedirs("outputs", exist_ok=True)
df_unified.to_excel(output_path, index=False)
print(f"\nFinal dataset saved to: {output_path}")