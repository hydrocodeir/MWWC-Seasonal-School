import telebot
from flask_sqlalchemy import SQLAlchemy

TELEGRAM_TOKEN = '8043272038:AAFbx_iyOmTSco0U_5pG7a-51NjZ7uLWcaU'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def init_bot(app):
    
    @bot.message_handler(commands=['check'])
    def check_registrations(message):
        from app.database.models import Register
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

def send_new_register(text, file_path=None):
    
    CHAT_ID = -4638690648
    
    bot.send_message(
        chat_id=CHAT_ID,
        text=text,
        parse_mode="HTML")
    
    if file_path:
        print(file_path)
        with open(file_path, 'rb') as file:
            bot.send_document(
                chat_id=CHAT_ID,
                document=file,
                caption="رزومه متقاضی"
                timeout=60
            )


def start_bot():
    bot.polling()
