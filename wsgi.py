import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import create_app
from app.bot import start_bot
import threading

app = create_app()

threading.Thread(target=start_bot, daemon=True).start()
