import os
from flask import Flask
from app.extensions import db, migrate, login_manager, bcrypt, cache
import app.exceptions as app_exception

def create_app():
    
    app = Flask(
        import_name=__name__,
        static_folder='assets',
        template_folder='templates'
    )
    
    from app.users.routes import blueprint as users_blueprint
    from app.dashboard.routes import blueprint as dashboard_blueprint
    from app.database.routes import blueprint as database_blueprint
    
    def register_blueprint(app):
        app.register_blueprint(blueprint=users_blueprint)
        app.register_blueprint(blueprint=dashboard_blueprint)
        app.register_blueprint(blueprint=database_blueprint)

    def register_error_handlers(app):
        app.register_error_handler(401, app_exception.unauthorized)
        app.register_error_handler(404, app_exception.page_not_found)
        app.register_error_handler(500, app_exception.server_error)


    register_blueprint(app)
    register_error_handlers(app)
    app.config.from_object('config.DevConfig')
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.jinja_env.auto_reload = True

    db.init_app(app)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Import Models Here
    from app.users.models import User
    from app.database.models import Register

    migrate.init_app(app=app, db=db)
    login_manager.init_app(app=app)
    bcrypt.init_app(app=app)
    cache.init_app(app=app)

    login_manager.login_view = 'users.login'
    login_manager.login_message = 'لطفا ابتدا وارد حساب کاربری خود بشوید!'
    login_manager.login_message_category = 'info'
    
    from app.bot import init_bot
    init_bot(app)
    
    return app