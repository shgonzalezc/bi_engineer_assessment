import pandas as pd

def clean_data(file_path):

    customers = pd.read_excel(file_path, sheet_name='customers')
    applications = pd.read_excel(file_path, sheet_name='applications')
    stores = pd.read_excel(file_path, sheet_name='stores')
    marketing = pd.read_excel(file_path, sheet_name='marketing')

    customers['DOB'] = pd.to_datetime(customers['DOB'])
    applications['submit_date'] = pd.to_datetime(applications['submit_date'])
    applications['approved_date'] = pd.to_datetime(applications['approved_date'])
    stores['start_dt'] = pd.to_datetime(stores['start_dt'])
    marketing['start_date'] = pd.to_datetime(marketing['start_date'])
    marketing['end_date'] = pd.to_datetime(marketing['end_date'])

    return customers, applications, stores, marketing


file_path = './datasets/sample_datasets.xlsx'
customers, applications, stores, marketing = clean_data(file_path)

print('Customers')
customers.info()
print('\nApplications')
applications.info()
print('\nStores')
stores.info()
print('\nMarketing')
marketing.info()