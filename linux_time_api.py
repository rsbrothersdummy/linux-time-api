from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/time')
def time():
    now = datetime.now()
    return jsonify({"time": now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
