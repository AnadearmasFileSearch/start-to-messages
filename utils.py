async def delete_message(context):
    try:
        message = context.job.context
        await context.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        print(f"Deleted message {message.message_id}")
    except Exception as e:
        print(f"Failed to delete message: {e}")

async def delete_reply(context):
    try:
        message = context.job.context
        await context.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        print(f"Deleted reply message {message.message_id}")
    except Exception as e:
        print(f"Failed to delete reply: {e}")