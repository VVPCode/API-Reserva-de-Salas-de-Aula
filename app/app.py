from flask import Flask
from app.config import Config
from app.database import db
from app.controllers.reserva_controller import reserva_bp
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(reserva_bp)

    @app.route('/')
    def home():
        return "API de Reserva de Salas no ar!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
