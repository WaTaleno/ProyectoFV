from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
#
from flask_socketio import SocketIO

login_manager = LoginManager()
db = SQLAlchemy()
#
socketio = SocketIO() 

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/talkFusion'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    login_manager.login_view = "login"

    db.init_app(app)

    socketio.init_app(app, cors_allowed_origins='*')

    # Registro de los Blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    socketio.run(app, host="localhost")  # Iniciar el servidor SocketIO