from flask import Flask

from app.models.boos import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.config.from_object('app.secure')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
    return app