from flask import Flask, jsonify, request
import random
import uuid

app = Flask(__name__)


# Не знаю насколько проще надо было, но потенциально какую нить бдшку кей-вэлью можно было подключить
dict_uniq_id = {}

@app.route('/generate', methods=['POST'])
def generate():
    random_number = random.randint(1, 1000)
    id = str(uuid.uuid4())
    dict_uniq_id[id] = random_number
    return jsonify({"id": id, "number": random_number}), 200

@app.route('/retrieve/<string:id>', methods=['GET'])
def retrieve(id):
    if id in dict_uniq_id:
        return jsonify({"id": id, "number": dict_uniq_id[id]}), 200
    else:
        return jsonify({"error": "ID not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)