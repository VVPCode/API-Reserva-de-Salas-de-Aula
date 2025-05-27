from flask import Flask

def create_app():
    app = Flask(__name__)

    from .controllers.reserva_controller import reserva_bp
    app.register_blueprint(reserva_bp)

    return app
