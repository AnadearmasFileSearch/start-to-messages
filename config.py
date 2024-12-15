# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env (only used in local development)
load_dotenv()

# Securely fetch the variables from environment
BOT_TOKEN = os.getenv("7524278392:AAGd21uCuExw-JAuko9UC5l9GLrqmwy-mh4")
MONGO_URL = os.getenv("mongodb+srv://NewFileShareBoT:EenaMeena@cluster0.7rbuejp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
ADMIN_ID = int(os.getenv("ADMIN_ID"))  # Ensure this is an integer
WEBHOOK_URL = os.getenv("https://start-to-messages.onrender.com")  # Add this line for your webhook URL

# Ensure all variables are set
if not BOT_TOKEN or not MONGO_URL or not ADMIN_ID or not WEBHOOK_URL:
    raise ValueError("Missing required environment variables: BOT_TOKEN, MONGO_URL, ADMIN_ID, or WEBHOOK_URL.")
