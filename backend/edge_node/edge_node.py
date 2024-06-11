from flask import Flask, request, jsonify

app = Flask(__name__)

def is_valid_reading(reading):
    """
    Validate the sensor reading.
    For example, check if the reading is within an expected range.
    """
    return 0 <= reading <= 100

def process_sensor_data(data):
    """
    Process sensor data:
    - Filter valid readings.
    - Calculate average of the readings.
    - Convert readings to a different unit if necessary.
    """
    readings = data.get('readings', [])
    valid_readings = [r for r in readings if is_valid_reading(r)]
    
    if not valid_readings:
        return {'status': 'error', 'message': 'No valid sensor readings'}

    average_reading = sum(valid_readings) / len(valid_readings)
    return {
        'status': 'success',
        'valid_readings': valid_readings,
        'average_reading': average_reading
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
