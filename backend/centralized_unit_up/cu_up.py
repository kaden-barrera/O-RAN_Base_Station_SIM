from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/manage_data', methods=['POST'])
def manage_data():
    data = request.json
    response = {
        'status': 'Data managed successfully',
        'data': data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

