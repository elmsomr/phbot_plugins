from phBot import *
import requests
import QtBind
import os

pName = "TelegramNotify"
pVersion = "1.0"

# Initialize GUI
gui = QtBind.init(__name__, pName)
QtBind.createLabel(gui, "📲 Telegram notification system is active.", 10, 10)

# Telegram Bot Token and Chat ID
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

inGame = None

# Function to send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        log(f"[{pName}] Error: {e}")

# Called when the bot gets disconnected
def handle_disconnection():
    message = "⚠️ phBot Disconnected!"
    send_telegram_message(message)
    log(f"[{pName}] Disconnected, Telegram notification sent.")

# Called when the bot connects to the server
def handle_connection():
    message = "✅ phBot Connected!"
    send_telegram_message(message)
    log(f"[{pName}] Connected, Telegram notification sent.")

# Called when a character successfully joins the game
def handle_character_selected():
    message = "🎭 Character successfully joined the game!"
    send_telegram_message(message)
    log(f"[{pName}] Character joined, Telegram notification sent.")

# Called when the party status changes
def handle_party_update():
    message = "🔄 Party Updated!"
    send_telegram_message(message)
    log(f"[{pName}] Party updated, Telegram notification sent.")

# phBot event hooks
def connected():
    global inGame
    inGame = None
    handle_connection()

def disconnected():
    handle_disconnection()

def joined_game():
    global inGame
    inGame = get_character_data()
    handle_character_selected()

def party_update(party):
    handle_party_update()

# Optional command handler (not required, but ensures plugin shows up in list)
def handle_command(args):
    log(f"[{pName}] Command received: {args}")

# Plugin loaded message
log(f"Plugin: {pName} v{pVersion} successfully loaded")