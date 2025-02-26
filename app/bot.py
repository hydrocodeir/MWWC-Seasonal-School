import telebot
from flask_sqlalchemy import SQLAlchemy
from . import app
from app.database.models import Register

TELEGRAM_TOKEN = '8043272038:AAFbx_iyOmTSco0U_5pG7a-51NjZ7uLWcaU'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['check'])
def check_registrations(message):

    with app.app_context():
        registrations = len(Register.query.all())
        print(registrations)
        bot.reply_to(message, f"{registrations} people have registered.")

def start_bot():
    bot.polling()
