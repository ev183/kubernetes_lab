# app.py

# import flask and jsonify to create the app and return JSON responses
from flask import Flask, jsonify

# create the flask application instance
app = Flask(__name__)

# define a route for GET /health
@app.route("/health")
def health():
    # return a JSON response with a 200 status
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # listen on all network interfaces so the container can receive external traffic
    app.run(host="0.0.0.0", port=5000)