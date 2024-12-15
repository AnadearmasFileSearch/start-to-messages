import os
import logging
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN, WEBHOOK_URL
import handlers  # Import the handlers module

# Debugging: Check if handlers are imported correctly
print("Handlers module:", handlers)
print("Functions available in handlers:", dir(handlers))

# Import the functions from handlers
from handlers import start, forward_message_to_admin, reply_to_user, broadcast, users  # Import your handlers

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
        update = Update.de_json(request_data, bot)
        application.process_update(update)
    except Exception as e:
        logger.error(f"Error processing update: {e}")

# Webhook endpoint function
def webhook(environ, start_response):
    try:
        # Read the request body and get the JSON data
        request_data = environ['wsgi.input'].read().decode('utf-8')  # Decode input data
        request_data = json.loads(request_data)  # Parse it into a Python dictionary
        process_update(request_data)  # Process the update

        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b"OK"]
    except Exception as e:
        logger.error(f"Error in webhook: {e}")
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [b"Internal Server Error"]

if __name__ == "__main__":
    # Set the webhook asynchronously
    import asyncio
    asyncio.run(set_webhook())

    # Start webhook handling (using Werkzeug server)
    from werkzeug.serving import run_simple
    run_simple("0.0.0.0", 5000, webhook)
