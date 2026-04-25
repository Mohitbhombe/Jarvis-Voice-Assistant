import speech_recognition as sr
import pyttsx3
import datetime
from commands import process_command

# Initialize the Text-To-Speech engine
engine = pyttsx3.init()

# Set speech rate to 170 (moderate speed)
engine.setProperty('rate', 170)

# Optional: Change the voice
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id) # 0 for male, 1 for female (on Windows)

def speak(text):
    """
    Takes a text string and converts it to speech using pyttsx3.
    It also prints the text to the terminal.
    """
    print(f"Jarvis: {text}")
    engine.say(text)
    # This command makes the program wait until speaking is finished
    engine.runAndWait()

def wish_me():
    """
    Greets the user properly based on the current time of day.
    """
    hour = datetime.datetime.now().hour
    
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis. How can I help you today?")

def take_command():
    """
    Listens to the microphone and uses Google Speech Recognition API 
    to convert the audio into text.
    Returns the recognized text as a string.
    """
    # Create a recognizer object
    recognizer = sr.Recognizer()
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("\nListening...")
        # Pause threshold gives the user 1 second of silence before considering the sentence finished
        recognizer.pause_threshold = 1
        
        # Listen to the audio
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        # Use Google's API to understand the audio
        # language='en-IN' is specifically for Indian English accents
        query = recognizer.recognize_google(audio, language='en-IN')
        print(f"User said: {query}")
        return query.lower()
        
    except sr.UnknownValueError:
        # Triggered when speech is unintelligible
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"
        
    except sr.RequestError:
        # Triggered when there is no internet connection to reach Google's servers
        print("Network error. Please check your internet connection.")
        return "None"

if __name__ == "__main__":
    # 1. Greet the user when the program starts
    wish_me()
    
    # 2. Main loop to keep listening for commands infinitely
    while True:
        # Get command from the user's microphone
        command = take_command()
        
        # If no valid command was heard, just listen again
        if command == "None":
            continue
            
        # 3. Process the command and figure out what Jarvis should say back
        response = process_command(command, engine)
        
        # 4. Speak the response out loud
        speak(response)
        
        # 5. Graceful Exit: if the response contains the goodbye message, break the loop
        if "Goodbye" in response:
            break
