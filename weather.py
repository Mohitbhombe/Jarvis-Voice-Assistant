import requests

def get_weather(city_name):
    """
    Fetches the current weather for a given city using the free wttr.in API.
    No API key required!
    """
    try:
        # We use wttr.in which provides free weather data without any API key
        url = f"https://wttr.in/{city_name}?format=j1"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract the current conditions from the JSON
            current = data["current_condition"][0]
            temperature = current["temp_C"]
            description = current["weatherDesc"][0]["value"]
            
            # Format the output string
            result = f"The temperature in {city_name} is {temperature} degrees Celsius with {description}."
            return result
        else:
            return f"Sorry, I couldn't find the weather for {city_name}."
            
    except Exception as e:
        # Handle cases like no internet connection
        return "Sorry, there was an error connecting to the weather service. Please check your internet connection."
