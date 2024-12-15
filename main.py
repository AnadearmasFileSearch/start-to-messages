import os
import logging
import json  # Ensure you import the json module
import handlers  # Ensure you import the handlers module

from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN, WEBHOOK_URL

# Import the functions from handlers
from handlers import start, forward_message_to_admin, reply_to_user, broadcast, users

# Set up logging to get detailed information
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

# Initialize the bot
bot = Bot(token=BOT_TOKEN)

# Initialize the Application object (v20.x and above)
application = Application.builder().token(BOT_TOKEN).build()

# Register command and message handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message_to_admin))
application.add_handler(CommandHandler("broadcast", broadcast))
application.add_handler(CommandHandler("users", users))
application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.PRIVATE, reply_to_user))

# Function to set the webhook for Telegram updates
async def set_webhook():
    webhook_url = f"{WEBHOOK_URL}/{BOT_TOKEN}"
    await bot.set_webhook(url=webhook_url)
    logger.info(f"Webhook set to {webhook_url}")

# Function to process incoming webhook requests
def process_update(request_data):
    try:
        # Parse the incoming update and process it using the application
        update = Update.de_json(request_data, bot)
        application.process_update(update)
    except Exception as e:
        logger.error(f"Error processing update: {e}")

# Webhook endpoint function with enhanced error handling
def webhook(environ, start_response):
    try:
        # Read the request body and get the JSON data
        request_data = environ['wsgi.input'].read().decode('utf-8')  # Decode input data
        
        # Check if request_data is empty and log it
        if not request_data:
            logger.error("Received empty request body.")
            start_response('400 Bad Request', [('Content-Type', 'text/plain')])
            return [b"Empty body"]

        # Try to parse the data into a Python dictionary
        try:
            request_data = json.loads(request_data)  # Parse it into a Python dictionary
        except json.JSONDecodeError as e:
            logger.error(f"JSON Decode Error: {str(e)}. Invalid JSON received.")
            start_response('400 Bad Request', [('Content-Type', 'text/plain')])
            return [b"Invalid JSON"]

        # Process the update
        process_update(request_data)

        # Send success response
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b"OK"]
    except Exception as e:
        # Log error if the webhook fails
        logger.error(f"Error in webhook: {e}")
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [b"Internal Server Error"]

if _name_ == "_main_":
    # Set the webhook asynchronously
    import asyncio
    asyncio.run(set_webhook())

    # Start webhook handling (using Werkzeug server for development)
    from werkzeug.serving import run_simple
    run_simple("0.0.0.0", 5000, webhook)
