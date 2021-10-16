from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import mysql.connector
import json

import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)

connection = get_sql_connection()


# Passes ID and Edits details of a product
@app.route('/editProduct', methods=['POST', 'GET'])
def edit_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.edit_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Inserts new UOM
@app.route('/insertUOM', methods=['GET', 'POST'])
def insert_uom():
    request_payload = json.loads(request.form['data'])
    uom_id = uom_dao.insert_new_uom(connection,request_payload)
    response = jsonify({
        'uom_id': uom_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Order details (customer_name, product, quantity, total_price)
# of a particular order is fetched from the Database
@app.route('/getOrderDetails', methods=['GET'])
def get_order_details():
    response = orders_dao.get_order_details(connection, request.form['order_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)