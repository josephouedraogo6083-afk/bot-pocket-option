import os
import telebot
from flask import Flask
from threading import Thread

# Partie pour que le bot reste allumé
app = Flask('')
@app.route('/')
def home(): return "Bot en ligne"
def run(): app.run(host='0.0.0.0', port=8080)

# TON TOKEN ICI
TOKEN = "6534888251:AAH8jXXXXXXXXXXXX" # Remplace ça par ton vrai Token
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m): bot.reply_to(m, "🚀 Bot Pocket Option Prêt !")

@bot.message_handler(commands=['signal'])
def signal(m): bot.reply_to(m, "🎯 SIGNAL : 🔴 PUT (Confiance 91%)")

if __name__ == "__main__":
    Thread(target=run).start()
    bot.polling()
  
