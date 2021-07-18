from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    '''
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config.db_user}:{config.db_password}@{config.db_ip}:5432/{config.db_name}'
    db.init_app(app)
    '''

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{config.db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    ''' logging sruff if i would add
    handler = RotatingFileHandler(config.log_file, maxBytes=100000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    '''

    from .main import main_app as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
