from flask import Flask, jsonify, request
import json

app = Flask(__name__)

todos = [
  { "label": "My first task", "done": False },
  { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    # #other way to transfor en list paython un group of data
    # request_body = request.json
    print("Incoming request with the following body", request_body)
    # return 'Response for the POST todo'
    todos.append(request_body)
    # json_text = jsonify({"lista":todos, "message":"ok"})
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  print(f"This is the position to delete: {position}")
  position = int(position)
  if position >= len(todos):
    return jsonify({"message":"El indice es mayor al tamanho de la lista"}), 429
  if position < 0:
    return jsonify({"message":"No se aceptan numeros negativos"})
  if len(todos) == 0:
    return jsonify({"message":"No hay nada que borrar"})
    

  todos.pop(position)
  json_text = jsonify(todos)
  return json_text











# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)