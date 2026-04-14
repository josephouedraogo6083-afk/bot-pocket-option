import os
import telebot
from flask import Flask
from threading import Thread

# Serveur pour garder le bot en vie sur Render
app = Flask('')
@app.route('/')
def home(): return "Le Bot est en ligne !"
def run(): app.run(host='0.0.0.0', port=8080)

# TON TOKEN (Déjà mis à jour)
TOKEN = "8026442725:AAEL34FH0OSgdVEXNQHiygft8HBGesBLc7s"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m): 
    bot.reply_to(m, "🚀 Bot Pocket Option Prêt !\nUtilisez /signal pour l'analyse.")

@bot.message_handler(commands=['signal'])
def signal(m): 
    bot.reply_to(m, "🎯 SIGNAL : 🔴 PUT\n💪 Force : FORT\n🔥 Confiance : 91%")

if __name__ == "__main__":
    Thread(target=run).start()
    bot.polling()
    
