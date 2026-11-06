from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Welcome to Our Comic Website!"

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json()

    name = data.get("name")
    opinion = data.get("feedback")
    solution = data.get("solution")

    print("New feedback received!")
    print("Name:", name)
    print("Opinion:", opinion)
    print("Solution:", solution)

    return jsonify({
        "message": "Thank you! Your feedback was received."
    })

if __name__ == "__main__":
    app.run(debug=True)