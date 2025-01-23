def weather_forecast():
    sky = input("Enter the sky condition (cloudy/clear): ")
    temperature = float(input("Enter the temperature in °C: "))
    wind = input("Enter the wind condition (none/some): ")
    if sky == "cloudy" and wind == "none":
        return "It might rain."
    elif temperature < 0 and sky == "clear":
        return "It might snow."
    elif temperature > 30 and wind == "none":
        return "It might be a hot day."
    elif sky == "clear" and wind == "some":
        return "It might be a pleasant day."
    else:
        return "Weather conditions are not covered by the rules."


forecast_result = weather_forecast()
print(forecast_result)
