// Get references to HTML elements
const chatContainer = document.getElementById('chat-container');
const textInput = document.getElementById('text-input');
const sendBtn = document.getElementById('send-btn');
const micBtn = document.getElementById('mic-btn');
const statusText = document.getElementById('status-text');

// Initialize Web Speech API for voice recognition (Browser Native)
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition;

if (SpeechRecognition) {
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.lang = 'en-IN'; // Set to Indian English
    recognition.interimResults = false;

    // Triggered when microphone starts listening
    recognition.onstart = () => {
        micBtn.classList.remove('ready');
        micBtn.classList.add('listening');
        statusText.innerText = "Sun raha hoon... (Listening)";
    };

    // Triggered when user finishes speaking
    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        textInput.value = transcript;
        sendMessage(); // Automatically send the spoken message
    };

    // Handle errors (e.g., no mic found)
    recognition.onerror = (event) => {
        console.error("Speech Recognition Error: ", event.error);
        statusText.innerText = "Error: Could not hear you. Try again.";
        resetMicButton();
    };

    recognition.onend = () => {
        resetMicButton();
    };
} else {
    // Hide mic button if browser doesn't support Speech API
    micBtn.style.display = 'none';
    statusText.innerText = "Voice recognition not supported in this browser. Please type.";
}

// Reset mic button to initial state
function resetMicButton() {
    micBtn.classList.remove('listening');
    micBtn.classList.add('ready');
    if(statusText.innerText.includes("Listening")) {
        statusText.innerText = "Ready";
    }
}

// Click listener for Mic button
micBtn.addEventListener('click', () => {
    if (recognition) {
        recognition.start();
    }
});

// Function to add a new message to the Chat UI
function appendMessage(sender, text) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    
    const p = document.createElement('p');
    p.innerText = text;
    messageDiv.appendChild(p);
    
    chatContainer.appendChild(messageDiv);
    
    // Auto scroll to the newest message at the bottom
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Function to speak the response out loud using Browser TTS
function speakText(text) {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel(); // Stop any current speech
        
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'en-IN';
        utterance.rate = 0.95; // Slightly slower
        
        window.speechSynthesis.speak(utterance);
    }
}

// Function to send the message to the Python Flask Backend
async function sendMessage() {
    const text = textInput.value.trim();
    if (!text) return; // Do nothing if input is empty
    
    // 1. Show user's message in UI
    appendMessage('user', text);
    textInput.value = '';
    statusText.innerText = "Processing...";
    
    try {
        // 2. Send POST request to Flask '/ask' route
        const response = await fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ command: text })
        });
        
        const data = await response.json();
        
        // 3. Show Jarvis's response in UI
        appendMessage('jarvis', data.response);
        statusText.innerText = "Ready";
        
        // 4. Speak the response out loud
        speakText(data.response);
        
    } catch (error) {
        console.error('Error connecting to backend:', error);
        appendMessage('jarvis', "Sorry, I lost connection to the server. Make sure app.py is running.");
        statusText.innerText = "Connection Error";
    }
}

// Press Enter key to send message
textInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Click send button to send message
sendBtn.addEventListener('click', sendMessage);
