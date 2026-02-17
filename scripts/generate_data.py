from faker import Faker
import pandas as pd
import random

fake = Faker()

customers = []
transactions = []
transactions_type = ['withdrawal', 'deposit', 'transfer', 'payment']

for i in range(1, 101):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "age": random.randint(18, 70),
        "income": random.randint(20000, 200000),
        "credit_score": random.randint(300, 850)
    })

for i in range(1, 1001):
    transactions.append({
        "transaction_id": i,
        "customer_id": random.randint(1, 100),
        "amount": random.randint(1, 10000),
        "transaction_date": fake.date(),
        "location": fake.city(),
        "transaction_type": random.choice(transactions_type),
    })

customers_df = pd.DataFrame(customers)
customers_df.to_csv("../data/customers.csv", index=False)

transactions_df = pd.DataFrame(transactions)
transactions_df.to_csv("../data/transactions.csv", index=False)


print("Customers dataset created.")
print("Transactions dataset created")
