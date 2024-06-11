from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def is_valid_reading(reading):
    return 0 <= reading <= 100

def process_sensor_data(data):
    readings = data.get('readings', [])
    valid_readings = [r for r in readings if is_valid_reading(r)]
    
    if not valid_readings:
        return {'status': 'error', 'message': 'No valid sensor readings'}

    average_reading = sum(valid_readings) / len(valid_readings)
    
    # Communicate with CU-CP to set up connection
    cu_cp_response = requests.post('http://cu-cp-container:5000/setup_connection', json={'average_reading': average_reading})
    
    if cu_cp_response.status_code != 200:
        return {'status': 'error', 'message': 'Failed to communicate with CU-CP'}

    return {
        'status': 'success',
        'valid_readings': valid_readings,
        'average_reading': average_reading,
        'cu_cp_response': cu_cp_response.json()
    }

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    if not data:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400

    result = process_sensor_data(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
