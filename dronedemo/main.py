from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the United Airlines Backend!"

@app.route("/booking", methods=["GET"])
def booking():
    # Simulate booking information for demonstration purposes
    booking_info = {
        "flight_number": "UA123",
        "departure": "San Francisco (SFO)",
        "arrival": "New York (JFK)",
        "status": "Confirmed",
    }
    return jsonify(booking_info), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
