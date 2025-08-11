import pandas as pd
from faker import Faker

def generate_products(num_products=100):
    fake = Faker()
    products = [fake.unique.word() for _ in range(num_products)]
    df = pd.DataFrame({
        'product_id': range(1, num_products + 1),
        'product_name': products,
        'stock_level': [fake.random_int(min=10, max=1000) for _ in range(num_products)],
        'supplier': [fake.company() for _ in range(num_products)]
    })
    df.to_csv('data/products.csv', index=False)

if __name__ == "__main__":
    generate_products()
