import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from app import create_app
from app.bot import start_bot
from livereload import Server
import threading

app = create_app()


if __name__ == '__main__':
    
    threading.Thread(target=start_bot).start()
    
    server = Server(app.wsgi_app)
    server.serve(
        host = "127.0.0.1",
        port=5505
    )
    
    # app.run(
    #     host="127.0.0.1",
    #     port=5505
    # )
