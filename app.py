from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/user/<string:name>', methods=['GET'])
def get_user(name):
    return jsonify({"message": f"Hello, {name}!"}), 200

@app.route('/data', methods=['POST'])
def add_data():
    data = request.json
    return jsonify({"received": data}), 201

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
