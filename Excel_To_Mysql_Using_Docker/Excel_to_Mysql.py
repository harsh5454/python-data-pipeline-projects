import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Step 1: Read Excel file
df = pd.read_excel("sales_data.xlsx", engine='openpyxl')

# Step 2: Connect to MySQL using SQLAlchemy + pymysql
engine = create_engine("mysql+pymysql://sales_user:salespass@localhost:3307/sales_db")

# Step 3: Insert into MySQL
df.to_sql(name='sales', con=engine, if_exists='replace', index=False)

print("✅ Excel data successfully inserted into MySQL!")
