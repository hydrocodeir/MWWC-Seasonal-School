import os


class Config:
    BASE_DIR = os.path.abspath(
        path=os.path.dirname(p=__file__)
    )
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = '7c0d2342b1ffdcdff5564aab8d9b182c4f071cd2368a92f433b2ddc9ad76ae4b'
    SECRET_KEY = '6bc38e8b34b729888304d57a5f35063d2b1aff060b80f3b1242c274c15cd0539'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300
    UPLOAD_FOLDER = './app/assets/uploads'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR, 'app.db')
    


class ProdConfig(Config):
    DEBUG = False
    # Database URLs:    dialect+driver://username:password@host:port/database
    # MySQL: 
    #   default:        mysql://username:password@host:port/database
    #   mysqlclient:    mysql+mysqldb://username:password@host:port/database
    #   PyMySQL:        mysql+pymysql://username:password@host:port/database
    # PostgreSQL:
    #   default:        postgresql://username:password@host:port/database
    #   psycopg2:       postgresql+psycopg2://username:password@host:port/database
    #   pg8000:         postgresql+pg8000://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = ...
    