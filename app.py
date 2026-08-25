from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Authoritative application state
reservations = {}

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/reserve", methods=["POST"])
def reserve():
    # Fault injection:
    # Tool claims success but DOES NOT actually create the reservation.
    declared_result = {
        "success": True,
        "reservation_id": "R-1042",
        "message": "Reservation created successfully"
    }

    reservation_id = declared_result["reservation_id"]

    # Independent state verification
    exists_in_state = reservation_id in reservations

    verification = (
        "VERIFIED"
        if declared_result["success"] and exists_in_state
        else "DIVERGENCE DETECTED"
    )

    return jsonify({
        "declared_result": "SUCCESS",
        "reservation_id": reservation_id,
        "actual_state": (
            "RESERVATION FOUND"
            if exists_in_state
            else "RESERVATION NOT FOUND"
        ),
        "verification": verification
    })


@app.route("/api/state")
def state():
    return jsonify(reservations)


if __name__ == "__main__":
    app.run(debug=True)