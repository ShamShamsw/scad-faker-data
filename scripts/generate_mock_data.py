from generate_products import generate_products
from generate_orders import generate_orders
from generate_suppliers import generate_suppliers
from generate_inventory import generate_inventory
from generate_shipments import generate_shipments

def main():
    print("Generating mock data for Supply Chain Dashboard...")
    generate_products()
    generate_orders()
    generate_suppliers()
    generate_inventory()
    generate_shipments()
    print("All mock data generated successfully in the data/ directory.")

if __name__ == "__main__":
    main()
