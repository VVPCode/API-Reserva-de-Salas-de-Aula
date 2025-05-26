from flask import Blueprint, request, jsonify
from app.models.reserva import Reserva
from app.database import db
import requests

reserva_bp = Blueprint('reserva_bp', __name__)

# URL da API de gerenciamento (ajuste conforme o ambiente)
API_GERENCIAMENTO_URL = "http://api-gerenciamento:5000/turmas"

@reserva_bp.route('/reservas', methods=['GET'])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([r.to_dict() for r in reservas]), 200


@reserva_bp.route('/reservas', methods=['POST'])
def criar_reserva():
    dados = request.json
    id_turma = dados.get('id_turma')
    sala = dados.get('sala')
    data_reserva = dados.get('data_reserva')
    horario = dados.get('horario')

    if not (id_turma and sala and data_reserva and horario):
        return jsonify({"erro": "Dados incompletos"}), 400

    # Valida se a turma existe na API de gerenciamento
    try:
        response = requests.get(f"{API_GERENCIAMENTO_URL}/{id_turma}")
        if response.status_code != 200:
            return jsonify({"erro": "ID da turma inválido"}), 400
    except requests.exceptions.RequestException:
        return jsonify({"erro": "Erro na comunicação com API de gerenciamento"}), 500

    nova_reserva = Reserva(
        id_turma=id_turma,
        sala=sala,
        data_reserva=data_reserva,
        horario=horario
    )

    db.session.add(nova_reserva)
    db.session.commit()

    return jsonify(nova_reserva.to_dict()), 201
