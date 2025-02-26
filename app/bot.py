import telebot
from flask_sqlalchemy import SQLAlchemy
import schedule
import time
from threading import Thread

TELEGRAM_TOKEN = '8043272038:AAFbx_iyOmTSco0U_5pG7a-51NjZ7uLWcaU'
bot = telebot.TeleBot(TELEGRAM_TOKEN)
CHAT_ID = -4638690648


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
    



def send_new_register(text, file_path=None):

    bot.send_message(
        chat_id=CHAT_ID,
        text=text,
        parse_mode="HTML"
    )
    
    if file_path:
        print(file_path)
        with open(file_path, 'rb') as file:
            bot.send_document(
                chat_id=CHAT_ID,
                document=file,
                caption="رزومه متقاضی",
                timeout=60
            )


def send_daily_message():    
    from app.database.models import Register
    from app import create_app
    app = create_app()
    with app.app_context():
        registrations = Register.query.count()
        message = f"این یک پیام خودکار است.\nتعداد افراد ثبت نام شده: {registrations} نفر."
        bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode="HTML"
        )

def start_scheduler():
    schedule.every().day.at("21:00").do(send_daily_message)
    schedule.every().day.at("9:00").do(send_daily_message)
    while True:
        schedule.run_pending()
        time.sleep(1)



def start_bot():
    scheduler_thread = Thread(target=start_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()
    bot.polling()
