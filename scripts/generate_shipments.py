import pandas as pd
from faker import Faker
import random

def generate_shipments(num_shipments=80, num_orders=200):
    fake = Faker()
    carriers = [fake.company() for _ in range(10)]
    df = pd.DataFrame({
        'shipment_id': range(1, num_shipments + 1),
        'order_id': [random.randint(1, num_orders) for _ in range(num_shipments)],
        'shipped_date': [fake.date_between(start_date='-1y', end_date='today').isoformat() for _ in range(num_shipments)],
        'carrier': [random.choice(carriers) for _ in range(num_shipments)],
        'tracking_number': [fake.unique.bothify(text='??#####??') for _ in range(num_shipments)]
    })
    df.to_csv('data/shipments.csv', index=False)

if __name__ == "__main__":
    generate_shipments()
