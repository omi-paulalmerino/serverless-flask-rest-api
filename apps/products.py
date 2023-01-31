from flask import Blueprint, jsonify

product_app = Blueprint('product_app', __name__, template_folder='templates')


@product_app.route('/products')
def products():
    products = [
        {"name": "MSI GP63 Leopard 8RE", "price": 90_000},
        {"name": "Macbook Pro 13in", "price": 90_000},
    ]
    return jsonify({'products': products})
