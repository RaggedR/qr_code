# QR Code Telegram Bot

A Telegram bot that generates QR codes from URLs.

## Getting Your Bot Token

1. Open Telegram and search for **@BotFather**
2. Start a chat and send `/newbot`
3. Follow the prompts to choose a name and username for your bot
4. BotFather will give you a token that looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`
5. Copy this token for the next step

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd qr

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install python-telegram-bot python-dotenv qrcode[pil]

# Create .env file with your token
echo "TELEGRAM_BOT_TOKEN=your_token_here" > .env
```

Replace `your_token_here` with the token from BotFather.

## Running the Bot

```bash
source venv/bin/activate
python bot.py
```

The bot will run until you press Ctrl+C.

## Usage

Once running, find your bot on Telegram (by the username you chose) and:

- `/start` - Start the bot and see available commands
- `/help` - Show help message
- `/qr <url>` - Generate a QR code (e.g., `/qr https://google.com`)
- `/echo <message>` - Echo back your message

Any other text message will be echoed back to you.
