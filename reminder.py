import threading
import time
import pyttsx3

def set_reminder(reminder_text, wait_time_seconds):
    """
    Sets a reminder to be spoken after a specified number of seconds.
    Uses threading so the main listening loop doesn't get blocked.
    """
    def reminder_thread():
        # Pause the thread for the given time
        time.sleep(wait_time_seconds)
        
        # Print the reminder to the console
        print(f"\n[Reminder] {reminder_text}")
        
        # Initialize a local text-to-speech engine for this thread
        # This prevents crashes that can happen if multiple threads use the same engine
        local_engine = pyttsx3.init()
        local_engine.setProperty('rate', 170)
        
        local_engine.say(f"Sir, I have a reminder for you: {reminder_text}")
        local_engine.runAndWait()
        
    # Create and start a new thread for the reminder
    thread = threading.Thread(target=reminder_thread)
    
    # A daemon thread will automatically exit when the main program stops
    thread.daemon = True
    thread.start()
    
    return "Reminder set successfully."
