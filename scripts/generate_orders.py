import pandas as pd
from faker import Faker
import random

def generate_orders(num_orders=200, num_products=100):
    fake = Faker()
    df = pd.DataFrame({
        'order_id': range(1, num_orders + 1),
        'product_id': [random.randint(1, num_products) for _ in range(num_orders)],
        'quantity': [random.randint(1, 50) for _ in range(num_orders)],
        'order_date': [fake.date_between(start_date='-1y', end_date='today').isoformat() for _ in range(num_orders)],
        'customer_name': [fake.name() for _ in range(num_orders)]
    })
    df.to_csv('data/orders.csv', index=False)

if __name__ == "__main__":
    generate_orders()
