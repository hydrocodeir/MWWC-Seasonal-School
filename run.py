import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from app import app
from app.bot import start_bot

if __name__ == '__main__':
    
    import threading
    threading.Thread(target=start_bot).start()
    
    from livereload import Server
    server = Server(app.wsgi_app)
    server.serve(
        host = "127.0.0.1",
        port=5505
    )
    
    # app.run(
    #     host="127.0.0.1",
    #     port=5505
    # )
