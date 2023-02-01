from flask import Flask, jsonify
from apps.products import product_app as products

app = Flask(__name__)
app.register_blueprint(products)


@app.route("/", methods=["GET"])
def home():
    return jsonify({'message': 'Hello world!'})
