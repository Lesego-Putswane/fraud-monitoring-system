from faker import Faker
import pandas as pd
import random

fake = Faker()

customers = []

for i in range(1, 101):  # 100 customers
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "age": random.randint(18, 70),
        "income": random.randint(20000, 200000),
        "credit_score": random.randint(300, 850)
    })

customers_df = pd.DataFrame(customers)
customers_df.to_csv("../data/customers.csv", index=False)

print("Customers dataset created.")
