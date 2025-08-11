import random
from faker import Faker

fake = Faker()

def random_price(min_price=1.0, max_price=100.0):
    """Generate a random price within a given range."""
    return round(random.uniform(min_price, max_price), 2)

def random_stock(min_stock=0, max_stock=500):
    """Generate a random stock level within a given range."""
    return random.randint(min_stock, max_stock)

def random_date(start_year=2020, end_year=2025):
    """Generate a random date as a string."""
    return fake.date_between(start_date=f"{start_year}-01-01", end_date=f"{end_year}-12-31").isoformat()

def random_category(categories):
    """Pick a random category from a list."""
    return random.choice(categories)

def random_email():
    """Generate a random email address."""
    return fake.email()

def random_name():
    """Generate a random full name."""
    return fake.name()

def random_address():
    """Generate a random address."""
    return fake.address().replace("\n", ", ")
