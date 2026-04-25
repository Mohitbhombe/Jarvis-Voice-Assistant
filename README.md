# Jarvis - Python Voice Assistant

A complete, beginner-friendly Python voice assistant named "Jarvis" that can perform various tasks through voice commands. 

**Author:** Mohit Vikas Bhombe

## 🌟 Features

- **Time & Date:** Tells the current time and date.
- **Web Navigation:** Opens YouTube and Google in your default browser.
- **Wikipedia Search:** Searches Wikipedia and reads out a 2-sentence summary.
- **Entertainment:** Tells random programming jokes.
- **Weather Updates:** Provides current weather for any city (requires OpenWeatherMap API key).
- **Reminders:** Set background reminders using threading (e.g., "remind me to drink water in 10 seconds").
- **Dynamic Greetings:** Greets you properly based on the time of day (Morning/Afternoon/Evening).
- **Graceful Exit:** Shuts down politely when you say "exit", "quit", or "stop".

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Speech Recognition:** Google Speech API (`SpeechRecognition`)
- **Text-To-Speech:** `pyttsx3` (Offline engine, speech rate 170)
- **Other Libraries:** `wikipedia`, `requests`, `pyaudio`, `threading`

## ⚙️ Setup Instructions

### 1. Prerequisites
Make sure you have Python 3.11 or newer installed. You can check by running `python --version` in your terminal.

### 2. VS Code Setup
1. Open Visual Studio Code.
2. Click on `File > Open Folder` and select your project folder.
3. Open a new terminal inside VS Code by clicking `Terminal > New Terminal` in the top menu.

### 3. Install Dependencies
Run the following command in your terminal to install all required libraries:

```bash
pip install -r requirements.txt
```

**Windows Users - PyAudio Fix:**
If you encounter an error installing `pyaudio` directly, it is a common Windows issue. Please install it using `pipwin` instead:
```bash
pip install pipwin
pipwin install pyaudio
```

### 4. API Keys Setup
To use the weather feature:
1. Go to [OpenWeatherMap](https://openweathermap.org/) and create a free account.
2. Generate an API key.
3. Open `weather.py` and replace `"YOUR_API_KEY_HERE"` with your actual API key.

## 🚀 Usage / Commands

To start Jarvis, run the `main.py` file:
```bash
python main.py
```

Wait until you hear the greeting and see `Listening...` in the console, then try saying:
- *"What is the time?"*
- *"What is today's date?"*
- *"Open YouTube"*
- *"Search Wikipedia for Albert Einstein"*
- *"Tell me a joke"*
- *"What is the weather in London?"*
- *"Remind me to drink water in 10 seconds"*
- *"Exit"*

## 📤 Pushing to GitHub

Follow these steps in your terminal to upload this project to your GitHub account:

1. **Initialize Git Repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Complete Jarvis voice assistant project"
   ```

2. **Create a new repository on GitHub:**
   - Go to github.com and log in.
   - Click the "+" icon in the top right and select "New repository".
   - Name it `Jarvis-Voice-Assistant`.
   - Do NOT initialize with a README, .gitignore, or license (leave those unchecked).
   - Click "Create repository".

3. **Link and Push:**
   Copy the commands provided by GitHub under "...or push an existing repository from the command line" and paste them in your VS Code terminal. It should look like this:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/Jarvis-Voice-Assistant.git
   git push -u origin main
   ```
