from flask import Flask
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)

    from app.bookcontroller import bp_books
    app.register_blueprint(bp_books)

    return app