import datetime
import webbrowser
import wikipedia
import requests
from weather import get_weather
from reminder import set_reminder

def get_time():
    """Returns the current time in a readable format."""
    time_str = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {time_str}."

def get_date():
    """Returns the current date in a readable format."""
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    return f"Today's date is {date_str}."

def open_website(site_name):
    """Opens popular websites in the default web browser."""
    if "youtube" in site_name.lower():
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."
    elif "google" in site_name.lower():
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    else:
        return "Sorry, I can only open YouTube and Google right now."

def search_wikipedia(query):
    """Searches Wikipedia and returns a 2-sentence summary."""
    try:
        # Clean up the query by removing the command words
        search_term = query.lower().replace("wikipedia", "").replace("search", "").replace("for", "").strip()
        
        if not search_term:
            return "What would you like me to search on Wikipedia?"
            
        # Get a 2-sentence summary from Wikipedia
        result = wikipedia.summary(search_term, sentences=2)
        return f"According to Wikipedia: {result}"
        
    except wikipedia.exceptions.DisambiguationError:
        return "There are too many results for that query. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "I couldn't find any information on that topic."
    except Exception as e:
        return "Sorry, there was an error connecting to Wikipedia."

def get_joke():
    """Fetches a random joke from an open API."""
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            setup = data["setup"]
            punchline = data["punchline"]
            # Return both parts of the joke
            return f"{setup}... {punchline}"
        else:
            return "I couldn't think of a joke right now."
            
    except Exception as e:
        return "Sorry, my joke book is currently unavailable."

def process_command(command, engine):
    """
    Main logic hub. Takes the user's spoken command and decides what feature to run.
    Returns the text that Jarvis should speak back.
    """
    command = command.lower()
    
    # 1. Check for exit commands
    if "exit" in command or "quit" in command or "stop" in command:
        return "Goodbye sir. Have a great day!"
        
    # 2. Time and Date
    elif "time" in command:
        return get_time()
        
    elif "date" in command:
        return get_date()
        
    # 3. Open Websites
    elif "open youtube" in command or "open google" in command:
        return open_website(command)
        
    # 4. Wikipedia Search
    elif "wikipedia" in command:
        return search_wikipedia(command)
        
    # 5. Tell a joke
    elif "joke" in command:
        return get_joke()
        
    # 6. Weather updates
    elif "weather" in command:
        # Extract city name (assuming user says "weather in [city]")
        if "in" in command:
            city = command.split("in")[-1].strip()
        else:
            # If no city is specified, default to a common one or ask
            city = "Delhi"
            
        return get_weather(city)
        
    # 7. Set Reminders
    elif "remind me" in command:
        # Simple parsing logic for beginners
        # Example command expected: "remind me to [drink water] in [10] seconds"
        try:
            parts = command.split("in")
            task = parts[0].replace("remind me to", "").strip()
            time_part = parts[1].strip()
            
            # Extract the number from the time string
            seconds = int(''.join(filter(str.isdigit, time_part)))
            
            # If the user said "minutes", convert to seconds
            if "minute" in time_part:
                seconds *= 60
                
            set_reminder(task, seconds)
            return f"I will remind you to {task} in {seconds} seconds."
            
        except Exception as e:
            return "Please specify what to remind you and when. For example: remind me to drink water in 10 seconds."
            
    # 8. Unrecognized Command
    else:
        return "I am not sure how to help with that. Please try another command."
