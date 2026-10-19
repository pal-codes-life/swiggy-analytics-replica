import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. Generate Users
users = pd.DataFrame({
    'user_id': range(1, 1001),
    'name': [f"User_{i}" for i in range(1, 1001)],
    'signup_date': [datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365)) for _ in range(1000)]
})

# 2. Generate Restaurants
cuisines = ['North Indian', 'South Indian', 'Chinese', 'Italian', 'Fast Food', 'Healthy']
restaurants = pd.DataFrame({
    'restaurant_id': range(1, 101),
    'restaurant_name': [f"Rest_{i}" for i in range(1, 101)],
    'cuisine': [random.choice(cuisines) for _ in range(100)],
    'rating': np.round(np.random.uniform(3.0, 5.0, 100), 1)
})

# 3. Generate Orders (The core transactional data)
num_orders = 10000
orders = pd.DataFrame({
    'order_id': range(1, num_orders + 1),
    'user_id': [random.randint(1, 1000) for _ in range(num_orders)],
    'restaurant_id': [random.randint(1, 100) for _ in range(num_orders)],
    'order_value': np.round(np.random.uniform(150, 1500, num_orders), 2),
    'order_date': [datetime(2024, 1, 1) + timedelta(days=random.randint(0, 300), hours=random.randint(8, 23)) for _ in range(num_orders)],
    'delivery_time_mins': [random.randint(15, 65) for _ in range(num_orders)]
})

# Export to CSV for your ETL pipeline
users.to_csv('users.csv', index=False)
restaurants.to_csv('restaurants.csv', index=False)
orders.to_csv('orders.csv', index=False)
print("Mock data generated successfully!")