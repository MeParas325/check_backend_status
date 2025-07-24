import time
import requests

# --- Config ---
BACKEND_URL = "https://bugs-backend.takeuforward.org"
TELEGRAM_BOT_TOKEN = "7462619254:AAEFKdgz9qnZuRYqg_cd5YuWEg6mYKaMq6k"
TELEGRAM_CHAT_ID = "1390912843"
CHECK_INTERVAL = 1800 # in seconds

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": msg,
        "parse_mode": "HTML"
    }
    try:
        res = requests.post(url, data=payload)
        if res.status_code == 200:
            print(f"[📲] Telegram: {msg}")
        else:
            print(f"[❌] Telegram error: {res.text}")
    except Exception as e:
        print("[!] Telegram Exception:", e)

def check_backend():
    try:
        res = requests.head(BACKEND_URL, timeout=10)
        return res.status_code < 500
    except:
        return False

def main():
    print("🛰️ Backend Monitoring Every 30 Minutes (Always Notifying)...")

    while True:
        is_up = check_backend()
        status_text = "✅ Backend is UP" if is_up else "❌ Backend is DOWN"
        send_telegram(f"<b>{status_text}</b>")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
