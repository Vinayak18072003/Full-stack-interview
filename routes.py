# routes.py
from flask import Blueprint, jsonify
from models import Product, Department, db

api = Blueprint('api', __name__)

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
            "department": p.department.name
        })
    return jsonify(result)

@api.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    p = Product.query.get_or_404(product_id)
    return jsonify({
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": float(p.price),
        "department": p.department.name
    })
