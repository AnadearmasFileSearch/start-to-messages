import os
from dotenv import load_dotenv

# Load environment variables from a .env file (useful in local development)
load_dotenv()

# Retrieve the environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
ADMIN_ID = os.getenv("ADMIN_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Check if all required variables are set
if not BOT_TOKEN:
    raise ValueError("Missing required environment variable: BOT_TOKEN")
if not MONGO_URL:
    raise ValueError("Missing required environment variable: MONGO_URL")
if not ADMIN_ID:
    raise ValueError("Missing required environment variable: ADMIN_ID")
if not WEBHOOK_URL:
    raise ValueError("Missing required environment variable: WEBHOOK_URL")

# Convert ADMIN_ID to an integer
try:
    ADMIN_ID = int(ADMIN_ID)
except ValueError:
    raise ValueError(f"ADMIN_ID must be an integer. Received: {ADMIN_ID}")

# Optional: Don't print sensitive information in production
if os.getenv('FLASK_ENV') != 'production':
    print(f'BOT_TOKEN: {BOT_TOKEN}')
    print(f'MONGO_URL: {MONGO_URL}')
    print(f'ADMIN_ID: {ADMIN_ID}')
    print(f'WEBHOOK_URL: {WEBHOOK_URL}')
