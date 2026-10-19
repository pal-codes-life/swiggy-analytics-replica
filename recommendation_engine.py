import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

print("Loading order history...")
# 1. Load the data
orders = pd.read_csv('orders.csv')

# 2. Create a User-Item Matrix
# Rows are Users, Columns are Restaurants, Values are the number of times ordered
print("Building user-restaurant matrix...")
user_restaurant_matrix = orders.pivot_table(
    index='user_id',
    columns='restaurant_id',
    values='order_id',
    aggfunc='count',
    fill_value=0
)

# 3. Calculate Cosine Similarity between users
print("Calculating user similarities...")
user_similarity = cosine_similarity(user_restaurant_matrix)
user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_restaurant_matrix.index,
    columns=user_restaurant_matrix.index
)


def recommend_restaurants(target_user_id, top_n=3):
    # Find the most similar user
    similar_users = user_similarity_df[target_user_id].sort_values(ascending=False)
    most_similar_user = similar_users.index[1]  # Index 0 is the user themselves (similarity of 1.0)

    # Find what the similar user ordered that the target user hasn't
    target_user_orders = set(orders[orders['user_id'] == target_user_id]['restaurant_id'])
    similar_user_orders = set(orders[orders['user_id'] == most_similar_user]['restaurant_id'])

    # Isolate the new restaurants
    recommendations = list(similar_user_orders - target_user_orders)

    print(f"\nTarget User {target_user_id} has ordered from: {list(target_user_orders)[:5]}...")
    print(f"Similar User {most_similar_user} also ordered from: {list(similar_user_orders)[:5]}...")

    return recommendations[:top_n]


# 4. Test the recommendation engine
target_user = 5
print(f"\n--- Top 3 Recommended Restaurant IDs for User {target_user} ---")
print(recommend_restaurants(target_user, top_n=3))