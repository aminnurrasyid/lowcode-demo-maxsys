from flask import Flask, jsonify, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def getWeather():
    return jsonify({"Weather":"Sunny"})

@app.route("/weather/date", methods=["GET"])
def getWeatherByDate():
    # Get date parameter from query string
    date_param = request.args.get('date')
    
    if not date_param:
        return jsonify({"error": "Date parameter is required. Format: YYYY-MM-DD"}), 400
    
    try:
        # Validate date format
        date_obj = datetime.strptime(date_param, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD"}), 400
    
    # Sample weather data based on different dates
    weather_samples = {
        "2024-01-15": {
            "date": "2024-01-15",
            "temperature": "2°C",
            "condition": "Snow",
            "humidity": "85%",
            "wind_speed": "15 km/h",
            "description": "Heavy snowfall expected throughout the day"
        },
        "2024-07-20": {
            "date": "2024-07-20",
            "temperature": "28°C",
            "condition": "Sunny",
            "humidity": "45%",
            "wind_speed": "8 km/h",
            "description": "Clear skies with bright sunshine"
        },
        "2024-10-03": {
            "date": "2024-10-03",
            "temperature": "18°C",
            "condition": "Rainy",
            "humidity": "90%",
            "wind_speed": "12 km/h",
            "description": "Light rain with overcast skies"
        }
    }
    
    # If the date matches one of our samples, return that data
    if formatted_date in weather_samples:
        return jsonify(weather_samples[formatted_date])
    
    # For other dates, generate dynamic weather data
    weather_conditions = ["Sunny", "Cloudy", "Rainy", "Snow", "Partly Cloudy", "Stormy"]
    temperatures = list(range(-5, 35))  # Temperature range from -5°C to 34°C
    humidity_levels = list(range(30, 100, 5))
    wind_speeds = list(range(5, 25, 2))
    
    # Use date as seed for consistent results
    random.seed(hash(formatted_date))
    
    condition = random.choice(weather_conditions)
    temperature = random.choice(temperatures)
    humidity = random.choice(humidity_levels)
    wind_speed = random.choice(wind_speeds)
    
    descriptions = {
        "Sunny": "Clear skies with bright sunshine",
        "Cloudy": "Overcast with thick cloud cover",
        "Rainy": "Precipitation expected throughout the day",
        "Snow": "Snowfall with cold temperatures",
        "Partly Cloudy": "Mix of sun and clouds",
        "Stormy": "Thunderstorms with heavy rain and strong winds"
    }
    
    return jsonify({
        "date": formatted_date,
        "temperature": f"{temperature}°C",
        "condition": condition,
        "humidity": f"{humidity}%",
        "wind_speed": f"{wind_speed} km/h",
        "description": descriptions[condition]
    })

if __name__ == "__main__":
    app.run(debug=True)
