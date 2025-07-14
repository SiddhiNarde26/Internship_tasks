from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    item = {
        "name": data["name"],
        "quantity": data["quantity"]
    }
    items.append(item)
    return jsonify({"message": "Item added", "item": item}), 201

@app.route("/items/<int:index>", methods=["PUT"])
def update_item(index):
    data = request.get_json()
    items[index] = {
        "name": data["name"],
        "quantity": data["quantity"]
    }
    return jsonify({"message": "Item updated", "item": items[index]})

@app.route("/items/<int:index>", methods=["DELETE"])
def delete_item(index):
    item = items.pop(index)
    return jsonify({"message": "Item deleted", "item": item})

if __name__ == "__main__":
    app.run(debug=True)
