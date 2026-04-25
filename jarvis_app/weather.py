import requests

def get_weather(city_name="Sambhajinagar"):
    """
    Fetches the current weather for a given city using the free wttr.in API.
    Defaults to Sambhajinagar as requested.
    """
    try:
        # Using wttr.in which provides free weather data without an API key
        url = f"https://wttr.in/{city_name}?format=j1"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract current conditions
            current = data["current_condition"][0]
            temperature = current["temp_C"]
            description = current["weatherDesc"][0]["value"]
            
            return f"The temperature in {city_name} is {temperature} degrees Celsius with {description}."
        else:
            return f"Sorry, I couldn't find the weather for {city_name}."
            
    except Exception as e:
        return "Sorry, there was an error connecting to the weather service."
