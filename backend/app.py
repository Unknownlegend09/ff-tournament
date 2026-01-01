import os
from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

FILE = "registrations.csv"

@app.route("/")
def home():
    return "Free Fire Tournament Server Running 🔥"

@app.route("/register", methods=["POST"])
def register():
    data = request.json

    name = data.get("name")
    uid = data.get("uid")
    phone = data.get("phone")
    mode = data.get("mode")

    if not name or not uid or not phone:
        return jsonify({"error": "Missing fields"}), 400

    file_exists = os.path.isfile(FILE)

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "UID", "Phone", "Mode"])
        writer.writerow([name, uid, phone, mode])

    return jsonify({"message": "Registration successful"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

