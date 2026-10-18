import requests
import time
import random
import sys
import os

# ==============================================================================
# CONFIGURATION - EDIT THESE LINES
# ==============================================================================

TOKEN = "---"  # <--- PUT YOUR TOKEN HERE
CHANNEL_ID = "---" # <--- PUT YOUR CHANNEL ID HERE (as string or int)

# ==============================================================================
# SETTINGS
# ==============================================================================

SPAM_INTERVAL = 0.4  # Seconds between messages
MIN_DIGITS = 10
MAX_DIGITS = 16

def generate_random_number():
    """Generates a random number with length between MIN_DIGITS and MAX_DIGITS"""
    length = random.randint(MIN_DIGITS, MAX_DIGITS)
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def send_message(token, channel_id, content):
    """Sends a message to the specified channel using the raw Discord API"""
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    payload = {
        "content": content,
        "tts": False,
        "nonce": str(int(time.time() * 1000)) + str(random.randint(1000, 9999))
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        
        if response.status_code == 200:
            return True
        elif response.status_code == 429:
            # Rate limited
            retry_after = response.json().get("retry_after", 1)
            time.sleep(retry_after)
            return False
        elif response.status_code == 401:
            print("[!] Invalid Token. Exiting.")
            sys.exit(1)
        else:
            print(f"[!] Error {response.status_code}: {response.text[:100]}")
            return False
            
    except Exception as e:
        print(f"[!] Connection Error: {e}")
        return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # Basic validation
    if TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("Error: Please edit line 6 and add your Token.")
        input("Press Enter to exit...")
        sys.exit(1)
        
    if CHANNEL_ID == "123456789012345678":
        print("Error: Please edit line 7 and add your Channel ID.")
        input("Press Enter to exit...")
        sys.exit(1)

    clear_screen()
    print(f"Starting spammer... Interval: {SPAM_INTERVAL}s")
    print("Press Ctrl+C to stop.")
    print("-" * 30)

    while True:
        msg = generate_random_number()
        success = send_message(TOKEN, CHANNEL_ID, msg)
        
        if not success:
            # If it failed due to rate limit or other error, 
            # we still wait the interval before trying again
            pass
            
        time.sleep(SPAM_INTERVAL)