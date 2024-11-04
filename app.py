from flask import Flask, jsonify, request
app = Flask(__name__)

# Settear puerto publico antes de probar, utilizar Body => raw (JSON) para agregar input en PostMan.

todos = [
    {"done": True, "label": "Sample Todo 1"},
    {"done": True, "label": "Sample Todo 2"}
]

@app.route("/todos", methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route("/todos", methods=['POST'])
def add_todos():
    new_todo = request.get_json()
    if "done" in new_todo and "label" in new_todo:
        todos.append(new_todo)
        return jsonify(todos), 201
    else:
        return jsonify({"error": "Invalid request"}), 400

@app.route("/todos/<int:id>", methods=['DELETE'])
def delete_todos(id):
    if 0 <= id < len(todos):
        todos.pop(id)
        return jsonify(todos), 200
    else:
        return jsonify({"error": "Task not found"}), 404

app.run(host='0.0.0.0', port="3000", debug=True)