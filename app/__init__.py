# encoding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    """
    
    :param config_name: 配置名 
    :return: 创建APP实例
    
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    # 注册main蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
