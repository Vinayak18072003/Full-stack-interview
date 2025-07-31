import pandas as pd
from models import Department, Product, db
from app import app

def load_data():
    with app.app_context():
        # Clear old data (optional for reruns)
        Product.query.delete()
        Department.query.delete()
        db.session.commit()

        # Load departments
        dept_df = pd.read_csv('departments.csv')
        for _, row in dept_df.iterrows():
            dept = Department(name=row['name'])
            db.session.add(dept)
        db.session.commit()

        # Load products
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

        print("Data loaded successfully.")

if __name__ == "__main__":
    load_data()
