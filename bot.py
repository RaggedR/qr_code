import os
import qrcode
from io import BytesIO
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command"""
    await update.message.reply_text(
        "Hello! I'm your new bot. How can I help you today?\n\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/echo <message> - Echo back your message\n"
        "/qr <url> - Generate a QR code from a URL"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /help command"""
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/echo <message> - Echo back your message\n"
        "/qr <url> - Generate a QR code from a URL"
    )

async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /echo command"""
    if context.args:
        message = ' '.join(context.args)
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("Usage: /echo <message>")

async def qr_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /qr command - Generate QR code from URL"""
    if context.args:
        url = ' '.join(context.args)

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)

        # Create image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save to BytesIO
        bio = BytesIO()
        img.save(bio, 'PNG')
        bio.seek(0)

        # Send photo to user
        await update.message.reply_photo(photo=bio, caption=f"QR Code for: {url}")
    else:
        await update.message.reply_text("Usage: /qr <url>\nExample: /qr https://google.com")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo any text message"""
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

def main():
    """Start the bot"""
    # Create the Application
    app = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("echo", echo_command))
    app.add_handler(CommandHandler("qr", qr_command))

    # Register message handler (echo)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    print("Bot is running... Press Ctrl+C to stop")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
