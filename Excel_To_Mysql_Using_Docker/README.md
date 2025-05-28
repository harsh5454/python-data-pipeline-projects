# Excel to MySQL (Docker)

## 🎯 Goal
Read a sales Excel file and load its contents into a MySQL database running in Docker.

## 🔧 Tools Used
- Python (pandas, openpyxl, sqlalchemy, pymysql)
- MySQL (via Docker)

## ▶️ How to Run

1. Start MySQL using Docker: docker-compose.yml

2. Install dependencies: pip install -r requiremnts.txt

3. Run the script: Excel_to_Mysql.py


## 🧾 Output

Your data will be stored in a table named `sales` inside the `sales_db` database in MySQL.

## 🧪 Sample Excel:

| OrderID | Customer | Product | Quantity | Price |
|---------|----------|---------|----------|-------|
| 1001    | Alice    | Mouse   | 2        | 400   |


