# FreqBot — FreqFlag CTF AI Assistant

A locally-running AI assistant for the FreqFlag CTF event.
Powered by Ollama + llama3.2 (2GB, runs on any laptop).

---

## Setup (one-time)

### 1. Install Ollama
Download from https://ollama.com and install it.
Then pull the model (2 GB download):

    ollama pull llama3.2

### 2. Install Python dependencies

    pip install -r requirements.txt

---

## Run for the event

Open two terminals:

**Terminal 1 — start Ollama:**

    ollama serve

**Terminal 2 — start FreqBot:**

    python app.py

Then open http://localhost:5000 in your browser.

---

## Share with students on your local network

Find your local IP:
- macOS/Linux: `ifconfig | grep inet`
- Windows: `ipconfig`

Students visit: http://YOUR_IP:5000

---

## Customization

Edit the SYSTEM_PROMPT in app.py to:
- Change the event name
- Add or remove challenges
- Make hints more/less generous
- Change the bot's personality
