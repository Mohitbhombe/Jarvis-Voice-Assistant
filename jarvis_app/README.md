# Jarvis - Voice Assistant Desktop App 🤖

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black.svg)
![GitHub](https://img.shields.io/badge/License-MIT-green.svg)

A complete, production-ready Voice Assistant Desktop Application with a modern dark-themed Web UI. Built using Python, Flask, and the Web Speech API.

**Author:** Mohit Vikas Bhombe  
**Location:** Sambhajinagar, Maharashtra  
**GitHub:** [Mohitbhombe](https://github.com/Mohitbhombe)  
**LinkedIn:** [Mohit Bhombe](https://www.linkedin.com/in/mohit-bhombe-578235294/)  

---

## 🌟 Features

| Feature | Description |
|---|---|
| **Voice & Text Input** | Interact using your microphone or by typing in the chatbox. |
| **Dark Theme UI** | A beautiful, GitHub-style dark theme interface with auto-scrolling. |
| **Live Weather** | Get real-time weather updates automatically. |
| **Wikipedia Search** | Ask questions and get a quick 2-sentence summary. |
| **Web Navigation** | Open YouTube, Google, ChatGPT, WhatsApp, and more. |
| **Screenshots** | Voice command to take a screenshot and save it with a timestamp. |
| **Reminders** | Set background reminders. |
| **Jokes** | Ask Jarvis to tell you a programming joke. |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, Vanilla CSS, JavaScript
- **Voice Recognition:** Web Speech API (Browser-native, extremely fast)
- **APIs Used:** `wttr.in` (Weather), Official Joke API, Wikipedia API
- **Desktop Packaging:** PyInstaller

---

## ⚙️ Installation & Setup

1. **Clone the repository** (or download the ZIP):
   ```bash
   git clone https://github.com/Mohitbhombe/Jarvis-Voice-Assistant.git
   cd Jarvis-Voice-Assistant/jarvis_app
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```
   *The app will automatically open in your default web browser.*

---

## 📦 Converting to .exe (Desktop App)

You can convert this complete web application into a single executable `.exe` file using PyInstaller.

Run the following command inside the `jarvis_app` folder:
```bash
pyinstaller --noconfirm --onedir --windowed --add-data "templates;templates/" --add-data "static;static/" app.py
```
After building, you will find `app.exe` inside the `dist/app/` folder. You can create a shortcut to this file and place it on your desktop!
