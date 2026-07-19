from flask import Flask, jsonify, request
from pymongo import MongoClient
from dontenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()  # Load environment variables from .env file

# MongoDB Atlas connection
MONGO_URI = os.getenv("MONGO_URL","mongodb://<USER>:<PASSWORD>@<CLUSTER>.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient(MONGO_URI)

db = client["test_db"]
collection = db["users"]

@app.route("/api/submit", methods=["POST"])
def submit():
    try:
        data = request.get_json()

        name = data.get("name") if data else None
        email = data.get("email") if data else None

        if not name or not email:
            return jsonify({"error": "Name and Email are required"}), 400

        collection.insert_one({
            "name": name,
            "email": email
        })

        return jsonify({"message": "Data submitted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)