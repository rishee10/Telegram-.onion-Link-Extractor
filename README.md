#  Telegram .onion Link Extractor

A Python script that connects to a public Telegram channel using the Telegram API (via Telethon) and extracts any `.onion` links from recent messages.

## 🔍 Features

- Connects to public Telegram channels (e.g., `@toronionlinks`)
- Extracts `.onion` links using regular expressions
- Saves results in structured JSON format
- Skips previously scanned messages using message ID tracking
- Handles Telegram rate limits and login sessions
- Uses asynchronous programming with `asyncio` and `Telethon`

---

## 📦 Requirements

- Python 3.7+
- Telethon

## How To Run

### Clone The Repo

`git clone https://github.com/rishee10/Telegram-.onion-Link-Extractor.git`

`cd Telegram-.onion-Link-Extractor`


### Create Virtual Enviroment

`python -m venv myenv`

### Activate the Virtual Enviroment

`myenv/Scripts/activate`

### Install telethon

`pip install telethon`


### Telegram API Setup

Go to ` https://my.telegram.org.`

Log in with your phone number.

Navigate to API Development Tools.

Create a new app and get your:

API ID

API HASH

Add Your API ID AND API HASH in the links.py

### Run the script

`python links.py`

### Sample Output Screen-shot

![Screenshot 2025-05-16 142922](https://github.com/user-attachments/assets/fbf02b75-08e0-446d-8fb8-9f14b86cfa3c)

![Screenshot 2025-05-16 143023](https://github.com/user-attachments/assets/3fb3e436-fc39-47ac-9d2a-7f1183df05b8)



