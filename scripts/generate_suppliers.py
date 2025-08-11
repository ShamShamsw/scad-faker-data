import pandas as pd
from faker import Faker

def generate_suppliers(num_suppliers=30):
    fake = Faker()
    df = pd.DataFrame({
        'supplier_id': range(1, num_suppliers + 1),
        'supplier_name': [fake.company() for _ in range(num_suppliers)],
        'contact_info': [fake.phone_number() for _ in range(num_suppliers)],
        'email': [fake.company_email() for _ in range(num_suppliers)],
        'address': [fake.address().replace("\n", ", ") for _ in range(num_suppliers)]
    })
    df.to_csv('data/suppliers.csv', index=False)

if __name__ == "__main__":
    generate_suppliers()
