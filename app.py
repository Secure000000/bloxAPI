from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Simple route to check if the API is working
@app.route('/', methods=['GET'])
def home():
    return jsonify(message="Welcome to the BloxAPI!")
