from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)


db_client = MongoClient("mongodb://mongodb:27017")
db = db_client.my_database

@app.route('/')
def index():
    return "Hi!"

@app.route('/create', methods=['POST'])
def create_key_value():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    db.my_collection.insert_one({'key': key, 'value': value})
    return jsonify({'message': 'Key-Value pair created successfully'})

@app.route('/update', methods=['PUT'])
def update_key_value():
    data = request.get_json()
    db = db_client.my_database
    key = data.get('key')
    value = data.get('value')
    db.my_collection.update_one({'key': key}, {'$set': {'value': value}})
    return jsonify({'message': 'Key-Value pair updated successfully'})

@app.route('/read', methods=['GET'])
def read_key_value():
    key = request.args.get('key')
    db = db_client.my_database
    result = db.my_collection.find_one({'key': key})
    if result:
        return jsonify({'key': result['key'], 'value': result['value']})
    return jsonify({'message': 'Key not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
