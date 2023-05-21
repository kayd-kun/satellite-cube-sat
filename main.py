from flask import Flask, jsonify
import os
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User'}
    return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')
