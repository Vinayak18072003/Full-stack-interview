from flask import Blueprint, jsonify, render_template
from models import Product, Department

api = Blueprint('api', __name__)

# ✅ Get all products
@api.route("/products", methods=["GET"])
def get_all_products():
    products = Product.query.all()
    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": float(p.price),
            "department": p.department.name,
            "department_id": p.department.id  # required for filtering
        })
    return jsonify(result)

# ✅ Get a single product by ID
@api.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    p = Product.query.get_or_404(product_id)
    return jsonify({
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": float(p.price),
        "department": p.department.name,
        "department_id": p.department.id
    })

# ✅ Get all departments
@api.route("/departments", methods=["GET"])
def get_departments():
    departments = Department.query.all()
    result = []
    for d in departments:
        result.append({
            "id": d.id,
            "name": d.name
        })
    return jsonify(result)

# ✅ HTML: Product list (all or filtered)
@api.route("/")
def index_page():
    return render_template("index.html")

@api.route("/department/<int:dept_id>")
def department_products_page(dept_id):
    return render_template("index.html", department_id=dept_id)

# ✅ HTML: Product detail page
@api.route("/product/<int:product_id>")
def product_page(product_id):
    return render_template("product.html")

# ✅ HTML: Department list page
@api.route("/departments-list")
def departments_page():
    return render_template("departments.html")
