from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/process_signal', methods=['POST'])
def process_signal():
    data = request.json
    # Add your signal processing logic here
    response = {
        'status': 'Signal processed',
        'data': data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

