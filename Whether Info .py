weather_data = {
    "Mumbai": {"Temperature": 31, "Condition": "Sunny"},
    "Delhi": {"Temperature": 37, "Condition": "Hot"},
    "Pune": {"Temperature": 29, "Condition": "Cloudy"},
    "Hyderabad": {"Temperature": 32, "Condition": "Rainy"},
    "Chennai": {"Temperature": 34, "Condition": "Humid"}
}

print("===== Weather App =====")

city = input("Enter City Name: ").title()

if city in weather_data:
    print("\nWeather Report")
    print("-------------------")
    print("City        :", city)
    print("Temperature :", weather_data[city]["Temperature"], "°C")
    print("Condition   :", weather_data[city]["Condition"])
else:
    print("City data not available.")