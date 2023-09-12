from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"data": data})

@app.route('/item', methods=['POST'])
def create_item():
    new_item = request.json
    data.append(new_item)
    return jsonify(new_item), 201

@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((x for x in data if x["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    update_data = request.json
    item.update(update_data)
    return jsonify(item)

@app.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [x for x in data if x["id"] != item_id]
    return jsonify({"result": "Item deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
