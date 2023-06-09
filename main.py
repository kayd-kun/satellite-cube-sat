from flask import Flask, jsonify, request
import os
from flask import render_template
import json

from threading import Thread
import time

# {
#     "altitude": "100",
#     "temperature": "30",
#     "pressure": "1",
#     "humidity": "30",
#     "vco index": "28",
#     "latitude": "89",
#     "longitude": "78"
# }

max_altitude = 0

app = Flask(__name__)
data = None

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def fetch_data():
    global data
    # Read data from data.json file
    data = json.load(open('data.json'))
    return data

# Check max altitude and return
def check_max_altitude(data):
    global max_altitude
    if data['altitude'] > max_altitude:
        max_altitude = data['altitude']
    return max_altitude

# Append received json to data_logs.txt file
def append_to_file(data):
    with open('data_logs.txt', 'a') as f:
        f.write(data + '\n')

@app.route('/get_data', methods=['GET'])
def get_json_data():
    new_data = fetch_data()
    return jsonify(new_data)

# Return the processed image
@app.route('/get_image', methods=['GET'])
def get_image():
    image_path = 'static/images/processed_image.jpg'

# Route that will accept POST data and save it to data.json
@app.route('/post_data', methods=['POST'])
def post_json_data():
    global data
    if request.method == 'POST':
        data = request.get_json()
        print('Received data: ', data)
        append_to_file(str(data))
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return jsonify(data)

if __name__ == '__main__':
    thread = Thread(target=fetch_data).start()
    thread.start() 
    app.run(debug=True, port=5000, host='0.0.0.0', threaded=True)
