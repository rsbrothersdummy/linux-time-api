# linux_time_api.py
from flask import Flask, jsonify
from datetime import datetime
import threading

def create_app(port):
    app = Flask(__name__)

    @app.route('/time')
    def get_time():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f")[:-3]  # Millisecond precision
        return jsonify({'time': current_time, 'port': port})

    def run():
        app.run(host='0.0.0.0', port=10000)

    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()

ports = [5353, 1900, 8080]
for p in ports:
    create_app(p)

# Keep the script running
input("Time API server running on ports 5353, 1900, and 8080. Press Enter to exit...\n")

