from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Authoritative application state
reservations = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/reserve", methods=["POST"])
def reserve():
    data = request.get_json(silent=True) or {}

    reservation_id = "R-1042"

    # Fault injection:
    # tool claims success, but reservation is NOT persisted.
    return jsonify({
        "success": True,
        "reservation_id": reservation_id,
        "party_size": data.get("party_size", 2),
        "time": data.get("time", "19:00"),
        "message": "Reservation created successfully"
    })


@app.route("/api/state/<reservation_id>")
def reservation_state(reservation_id):
    reservation = reservations.get(reservation_id)

    return jsonify({
        "reservation_id": reservation_id,
        "exists": reservation is not None,
        "reservation": reservation
    })


if __name__ == "__main__":
    app.run(debug=True)
