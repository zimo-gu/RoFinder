import os
from dotenv import load_dotenv

load_dotenv()

def get_webhook_url():
    webhook_url = os.getenv("DISCORD_WEBHOOK")

    if not webhook_url:
        print("Warning: Discord webhook URL is not set in the .env file.")
        webhook_url = input("Please enter your Discord webhook URL manually: ")

    return webhook_url

def get_thread_count():
    return 99999999999999999
