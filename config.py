# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env (only used in local development)
load_dotenv()

# Securely fetch the variables from environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
ADMIN_ID = int(os.getenv("ADMIN_ID"))  # Ensure this is an integer
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Add this line for your webhook URL

# Ensure all variables are set
if not BOT_TOKEN or not MONGO_URL or not ADMIN_ID or not WEBHOOK_URL:
    raise ValueError("Missing required environment variables: BOT_TOKEN, MONGO_URL, ADMIN_ID, or WEBHOOK_URL.")