import pandas as pd
import sqlite3

# Step 1: Read the CSV file
df = pd.read_csv("historical_stock.csv")
print("CSV Loaded:")
print(df.head())

# Step 2: Connect to SQLite database
conn = sqlite3.connect("stock_data.db")

# Step 3: Write the data to a new table
df.to_sql("stocks", conn, if_exists='replace', index=False)

# Step 4: Close connection
conn.close()
print("Data inserted into stock_data.db successfully!")
