import os
import sys
import datetime
import webbrowser
import wikipedia
import requests
import pyautogui
import urllib.request
import urllib.parse
import re
from flask import Flask, render_template, request, jsonify
from weather import get_weather
from reminder import set_reminder

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Initialize Flask App with correct paths for PyInstaller compatibility
app = Flask(__name__, 
            template_folder=resource_path('templates'),
            static_folder=resource_path('static'))

# --- HELPER FUNCTIONS ---

def get_time():
    time_str = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {time_str}."

def get_date():
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    return f"Today's date is {date_str}."

def open_website(command):
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "chatgpt": "https://chatgpt.com",
        "whatsapp": "https://web.whatsapp.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "github": "https://github.com"
    }
    for site, url in sites.items():
        if f"open {site}" in command.lower():
            webbrowser.open(url)
            display_name = site.capitalize()
            if site == "chatgpt": display_name = "ChatGPT"
            if site == "whatsapp": display_name = "WhatsApp"
            if site == "youtube": display_name = "YouTube"
            return f"Opening {display_name}."
    return "Sorry, I don't know how to open that website yet."

def play_music(command):
    try:
        is_spotify = "spotify" in command.lower()
        song_name = command.lower().replace("play", "").replace("on spotify", "").replace("on youtube", "").strip()
        
        if not song_name:
            return "Please specify what you want me to play."
            
        if is_spotify:
            query_string = urllib.parse.quote(song_name)
            url = f"https://open.spotify.com/search/{query_string}"
            webbrowser.open(url)
            return f"Searching for {song_name} on Spotify."
        else:
            query_string = urllib.parse.urlencode({"search_query": song_name})
            html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())
            
            if search_results:
                url = "https://www.youtube.com/watch?v=" + search_results[0]
                webbrowser.open(url)
                return f"Playing {song_name} on YouTube."
            else:
                return f"Sorry, I couldn't find the song {song_name}."
    except Exception:
        return "Sorry, I encountered an error while trying to play the music."

def search_wikipedia(query):
    try:
        search_term = query.lower().replace("wikipedia", "").replace("search", "").replace("for", "").strip()
        if not search_term:
            return "What would you like me to search on Wikipedia?"
        result = wikipedia.summary(search_term, sentences=2)
        return f"According to Wikipedia: {result}"
    except wikipedia.exceptions.DisambiguationError:
        return "There are too many results for that query. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "I couldn't find any information on that topic."
    except Exception as e:
        return "Sorry, there was an error connecting to Wikipedia."

def get_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return f"{data['setup']}... {data['punchline']}"
        return "I couldn't think of a joke right now."
    except Exception:
        return "Sorry, my joke book is currently unavailable."

def take_screenshot():
    try:
        # Create screenshots folder in the current working directory
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        time_str = datetime.datetime.now().strftime("%H%M%S")
        filename = f"screenshot_{time_str}.png"
        filepath = os.path.join("screenshots", filename)
        
        # Take screenshot and save
        screenshot = pyautogui.screenshot()
        screenshot.save(filepath)
        return f"Screenshot le liya! {filename} mein save ho gaya."
    except Exception:
        return "Sorry, there was an error taking the screenshot."

# --- FLASK ROUTES ---

@app.route('/')
def index():
    # Renders the index.html from the templates folder
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    # This route handles all incoming requests from the frontend Web UI
    data = request.get_json()
    command = data.get('command', '').lower()
    response = ""
    
    if not command:
        response = "Please say something."
        return jsonify({"response": response})
        
    # 1. Exit Commands
    if "exit" in command or "quit" in command or "stop" in command:
        response = "Goodbye sir. Have a great day!"
        
    # 2. Time and Date
    elif "time" in command:
        response = get_time()
    elif "date" in command:
        response = get_date()
        
    # 3. Web Navigation
    elif "open" in command and any(site in command for site in ["youtube", "google", "chatgpt", "whatsapp", "facebook", "instagram", "github"]):
        response = open_website(command)
        
    elif "play" in command:
        response = play_music(command)
        
    # 4. Utilities
    elif "take screenshot" in command or "screenshot" in command:
        response = take_screenshot()
        
    elif "wikipedia" in command:
        response = search_wikipedia(command)
        
    elif "joke" in command:
        response = get_joke()
        
    elif "weather" in command or "temperature" in command:
        if "in" in command:
            city = command.split("in")[-1].strip()
            response = get_weather(city)
        else:
            response = get_weather() # defaults to Sambhajinagar as set in weather.py
            
    elif "remind me" in command:
        try:
            parts = command.split("in")
            task = parts[0].replace("remind me to", "").strip()
            time_part = parts[1].strip()
            seconds = int(''.join(filter(str.isdigit, time_part)))
            if "minute" in time_part:
                seconds *= 60
            set_reminder(task, seconds)
            response = f"I will remind you to {task} in {seconds} seconds."
        except Exception:
            response = "Please specify what to remind you and when. For example: remind me to drink water in 10 seconds."
            
    # 5. Basic Conversation
    elif "how are you" in command:
        response = "I am doing great, sir. How can I help you today?"
    elif "who made you" in command or "who created you" in command:
        response = "Mohit Vikas Bhombe"
    elif "who are you" in command or "what is your name" in command:
        response = "I am Jarvis, your personal voice assistant."
    elif "hello" in command or "hi " in command or "hey " in command:
        response = "Hello sir! How can I assist you?"
        
    # 6. Fallback General Questions
    elif "who is" in command or "what is" in command or "where is" in command:
        response = search_wikipedia(command)
        
    # 7. Unrecognized Command
    else:
        response = "I am not sure how to help with that. Please try another command."
        
    # Return JSON to the frontend
    return jsonify({"response": response})

if __name__ == "__main__":
    # Start a timer to open the browser automatically after 1 second
    import threading
    threading.Timer(1.0, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    
    # Start the Flask app
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
