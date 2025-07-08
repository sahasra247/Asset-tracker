#create rssi_server.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/rssi", methods=["POST"])
def receive_rssi():
    data = request.json
    rpi_id = data.get("rpi")
    rssi = data.get("rssi")
    print(f"Received from {rpi_id}: RSSI = {rssi} dBm")
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)