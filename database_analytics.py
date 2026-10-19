import sqlite3
import pandas as pd

print("Connecting to database...")
# 1. Create a connection to a new SQLite database (it will create the file automatically)
conn = sqlite3.connect('swiggy.db')

# 2. Load the CSVs you generated earlier
print("Loading CSV files into SQL tables...")
users = pd.read_csv('users.csv')
restaurants = pd.read_csv('restaurants.csv')
orders = pd.read_csv('orders.csv')

# 3. Write the data into SQL tables
users.to_sql('Users', conn, if_exists='replace', index=False)
restaurants.to_sql('Restaurants', conn, if_exists='replace', index=False)
orders.to_sql('Orders', conn, if_exists='replace', index=False)

print("Database created successfully!\n")

# 4. Write your SQL Business Intelligence Query
query = """
SELECT 
    r.cuisine, 
    COUNT(o.order_id) AS total_orders, 
    ROUND(SUM(o.order_value), 2) AS total_revenue
FROM Orders o
JOIN Restaurants r ON o.restaurant_id = r.restaurant_id
GROUP BY r.cuisine
ORDER BY total_revenue DESC;
"""

# 5. Execute the SQL query and print the results
print("--- Most Popular Cuisines by Revenue ---")
results = pd.read_sql_query(query, conn)
print(results)

# Close the connection
conn.close()