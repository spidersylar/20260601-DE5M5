import os 
import datetime 
import pandas as p
from sqlalchemy import create_engine

# Extract 
def load_data(data_dir="Data"):
    #Loads raw data 
    checkouts = p.read_csv(os.path.join(data_dir, '03_Library Systembook.csv'))
    customers = p.read_csv(os.path.join(data_dir, '03_Library SystemCustomers.csv'))
    return checkouts,customers 

def clean_customers(df):
    #takes the customers data and cleans it
    df_clean = df.dropna().copy()
    df_clean['Customer Name'] = df_clean['Customer Name'].astype(str).str.strip()
    df_clean['Customer ID'] = df_clean['Customer ID'].astype(int)
    return df_clean

def clean_checkouts(df):
    #takes the checkouts data and cleans it 
    # Remove completely empty rows and missing essential fields
    df_clean = df.dropna(how='all').copy()
    df_clean = df_clean.dropna(subset=['Id', 'Books', 'Customer ID'])
    
    # Strip spaces and literal quotes using regex
    df_clean['Books'] = df_clean['Books'].astype(str).str.strip()
    df_clean['Book checkout'] = df_clean['Book checkout'].astype(str).str.replace(r'["\']', '', regex=True).str.strip()
    df_clean['Book Returned'] = df_clean['Book Returned'].astype(str).str.replace(r'["\']', '', regex=True).str.strip()
    
    # Convert and validate dates
    df_clean['Book checkout_dt'] = p.to_datetime(df_clean['Book checkout'], format='%d/%m/%Y', errors='coerce')
    df_clean['Book Returned_dt'] = p.to_datetime(df_clean['Book Returned'], format='%d/%m/%Y', errors='coerce')
    df_clean = df_clean.dropna(subset=['Book checkout_dt', 'Book Returned_dt'])
    
    # Filter out future dates and logical chronological errors
    current_year = datetime.datetime.now().year
    df_clean = df_clean[df_clean['Book checkout_dt'].dt.year <= current_year]
    df_clean = df_clean[df_clean['Book Returned_dt'] >= df_clean['Book checkout_dt']]

    # calculate loan duration
    weeks = df_clean['Days allowed to borrow'].str.extract(r'(\d+)').astype(float).fillna(2)
    df_clean['Days Allowed'] = (weeks * 7).astype(int)
    df_clean['Actual Days Checked Out'] = (df_clean['Book Returned_dt'] - df_clean['Book checkout_dt']).dt.days
    df_clean['Exceeded Allowed Days'] = df_clean['Actual Days Checked Out'] > df_clean['Days Allowed']
    
    # Drop duplicates and cleanup types
    df_clean = df_clean.drop_duplicates(subset=['Books', 'Book checkout', 'Customer ID'])
    df_clean['Id'] = df_clean['Id'].astype(int)
    df_clean['Customer ID'] = df_clean['Customer ID'].astype(int)
    
    # Return with columns formatted matching original structure
    return df_clean.drop(columns=['Book checkout_dt', 'Book Returned_dt'])

def metrics(name,initial_count,final_count):
    # counts rows dropped
    dropped = initial_count - final_count
    print(f"Rows Dropped from {name}: {dropped}")

""" def load_to_csv(cust,checko):
    checko.to_csv('Data/Clean_CheckOuts.csv')
    cust.to_csv('Data/Clean_Customers.csv') """


def load_to_ssms(df,table_name,server_name=".",database_name="Library_Project"):
    #create connection to datanase
    connection_string =  f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    engine = create_engine(connection_string)

    #overwrite table if exists or creates if new
    df.to_sql(table_name,con=engine, if_exists='replace',index=False)


if __name__ == "__main__":
    #Extract Data
    raw_checkouts, raw_customers = load_data()

    #Transform Data
    clean_cust_df = clean_customers(raw_customers)
    clean_check_df = clean_checkouts(raw_checkouts)

    #Metrics
    metrics('Checkouts',len(raw_checkouts), len(clean_check_df))
    metrics('Customers',len(raw_customers), len(clean_cust_df))


    #Load to SSMS (WIP)
    #load_to_csv(clean_cust_df,clean_check_df)

    load_to_ssms(clean_cust_df, table_name="Customers", server_name=".", database_name="Library_Project")
    load_to_ssms(clean_check_df, table_name="Checkouts", server_name=".", database_name="Library_Project")