from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Slack bot is running!"

@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.get_json()

    # ✅ Respond to Slack's URL verification challenge
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})

    # 👇 Your logic to handle other Slack events can go here
    return "", 200

if __name__ == "__main__":
    app.run(debug=True)
