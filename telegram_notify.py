from phBot import *
import requests
import QtBind
import os

pName = "TelegramNotify"
pVersion = "1.0"

# GUI oluştur
gui = QtBind.init(__name__, pName)
QtBind.createLabel(gui, "📲 Telegram bildirim sistemi aktif.", 10, 10)

# Telegram Bot Token ve Kullanıcı ID'si
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

inGame = None

# Telegram mesaj gönderme fonksiyonu
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        log(f"[{pName}] Hata: {e}")

# Bağlantı kesildiğinde çağrılacak fonksiyon
def handle_disconnection():
    message = "⚠️ phBot Bağlantısı Kesildi!"
    send_telegram_message(message)
    log(f"[{pName}] Bağlantı kesildi, Telegram bildirimi gönderildi.")

# Bağlantı kurulduğunda çağrılacak fonksiyon
def handle_connection():
    message = "✅ phBot Bağlantı Kuruldu!"
    send_telegram_message(message)
    log(f"[{pName}] Bağlantı kuruldu, Telegram bildirimi gönderildi.")

# Karakter seçildiğinde çağrılacak fonksiyon
def handle_character_selected():
    message = "🎭 Karakter Başarıyla Seçildi!"
    send_telegram_message(message)
    log(f"[{pName}] Karakter seçildi, Telegram bildirimi gönderildi.")

# Parti güncellendiğinde
def handle_party_update():
    message = "🔄 Parti Güncellendi!"
    send_telegram_message(message)
    log(f"[{pName}] Parti güncellendi, Telegram bildirimi gönderildi.")

# Olaylar

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

# Komut yakalayıcı
def handle_command(args):
    log(f"[{pName}] Komut alındı: {args}")

# Plugin yüklendi mesajı
log(f"Plugin: {pName} v{pVersion} başarıyla yüklendi")
