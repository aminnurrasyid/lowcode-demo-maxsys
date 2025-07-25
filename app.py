from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Sample weather data for 3 different dates
SAMPLE_WEATHER_DATA = {
    "2024-01-15": {
        "date": "2024-01-15",
        "temperature": 22,
        "condition": "Sunny",
        "humidity": 45,
        "wind_speed": 12,
        "description": "Clear skies with gentle breeze"
    },
    "2024-01-16": {
        "date": "2024-01-16", 
        "temperature": 18,
        "condition": "Cloudy",
        "humidity": 70,
        "wind_speed": 8,
        "description": "Overcast with light winds"
    },
    "2024-01-17": {
        "date": "2024-01-17",
        "temperature": 15,
        "condition": "Rainy",
        "humidity": 85,
        "wind_speed": 20,
        "description": "Heavy rain with strong winds"
    }
}

@app.route("/weather", methods=["GET"])
def getWeather():
    return jsonify({"Weather":"Sunny"})

@app.route("/weather/date", methods=["GET"])
def getWeatherByDate():
    # Get date parameter from query string
    date = request.args.get('date')
    
    if not date:
        return jsonify({
            "error": "Date parameter is required",
            "format": "YYYY-MM-DD",
            "example": "/weather/date?date=2024-01-15"
        }), 400
    
    # Validate date format
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return jsonify({
            "error": "Invalid date format",
            "format": "YYYY-MM-DD",
            "provided": date
        }), 400
    
    # Check if we have weather data for this date
    if date in SAMPLE_WEATHER_DATA:
        return jsonify(SAMPLE_WEATHER_DATA[date])
    else:
        return jsonify({
            "error": "Weather data not available for this date",
            "date": date,
            "available_dates": list(SAMPLE_WEATHER_DATA.keys())
        }), 404

if __name__ == '__main__':
    app.run(debug=True)
