import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):

    app = Flask(__name__)

    # 设置日志
    app.logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    app.logger.addHandler(console_handler)

    # load configuration
    app.config.from_object(config_class)

    # 创建数据库连接
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.blueprints.map import bp_map
    app.register_blueprint(bp_map)

    return app