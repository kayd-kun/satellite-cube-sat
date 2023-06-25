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

@app.route('/get_data', methods=['GET'])
def get_json_data():
    new_data = fetch_data()
    return jsonify(new_data)

# Route that will accept POST data and save it to data.json
@app.route('/post_data', methods=['POST'])
def post_json_data():
    global data
    if request.method == 'POST':
        data = request.get_json()
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return jsonify(data)

if __name__ == '__main__':
    thread = Thread(target=fetch_data).start()
    thread.start() 
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0', threaded=True)
