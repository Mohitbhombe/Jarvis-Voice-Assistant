import requests

def get_weather(city_name):
    """
    Fetches the current weather for a given city using OpenWeatherMap API.
    """
    # NOTE: You need to sign up at https://openweathermap.org/ to get a free API key
    api_key = "YOUR_API_KEY_HERE"
    
    # Check if the API key has been replaced
    if api_key == "YOUR_API_KEY_HERE":
        return "Please add your OpenWeatherMap API key in the weather file to use this feature."
        
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Get temperature in Celsius
    }
    
    try:
        # Send a GET request to the OpenWeatherMap API
        response = requests.get(base_url, params=params)
        data = response.json()
        
        # '200' means the request was successful and the city was found
        if data.get("cod") == 200:
            main_data = data["main"]
            weather_data = data["weather"][0]
            
            temperature = main_data["temp"]
            description = weather_data["description"]
            
            # Format the output string
            result = f"The temperature in {city_name} is {temperature} degrees Celsius with {description}."
            return result
        else:
            return f"Sorry, I couldn't find the weather for {city_name}."
            
    except Exception as e:
        # Handle cases like no internet connection
        return "Sorry, there was an error connecting to the weather service. Please check your internet connection."
