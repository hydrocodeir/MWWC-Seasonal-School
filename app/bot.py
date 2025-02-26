import telebot
from flask_sqlalchemy import SQLAlchemy
from . import app
from app.database.models import Register

TELEGRAM_TOKEN = '8043272038:AAFbx_iyOmTSco0U_5pG7a-51NjZ7uLWcaU'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['check'])
def check_registrations(message):

    with app.app_context():
        registrations = Register.query.all()
        
        txt = f"{len(registrations)} نفر - تعداد افراد ثبت نام شده.\n\n"
        
        for i in registrations:
            txt = txt + f"{i.first_name} {i.last_name} - {i.university} - {i.educational_stage} - {i.academic_discipline}\n\n"
            
        bot.reply_to(
            message=message, 
            text=txt,
            parse_mode="HTML",
        )
    
# @bot.message_handler(func=lambda message: True)
# def get_group_chat_id(message):
#     chat_id = message.chat.id
#     bot.reply_to(message, f"This group's chat ID is: {chat_id}")

def send_new_register(text):
    bot.send_message(
        chat_id="7690029281",
        text=text,
        parse_mode="HTML")

def start_bot():
    bot.polling()
