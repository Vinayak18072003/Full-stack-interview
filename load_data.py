import pandas as pd
from models import Department, Product, db
from app import app

def load_data():
    with app.app_context():
        # Load Departments
        dept_df = pd.read_csv('departments.csv')
        for _, row in dept_df.iterrows():
            dept = Department(name=row['name'])
            db.session.add(dept)
        db.session.commit()

        # Load Products
        prod_df = pd.read_csv('products.csv')
        for _, row in prod_df.iterrows():
            prod = Product(
                name=row['name'],
                description=row['description'],
                price=row['price'],
                department_id=row['department_id']
            )
            db.session.add(prod)
        db.session.commit()

if __name__ == "__main__":
    load_data()
    print("CSV data loaded successfully.")
