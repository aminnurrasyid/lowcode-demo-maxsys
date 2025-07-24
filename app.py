from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def getWeather():
    return jsonify({"Weather":"Sunny"})
