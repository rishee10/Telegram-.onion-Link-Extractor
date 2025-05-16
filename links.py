import re
import json
import asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest

# === Configuration ===
API_ID = 'Your_API_ID'
API_HASH = 'Your_API_HASH'

CHANNEL_USERNAME = 'toronionlinks'  # or any other public channel which contains onion links
OUTPUT_FILE = 'onion_links.json'
LAST_ID_FILE = 'last_message_id.txt'
SESSION_NAME = 'anon_session'

# === Regex for .onion URLs ===
ONION_REGEX = r'(http[s]?://[a-zA-Z0-9]{16,56}\.onion)'

# === Load last message ID ===
def load_last_message_id():
    try:
        with open(LAST_ID_FILE, 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0
    
# === Save last message ID ===
def save_last_message_id(message_id):
    with open(LAST_ID_FILE, 'w') as f:
        f.write(str(message_id))

# === Save link as JSON ===
def save_onion_link(url, discovered_at, context):
    entry = {
        "source": "telegram",
        "url": url,
        "discovered_at": discovered_at,
        "context": context,
        "status": "pending"
    }
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
        json.dump(entry, f)
        f.write('\n')

# === Main Async Function ===
async def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start()

    last_id = load_last_message_id()
    max_id = last_id

    try:
        channel = await client.get_entity(CHANNEL_USERNAME)

        history = await client(GetHistoryRequest(
            peer=channel,
            limit=100,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=last_id,
            add_offset=0,
            hash=0
        ))

        messages = history.messages
        print(f"[INFO] Fetched {len(messages)} new messages...")

        for message in reversed(messages):
            if message.id > max_id:
                max_id = message.id

            if message.message:
                found_links = re.findall(ONION_REGEX, message.message)
                if found_links:
                    timestamp = message.date.strftime('%Y-%m-%dT%H:%M:%SZ')
                    for url in found_links:
                        print(f"[FOUND] {url}")
                        save_onion_link(
                            url=url,
                            discovered_at=timestamp,
                            context=f"Found in Telegram channel @{CHANNEL_USERNAME}"
                        )

        # Save last processed message ID
        if max_id > last_id:
            save_last_message_id(max_id)

    except FloodWaitError as e:
        print(f"[ERROR] Rate limited. Waiting for {e.seconds} seconds.")
        await asyncio.sleep(e.seconds)
    except Exception as e:
        print(f"[ERROR] {str(e)}")
    finally:
        await client.disconnect()

# === Run the script ===
if __name__ == "__main__":
    asyncio.run(main())
