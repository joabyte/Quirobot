import os
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/api/key")
def get_key():
    return jsonify({"key": os.environ.get("ANTHROPIC_API_KEY", "")})

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
