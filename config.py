import os

# Retrieve the environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
ADMIN_ID = int(os.getenv("ADMIN_ID"))  # Ensure this is an integer
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Print the values to check if they are correctly set
print(f'BOT_TOKEN: {BOT_TOKEN}')
print(f'MONGO_URL: {MONGO_URL}')
print(f'ADMIN_ID: {ADMIN_ID}')
print(f'WEBHOOK_URL: {WEBHOOK_URL}')

# Raise an error if any variable is missing
if not BOT_TOKEN or not MONGO_URL or not ADMIN_ID or not WEBHOOK_URL:
    raise ValueError("Missing required environment variables: BOT_TOKEN, MONGO_URL, ADMIN_ID, or WEBHOOK_URL.")
