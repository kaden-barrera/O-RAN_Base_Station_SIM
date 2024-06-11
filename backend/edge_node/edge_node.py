from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    # Add your edge node processing logic here
    response = {
        'status': 'Data processed',
        'data': data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

