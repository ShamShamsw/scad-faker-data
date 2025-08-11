# SCAD Faker Data Scripts Repository Design

This repository is dedicated to scripts for generating synthetic ("faker") data for use with the SCAD Dashboard project. The goal is to keep data generation logic, outputs, and configuration separate from the main ETL and dashboard codebases, improving modularity and maintainability.

---

## Directory Structure

```
scad-faker-data/
├── scripts/                # Python scripts for generating fake data
│   ├── generate_products.py
│   ├── generate_orders.py
│   ├── generate_customers.py
│   └── utils.py            # Shared faker utilities/functions
├── configs/                # YAML or JSON config files for data generation
│   ├── products_config.yaml
│   ├── orders_config.yaml
│   └── customers_config.yaml
├── output/                 # All generated datasets (CSV, JSON, etc.)
│   ├── products_fake.csv
│   ├── orders_fake.csv
│   └── customers_fake.csv
├── requirements.txt        # Python dependencies for faker scripts
├── README.md               # This documentation
└── .github/
    └── workflows/
        └── ci.yml         # (Optional) CI for linting/testing data scripts
```

---

## Directory Details

- **scripts/**  
  All Python scripts for generating fake data should live here. Each entity (products, orders, customers) gets its own script. Shared utilities go in `utils.py`.

- **configs/**  
  Place configuration files (YAML, JSON, etc.) to control the parameters of fake data generation (e.g., number of rows, value ranges, allowed categories).

- **output/**  
  All generated data files (CSV, JSON, etc.) are saved here. Do not commit large files to source control; use `.gitignore` as needed.

---

## Example Usage

To generate fake products data:
```bash
python scripts/generate_products.py --config configs/products_config.yaml --output output/products_fake.csv
```

---

## requirements.txt Example

```txt name=requirements.txt
faker
pandas
pyyaml
```

---

## Best Practices

- Do not mix fake data generation scripts with ETL or dashboard code.
- Keep the `output/` directory out of version control if files are large.
- Use configs to make data generation reproducible and configurable.
- Document each script’s purpose in the `README.md`.

---

## Extending

- Add new scripts in `scripts/` for new entities.
- Add corresponding configs and outputs.
- Optionally, use a CI workflow to lint or test data generation scripts.
