from flask import Flask
from config import Config
from database import db
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from models.reserva import Reserva
        db.create_all()

        # Importações locais para evitar circular imports
        from controllers.reserva_controller import reserva_bp
        app.register_blueprint(reserva_bp)

    @app.route('/')
    def home():
        return "API de Reserva de Salas no ar!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
