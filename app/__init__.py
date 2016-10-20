from flask import Flask
from flask_oauthlib.provider import OAuth2Provider
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config
import logging
from oauthlib import oauth2

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()
oauth = OAuth2Provider()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth'


def create_app(config_name):
    app = Flask(__name__)

    # TODO:先简单的创建日志文件
    log_handler = logging.FileHandler('flask.log')
    app.logger.addHandler(log_handler)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

