import json
from flask import Flask, jsonify, request

from .services import retrieve_orders, create_order

app = Flask(__name__)

@app.route('/api/orders/computers', methods=['GET'])
def getOrders():
    return jsonify(retrieve_orders())

@app.route('/api/orders/computers', methods=['POST'])
def create_computer_order():
    if request.method == 'POST':
        data = request.get_json()

        # Validate data (example: check for required fields)
        if not all(key in data for key in ['status', 'created_at', 'created_by']):
            return jsonify({'message': 'Missing required fields: status, created_at, or created_by'}), 400
    
        new_order = create_order(data);

        return jsonify(new_order, 201)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

if __name__ == '__main__':
    app.run()
